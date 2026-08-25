# Cómo contribuir

## Lo que más sirve

1. **Correcciones normativas.** Una norma mal citada, una vigencia equivocada, una
   exequibilidad condicionada que falta. Esto es lo más valioso que puede aportar.
2. **Jurisprudencia superada.** Una línea que cambió, una sentencia de unificación
   posterior.
3. **Skills nuevas** de un área que falta, o de un procedimiento que se usa mucho.
4. **Rutas procesales reales.** Cómo funciona de verdad en su circuito, que no siempre
   es como dice el código.

## Reglas del contenido jurídico

**Toda cita se aporta verificada.** En el PR, indique la fuente oficial consultada y la
fecha. Si no la verificó, márquela `[verificar]` y dígalo.

**Nada de datos reales.** Ni expedientes, ni nombres de clientes, ni radicados de casos
en curso. Los ejemplos van hipotéticos o anonimizados. Cargar un expediente real a un
repositorio viola la reserva profesional y la Ley 1581 de 2012.

**No afirme lo que no sabe.** Un `[PENDIENTE]` honesto vale más que un valor por
defecto que nadie decidió. Una skill que dice «no sé, verifique aquí» es mejor que una
que inventa con seguridad.

## Reglas técnicas

- **Frontmatter:** toda `SKILL.md` necesita `name` y `description`; todo `agents/*.md`
  necesita `name` y `description`. El `name` debe coincidir con el nombre del directorio.
- **Los nombres de skill en prosa deben ser reales.** Si una skill dice «corra `/foo`»,
  `foo` debe ser un directorio que exista. El validador lo comprueba.
- **El `CLAUDE.md` de cada plugin es una plantilla**, no contexto de proyecto. Nunca
  escriba datos de usuario ahí.
- **El andamiaje común se genera.** Si va a cambiar la entrevista inicial, la
  personalización, la verificación de citas o el espacio de asunto, edite
  `scripts/generar-comunes.py` o `scripts/_bloques.py` y regenere. No edite los
  archivos generados a mano: se pierden en la siguiente generación.
- **Formato:** JSON con indentación de 2 espacios, salto de línea final en todo archivo
  de texto, sin espacios al final de línea.

## Antes de abrir el PR

```bash
python3 scripts/generar-comunes.py
python3 scripts/validar.py
```

El validador debe salir con 0 errores.

## Estructura de una skill nueva

```
<plugin>/skills/<nombre-en-kebab>/SKILL.md
```

```markdown
---
name: nombre-en-kebab
description: >
  Qué hace y cuándo debe activarse, en términos de lo que el usuario diría. Incluya las
  frases que la deben disparar. Este campo es lo que decide si la skill se usa o no.
---

# Título

## Antes de empezar
[Compuerta: qué se necesita del perfil, qué se detiene si falta]

## Qué produce
## Cómo se hace
## Salida
## Compuertas y advertencias
## Lo que esta skill NO hace
```

Ver `hub-constructor-legal-co/skills/crear-skill-juridica/SKILL.md` para el detalle.

## Código de conducta

[CODIGO-DE-CONDUCTA.md](CODIGO-DE-CONDUCTA.md).
