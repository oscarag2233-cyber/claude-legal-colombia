# CLAUDE.md

Guía para trabajar **en este repositorio**. `claude-legal-colombia` es un marketplace
de plugins de Claude Code: diecinueve plugins jurídicos colombianos y sus cookbooks de
agentes. Casi todo el trabajo aquí es editar contenido de prompts (skills, agentes,
perfiles) y metadatos, no código de aplicación.

## Distribución

```
.claude-plugin/marketplace.json   # manifiesto — una entrada por plugin (GENERADO)
<plugin>/                         # 19 plugins
  .claude-plugin/plugin.json      # manifiesto del plugin (GENERADO)
  .mcp.json                       # servidores MCP (GENERADO)
  CLAUDE.md                       # PLANTILLA del perfil de práctica (GENERADO)
  README.md                       # documentación del plugin (GENERADO)
  skills/<nombre>/SKILL.md         # skills — las propias se escriben A MANO
  agents/<nombre>.md               # agentes — A MANO
  hooks/hooks.json                 # ganchos (GENERADO, vacío por defecto)
referencias/                      # material compartido — A MANO
cookbooks-agentes/<nombre>/       # orquestador + subagentes + ejemplos de conducción
scripts/
  registro.py                     # FUENTE DE VERDAD: metadatos de los 19 plugins
  _bloques.py                     # bloques de texto compartidos (guardarraíles, salidas)
  generar-comunes.py              # emite todo lo marcado (GENERADO)
  validar.py                      # validador
```

## Regla número uno: no edite a mano lo que se genera

`marketplace.json`, `plugin.json`, `.mcp.json`, `hooks.json`, el `CLAUDE.md` y el
`README.md` de cada plugin, y las cuatro skills comunes
(`entrevista-inicial`, `personalizar`, `verificar-citas`, `espacio-de-asunto`)
**se generan**. Editarlos a mano funciona hasta la próxima generación y luego se pierde.

Para cambiarlos:

1. Metadatos de un plugin (descripción, normas, autoridades, integraciones, criterios,
   skills que anuncia el README) → `scripts/registro.py`.
2. Texto que comparten todos los plugins (guardarraíles, encabezados de salida, postura)
   → `scripts/_bloques.py`.
3. Estructura de las skills comunes o de la plantilla de perfil →
   `scripts/generar-comunes.py`.

Luego:

```bash
python3 scripts/generar-comunes.py
python3 scripts/validar.py
```

Las **skills propias** de cada área (`revisar-contrato`, `redactar-demanda`,
`liquidar-prestaciones`, …) y los **agentes** se escriben a mano y el generador no los
toca.

## Validación antes de abrir un PR

```bash
python3 scripts/generar-comunes.py     # 1. regenerar el andamiaje
python3 scripts/validar.py             # 2. validar (debe salir 0 errores)
python3 scripts/verificar-alcance.py   # 3. alcance de los cookbooks (0 errores)
```

El validador comprueba:

- **Manifiesto:** orden alfabético, sin duplicados, `name` con formato válido,
  descripción entre 10 y 2000 caracteres sin espacios sobrantes, `source` sin `..` ni
  metacaracteres, sin Unicode oculto, y que cada `source` apunte a un directorio con
  `.claude-plugin/plugin.json`.
- **Coherencia:** `name`, `description` y `author` iguales en `marketplace.json` y en
  `plugin.json`.
- **Frontmatter:** toda `SKILL.md` con `description`, y `name` coincidente con el
  directorio; todo `agents/*.md` con `name` y `description`.
- **Referencias de skill en prosa:** toda mención `/plugin:skill` debe apuntar a una
  skill que exista. Este chequeo es el que impide anunciar comandos muertos.
- **JSON parseable**, salto de línea final, sin espacios al final de línea.

## Cookbooks de agentes

Cada `cookbooks-agentes/<nombre>/` tiene `agent.yaml` (orquestador),
`subagents/*.yaml` (hojas), `steering-examples.json` y `README.md`. Dos reglas que
`scripts/verificar-alcance.py` hace cumplir:

1. **El orquestador solo tiene herramientas locales de lectura** (`read`, `grep`, `glob`).
   La red y los MCP viven en hojas específicas; la escritura, en **una sola** hoja.
2. **El README de cada cookbook debe declarar lo que el YAML concede.** No prometer menos
   herramientas de las que el manifiesto habilita.

Y una tercera, que no es automatizable pero es la que importa: **toda hoja con `web_fetch`
lee contenido no confiable.** Su prompt debe decirlo, su `allowed_hosts` debe ser corta, y
el resultado nunca puede ser una acción: solo datos estructurados.

## Convenciones de contenido jurídico

Estas no son de estilo; son de responsabilidad profesional.

1. **Ninguna cita se declara verificada si no se recuperó de fuente oficial en la
   sesión.** El valor por defecto es `[conocimiento del modelo — verificar]`. Ver
   `referencias/verificacion-de-fuentes.md`.
2. **Ningún término sale como número suelto.** Norma que lo fija, hábiles o calendario,
   día de inicio y su razón, advertencia de calendario judicial.
3. **Toda skill que produzca una pieza que va a salir del despacho** debe cerrar con la
   nota al revisor y con el árbol de próximos pasos, y debe pasar por la compuerta de
   revisión profesional cuando el Rol configurado no sea abogado inscrito.
4. **Ninguna skill escribe datos de clientes al repositorio.** La configuración y los
   asuntos viven en `~/.claude/plugins/config/claude-legal-colombia/`.
5. **Los criterios de la casa no pueden autorizar lo que la ley prohíbe.** Si el usuario
   configura una posición que choca con derecho imperativo, la skill la marca igual.

## Cómo se escribe una skill propia

Estructura mínima:

```markdown
---
name: <igual al directorio>
description: >
  Qué hace y cuándo se activa, con las frases que el usuario diría. Este campo decide
  si la skill se usa; escríbalo pensando en el disparo, no en el resumen.
---

# Título

## Antes de empezar
Compuerta: qué se lee del perfil, qué se detiene si falta, qué se pregunta.

## Qué produce
## Marco normativo que aplica
## Cómo se hace
## Salida
## Compuertas y advertencias
## Lo que esta skill NO hace
```

Reglas de redacción:

- **Densidad, no volumen.** Una skill de 120 líneas útiles vence a una de 400 que
  repite guardarraíles ya escritos en el perfil. Referencie la sección canónica del
  `CLAUDE.md` del plugin en vez de copiarla.
- **Nombres de skill reales.** Si escribe «corra `/foo`», `foo` debe existir.
- **Las tablas normativas van con artículo**, no solo con el nombre de la ley.
- **Todo umbral en SMLMV o UVT va con el año.**

## Cosas que se dejan quietas

- Las tablas de `referencias/valores-anuales.md` caducan cada año a propósito y llevan
  marcas `[verificar]` deliberadas. No las «limpie».
- Las marcas `[verificar]` sobre jurisprudencia y sobre circulares de superintendencia
  son intencionales: quitar la marca sin haber verificado es exactamente el error que
  el repositorio trata de evitar.
- Los `.gitignore` de cada plugin excluyen `config/`, `asuntos/` y
  `bitacora-verificacion.md`. No los relaje.
