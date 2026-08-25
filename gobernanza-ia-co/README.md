# Gobernanza de Inteligencia Artificial

Gobierna el uso de IA en la organización y en la práctica jurídica desde el marco colombiano: inventario de sistemas, triage de casos de uso por riesgo, evaluación de impacto que cruza protección de datos y derechos fundamentales, política interna de uso de IA, revisión de contratos con proveedores de IA, y las reglas de uso de IA generativa en actuaciones judiciales.

> **Todo lo que produce este plugin es un borrador sujeto a revisión profesional.**
> No es concepto jurídico ni asesoría, y no reemplaza a un abogado titulado e inscrito.
> Ver [AVISO-LEGAL.md](../AVISO-LEGAL.md).

**Ámbito:** Gobernanza, riesgo y cumplimiento de sistemas de inteligencia artificial en Colombia.

## Instalación

```bash
/plugin marketplace add oscarag2233-cyber/claude-legal-colombia
/plugin install gobernanza-ia-co@claude-legal-colombia
```

Luego, sin excepción:

```bash
/gobernanza-ia-co:entrevista-inicial
```

Sin la entrevista, las skills se detienen: prefieren no responder a responder genérico.

## Skills

### Propias del área

| Skill | Qué hace |
|---|---|
| `/gobernanza-ia-co:inventario-de-ia` | Levanta y mantiene el inventario de sistemas de IA con propósito, datos, proveedor, decisiones que afecta y responsable. |
| `/gobernanza-ia-co:triage-de-caso-de-uso` | Clasifica un caso de uso propuesto por riesgo y decide qué controles y qué aprobaciones se activan. |
| `/gobernanza-ia-co:evaluacion-de-impacto-ia` | Evaluación de impacto que cruza el régimen de datos personales con los derechos fundamentales que el sistema puede afectar. |
| `/gobernanza-ia-co:politica-de-uso-de-ia` | Redacta la política interna: usos permitidos, prohibidos, revisión humana obligatoria y régimen de datos. |
| `/gobernanza-ia-co:revision-de-proveedor-ia` | Revisa el contrato del proveedor: entrenamiento con datos del cliente, subencargados, transferencias, auditoría y responsabilidad. |
| `/gobernanza-ia-co:ia-en-la-practica-juridica` | Reglas de uso de IA en piezas que se radican: verificación de citas, transparencia frente al despacho y reserva profesional. |

### Comunes a todos los plugins

| Skill | Qué hace |
|---|---|
| `/gobernanza-ia-co:entrevista-inicial` | Entrevista de arranque. Levanta el perfil de práctica, los criterios de la casa y el estado de las integraciones. **Córrala primero.** |
| `/gobernanza-ia-co:personalizar` | Ajusta el perfil sin repetir la entrevista completa: cambiar una posición, un umbral, un destinatario. |
| `/gobernanza-ia-co:verificar-citas` | Compuerta de verificación: toma una pieza y revisa cada norma, sentencia y término citado contra fuente oficial, dejando marcado lo que no se pudo confirmar. |
| `/gobernanza-ia-co:espacio-de-asunto` | Crea, cambia y cierra espacios de asunto cuando se quiere aislar contexto y salidas por caso. |

## Marco normativo que aplica

- **Constitución Política, arts. 15, 20 y 29** — Habeas data, información y debido proceso frente a decisiones automatizadas
- **Ley 1581 de 2012 y Decreto 1074 de 2015** — Tratamiento de datos personales en sistemas de IA; principios de finalidad, necesidad y calidad del dato
- **Ley 1712 de 2014** — Transparencia y acceso a la información pública, aplicable a IA en el sector público
- **Ley 2213 de 2022** — Uso de TIC en actuaciones judiciales
- **Ley 1123 de 2007** — Deberes de diligencia, lealtad y reserva del abogado que usa herramientas de IA
- **CONPES de política nacional de inteligencia artificial** — Lineamientos de política pública `[verificar número, fecha y vigencia]`
- **Lineamientos del Consejo Superior de la Judicatura sobre IA en la Rama Judicial** — `[verificar acuerdo o circular vigente]`
- **Ley 1480 de 2011** — Información al consumidor cuando la IA interviene en la relación de consumo

La tabla completa, con su estado de verificación, está en el `CLAUDE.md` del plugin.

## Lo que este plugin NO hace

- Emitir asesoría jurídica. Todo lo que produce es borrador para revisión de abogado
- Radicar, firmar, notificar o comunicarse con autoridades o contrapartes por su cuenta
- Afirmar que una cita está verificada cuando no la recuperó de fuente oficial
- Decidir por usted una calificación jurídica discutible: la marca y la escala

## Configuración

La configuración del usuario vive en
`~/.claude/plugins/config/claude-legal-colombia/gobernanza-ia-co/CLAUDE.md`,
fuera del control de versiones. El `CLAUDE.md` de este directorio es la **plantilla**
que la entrevista inicial copia allá.

El perfil de la organización, compartido por todos los plugins, vive en
`~/.claude/plugins/config/claude-legal-colombia/perfil-organizacion.md`.
