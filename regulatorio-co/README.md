# Regulatorio y Vigilancia Normativa

Mantiene al equipo al día con lo que se publica y con lo que decide la jurisprudencia: vigilancia del Diario Oficial, de las superintendencias y de las altas cortes, análisis de impacto de una norma nueva sobre las obligaciones vigentes, comentarios a proyectos normativos en consulta pública, mapa de obligaciones por área, y el boletín que el equipo sí lee el lunes.

> **Todo lo que produce este plugin es un borrador sujeto a revisión profesional.**
> No es concepto jurídico ni asesoría, y no reemplaza a un abogado titulado e inscrito.
> Ver [AVISO-LEGAL.md](../AVISO-LEGAL.md).

**Ámbito:** Vigilancia normativa y jurisprudencial, análisis de impacto regulatorio y gestión de obligaciones.

## Instalación

```bash
/plugin marketplace add oscarag2233-cyber/claude-legal-colombia
/plugin install regulatorio-co@claude-legal-colombia
```

Luego, sin excepción:

```bash
/regulatorio-co:entrevista-inicial
```

Sin la entrevista, las skills se detienen: prefieren no responder a responder genérico.

## Skills

### Propias del área

| Skill | Qué hace |
|---|---|
| `/regulatorio-co:vigilancia-normativa` | Barrido periódico de fuentes oficiales con filtro de materialidad, para que el equipo lea diez líneas y no doscientas. |
| `/regulatorio-co:analisis-de-impacto` | Toma una norma nueva y dice qué cambia en las obligaciones, en los contratos y en los procesos de la organización. |
| `/regulatorio-co:comentarios-a-proyecto` | Redacta comentarios a un proyecto en consulta pública con argumento técnico y propuesta de texto. |
| `/regulatorio-co:mapa-de-obligaciones` | Construye y mantiene la matriz de obligaciones normativas por área, con responsable y evidencia. |
| `/regulatorio-co:boletin-normativo` | Arma el boletín periódico con novedades priorizadas y acción concreta por cada una. |

### Comunes a todos los plugins

| Skill | Qué hace |
|---|---|
| `/regulatorio-co:entrevista-inicial` | Entrevista de arranque. Levanta el perfil de práctica, los criterios de la casa y el estado de las integraciones. **Córrala primero.** |
| `/regulatorio-co:personalizar` | Ajusta el perfil sin repetir la entrevista completa: cambiar una posición, un umbral, un destinatario. |
| `/regulatorio-co:verificar-citas` | Compuerta de verificación: toma una pieza y revisa cada norma, sentencia y término citado contra fuente oficial, dejando marcado lo que no se pudo confirmar. |
| `/regulatorio-co:espacio-de-asunto` | Crea, cambia y cierra espacios de asunto cuando se quiere aislar contexto y salidas por caso. |

## Agentes

| Agente | Qué hace |
|---|---|
| `vigia-normativo` | Corre la vigilancia en la periodicidad configurada, filtra por materialidad y entrega el digest listo para publicar. |

Los agentes corren en la periodicidad que se configure y escriben en el
destino definido en el perfil de práctica. No radican, no firman y no deciden.

## Marco normativo que aplica

- **Ley 1437 de 2011, art. 8** — Deber de publicidad y consulta de proyectos de regulación
- **Decreto 1081 de 2015** — DUR de la Presidencia: publicidad de proyectos de actos administrativos
- **Ley 1712 de 2014** — Transparencia y acceso a la información pública
- **Ley 153 de 1887, arts. 71-72** — Derogatoria expresa, orgánica y tácita
- **Constitución Política, arts. 241 y 243** — Control de constitucionalidad y cosa juzgada constitucional

La tabla completa, con su estado de verificación, está en el `CLAUDE.md` del plugin.

## Lo que este plugin NO hace

- Emitir asesoría jurídica. Todo lo que produce es borrador para revisión de abogado
- Radicar, firmar, notificar o comunicarse con autoridades o contrapartes por su cuenta
- Afirmar que una cita está verificada cuando no la recuperó de fuente oficial
- Decidir por usted una calificación jurídica discutible: la marca y la escala

## Configuración

La configuración del usuario vive en
`~/.claude/plugins/config/claude-legal-colombia/regulatorio-co/CLAUDE.md`,
fuera del control de versiones. El `CLAUDE.md` de este directorio es la **plantilla**
que la entrevista inicial copia allá.

El perfil de la organización, compartido por todos los plugins, vive en
`~/.claude/plugins/config/claude-legal-colombia/perfil-organizacion.md`.
