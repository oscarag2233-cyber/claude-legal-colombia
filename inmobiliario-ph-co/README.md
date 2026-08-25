# Inmobiliario y Propiedad Horizontal

Cubre la vida del inmueble: estudio de títulos con lectura de folio de matrícula, contratos de compraventa y arrendamiento urbano bajo la Ley 820 de 2003, restitución de inmueble arrendado, y la operación de la propiedad horizontal bajo la Ley 675 de 2001 — asambleas, reglamento, cuotas, sanciones y conflictos entre copropietarios.

> **Todo lo que produce este plugin es un borrador sujeto a revisión profesional.**
> No es concepto jurídico ni asesoría, y no reemplaza a un abogado titulado e inscrito.
> Ver [AVISO-LEGAL.md](../AVISO-LEGAL.md).

**Ámbito:** Derecho inmobiliario, registro, arrendamiento urbano y propiedad horizontal.

## Instalación

```bash
/plugin marketplace add oscarag2233-cyber/claude-legal-colombia
/plugin install inmobiliario-ph-co@claude-legal-colombia
```

Luego, sin excepción:

```bash
/inmobiliario-ph-co:entrevista-inicial
```

Sin la entrevista, las skills se detienen: prefieren no responder a responder genérico.

## Skills

### Propias del área

| Skill | Qué hace |
|---|---|
| `/inmobiliario-ph-co:estudio-de-titulos` | Lee el folio de matrícula anotación por anotación, reconstruye la tradición y emite concepto de saneamiento con riesgos y su mitigación. |
| `/inmobiliario-ph-co:contrato-de-arrendamiento` | Redacta o revisa el arrendamiento distinguiendo vivienda urbana (imperativa) de comercial y de otros destinos. |
| `/inmobiliario-ph-co:restitucion-de-inmueble` | Arma el proceso de restitución con la causal correcta, los requisitos de procedibilidad y las cargas del arrendatario para ser oído. |
| `/inmobiliario-ph-co:asamblea-y-reglamento-ph` | Convoca, desarrolla y documenta la asamblea conforme a la Ley 675, y revisa el reglamento contra la norma imperativa. |
| `/inmobiliario-ph-co:conflictos-en-ph` | Resuelve el conflicto de copropiedad por la vía que corresponde: comité de convivencia, asamblea, policía o juez. |

### Comunes a todos los plugins

| Skill | Qué hace |
|---|---|
| `/inmobiliario-ph-co:entrevista-inicial` | Entrevista de arranque. Levanta el perfil de práctica, los criterios de la casa y el estado de las integraciones. **Córrala primero.** |
| `/inmobiliario-ph-co:personalizar` | Ajusta el perfil sin repetir la entrevista completa: cambiar una posición, un umbral, un destinatario. |
| `/inmobiliario-ph-co:verificar-citas` | Compuerta de verificación: toma una pieza y revisa cada norma, sentencia y término citado contra fuente oficial, dejando marcado lo que no se pudo confirmar. |
| `/inmobiliario-ph-co:espacio-de-asunto` | Crea, cambia y cierra espacios de asunto cuando se quiere aislar contexto y salidas por caso. |

## Marco normativo que aplica

- **Código Civil, Libro II** — Bienes, tradición, posesión, servidumbres, acciones reales
- **Ley 1579 de 2012** — Estatuto de Registro de Instrumentos Públicos
- **Ley 820 de 2003** — Arrendamiento de vivienda urbana: canon, reajuste, causales de terminación, restitución
- **Ley 675 de 2001** — Régimen de propiedad horizontal: órganos, coeficientes, cuotas, sanciones, órgano de convivencia
- **Ley 1564 de 2012** — CGP: restitución de inmueble arrendado (art. 384), pertenencia (art. 375), divisorios, ejecutivo por cuotas de administración
- **Ley 388 de 1997** — Ordenamiento territorial, licencias y usos del suelo
- **Decreto 1077 de 2015** — DUR de Vivienda, Ciudad y Territorio; licencias urbanísticas y curadurías

La tabla completa, con su estado de verificación, está en el `CLAUDE.md` del plugin.

## Lo que este plugin NO hace

- Emitir asesoría jurídica. Todo lo que produce es borrador para revisión de abogado
- Radicar, firmar, notificar o comunicarse con autoridades o contrapartes por su cuenta
- Afirmar que una cita está verificada cuando no la recuperó de fuente oficial
- Decidir por usted una calificación jurídica discutible: la marca y la escala

## Configuración

La configuración del usuario vive en
`~/.claude/plugins/config/claude-legal-colombia/inmobiliario-ph-co/CLAUDE.md`,
fuera del control de versiones. El `CLAUDE.md` de este directorio es la **plantilla**
que la entrevista inicial copia allá.

El perfil de la organización, compartido por todos los plugins, vive en
`~/.claude/plugins/config/claude-legal-colombia/perfil-organizacion.md`.
