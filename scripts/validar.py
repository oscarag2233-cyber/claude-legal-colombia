#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Validador del marketplace claude-legal-colombia.

Comprueba las invariantes del manifiesto, el frontmatter de skills y agentes, la
coherencia entre marketplace.json y cada plugin.json, y que toda referencia del tipo
`/plugin:skill` que aparezca en prosa apunte a una skill que existe.

Uso:  python3 scripts/validar.py
Sale con código 1 si hay errores.
"""
import glob
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ERR, WARN = [], []


def err(m):
    ERR.append(m)


def warn(m):
    WARN.append(m)


def frontmatter(ruta):
    with open(ruta, encoding="utf-8") as f:
        t = f.read()
    if not t.startswith("---\n"):
        return None, t
    fin = t.find("\n---\n", 4)
    if fin == -1:
        return None, t
    return t[4:fin], t[fin + 5:]


def campo(fm, nombre):
    m = re.search(r"^%s:\s*(.*)$" % nombre, fm, re.M)
    return m.group(1).strip() if m else None


def main():
    mp_ruta = os.path.join(RAIZ, ".claude-plugin", "marketplace.json")
    if not os.path.exists(mp_ruta):
        err("falta .claude-plugin/marketplace.json")
        return
    mp = json.load(open(mp_ruta, encoding="utf-8"))

    nombres = [p["name"] for p in mp["plugins"]]
    # I1 orden alfabético
    if nombres != sorted(nombres, key=str.lower):
        warn("marketplace.plugins no está ordenado alfabéticamente")
    # I2 sin duplicados
    if len(nombres) != len(set(nombres)):
        err("hay nombres de plugin duplicados en marketplace.json")

    for entrada in mp["plugins"]:
        n = entrada["name"]
        # I11 formato del nombre
        if not re.match(r"^[a-z0-9][a-z0-9-]{1,63}$", n):
            err("%s: el nombre no cumple ^[a-z0-9][a-z0-9-]{1,63}$" % n)
        # I3 descripción
        d = entrada.get("description", "")
        if not (10 <= len(d) <= 2000):
            err("%s: descripción de %d caracteres (debe estar entre 10 y 2000)" % (n, len(d)))
        if d != d.strip():
            err("%s: la descripción tiene espacios al inicio o al final" % n)
        # I9 source seguro
        src = entrada.get("source", "")
        if ".." in src or any(c in src for c in ";|&$`"):
            err("%s: source con caracteres peligrosos o '..'" % n)
        # I10 unicode oculto
        for campo_t in (n, d):
            if any(ord(c) in (0x200b, 0x200c, 0x200d, 0x202e, 0xfeff) for c in campo_t):
                err("%s: contiene caracteres Unicode ocultos" % n)
        # I8 el source apunta a un plugin real
        dirp = os.path.join(RAIZ, src.lstrip("./"))
        pj = os.path.join(dirp, ".claude-plugin", "plugin.json")
        if not os.path.exists(pj):
            err("%s: source '%s' no contiene .claude-plugin/plugin.json" % (n, src))
            continue
        plug = json.load(open(pj, encoding="utf-8"))
        if plug["name"] != n:
            err("%s: plugin.json declara name '%s'" % (n, plug["name"]))
        if plug.get("description") != d:
            err("%s: la descripción de plugin.json no coincide con marketplace.json" % n)
        if plug.get("author") != entrada.get("author"):
            err("%s: el author de plugin.json no coincide con marketplace.json" % n)

    # Frontmatter de skills y agentes
    skills_existentes = set()
    for sk in glob.glob(os.path.join(RAIZ, "*", "skills", "*", "SKILL.md")):
        rel = os.path.relpath(sk, RAIZ)
        plugin = rel.split(os.sep)[0]
        nombre_dir = rel.split(os.sep)[2]
        skills_existentes.add("%s:%s" % (plugin, nombre_dir))
        fm, _ = frontmatter(sk)
        if fm is None:
            err("%s: sin frontmatter" % rel)
            continue
        if not campo(fm, "description"):
            err("%s: falta 'description' en el frontmatter" % rel)
        n = campo(fm, "name")
        if n and n != nombre_dir:
            err("%s: frontmatter name '%s' ≠ directorio '%s'" % (rel, n, nombre_dir))

    for ag in glob.glob(os.path.join(RAIZ, "*", "agents", "*.md")):
        rel = os.path.relpath(ag, RAIZ)
        fm, _ = frontmatter(ag)
        if fm is None:
            err("%s: sin frontmatter" % rel)
            continue
        for c in ("name", "description"):
            if not campo(fm, c):
                err("%s: falta '%s' en el frontmatter" % (rel, c))

    # Referencias /plugin:skill en prosa
    patron = re.compile(r"/([a-z0-9][a-z0-9-]{1,63}):([a-z0-9][a-z0-9-]{1,63})")
    for md in glob.glob(os.path.join(RAIZ, "**", "*.md"), recursive=True):
        rel = os.path.relpath(md, RAIZ)
        if rel.startswith(("referencias", "cookbooks-agentes")) or os.sep not in rel:
            continue
        texto = open(md, encoding="utf-8").read()
        for plugin, skill in set(patron.findall(texto)):
            if plugin not in nombres:
                continue
            if "%s:%s" % (plugin, skill) not in skills_existentes:
                err("%s: referencia a /%s:%s pero esa skill no existe" % (rel, plugin, skill))

    # JSON parseable y formato de archivos
    for j in glob.glob(os.path.join(RAIZ, "**", "*.json"), recursive=True):
        try:
            json.load(open(j, encoding="utf-8"))
        except Exception as e:
            err("%s: JSON inválido — %s" % (os.path.relpath(j, RAIZ), e))

    for t in glob.glob(os.path.join(RAIZ, "**", "*.md"), recursive=True):
        contenido = open(t, encoding="utf-8").read()
        rel = os.path.relpath(t, RAIZ)
        if contenido and not contenido.endswith("\n"):
            warn("%s: falta el salto de línea final" % rel)
        if re.search(r"[ \t]+\n", contenido):
            warn("%s: tiene espacios en blanco al final de alguna línea" % rel)


if __name__ == "__main__":
    main()
    for w in WARN:
        print("AVISO  ", w)
    for e in ERR:
        print("ERROR  ", e)
    print("\n%d error(es), %d aviso(s)" % (len(ERR), len(WARN)))
    sys.exit(1 if ERR else 0)
