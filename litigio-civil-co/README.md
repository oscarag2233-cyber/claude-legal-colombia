# Litigio Civil y Comercial

Lleva el proceso bajo el Código General del Proceso de punta a punta: competencia y viabilidad, demanda que no se inadmite, contestación con excepciones bien planteadas, plan probatorio, ejecutivo, medidas cautelares, recursos y cronología del caso. Controla términos con la norma a la vista y marca toda cita que no haya sido verificada en fuente oficial.

> **Todo lo que produce este plugin es un borrador sujeto a revisión profesional.**
> No es concepto jurídico ni asesoría, y no reemplaza a un abogado titulado e inscrito.
> Ver [AVISO-LEGAL.md](../AVISO-LEGAL.md).

**Ámbito:** Proceso civil, comercial y de familia en la jurisdicción ordinaria; arbitraje.

## Instalación

```bash
/plugin marketplace add oscarag2233-cyber/claude-legal-colombia
/plugin install litigio-civil-co@claude-legal-colombia
```

Luego, sin excepción:

```bash
/litigio-civil-co:entrevista-inicial
```

Sin la entrevista, las skills se detienen: prefieren no responder a responder genérico.

## Skills

### Propias del área

| Skill | Qué hace |
|---|---|
| `/litigio-civil-co:viabilidad-y-competencia` | Antes de redactar: pretensión viable, juez competente, cuantía, trámite, caducidad o prescripción y requisito de procedibilidad. |
| `/litigio-civil-co:redactar-demanda` | Demanda completa contra la lista del art. 82 del CGP, con hechos numerados, juramento estimatorio razonado y pruebas amarradas a cada hecho. |
| `/litigio-civil-co:contestar-demanda` | Contestación con pronunciamiento hecho por hecho, excepciones de mérito estructuradas y objeción oportuna al juramento estimatorio. |
| `/litigio-civil-co:plan-probatorio` | Convierte la teoría del caso en un plan de prueba: qué hay que probar, con qué medio, quién lo tiene y qué se pide al juez. |
| `/litigio-civil-co:proceso-ejecutivo` | Verifica el título ejecutivo, arma el mandamiento de pago y anticipa las excepciones del ejecutado. |
| `/litigio-civil-co:medidas-cautelares` | Escoge la cautelar procedente, sustenta apariencia de buen derecho y peligro en la demora, y calcula la caución. |
| `/litigio-civil-co:recursos` | Escoge el recurso, controla la oportunidad y sustenta con reparos concretos, no con inconformidad genérica. |
| `/litigio-civil-co:cronologia-del-caso` | Construye la línea de tiempo del expediente con fuente y folio de cada hecho, marcando lo que no está probado. |

### Comunes a todos los plugins

| Skill | Qué hace |
|---|---|
| `/litigio-civil-co:entrevista-inicial` | Entrevista de arranque. Levanta el perfil de práctica, los criterios de la casa y el estado de las integraciones. **Córrala primero.** |
| `/litigio-civil-co:personalizar` | Ajusta el perfil sin repetir la entrevista completa: cambiar una posición, un umbral, un destinatario. |
| `/litigio-civil-co:verificar-citas` | Compuerta de verificación: toma una pieza y revisa cada norma, sentencia y término citado contra fuente oficial, dejando marcado lo que no se pudo confirmar. |
| `/litigio-civil-co:espacio-de-asunto` | Crea, cambia y cierra espacios de asunto cuando se quiere aislar contexto y salidas por caso. |

## Agentes

| Agente | Qué hace |
|---|---|
| `vigia-terminos` | Revisa los procesos activos, cruza actuaciones y estados con los términos legales y avisa lo que vence, con la norma del término a la vista. |

Los agentes corren en la periodicidad que se configure y escriben en el
destino definido en el perfil de práctica. No radican, no firman y no deciden.

## Marco normativo que aplica

- **Ley 1564 de 2012** — Código General del Proceso: competencia (arts. 15-33), demanda (arts. 82-85), contestación (art. 96), excepciones previas (art. 100), pruebas (arts. 164-275), cautelares (arts. 590-604), verbal (arts. 368-373), verbal sumario (arts. 390-392), ejecutivo (arts. 422-472), recursos (arts. 318-355)
- **Ley 2213 de 2022** — Actuaciones judiciales por medios electrónicos, poderes y notificaciones
- **Ley 2220 de 2022** — Estatuto de Conciliación: requisito de procedibilidad `[verificar]`
- **Ley 1563 de 2012** — Estatuto de Arbitraje Nacional e Internacional
- **Código Civil y Código de Comercio** — Derecho sustancial que se hace valer en el proceso
- **Sentencia C-157 de 2013** — Condicionamiento de la sanción por juramento estimatorio `[verificar]`

La tabla completa, con su estado de verificación, está en el `CLAUDE.md` del plugin.

## Lo que este plugin NO hace

- Emitir asesoría jurídica. Todo lo que produce es borrador para revisión de abogado
- Radicar, firmar, notificar o comunicarse con autoridades o contrapartes por su cuenta
- Afirmar que una cita está verificada cuando no la recuperó de fuente oficial
- Decidir por usted una calificación jurídica discutible: la marca y la escala

## Configuración

La configuración del usuario vive en
`~/.claude/plugins/config/claude-legal-colombia/litigio-civil-co/CLAUDE.md`,
fuera del control de versiones. El `CLAUDE.md` de este directorio es la **plantilla**
que la entrevista inicial copia allá.

El perfil de la organización, compartido por todos los plugins, vive en
`~/.claude/plugins/config/claude-legal-colombia/perfil-organizacion.md`.
