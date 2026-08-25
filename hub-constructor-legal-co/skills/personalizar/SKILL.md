---
name: personalizar
description: >
  Ajusta el perfil de práctica de Hub de Constructores Legales sin repetir la entrevista completa: cambiar
  una posición de la casa, un umbral de escalamiento, un destinatario de alertas, el
  estilo de los escritos o el estado de una integración. Actívela cuando el usuario diga
  que algo del perfil quedó mal, que cambió una política, o que quiere que las salidas
  se vean distinto.
---

# Personalizar — Hub de Constructores Legales

## Qué hace

Edita `~/.claude/plugins/config/claude-legal-colombia/hub-constructor-legal-co/CLAUDE.md` (y `~/.claude/plugins/config/claude-legal-colombia/perfil-organizacion.md` cuando el cambio es
de la organización y no del área) de forma quirúrgica.

## Cómo

1. **Leer antes de escribir.** Cargar el perfil actual y mostrar la sección que se va a
   tocar, tal como está hoy.
2. **Confirmar el cambio en una frase.** «Hoy dice X. ¿Lo cambio a Y?»
3. **Escribir solo esa sección.** No reescribir el archivo completo. No reformatear lo
   que no se pidió tocar.
4. **Decir qué skills quedan afectadas.** Un cambio de umbral de escalamiento cambia el
   comportamiento de varias skills; decir cuáles.

## Qué se puede cambiar

| Pedido típico | Sección que se toca |
|---|---|
| «Ese tope ya no es el nuestro» | `## Criterios de la casa` |
| «Ahora esto lo aprueba otra persona» | `## Escalamiento` |
| «Las alertas van a otro lado» | `## Estilo de la casa` |
| «Conectamos el gestor documental» | `## Integraciones disponibles` |
| «Los conceptos deben ser más cortos» | `## Estilo de la casa` |
| «Verificamos la tabla de normas» | `## Marco normativo de referencia` |
| «Queremos separar por casos» | `## Espacios de asunto` |
| «Somos más conservadores de lo que quedó» | `## Postura ante decisiones jurídicas discutibles` |

## Reglas

- **Nunca borrar una posición sin dejar constancia.** Si se reemplaza una posición de
  la casa, anotar la fecha del cambio al lado. El perfil es un documento que se audita.
- **Un `[PENDIENTE]` que se llena se llena con lo que dijo el usuario**, no con una
  redacción mejorada que cambie el sentido.
- **Si el cambio contradice derecho imperativo, decirlo.** El usuario puede fijar la
  política de la casa, pero no puede fijar que se acepte una cláusula nula. Ejemplo:
  «Puedo dejar registrada esa posición, pero tenga en cuenta que la condonación del dolo
  futuro no vale (CC art. 1522), así que la skill la va a marcar igual.»

## Si el perfil no existe

Decir: «Todavía no hay perfil que ajustar. ¿Corremos `/hub-constructor-legal-co:entrevista-inicial`?»
