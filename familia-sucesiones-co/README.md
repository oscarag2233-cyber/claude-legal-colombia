# Familia y Sucesiones

Trabaja los asuntos de familia y sucesorios con el cuidado que exigen: alimentos, custodia y visitas bajo el interés superior del menor, divorcio y liquidación de la sociedad conyugal o patrimonial, unión marital de hecho, y sucesiones notariales y judiciales. Incorpora las rutas de protección frente a violencia intrafamiliar y las reglas de capacidad de la Ley 1996 de 2019.

> **Todo lo que produce este plugin es un borrador sujeto a revisión profesional.**
> No es concepto jurídico ni asesoría, y no reemplaza a un abogado titulado e inscrito.
> Ver [AVISO-LEGAL.md](../AVISO-LEGAL.md).

**Ámbito:** Derecho de familia, infancia y adolescencia, régimen económico de la pareja y derecho sucesoral.

## Instalación

```bash
/plugin marketplace add oscarag2233-cyber/claude-legal-colombia
/plugin install familia-sucesiones-co@claude-legal-colombia
```

Luego, sin excepción:

```bash
/familia-sucesiones-co:entrevista-inicial
```

Sin la entrevista, las skills se detienen: prefieren no responder a responder genérico.

## Skills

### Propias del área

| Skill | Qué hace |
|---|---|
| `/familia-sucesiones-co:alimentos` | Fija o revisa la cuota alimentaria con capacidad económica, necesidad y concurrencia de obligados, y arma la ruta de exigibilidad. |
| `/familia-sucesiones-co:custodia-y-visitas` | Estructura el acuerdo o la demanda de custodia y régimen de visitas aplicando el interés superior del menor como criterio operativo, no como frase. |
| `/familia-sucesiones-co:divorcio-y-liquidacion` | Escoge la causal o la vía de mutuo acuerdo, y liquida la sociedad conyugal o patrimonial con inventario, avalúos y adjudicación. |
| `/familia-sucesiones-co:sucesion` | Arma la sucesión notarial o judicial: acervo, órdenes hereditarios, asignaciones forzosas, porción conyugal, colación y partición. |
| `/familia-sucesiones-co:proteccion-frente-a-violencia` | Ruta de medidas de protección ante comisaría o juez, con lo que hay que probar y lo que se puede pedir el mismo día. |

### Comunes a todos los plugins

| Skill | Qué hace |
|---|---|
| `/familia-sucesiones-co:entrevista-inicial` | Entrevista de arranque. Levanta el perfil de práctica, los criterios de la casa y el estado de las integraciones. **Córrala primero.** |
| `/familia-sucesiones-co:personalizar` | Ajusta el perfil sin repetir la entrevista completa: cambiar una posición, un umbral, un destinatario. |
| `/familia-sucesiones-co:verificar-citas` | Compuerta de verificación: toma una pieza y revisa cada norma, sentencia y término citado contra fuente oficial, dejando marcado lo que no se pudo confirmar. |
| `/familia-sucesiones-co:espacio-de-asunto` | Crea, cambia y cierra espacios de asunto cuando se quiere aislar contexto y salidas por caso. |

## Marco normativo que aplica

- **Código Civil, Libro I y Libro III** — Familia, matrimonio, filiación, sucesiones y particiones
- **Ley 1098 de 2006** — Código de la Infancia y la Adolescencia: interés superior, custodia, alimentos, restablecimiento de derechos
- **Ley 25 de 1992** — Divorcio del matrimonio civil y cesación de efectos civiles del religioso
- **Ley 54 de 1990, modificada por la Ley 979 de 2005** — Unión marital de hecho y sociedad patrimonial entre compañeros permanentes
- **Ley 1564 de 2012** — CGP: procesos de familia, sucesión (arts. 487 y ss.), verbal sumario
- **Decreto 902 de 1988** — Sucesión ante notario cuando hay acuerdo entre herederos capaces
- **Ley 1996 de 2019** — Régimen de capacidad legal de personas con discapacidad; sustituye la interdicción por apoyos
- **Ley 294 de 1996 y Ley 1257 de 2008** — Violencia intrafamiliar y violencia contra la mujer: medidas de protección

La tabla completa, con su estado de verificación, está en el `CLAUDE.md` del plugin.

## Lo que este plugin NO hace

- Emitir asesoría jurídica. Todo lo que produce es borrador para revisión de abogado
- Radicar, firmar, notificar o comunicarse con autoridades o contrapartes por su cuenta
- Afirmar que una cita está verificada cuando no la recuperó de fuente oficial
- Decidir por usted una calificación jurídica discutible: la marca y la escala

## Configuración

La configuración del usuario vive en
`~/.claude/plugins/config/claude-legal-colombia/familia-sucesiones-co/CLAUDE.md`,
fuera del control de versiones. El `CLAUDE.md` de este directorio es la **plantilla**
que la entrevista inicial copia allá.

El perfil de la organización, compartido por todos los plugins, vive en
`~/.claude/plugins/config/claude-legal-colombia/perfil-organizacion.md`.
