# Consultorio Jurídico

Sostiene la operación del consultorio jurídico universitario bajo la Ley 2113 de 2021: entrevista y ficha de consulta, concepto para el usuario en lenguaje claro, control de términos con criterio de prevención del daño, cola de revisión del docente antes de que salga cualquier pieza, y entrega ordenada de casos al final del semestre.

> **Todo lo que produce este plugin es un borrador sujeto a revisión profesional.**
> No es concepto jurídico ni asesoría, y no reemplaza a un abogado titulado e inscrito.
> Ver [AVISO-LEGAL.md](../AVISO-LEGAL.md).

**Ámbito:** Consultorios jurídicos y centros de conciliación universitarios; asistencia jurídica gratuita.

## Instalación

```bash
/plugin marketplace add oscarag2233-cyber/claude-legal-colombia
/plugin install consultorio-juridico-co@claude-legal-colombia
```

Luego, sin excepción:

```bash
/consultorio-juridico-co:entrevista-inicial
```

Sin la entrevista, las skills se detienen: prefieren no responder a responder genérico.

## Skills

### Propias del área

| Skill | Qué hace |
|---|---|
| `/consultorio-juridico-co:entrevista-de-consulta` | Guía la entrevista para levantar los hechos completos, identificar el problema jurídico y detectar términos que corran. |
| `/consultorio-juridico-co:concepto-para-usuario` | Redacta el concepto en lenguaje claro, con la ruta, los términos y lo que el usuario debe hacer y aportar. |
| `/consultorio-juridico-co:control-de-terminos` | Lleva el tablero de términos del consultorio con criterio de prevención del daño al usuario. |
| `/consultorio-juridico-co:cola-de-revision-docente` | Ninguna pieza sale sin revisión: arma la cola con lo que el docente necesita para revisar rápido. |
| `/consultorio-juridico-co:entrega-de-semestre` | Prepara la entrega de casos al siguiente estudiante con todo lo que hay que saber para no perder un término. |

### Comunes a todos los plugins

| Skill | Qué hace |
|---|---|
| `/consultorio-juridico-co:entrevista-inicial` | Entrevista de arranque. Levanta el perfil de práctica, los criterios de la casa y el estado de las integraciones. **Córrala primero.** |
| `/consultorio-juridico-co:personalizar` | Ajusta el perfil sin repetir la entrevista completa: cambiar una posición, un umbral, un destinatario. |
| `/consultorio-juridico-co:verificar-citas` | Compuerta de verificación: toma una pieza y revisa cada norma, sentencia y término citado contra fuente oficial, dejando marcado lo que no se pudo confirmar. |
| `/consultorio-juridico-co:espacio-de-asunto` | Crea, cambia y cierra espacios de asunto cuando se quiere aislar contexto y salidas por caso. |

## Agentes

| Agente | Qué hace |
|---|---|
| `vigia-de-consultorio` | Revisa la cola de casos y avisa términos próximos y piezas pendientes de revisión docente. |

Los agentes corren en la periodicidad que se configure y escriben en el
destino definido en el perfil de práctica. No radican, no firman y no deciden.

## Marco normativo que aplica

- **Ley 2113 de 2021** — Consultorios jurídicos: naturaleza, funciones, competencias y supervisión docente
- **Decreto 196 de 1971 y Ley 1123 de 2007** — Ejercicio de la abogacía y régimen disciplinario aplicable a quien supervisa
- **Ley 1564 de 2012** — CGP: amparo de pobreza, representación y competencias
- **Ley 2220 de 2022** — Conciliación en centros universitarios `[verificar]`
- **Ley 1581 de 2012** — Protección de datos de los usuarios del consultorio

La tabla completa, con su estado de verificación, está en el `CLAUDE.md` del plugin.

## Lo que este plugin NO hace

- Emitir asesoría jurídica. Todo lo que produce es borrador para revisión de abogado
- Radicar, firmar, notificar o comunicarse con autoridades o contrapartes por su cuenta
- Afirmar que una cita está verificada cuando no la recuperó de fuente oficial
- Decidir por usted una calificación jurídica discutible: la marca y la escala

## Configuración

La configuración del usuario vive en
`~/.claude/plugins/config/claude-legal-colombia/consultorio-juridico-co/CLAUDE.md`,
fuera del control de versiones. El `CLAUDE.md` de este directorio es la **plantilla**
que la entrevista inicial copia allá.

El perfil de la organización, compartido por todos los plugins, vive en
`~/.claude/plugins/config/claude-legal-colombia/perfil-organizacion.md`.
