# Responsabilidad Civil y Seguros

Analiza responsabilidad civil contractual y extracontractual bajo el Código Civil y la jurisprudencia de la Sala Civil: identifica el régimen aplicable, prueba los elementos, liquida perjuicios materiales e inmateriales con las fórmulas usadas por los jueces colombianos, gestiona la reclamación al asegurador y evalúa la viabilidad del litigio antes de demandar.

> **Todo lo que produce este plugin es un borrador sujeto a revisión profesional.**
> No es concepto jurídico ni asesoría, y no reemplaza a un abogado titulado e inscrito.
> Ver [AVISO-LEGAL.md](../AVISO-LEGAL.md).

**Ámbito:** Responsabilidad civil contractual y extracontractual, actividades peligrosas, responsabilidad médica y de tránsito, seguros de daños y de responsabilidad.

## Instalación

```bash
/plugin marketplace add oscarag2233-cyber/claude-legal-colombia
/plugin install responsabilidad-civil-co@claude-legal-colombia
```

Luego, sin excepción:

```bash
/responsabilidad-civil-co:entrevista-inicial
```

Sin la entrevista, las skills se detienen: prefieren no responder a responder genérico.

## Skills

### Propias del área

| Skill | Qué hace |
|---|---|
| `/responsabilidad-civil-co:analisis-de-responsabilidad` | Determina el régimen aplicable, mapea los elementos y evalúa las causales de exoneración con el sustrato probatorio disponible. |
| `/responsabilidad-civil-co:liquidar-perjuicios` | Liquida daño emergente, lucro cesante consolidado y futuro, y perjuicios inmateriales con memoria de cálculo completa. |
| `/responsabilidad-civil-co:reclamacion-a-aseguradora` | Arma la reclamación con la carga probatoria del art. 1077 del C.Co., controla el plazo del art. 1080 y evalúa la objeción del asegurador. |
| `/responsabilidad-civil-co:viabilidad-de-litigio` | Puntúa el caso antes de demandar: prueba, prescripción, solvencia del demandado, costo y escenarios de transacción. |
| `/responsabilidad-civil-co:demanda-de-responsabilidad` | Redacta la demanda con hechos numerados, juramento estimatorio razonado y plan probatorio coherente. |

### Comunes a todos los plugins

| Skill | Qué hace |
|---|---|
| `/responsabilidad-civil-co:entrevista-inicial` | Entrevista de arranque. Levanta el perfil de práctica, los criterios de la casa y el estado de las integraciones. **Córrala primero.** |
| `/responsabilidad-civil-co:personalizar` | Ajusta el perfil sin repetir la entrevista completa: cambiar una posición, un umbral, un destinatario. |
| `/responsabilidad-civil-co:verificar-citas` | Compuerta de verificación: toma una pieza y revisa cada norma, sentencia y término citado contra fuente oficial, dejando marcado lo que no se pudo confirmar. |
| `/responsabilidad-civil-co:espacio-de-asunto` | Crea, cambia y cierra espacios de asunto cuando se quiere aislar contexto y salidas por caso. |

## Agentes

| Agente | Qué hace |
|---|---|
| `vigia-prescripcion` | Revisa los casos abiertos y avisa cuáles se acercan a la prescripción o a la caducidad, con la norma del término a la vista. |

Los agentes corren en la periodicidad que se configure y escriben en el
destino definido en el perfil de práctica. No radican, no firman y no deciden.

## Marco normativo que aplica

- **Código Civil, arts. 2341 a 2360** — Responsabilidad extracontractual: hecho propio, hecho ajeno, cosas y actividades peligrosas (art. 2356)
- **Código Civil, arts. 1613 a 1616** — Perjuicios contractuales: daño emergente, lucro cesante, previsibilidad
- **Código Civil, art. 2357** — Reducción por concurrencia de culpas de la víctima
- **Código de Comercio, arts. 1036 a 1162** — Contrato de seguro; art. 1077 (carga de la prueba), art. 1080 (plazo de pago del siniestro), art. 1081 (prescripción)
- **Código de Comercio, arts. 1127 y ss.** — Seguro de responsabilidad civil y acción directa de la víctima (art. 1133)
- **Ley 769 de 2002** — Código Nacional de Tránsito; SOAT y responsabilidad por accidentes de tránsito
- **Ley 1564 de 2012** — CGP: juramento estimatorio (art. 206), prueba pericial, medidas cautelares

La tabla completa, con su estado de verificación, está en el `CLAUDE.md` del plugin.

## Lo que este plugin NO hace

- Emitir asesoría jurídica. Todo lo que produce es borrador para revisión de abogado
- Radicar, firmar, notificar o comunicarse con autoridades o contrapartes por su cuenta
- Afirmar que una cita está verificada cuando no la recuperó de fuente oficial
- Decidir por usted una calificación jurídica discutible: la marca y la escala

## Configuración

La configuración del usuario vive en
`~/.claude/plugins/config/claude-legal-colombia/responsabilidad-civil-co/CLAUDE.md`,
fuera del control de versiones. El `CLAUDE.md` de este directorio es la **plantilla**
que la entrevista inicial copia allá.

El perfil de la organización, compartido por todos los plugins, vive en
`~/.claude/plugins/config/claude-legal-colombia/perfil-organizacion.md`.
