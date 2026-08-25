# Hub de Constructores Legales

Encuentra, evalúa, instala y mantiene skills jurídicas de la comunidad colombiana con una compuerta de revisión de seguridad y de calidad jurídica antes de que algo entre al entorno. Incluye un creador de skills que impone las convenciones de este repositorio: verificación de fuentes, control de términos y compuertas de revisión profesional.

> **Todo lo que produce este plugin es un borrador sujeto a revisión profesional.**
> No es concepto jurídico ni asesoría, y no reemplaza a un abogado titulado e inscrito.
> Ver [AVISO-LEGAL.md](../AVISO-LEGAL.md).

**Ámbito:** Gestión del ecosistema de skills jurídicas: descubrimiento, revisión, instalación y control de calidad.

## Instalación

```bash
/plugin marketplace add oscarag2233-cyber/claude-legal-colombia
/plugin install hub-constructor-legal-co@claude-legal-colombia
```

Luego, sin excepción:

```bash
/hub-constructor-legal-co:entrevista-inicial
```

Sin la entrevista, las skills se detienen: prefieren no responder a responder genérico.

## Skills

### Propias del área

| Skill | Qué hace |
|---|---|
| `/hub-constructor-legal-co:explorar-registro` | Busca skills jurídicas colombianas en los registros configurados y las resume con su procedencia y su frescura. |
| `/hub-constructor-legal-co:revisar-seguridad` | Compuerta obligatoria: revisa la skill antes de instalarla — permisos, comandos, exfiltración, dependencias y calidad jurídica. |
| `/hub-constructor-legal-co:instalar-skill` | Instala solo lo que pasó la revisión, deja registro y explica qué quedó habilitado. |
| `/hub-constructor-legal-co:crear-skill-juridica` | Crea una skill nueva con las convenciones del repositorio: frontmatter, verificación de fuentes, compuertas y salidas. |
| `/hub-constructor-legal-co:control-de-calidad` | Audita las skills instaladas contra la lista de calidad: citas, términos, compuertas y actualidad normativa. |

### Comunes a todos los plugins

| Skill | Qué hace |
|---|---|
| `/hub-constructor-legal-co:entrevista-inicial` | Entrevista de arranque. Levanta el perfil de práctica, los criterios de la casa y el estado de las integraciones. **Córrala primero.** |
| `/hub-constructor-legal-co:personalizar` | Ajusta el perfil sin repetir la entrevista completa: cambiar una posición, un umbral, un destinatario. |
| `/hub-constructor-legal-co:verificar-citas` | Compuerta de verificación: toma una pieza y revisa cada norma, sentencia y término citado contra fuente oficial, dejando marcado lo que no se pudo confirmar. |
| `/hub-constructor-legal-co:espacio-de-asunto` | Crea, cambia y cierra espacios de asunto cuando se quiere aislar contexto y salidas por caso. |

## Marco normativo que aplica

- **Ley 1123 de 2007** — Los deberes profesionales viajan con la herramienta: una skill mal hecha no exonera al abogado
- **Ley 1581 de 2012** — Ninguna skill instalada puede exfiltrar datos de clientes
- **Ley 1273 de 2009** — Delitos informáticos: acceso abusivo y uso de software malicioso

La tabla completa, con su estado de verificación, está en el `CLAUDE.md` del plugin.

## Lo que este plugin NO hace

- Emitir asesoría jurídica. Todo lo que produce es borrador para revisión de abogado
- Radicar, firmar, notificar o comunicarse con autoridades o contrapartes por su cuenta
- Afirmar que una cita está verificada cuando no la recuperó de fuente oficial
- Decidir por usted una calificación jurídica discutible: la marca y la escala

## Configuración

La configuración del usuario vive en
`~/.claude/plugins/config/claude-legal-colombia/hub-constructor-legal-co/CLAUDE.md`,
fuera del control de versiones. El `CLAUDE.md` de este directorio es la **plantilla**
que la entrevista inicial copia allá.

El perfil de la organización, compartido por todos los plugins, vive en
`~/.claude/plugins/config/claude-legal-colombia/perfil-organizacion.md`.
