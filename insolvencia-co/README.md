# Insolvencia y Reorganización

Diagnostica si la empresa o la persona natural está en los supuestos de insolvencia, prepara la solicitud de reorganización o de liquidación judicial ante la Superintendencia de Sociedades bajo la Ley 1116 de 2006, revisa la calificación y graduación de créditos, negocia el acuerdo, y maneja la insolvencia de persona natural no comerciante ante centro de conciliación o notaría.

> **Todo lo que produce este plugin es un borrador sujeto a revisión profesional.**
> No es concepto jurídico ni asesoría, y no reemplaza a un abogado titulado e inscrito.
> Ver [AVISO-LEGAL.md](../AVISO-LEGAL.md).

**Ámbito:** Régimen de insolvencia empresarial y de persona natural no comerciante.

## Instalación

```bash
/plugin marketplace add oscarag2233-cyber/claude-legal-colombia
/plugin install insolvencia-co@claude-legal-colombia
```

Luego, sin excepción:

```bash
/insolvencia-co:entrevista-inicial
```

Sin la entrevista, las skills se detienen: prefieren no responder a responder genérico.

## Skills

### Propias del área

| Skill | Qué hace |
|---|---|
| `/insolvencia-co:diagnostico-de-insolvencia` | Determina si se configuran cesación de pagos o incapacidad de pago inminente, y cuál es el régimen y el juez competente. |
| `/insolvencia-co:solicitud-de-reorganizacion` | Arma la solicitud con los anexos que exige la ley y anticipa los requerimientos que suele hacer la Superintendencia. |
| `/insolvencia-co:calificacion-y-graduacion` | Revisa la calificación y graduación de créditos y prepara objeciones con soporte. |
| `/insolvencia-co:acuerdo-de-reorganizacion` | Estructura el acuerdo: clases de acreedores, mayorías, prelación legal y flujo de pagos sostenible. |
| `/insolvencia-co:insolvencia-persona-natural` | Ruta completa del procedimiento de negociación de deudas de persona natural no comerciante. |

### Comunes a todos los plugins

| Skill | Qué hace |
|---|---|
| `/insolvencia-co:entrevista-inicial` | Entrevista de arranque. Levanta el perfil de práctica, los criterios de la casa y el estado de las integraciones. **Córrala primero.** |
| `/insolvencia-co:personalizar` | Ajusta el perfil sin repetir la entrevista completa: cambiar una posición, un umbral, un destinatario. |
| `/insolvencia-co:verificar-citas` | Compuerta de verificación: toma una pieza y revisa cada norma, sentencia y término citado contra fuente oficial, dejando marcado lo que no se pudo confirmar. |
| `/insolvencia-co:espacio-de-asunto` | Crea, cambia y cierra espacios de asunto cuando se quiere aislar contexto y salidas por caso. |

## Marco normativo que aplica

- **Ley 1116 de 2006** — Régimen de insolvencia empresarial: reorganización, liquidación judicial, validación de acuerdos extrajudiciales
- **Ley 1564 de 2012, arts. 531 a 576** — Insolvencia de la persona natural no comerciante: negociación de deudas, convalidación y liquidación patrimonial
- **Decreto 1074 de 2015** — Reglamentación del régimen de insolvencia; requisitos de la solicitud
- **Ley 2069 de 2020** — Emprendimiento: ajustes al régimen de insolvencia y procesos de menor cuantía
- **Código de Comercio, arts. 1 y ss.** — Calidad de comerciante, que determina el régimen aplicable

La tabla completa, con su estado de verificación, está en el `CLAUDE.md` del plugin.

## Lo que este plugin NO hace

- Emitir asesoría jurídica. Todo lo que produce es borrador para revisión de abogado
- Radicar, firmar, notificar o comunicarse con autoridades o contrapartes por su cuenta
- Afirmar que una cita está verificada cuando no la recuperó de fuente oficial
- Decidir por usted una calificación jurídica discutible: la marca y la escala

## Configuración

La configuración del usuario vive en
`~/.claude/plugins/config/claude-legal-colombia/insolvencia-co/CLAUDE.md`,
fuera del control de versiones. El `CLAUDE.md` de este directorio es la **plantilla**
que la entrevista inicial copia allá.

El perfil de la organización, compartido por todos los plugins, vive en
`~/.claude/plugins/config/claude-legal-colombia/perfil-organizacion.md`.
