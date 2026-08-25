---
name: entrevista-inicial
description: >
  Entrevista de arranque del plugin Datos Personales y Habeas Data. Levanta el perfil de la organización, el
  perfil de práctica del área, los criterios de la casa, el escalamiento y el estado de
  las integraciones, y los escribe en la configuración del usuario. Es la única skill
  que corre sin configuración previa, y todas las demás dependen de ella. Actívela
  cuando el usuario instale el plugin, cuando pida configurarlo, o cuando otra skill se
  haya detenido por falta de configuración.
---

# Entrevista inicial — Datos Personales y Habeas Data

## Qué produce

Dos archivos:

1. `~/.claude/plugins/config/claude-legal-colombia/perfil-organizacion.md` — compartido por todos los plugins. Si ya existe, no
   se repiten esas preguntas: se leen y se confirman en una sola pantalla.
2. `~/.claude/plugins/config/claude-legal-colombia/datos-personales-co/CLAUDE.md` — el perfil de práctica de esta área, a partir de la
   plantilla que trae el plugin.

## Cómo se conduce

**Una pregunta a la vez.** No se lanzan diez preguntas en un bloque. Se pregunta, se
escucha, se repregunta si la respuesta quedó a medias, y se sigue. La entrevista dura
entre 10 y 15 minutos y produce un archivo que el usuario va a editar durante meses.

**Se puede pausar.** Si el usuario dice «después», se guarda lo que haya, se marca lo
que falta y se dice exactamente qué skills no van a funcionar hasta completar.

**No se inventan respuestas.** Si el usuario no sabe cuál es la posición de la casa
sobre algo, se deja `[PENDIENTE]` y se anota que esa skill va a preguntar cuando llegue
el caso. Un `[PENDIENTE]` honesto es mejor que un valor por defecto que nadie decidió.

## Banderas

- `--completa` — entrevista entera (por defecto en la primera ejecución).
- `--revisar-integraciones` — solo verifica qué conectores están respondiendo y
  actualiza esa tabla. Corre sin configuración previa.
- `--solo-criterios` — vuelve sobre la sección de criterios de la casa.

## Secuencia

### Bloque 0 — Antes de preguntar nada

Verificar si existe `~/.claude/plugins/config/claude-legal-colombia/perfil-organizacion.md`. Si existe, leerlo y mostrar un
resumen de tres líneas: «Ya tengo esto de su organización: [...]. ¿Sigue vigente?»
Si no existe, arrancar por el Bloque 1.

Verificar también si hay un `CLAUDE.md` diligenciado en la ruta antigua de caché del
plugin; si lo hay y no hay uno en la ruta de configuración, copiarlo antes de seguir.

### Bloque 1 — Quiénes son *(solo si no existe el perfil de organización)*

1. ¿Cómo se llama la organización y qué es? (firma, departamento jurídico, despacho
   individual, consultorio, entidad pública)
2. ¿Cuántas personas son en el equipo jurídico?
3. ¿En qué ciudades y circuitos actúan?
4. ¿Cuál es el sector o la industria?

### Bloque 2 — Quién va a usar esto

5. ¿Usted es abogado con tarjeta profesional vigente?
   - **Si sí:** registrar nombre y T.P. El encabezado de producto de trabajo será el de
     abogado.
   - **Si no:** preguntar si tiene abogado a quien consultar y quién es. El encabezado
     será el de notas de trabajo y **se activa la compuerta de revisión profesional en
     todas las skills**. Decirlo explícitamente ahora, no cuando ya esté por radicar.

6. ¿Es firma que representa clientes, área jurídica de una empresa, o ambas cosas?
   Esta respuesta cambia los encabezados, las compuertas y a quién se escala.

### Bloque 3 — Lo que duele

7. «¿Qué es lo que más tiempo le quita o más problemas le ha traído en Habeas data, protección de datos personales y dato financiero y crediticio?»
   Recoger la respuesta **en las palabras del usuario** y ponerla textual en el perfil.
   Esa frase es la que orienta qué skill se sugiere primero después.

### Bloque 4 — Criterios de la casa

Recorrer, una por una, las decisiones que este plugin necesita resueltas:

- Postura sobre bases de legitimación distintas de la autorización
- Umbral para reportar un incidente a la SIC
- Política sobre uso de datos de clientes en herramientas de IA
- Responsable interno del RNBD y de la atención de titulares

Para cada una: ¿cuál es la posición estándar, cuál es la alternativa que aceptan, y
qué es lo que nunca aceptan? Si el usuario duda, ofrecer dos o tres opciones típicas
del mercado colombiano **marcadas como sugerencia**, no como estándar. Nunca escribir
una posición que el usuario no haya confirmado.

### Bloque 5 — Escalamiento

8. ¿Quién puede decidir qué, sin consultar?
9. ¿A quién se escala y por qué medio?
10. ¿Qué escala siempre, sin importar la cuantía?

### Bloque 6 — Integraciones

Recorrer y marcar ✓/✗:

- Gestor documental
- Correo
- Herramienta de anonimización

Para cada una que esté en ✗, decir en una línea qué se hace en su lugar. El usuario
debe salir de la entrevista sabiendo qué va a tener que hacer a mano.

### Bloque 7 — Estilo y salidas

11. ¿Cómo tratan al juez o a la autoridad en los escritos?
12. ¿Dónde queda el producto de trabajo?
13. ¿A dónde van las alertas de términos?
14. ¿Extensión típica de un concepto?

### Bloque 8 — Documentos semilla

15. «¿Tiene minutas, manuales, formatos o conceptos modelo de la casa? Si me los
    señala, los uso como referencia de estilo y de posiciones.»

Registrar cada uno en la tabla `## Documentos semilla revisados`. **No copiar su
contenido al perfil**: registrar la ruta y qué aporta.

### Bloque 9 — Verificación normativa

16. «La tabla de marco normativo de este plugin trae [N] normas. ¿Quiere que alguien
    del equipo verifique su vigencia y firme esa tabla? Es lo que después permite que
    las skills citen sin marca de duda.»

Registrar quién y cuándo en `**Estado de verificación de esta tabla:**`.

## Al cerrar

1. Escribir los dos archivos.
2. Mostrar un resumen de lo que quedó `[PENDIENTE]` y qué skill lo va a pedir.
3. Sugerir **una** skill concreta para empezar, elegida por lo que el usuario respondió
   en el Bloque 3.
4. Recordar en una línea: todo lo que salga de aquí es borrador para revisión
   profesional.

## Lo que esta skill NO hace

- No decide por el usuario las posiciones de la casa.
- No llena `[PENDIENTE]` con valores por defecto.
- No copia documentos del usuario al repositorio.
