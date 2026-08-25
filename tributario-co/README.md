# Tributario

Trabaja el procedimiento y el riesgo tributario bajo el Estatuto Tributario: revisión de declaraciones y correcciones, respuesta a requerimientos especiales y pliegos, recurso de reconsideración, procedimiento administrativo de cobro coactivo, obligaciones formales y facturación electrónica, y análisis de riesgo de posiciones fiscales antes de tomarlas.

> **Todo lo que produce este plugin es un borrador sujeto a revisión profesional.**
> No es concepto jurídico ni asesoría, y no reemplaza a un abogado titulado e inscrito.
> Ver [AVISO-LEGAL.md](../AVISO-LEGAL.md).

**Ámbito:** Procedimiento tributario nacional y territorial, obligaciones formales y contingencias fiscales.

## Instalación

```bash
/plugin marketplace add oscarag2233-cyber/claude-legal-colombia
/plugin install tributario-co@claude-legal-colombia
```

Luego, sin excepción:

```bash
/tributario-co:entrevista-inicial
```

Sin la entrevista, las skills se detienen: prefieren no responder a responder genérico.

## Skills

### Propias del área

| Skill | Qué hace |
|---|---|
| `/tributario-co:revision-de-declaracion` | Revisa la declaración contra el soporte, identifica inconsistencias y decide entre corrección voluntaria, provocada o defensa. |
| `/tributario-co:respuesta-a-requerimiento` | Responde el requerimiento especial o el emplazamiento dentro del término, con prueba y con la discusión jurídica que después sostiene el recurso. |
| `/tributario-co:recurso-de-reconsideracion` | Sustenta el recurso preservando los cargos para la eventual demanda de nulidad y restablecimiento. |
| `/tributario-co:cobro-coactivo` | Ruta frente al mandamiento de pago: excepciones, facilidades de pago, medidas cautelares y prescripción de la acción de cobro. |
| `/tributario-co:riesgo-de-posicion-fiscal` | Evalúa una posición antes de tomarla: soporte normativo, doctrina de la DIAN, jurisprudencia y exposición sancionatoria. |

### Comunes a todos los plugins

| Skill | Qué hace |
|---|---|
| `/tributario-co:entrevista-inicial` | Entrevista de arranque. Levanta el perfil de práctica, los criterios de la casa y el estado de las integraciones. **Córrala primero.** |
| `/tributario-co:personalizar` | Ajusta el perfil sin repetir la entrevista completa: cambiar una posición, un umbral, un destinatario. |
| `/tributario-co:verificar-citas` | Compuerta de verificación: toma una pieza y revisa cada norma, sentencia y término citado contra fuente oficial, dejando marcado lo que no se pudo confirmar. |
| `/tributario-co:espacio-de-asunto` | Crea, cambia y cierra espacios de asunto cuando se quiere aislar contexto y salidas por caso. |

## Agentes

| Agente | Qué hace |
|---|---|
| `vigia-tributario` | Avisa vencimientos de calendario tributario, términos de respuesta a requerimientos y fechas de firmeza de las declaraciones. |

Los agentes corren en la periodicidad que se configure y escriben en el
destino definido en el perfil de práctica. No radican, no firman y no deciden.

## Marco normativo que aplica

- **Estatuto Tributario (Decreto 624 de 1989)** — Procedimiento: firmeza (art. 714), requerimiento especial (arts. 703-707), liquidación de revisión (art. 710), recurso de reconsideración (art. 720), sanciones (arts. 634 y ss.), cobro coactivo (arts. 823 y ss.)
- **Ley 2277 de 2022** — Reforma tributaria para la igualdad y la justicia social `[verificar artículos declarados inexequibles]`
- **Ley 2010 de 2019** — Ley de crecimiento económico; reexpidió buena parte de la Ley 1943 de 2018
- **Sentencia C-481 de 2019** — Inexequibilidad de la Ley 1943 de 2018 por vicios de trámite, con efectos diferidos `[verificar]`
- **Decreto 1625 de 2016** — DUR en materia tributaria
- **Ley 1437 de 2011** — CPACA: control judicial de los actos de la DIAN
- **Resoluciones de la DIAN** — Facturación electrónica, UVT, plazos y formularios `[verificar año]`

La tabla completa, con su estado de verificación, está en el `CLAUDE.md` del plugin.

## Lo que este plugin NO hace

- Emitir asesoría jurídica. Todo lo que produce es borrador para revisión de abogado
- Radicar, firmar, notificar o comunicarse con autoridades o contrapartes por su cuenta
- Afirmar que una cita está verificada cuando no la recuperó de fuente oficial
- Decidir por usted una calificación jurídica discutible: la marca y la escala

## Configuración

La configuración del usuario vive en
`~/.claude/plugins/config/claude-legal-colombia/tributario-co/CLAUDE.md`,
fuera del control de versiones. El `CLAUDE.md` de este directorio es la **plantilla**
que la entrevista inicial copia allá.

El perfil de la organización, compartido por todos los plugins, vive en
`~/.claude/plugins/config/claude-legal-colombia/perfil-organizacion.md`.
