#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verificador de alcance de herramientas de los cookbooks de agentes.

Comprueba la regla estructural de `cookbooks-agentes/`:

  1. El ORQUESTADOR (agent.yaml) no tiene herramientas de escritura ni de red,
     ni servidores MCP. Solo lectura local.
  2. Toda hoja con `web_fetch` habilitado declara una lista blanca
     `allowed_hosts` no vacía y bloquea redes privadas.
  3. Exactamente UNA hoja por cookbook tiene `write`.
  4. Cada cookbook tiene agent.yaml, README.md, steering-examples.json y al
     menos una hoja en subagents/.
  5. El README de cada cookbook menciona cada herramienta que el YAML concede,
     para que la documentación no prometa menos de lo que el YAML permite.

No usa librerías externas: hace un barrido de líneas, que es suficiente para
la forma acotada de estos manifiestos.

Uso:  python3 scripts/verificar-alcance.py
Sale con código 1 si hay errores.
"""
import glob
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COOKBOOKS = os.path.join(RAIZ, "cookbooks-agentes")

ERR, AVISO = [], []
ESCRITURA = {"write", "edit", "notebook_edit"}
RED = {"web_fetch", "web_search"}


def err(m):
    ERR.append(m)


def aviso(m):
    AVISO.append(m)


def herramientas_habilitadas(texto):
    """Devuelve el conjunto de herramientas con enabled: true."""
    hab = set()
    # forma en línea:  - { name: read, enabled: true }
    for m in re.finditer(r"-\s*\{\s*name:\s*([a-z_]+)\s*,\s*enabled:\s*true", texto):
        hab.add(m.group(1))
    # forma en bloque:
    #   - name: web_fetch
    #     enabled: true
    lineas = texto.splitlines()
    for i, linea in enumerate(lineas):
        m = re.match(r"\s*-\s*name:\s*([a-z_]+)\s*$", linea)
        if not m:
            continue
        nombre = m.group(1)
        for j in range(i + 1, min(i + 4, len(lineas))):
            if re.match(r"\s*enabled:\s*true\s*$", lineas[j]):
                hab.add(nombre)
                break
    return hab


def mcp_no_vacio(texto):
    m = re.search(r"^mcp_servers:\s*(.*)$", texto, re.M)
    if not m:
        return False
    resto = m.group(1).strip()
    if resto in ("[]", ""):
        # si está vacío en línea, no hay servidores; si está vacío a secas,
        # mirar si la línea siguiente abre una lista
        if resto == "[]":
            return False
        idx = m.end()
        siguiente = texto[idx:idx + 200].lstrip("\n")
        return siguiente.startswith("-") or siguiente.startswith("  -")
    return True


def revisar_cookbook(d):
    nombre = os.path.basename(d)
    agente = os.path.join(d, "agent.yaml")
    readme = os.path.join(d, "README.md")
    steering = os.path.join(d, "steering-examples.json")
    hojas = sorted(glob.glob(os.path.join(d, "subagents", "*.yaml")))

    # 4 — estructura
    for ruta, etiqueta in ((agente, "agent.yaml"), (readme, "README.md"),
                           (steering, "steering-examples.json")):
        if not os.path.exists(ruta):
            err("%s: falta %s" % (nombre, etiqueta))
    if not hojas:
        err("%s: no tiene subagentes en subagents/" % nombre)
    if not os.path.exists(agente):
        return

    if os.path.exists(steering):
        try:
            ejemplos = json.load(open(steering, encoding="utf-8"))
            if not isinstance(ejemplos, list) or not ejemplos:
                err("%s: steering-examples.json debe ser una lista no vacía" % nombre)
            else:
                for e in ejemplos:
                    if "event" not in e or "description" not in e:
                        err("%s: un ejemplo de steering no tiene 'event' y 'description'" % nombre)
        except Exception as e:
            err("%s: steering-examples.json inválido — %s" % (nombre, e))

    texto_readme = open(readme, encoding="utf-8").read() if os.path.exists(readme) else ""

    # 1 — el orquestador es de solo lectura local
    t = open(agente, encoding="utf-8").read()
    hab = herramientas_habilitadas(t)
    for h in sorted(hab & ESCRITURA):
        err("%s/agent.yaml: el orquestador concede '%s'. La escritura es de las hojas." % (nombre, h))
    for h in sorted(hab & RED):
        err("%s/agent.yaml: el orquestador concede '%s'. La red es de las hojas." % (nombre, h))
    if mcp_no_vacio(t):
        err("%s/agent.yaml: el orquestador declara servidores MCP. Los MCP van en las hojas." % nombre)

    # 2 y 3 — hojas
    con_escritura = []
    for hoja in hojas:
        rel = os.path.relpath(hoja, RAIZ)
        th = open(hoja, encoding="utf-8").read()
        habh = herramientas_habilitadas(th)

        if habh & ESCRITURA:
            con_escritura.append(os.path.basename(hoja))

        if "web_fetch" in habh:
            bloque = th[th.find("web_fetch"):]
            if "allowed_hosts" not in bloque:
                err("%s: habilita web_fetch sin lista blanca allowed_hosts." % rel)
            else:
                lista = re.search(r"allowed_hosts:\s*\n((?:\s+-\s*.+\n)+)", bloque)
                if not lista or not lista.group(1).strip():
                    err("%s: allowed_hosts está vacía." % rel)
            if "block_private_networks: true" not in bloque:
                aviso("%s: web_fetch sin block_private_networks: true." % rel)

        # 5 — el README declara lo que el YAML concede
        if texto_readme:
            for h in sorted(habh):
                if h not in texto_readme:
                    aviso("%s/README.md: no menciona la herramienta '%s' que concede %s."
                          % (nombre, h, os.path.basename(hoja)))

    if len(con_escritura) == 0:
        aviso("%s: ninguna hoja tiene escritura; el cookbook no puede producir salida." % nombre)
    elif len(con_escritura) > 1:
        err("%s: más de una hoja con escritura (%s). Debe haber exactamente una."
            % (nombre, ", ".join(con_escritura)))


def main():
    if not os.path.isdir(COOKBOOKS):
        err("no existe el directorio cookbooks-agentes/")
        return
    dirs = [d for d in sorted(glob.glob(os.path.join(COOKBOOKS, "*")))
            if os.path.isdir(d)]
    if not dirs:
        err("cookbooks-agentes/ no contiene cookbooks")
        return
    for d in dirs:
        revisar_cookbook(d)
    print("Cookbooks revisados: %d" % len(dirs))


if __name__ == "__main__":
    main()
    for a in AVISO:
        print("AVISO  ", a)
    for e in ERR:
        print("ERROR  ", e)
    print("\n%d error(es), %d aviso(s)" % (len(ERR), len(AVISO)))
    sys.exit(1 if ERR else 0)
