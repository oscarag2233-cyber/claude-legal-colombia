# Contratos y Derecho Comercial

Revisa y redacta contratos civiles y mercantiles bajo el Código Civil y el Código de Comercio: califica el tipo contractual, contrasta el clausulado contra los criterios de la casa, marca cláusulas abusivas y de riesgo, analiza incumplimiento y remedios, y traduce la revisión a un resumen que el cliente o el área de negocio sí lee.

> **Todo lo que produce este plugin es un borrador sujeto a revisión profesional.**
> No es concepto jurídico ni asesoría, y no reemplaza a un abogado titulado e inscrito.
> Ver [AVISO-LEGAL.md](../AVISO-LEGAL.md).

**Ámbito:** Contratación civil y mercantil, obligaciones, garantías y remedios contractuales.

## Instalación

```bash
/plugin marketplace add oscarag2233-cyber/claude-legal-colombia
/plugin install contratos-comercial-co@claude-legal-colombia
```

Luego, sin excepción:

```bash
/contratos-comercial-co:entrevista-inicial
```

Sin la entrevista, las skills se detienen: prefieren no responder a responder genérico.

## Skills

### Propias del área

| Skill | Qué hace |
|---|---|
| `/contratos-comercial-co:revisar-contrato` | Revisión cláusula por cláusula contra los criterios de la casa, con marcación de desviaciones y propuesta de redlines quirúrgicos. |
| `/contratos-comercial-co:minutar-contrato` | Redacta o adapta una minuta a partir del negocio real, con las cláusulas que el tipo contractual exige y las que la práctica colombiana espera. |
| `/contratos-comercial-co:clausulas-de-riesgo` | Barrido específico de cláusulas abusivas, penales excesivas, limitaciones de responsabilidad inválidas y pactos que no resisten el control judicial. |
| `/contratos-comercial-co:incumplimiento-y-remedios` | Califica el incumplimiento y mapea los remedios disponibles con sus requisitos, términos y costo procesal. |
| `/contratos-comercial-co:resumen-para-el-negocio` | Traduce la revisión a un resumen accionable para quien decide, sin perder las advertencias jurídicas. |

### Comunes a todos los plugins

| Skill | Qué hace |
|---|---|
| `/contratos-comercial-co:entrevista-inicial` | Entrevista de arranque. Levanta el perfil de práctica, los criterios de la casa y el estado de las integraciones. **Córrala primero.** |
| `/contratos-comercial-co:personalizar` | Ajusta el perfil sin repetir la entrevista completa: cambiar una posición, un umbral, un destinatario. |
| `/contratos-comercial-co:verificar-citas` | Compuerta de verificación: toma una pieza y revisa cada norma, sentencia y término citado contra fuente oficial, dejando marcado lo que no se pudo confirmar. |
| `/contratos-comercial-co:espacio-de-asunto` | Crea, cambia y cierra espacios de asunto cuando se quiere aislar contexto y salidas por caso. |

## Agentes

| Agente | Qué hace |
|---|---|
| `vigia-renovaciones` | Revisa el registro de contratos y avisa qué vence o se renueva automáticamente antes de que se cierre la ventana de preaviso. |

Los agentes corren en la periodicidad que se configure y escriben en el
destino definido en el perfil de práctica. No radican, no firman y no deciden.

## Marco normativo que aplica

- **Código Civil (Ley 84 de 1873)** — Obligaciones y contratos: arts. 1494 y ss., 1502 (requisitos), 1602 (fuerza obligatoria), 1603 (buena fe), 1616 (previsibilidad), 1546 (condición resolutoria tácita)
- **Código de Comercio (Decreto 410 de 1971)** — Actos de comercio, contratos mercantiles típicos, art. 822 (remisión al civil), art. 830 (abuso del derecho), art. 871 (buena fe), art. 884 (intereses)
- **Ley 1480 de 2011** — Estatuto del Consumidor: aplica cuando una parte es consumidor; cláusulas abusivas, garantía legal
- **Ley 527 de 1999** — Comercio electrónico, mensajes de datos y firmas electrónicas
- **Decreto 1074 de 2015** — Decreto Único Reglamentario del sector Comercio, Industria y Turismo
- **Ley 2213 de 2022** — Mensajes de datos y actuaciones electrónicas

La tabla completa, con su estado de verificación, está en el `CLAUDE.md` del plugin.

## Lo que este plugin NO hace

- Emitir asesoría jurídica. Todo lo que produce es borrador para revisión de abogado
- Radicar, firmar, notificar o comunicarse con autoridades o contrapartes por su cuenta
- Afirmar que una cita está verificada cuando no la recuperó de fuente oficial
- Decidir por usted una calificación jurídica discutible: la marca y la escala

## Configuración

La configuración del usuario vive en
`~/.claude/plugins/config/claude-legal-colombia/contratos-comercial-co/CLAUDE.md`,
fuera del control de versiones. El `CLAUDE.md` de este directorio es la **plantilla**
que la entrevista inicial copia allá.

El perfil de la organización, compartido por todos los plugins, vive en
`~/.claude/plugins/config/claude-legal-colombia/perfil-organizacion.md`.
