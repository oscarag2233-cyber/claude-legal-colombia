# Consumidor y Competencia

Trabaja el Estatuto del Consumidor y el régimen de competencia ante la SIC: garantía legal y calidad e idoneidad, demandas de protección al consumidor, publicidad engañosa y cláusulas abusivas, prácticas comerciales restrictivas y actos de competencia desleal, con la lógica de la actuación administrativa y de la jurisdiccional de la Superintendencia.

> **Todo lo que produce este plugin es un borrador sujeto a revisión profesional.**
> No es concepto jurídico ni asesoría, y no reemplaza a un abogado titulado e inscrito.
> Ver [AVISO-LEGAL.md](../AVISO-LEGAL.md).

**Ámbito:** Protección al consumidor, publicidad, prácticas restrictivas de la competencia y competencia desleal.

## Instalación

```bash
/plugin marketplace add oscarag2233-cyber/claude-legal-colombia
/plugin install consumidor-competencia-co@claude-legal-colombia
```

Luego, sin excepción:

```bash
/consumidor-competencia-co:entrevista-inicial
```

Sin la entrevista, las skills se detienen: prefieren no responder a responder genérico.

## Skills

### Propias del área

| Skill | Qué hace |
|---|---|
| `/consumidor-competencia-co:garantia-y-calidad` | Determina si hay incumplimiento de la garantía legal, quién responde solidariamente y cuál es el remedio que corresponde pedir. |
| `/consumidor-competencia-co:demanda-de-proteccion-al-consumidor` | Redacta la demanda ante la SIC o el juez, con la pretensión correcta y la caducidad controlada. |
| `/consumidor-competencia-co:publicidad-y-clausulas-abusivas` | Audita piezas publicitarias y clausulados de adhesión contra los arts. 29 a 33 y 42 a 43 de la Ley 1480. |
| `/consumidor-competencia-co:practicas-restrictivas` | Evalúa riesgo de acuerdo restrictivo, abuso de posición dominante o integración que requiere autorización. |
| `/consumidor-competencia-co:competencia-desleal` | Califica la conducta bajo la Ley 256 de 1996 y define la vía: jurisdiccional ante la SIC o ante el juez. |

### Comunes a todos los plugins

| Skill | Qué hace |
|---|---|
| `/consumidor-competencia-co:entrevista-inicial` | Entrevista de arranque. Levanta el perfil de práctica, los criterios de la casa y el estado de las integraciones. **Córrala primero.** |
| `/consumidor-competencia-co:personalizar` | Ajusta el perfil sin repetir la entrevista completa: cambiar una posición, un umbral, un destinatario. |
| `/consumidor-competencia-co:verificar-citas` | Compuerta de verificación: toma una pieza y revisa cada norma, sentencia y término citado contra fuente oficial, dejando marcado lo que no se pudo confirmar. |
| `/consumidor-competencia-co:espacio-de-asunto` | Crea, cambia y cierra espacios de asunto cuando se quiere aislar contexto y salidas por caso. |

## Marco normativo que aplica

- **Ley 1480 de 2011** — Estatuto del Consumidor: garantía legal (arts. 7-8), calidad e idoneidad, información, publicidad, cláusulas abusivas (arts. 42-43), acción de protección al consumidor (art. 56 y ss.)
- **Ley 155 de 1959 y Decreto 2153 de 1992** — Régimen general de competencia; acuerdos y abusos de posición dominante
- **Ley 1340 de 2009** — Protección de la competencia: integraciones empresariales, beneficios por colaboración, caducidad
- **Ley 256 de 1996** — Competencia desleal: cláusula general y actos típicos
- **Decreto 1074 de 2015** — Reglamentación de consumidor y competencia
- **Ley 2300 de 2023** — Protección frente a prácticas abusivas de cobranza

La tabla completa, con su estado de verificación, está en el `CLAUDE.md` del plugin.

## Lo que este plugin NO hace

- Emitir asesoría jurídica. Todo lo que produce es borrador para revisión de abogado
- Radicar, firmar, notificar o comunicarse con autoridades o contrapartes por su cuenta
- Afirmar que una cita está verificada cuando no la recuperó de fuente oficial
- Decidir por usted una calificación jurídica discutible: la marca y la escala

## Configuración

La configuración del usuario vive en
`~/.claude/plugins/config/claude-legal-colombia/consumidor-competencia-co/CLAUDE.md`,
fuera del control de versiones. El `CLAUDE.md` de este directorio es la **plantilla**
que la entrevista inicial copia allá.

El perfil de la organización, compartido por todos los plugins, vive en
`~/.claude/plugins/config/claude-legal-colombia/perfil-organizacion.md`.
