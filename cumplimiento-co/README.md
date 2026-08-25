# Cumplimiento — SAGRILAFT, PTEE y Antisoborno

Determina qué régimen de cumplimiento obliga a la empresa y lo implementa: SAGRILAFT y PTEE bajo la Circular Básica Jurídica de la Superintendencia de Sociedades, responsabilidad administrativa por soborno transnacional de la Ley 1778 de 2016, debida diligencia de contrapartes, canal de denuncias y reporte a autoridades. Incluye la interacción con el régimen de datos personales.

> **Todo lo que produce este plugin es un borrador sujeto a revisión profesional.**
> No es concepto jurídico ni asesoría, y no reemplaza a un abogado titulado e inscrito.
> Ver [AVISO-LEGAL.md](../AVISO-LEGAL.md).

**Ámbito:** Prevención de LA/FT/FPADM, transparencia y ética empresarial, antisoborno y anticorrupción privada.

## Instalación

```bash
/plugin marketplace add oscarag2233-cyber/claude-legal-colombia
/plugin install cumplimiento-co@claude-legal-colombia
```

Luego, sin excepción:

```bash
/cumplimiento-co:entrevista-inicial
```

Sin la entrevista, las skills se detienen: prefieren no responder a responder genérico.

## Skills

### Propias del área

| Skill | Qué hace |
|---|---|
| `/cumplimiento-co:diagnostico-de-obligados` | Determina si la empresa es sujeto obligado a SAGRILAFT, a PTEE, a ambos o a ninguno, con los umbrales y el año de corte. |
| `/cumplimiento-co:sagrilaft` | Estructura o audita el sistema: matriz de riesgo, segmentación, debida diligencia, señales de alerta, oficial de cumplimiento y reportes. |
| `/cumplimiento-co:ptee` | Diseña o revisa el Programa de Transparencia y Ética Empresarial y su articulación con el gobierno corporativo. |
| `/cumplimiento-co:debida-diligencia-de-contraparte` | Aplica debida diligencia simplificada, normal o intensificada según el riesgo, respetando el régimen de datos personales. |
| `/cumplimiento-co:canal-de-denuncias` | Diseña el canal y el protocolo de investigación interna con debido proceso y protección al denunciante. |

### Comunes a todos los plugins

| Skill | Qué hace |
|---|---|
| `/cumplimiento-co:entrevista-inicial` | Entrevista de arranque. Levanta el perfil de práctica, los criterios de la casa y el estado de las integraciones. **Córrala primero.** |
| `/cumplimiento-co:personalizar` | Ajusta el perfil sin repetir la entrevista completa: cambiar una posición, un umbral, un destinatario. |
| `/cumplimiento-co:verificar-citas` | Compuerta de verificación: toma una pieza y revisa cada norma, sentencia y término citado contra fuente oficial, dejando marcado lo que no se pudo confirmar. |
| `/cumplimiento-co:espacio-de-asunto` | Crea, cambia y cierra espacios de asunto cuando se quiere aislar contexto y salidas por caso. |

## Agentes

| Agente | Qué hace |
|---|---|
| `vigia-de-cumplimiento` | Avisa los vencimientos del calendario de cumplimiento: informes del oficial, capacitaciones, actualización de matrices y reportes a la Superintendencia. |

Los agentes corren en la periodicidad que se configure y escriben en el
destino definido en el perfil de práctica. No radican, no firman y no deciden.

## Marco normativo que aplica

- **Circular Básica Jurídica de la Superintendencia de Sociedades — Capítulo X** — SAGRILAFT: sujetos obligados, factores de riesgo, debida diligencia, oficial de cumplimiento, reportes `[verificar circular externa vigente]`
- **Circular Básica Jurídica — Capítulo XIII** — PTEE: Programas de Transparencia y Ética Empresarial `[verificar]`
- **Ley 1778 de 2016** — Responsabilidad administrativa de personas jurídicas por soborno transnacional; competencia de la Superintendencia de Sociedades
- **Ley 2195 de 2022** — Transparencia y prevención de la corrupción; responsabilidad administrativa de personas jurídicas; ampliación de programas de cumplimiento
- **Ley 1474 de 2011** — Estatuto Anticorrupción
- **Ley 599 de 2000** — Delitos de lavado de activos (art. 323), enriquecimiento ilícito, cohecho, soborno transnacional (art. 433)
- **Estatuto Orgánico del Sistema Financiero y circulares de la SFC (SARLAFT)** — Para entidades vigiladas por la Superintendencia Financiera
- **Ley 1581 de 2012** — Límite al tratamiento de datos en la debida diligencia y en las investigaciones internas

La tabla completa, con su estado de verificación, está en el `CLAUDE.md` del plugin.

## Lo que este plugin NO hace

- Emitir asesoría jurídica. Todo lo que produce es borrador para revisión de abogado
- Radicar, firmar, notificar o comunicarse con autoridades o contrapartes por su cuenta
- Afirmar que una cita está verificada cuando no la recuperó de fuente oficial
- Decidir por usted una calificación jurídica discutible: la marca y la escala

## Configuración

La configuración del usuario vive en
`~/.claude/plugins/config/claude-legal-colombia/cumplimiento-co/CLAUDE.md`,
fuera del control de versiones. El `CLAUDE.md` de este directorio es la **plantilla**
que la entrevista inicial copia allá.

El perfil de la organización, compartido por todos los plugins, vive en
`~/.claude/plugins/config/claude-legal-colombia/perfil-organizacion.md`.
