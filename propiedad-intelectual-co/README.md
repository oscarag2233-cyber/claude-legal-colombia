# Propiedad Intelectual

Gestiona la propiedad intelectual bajo el régimen andino y la ley colombiana: viabilidad y registro de marca ante la SIC con análisis de confundibilidad, oposiciones y cancelaciones, derecho de autor y registro de software ante la DNDA, contratos de licencia y cesión, acciones por infracción y competencia desleal, y control de vencimientos de la cartera.

> **Todo lo que produce este plugin es un borrador sujeto a revisión profesional.**
> No es concepto jurídico ni asesoría, y no reemplaza a un abogado titulado e inscrito.
> Ver [AVISO-LEGAL.md](../AVISO-LEGAL.md).

**Ámbito:** Propiedad industrial (marcas, patentes, diseños), derecho de autor y derechos conexos, secretos empresariales.

## Instalación

```bash
/plugin marketplace add oscarag2233-cyber/claude-legal-colombia
/plugin install propiedad-intelectual-co@claude-legal-colombia
```

Luego, sin excepción:

```bash
/propiedad-intelectual-co:entrevista-inicial
```

Sin la entrevista, las skills se detienen: prefieren no responder a responder genérico.

## Skills

### Propias del área

| Skill | Qué hace |
|---|---|
| `/propiedad-intelectual-co:viabilidad-de-marca` | Analiza distintividad, causales absolutas y relativas y riesgo de confusión antes de gastar en un registro que se va a negar. |
| `/propiedad-intelectual-co:oposicion-y-cancelacion` | Arma la oposición o la cancelación por no uso con la carga probatoria que exige la Decisión 486. |
| `/propiedad-intelectual-co:derecho-de-autor-y-software` | Determina titularidad, obra por encargo y relación laboral, y arma el registro ante la DNDA. |
| `/propiedad-intelectual-co:contratos-de-pi` | Licencia, cesión y desarrollo: qué se transfiere, qué no se puede transferir y qué exige el registro para ser oponible. |
| `/propiedad-intelectual-co:infraccion-y-cese` | Evalúa la infracción, redacta el requerimiento de cese y define la vía y las cautelares. |

### Comunes a todos los plugins

| Skill | Qué hace |
|---|---|
| `/propiedad-intelectual-co:entrevista-inicial` | Entrevista de arranque. Levanta el perfil de práctica, los criterios de la casa y el estado de las integraciones. **Córrala primero.** |
| `/propiedad-intelectual-co:personalizar` | Ajusta el perfil sin repetir la entrevista completa: cambiar una posición, un umbral, un destinatario. |
| `/propiedad-intelectual-co:verificar-citas` | Compuerta de verificación: toma una pieza y revisa cada norma, sentencia y término citado contra fuente oficial, dejando marcado lo que no se pudo confirmar. |
| `/propiedad-intelectual-co:espacio-de-asunto` | Crea, cambia y cierra espacios de asunto cuando se quiere aislar contexto y salidas por caso. |

## Agentes

| Agente | Qué hace |
|---|---|
| `vigia-de-cartera-pi` | Vigila vencimientos de renovación de marcas, anualidades de patentes y plazos de oposición y de prueba de uso. |

Los agentes corren en la periodicidad que se configure y escriben en el
destino definido en el perfil de práctica. No radican, no firman y no deciden.

## Marco normativo que aplica

- **Decisión Andina 486 de 2000** — Régimen común de propiedad industrial: marcas (arts. 134-189), patentes, diseños, secretos empresariales, acciones por infracción (arts. 238 y ss.)
- **Decisión Andina 351 de 1993** — Régimen común de derecho de autor y derechos conexos
- **Ley 23 de 1982** — Derecho de autor en Colombia
- **Ley 1915 de 2018** — Modernización del derecho de autor: excepciones, medidas tecnológicas, indemnizaciones preestablecidas
- **Ley 256 de 1996** — Competencia desleal, incluida la explotación de la reputación ajena y la violación de secretos
- **Ley 1564 de 2012** — CGP: proceso verbal para infracción; facultades jurisdiccionales de la SIC
- **Circular Única de la SIC — Título X** — Trámites de propiedad industrial `[verificar versión vigente]`

La tabla completa, con su estado de verificación, está en el `CLAUDE.md` del plugin.

## Lo que este plugin NO hace

- Emitir asesoría jurídica. Todo lo que produce es borrador para revisión de abogado
- Radicar, firmar, notificar o comunicarse con autoridades o contrapartes por su cuenta
- Afirmar que una cita está verificada cuando no la recuperó de fuente oficial
- Decidir por usted una calificación jurídica discutible: la marca y la escala

## Configuración

La configuración del usuario vive en
`~/.claude/plugins/config/claude-legal-colombia/propiedad-intelectual-co/CLAUDE.md`,
fuera del control de versiones. El `CLAUDE.md` de este directorio es la **plantilla**
que la entrevista inicial copia allá.

El perfil de la organización, compartido por todos los plugins, vive en
`~/.claude/plugins/config/claude-legal-colombia/perfil-organizacion.md`.
