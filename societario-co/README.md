# Societario

Acompaña la vida de la sociedad: elección de tipo societario y constitución de SAS, convocatoria y desarrollo de asambleas con actas que resistan impugnación, reformas estatutarias, deberes y responsabilidad de administradores bajo la Ley 222 de 1995, conflictos societarios ante la Superintendencia de Sociedades, y debida diligencia societaria para transacciones.

> **Todo lo que produce este plugin es un borrador sujeto a revisión profesional.**
> No es concepto jurídico ni asesoría, y no reemplaza a un abogado titulado e inscrito.
> Ver [AVISO-LEGAL.md](../AVISO-LEGAL.md).

**Ámbito:** Derecho societario, gobierno corporativo y conflictos entre socios.

## Instalación

```bash
/plugin marketplace add oscarag2233-cyber/claude-legal-colombia
/plugin install societario-co@claude-legal-colombia
```

Luego, sin excepción:

```bash
/societario-co:entrevista-inicial
```

Sin la entrevista, las skills se detienen: prefieren no responder a responder genérico.

## Skills

### Propias del área

| Skill | Qué hace |
|---|---|
| `/societario-co:tipo-societario-y-constitucion` | Escoge el tipo societario por las razones correctas y arma el documento de constitución con los estatutos que el negocio necesita. |
| `/societario-co:asamblea-y-actas` | Convocatoria, quórum, mayorías y acta redactada para resistir impugnación y para servir de prueba. |
| `/societario-co:reforma-estatutaria` | Estructura la reforma con el procedimiento, las mayorías y el registro que exige cada tipo societario. |
| `/societario-co:deberes-de-administradores` | Evalúa la actuación del administrador contra el art. 23 de la Ley 222, el conflicto de interés y la exposición a la acción social de responsabilidad. |
| `/societario-co:conflicto-societario` | Mapea la vía para el conflicto entre socios: impugnación, acción social, abuso del derecho de voto, desestimación o arbitraje. |

### Comunes a todos los plugins

| Skill | Qué hace |
|---|---|
| `/societario-co:entrevista-inicial` | Entrevista de arranque. Levanta el perfil de práctica, los criterios de la casa y el estado de las integraciones. **Córrala primero.** |
| `/societario-co:personalizar` | Ajusta el perfil sin repetir la entrevista completa: cambiar una posición, un umbral, un destinatario. |
| `/societario-co:verificar-citas` | Compuerta de verificación: toma una pieza y revisa cada norma, sentencia y término citado contra fuente oficial, dejando marcado lo que no se pudo confirmar. |
| `/societario-co:espacio-de-asunto` | Crea, cambia y cierra espacios de asunto cuando se quiere aislar contexto y salidas por caso. |

## Agentes

| Agente | Qué hace |
|---|---|
| `vigia-societario` | Avisa los vencimientos societarios del año: reunión ordinaria de marzo, renovación de matrícula mercantil, informes y reportes a la Superintendencia. |

Los agentes corren en la periodicidad que se configure y escriben en el
destino definido en el perfil de práctica. No radican, no firman y no deciden.

## Marco normativo que aplica

- **Código de Comercio, Libro Segundo** — Sociedades comerciales: tipos, constitución, aportes, reformas, disolución y liquidación
- **Ley 222 de 1995** — Deberes de administradores (art. 23), responsabilidad (art. 24), acción social de responsabilidad (art. 25), impugnación de decisiones (art. 191), grupos empresariales (arts. 26-31), derecho de inspección
- **Ley 1258 de 2008** — Sociedad por Acciones Simplificada: libertad estatutaria, abuso del derecho de voto (art. 43), desestimación de la personalidad jurídica (art. 42), arbitraje societario
- **Ley 1727 de 2014 y Decreto 1074 de 2015** — Registro mercantil y cámaras de comercio
- **Ley 1901 de 2018** — Sociedades BIC
- **Circular Básica Jurídica de la Superintendencia de Sociedades** — Doctrina vigente sobre gobierno, administradores y conflictos `[verificar versión]`

La tabla completa, con su estado de verificación, está en el `CLAUDE.md` del plugin.

## Lo que este plugin NO hace

- Emitir asesoría jurídica. Todo lo que produce es borrador para revisión de abogado
- Radicar, firmar, notificar o comunicarse con autoridades o contrapartes por su cuenta
- Afirmar que una cita está verificada cuando no la recuperó de fuente oficial
- Decidir por usted una calificación jurídica discutible: la marca y la escala

## Configuración

La configuración del usuario vive en
`~/.claude/plugins/config/claude-legal-colombia/societario-co/CLAUDE.md`,
fuera del control de versiones. El `CLAUDE.md` de este directorio es la **plantilla**
que la entrevista inicial copia allá.

El perfil de la organización, compartido por todos los plugins, vive en
`~/.claude/plugins/config/claude-legal-colombia/perfil-organizacion.md`.
