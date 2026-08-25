# Datos Personales y Habeas Data

Implementa y sostiene el régimen colombiano de protección de datos: evaluación del tratamiento, política y aviso de privacidad, atención de consultas y reclamos en los términos de la Ley 1581 de 2012, gestión de incidentes de seguridad ante la SIC, transferencias y transmisiones internacionales, contratos de encargo y el régimen especial de dato financiero de la Ley 1266 de 2008.

> **Todo lo que produce este plugin es un borrador sujeto a revisión profesional.**
> No es concepto jurídico ni asesoría, y no reemplaza a un abogado titulado e inscrito.
> Ver [AVISO-LEGAL.md](../AVISO-LEGAL.md).

**Ámbito:** Habeas data, protección de datos personales y dato financiero y crediticio.

## Instalación

```bash
/plugin marketplace add oscarag2233-cyber/claude-legal-colombia
/plugin install datos-personales-co@claude-legal-colombia
```

Luego, sin excepción:

```bash
/datos-personales-co:entrevista-inicial
```

Sin la entrevista, las skills se detienen: prefieren no responder a responder genérico.

## Skills

### Propias del área

| Skill | Qué hace |
|---|---|
| `/datos-personales-co:evaluacion-de-tratamiento` | Mapea la actividad de tratamiento, determina rol (responsable o encargado), base de legitimación, riesgos y obligaciones que se activan. |
| `/datos-personales-co:politica-y-aviso` | Redacta política de tratamiento y aviso de privacidad con el contenido mínimo del Decreto 1074, ajustados al tratamiento real. |
| `/datos-personales-co:atender-consulta-o-reclamo` | Procesa la consulta o el reclamo del titular dentro de los términos legales, con la respuesta y el registro de trazabilidad. |
| `/datos-personales-co:incidente-de-seguridad` | Ruta de respuesta a una violación de datos: contención, evaluación, reporte a la SIC y comunicación a titulares. |
| `/datos-personales-co:transferencia-internacional` | Evalúa si la operación es transferencia o transmisión, qué exige cada una y cómo se documenta. |
| `/datos-personales-co:habeas-data-financiero` | Aplica la Ley 1266 y la Ley 2157: permanencia del dato negativo, notificación previa al reporte y rutas de corrección. |

### Comunes a todos los plugins

| Skill | Qué hace |
|---|---|
| `/datos-personales-co:entrevista-inicial` | Entrevista de arranque. Levanta el perfil de práctica, los criterios de la casa y el estado de las integraciones. **Córrala primero.** |
| `/datos-personales-co:personalizar` | Ajusta el perfil sin repetir la entrevista completa: cambiar una posición, un umbral, un destinatario. |
| `/datos-personales-co:verificar-citas` | Compuerta de verificación: toma una pieza y revisa cada norma, sentencia y término citado contra fuente oficial, dejando marcado lo que no se pudo confirmar. |
| `/datos-personales-co:espacio-de-asunto` | Crea, cambia y cierra espacios de asunto cuando se quiere aislar contexto y salidas por caso. |

## Agentes

| Agente | Qué hace |
|---|---|
| `vigia-de-terminos-habeas-data` | Vigila los términos de consultas y reclamos de titulares y avisa antes de que venzan los 10 y 15 días hábiles. |

Los agentes corren en la periodicidad que se configure y escriben en el
destino definido en el perfil de práctica. No radican, no firman y no deciden.

## Marco normativo que aplica

- **Constitución Política, arts. 15 y 20** — Derecho fundamental al habeas data y a la intimidad
- **Ley 1581 de 2012** — Régimen general de protección de datos personales (estatutaria). Principios (art. 4), datos sensibles (art. 5-7), derechos (art. 8), deberes (arts. 17-18), sanciones (art. 23)
- **Decreto 1074 de 2015, Libro 2, Parte 2, Título 2, Capítulo 25** — Compiló el Decreto 1377 de 2013: autorización, aviso de privacidad, política, transferencias, RNBD
- **Ley 1266 de 2008, modificada por la Ley 2157 de 2021** — Habeas data financiero, crediticio y comercial; permanencia del dato negativo
- **Ley 1273 de 2009** — Delitos informáticos: violación de datos personales (art. 269F)
- **Circulares externas de la SIC** — RNBD, incidentes de seguridad, transferencias internacionales `[verificar versión vigente]`
- **Sentencia C-748 de 2011** — Control previo de la Ley 1581; condicionamientos que siguen gobernando su interpretación `[verificar]`

La tabla completa, con su estado de verificación, está en el `CLAUDE.md` del plugin.

## Lo que este plugin NO hace

- Emitir asesoría jurídica. Todo lo que produce es borrador para revisión de abogado
- Radicar, firmar, notificar o comunicarse con autoridades o contrapartes por su cuenta
- Afirmar que una cita está verificada cuando no la recuperó de fuente oficial
- Decidir por usted una calificación jurídica discutible: la marca y la escala

## Configuración

La configuración del usuario vive en
`~/.claude/plugins/config/claude-legal-colombia/datos-personales-co/CLAUDE.md`,
fuera del control de versiones. El `CLAUDE.md` de este directorio es la **plantilla**
que la entrevista inicial copia allá.

El perfil de la organización, compartido por todos los plugins, vive en
`~/.claude/plugins/config/claude-legal-colombia/perfil-organizacion.md`.
