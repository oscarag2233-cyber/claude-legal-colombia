# Laboral y Seguridad Social

Resuelve el día a día laboral bajo el CST y la reforma de 2025: liquidación de prestaciones e indemnizaciones, terminación con y sin justa causa, procedimiento disciplinario con debido proceso, tipo de vinculación y riesgo de tercerización, acoso laboral bajo la Ley 1010 de 2006, riesgos laborales y accidentes de trabajo, y las rutas de pensión y seguridad social.

> **Todo lo que produce este plugin es un borrador sujeto a revisión profesional.**
> No es concepto jurídico ni asesoría, y no reemplaza a un abogado titulado e inscrito.
> Ver [AVISO-LEGAL.md](../AVISO-LEGAL.md).

**Ámbito:** Derecho individual y colectivo del trabajo, seguridad social integral y riesgos laborales.

## Instalación

```bash
/plugin marketplace add oscarag2233-cyber/claude-legal-colombia
/plugin install laboral-seguridad-social-co@claude-legal-colombia
```

Luego, sin excepción:

```bash
/laboral-seguridad-social-co:entrevista-inicial
```

Sin la entrevista, las skills se detienen: prefieren no responder a responder genérico.

## Skills

### Propias del área

| Skill | Qué hace |
|---|---|
| `/laboral-seguridad-social-co:liquidar-prestaciones` | Liquida cesantías, intereses, prima, vacaciones, indemnizaciones y sanciones moratorias con memoria de cálculo y base salarial explícita. |
| `/laboral-seguridad-social-co:terminacion-y-justa-causa` | Evalúa si la causal invocada se sostiene, qué hay que probar, qué procedimiento previo se exige y cuál es la exposición si el despido cae. |
| `/laboral-seguridad-social-co:procedimiento-disciplinario` | Estructura descargos y decisión con debido proceso: citación, imputación clara, oportunidad de defensa y proporcionalidad. |
| `/laboral-seguridad-social-co:vinculacion-y-tercerizacion` | Califica la relación real por encima de la forma y evalúa el riesgo de contrato realidad, intermediación ilegal y solidaridad. |
| `/laboral-seguridad-social-co:acoso-laboral` | Ruta de la Ley 1010: comité de convivencia, medidas preventivas y correctivas, y control de la caducidad de seis meses. |
| `/laboral-seguridad-social-co:riesgos-y-atel` | Accidente de trabajo y enfermedad laboral: calificación de origen, prestaciones, controversias ante junta y responsabilidad del empleador. |

### Comunes a todos los plugins

| Skill | Qué hace |
|---|---|
| `/laboral-seguridad-social-co:entrevista-inicial` | Entrevista de arranque. Levanta el perfil de práctica, los criterios de la casa y el estado de las integraciones. **Córrala primero.** |
| `/laboral-seguridad-social-co:personalizar` | Ajusta el perfil sin repetir la entrevista completa: cambiar una posición, un umbral, un destinatario. |
| `/laboral-seguridad-social-co:verificar-citas` | Compuerta de verificación: toma una pieza y revisa cada norma, sentencia y término citado contra fuente oficial, dejando marcado lo que no se pudo confirmar. |
| `/laboral-seguridad-social-co:espacio-de-asunto` | Crea, cambia y cierra espacios de asunto cuando se quiere aislar contexto y salidas por caso. |

## Agentes

| Agente | Qué hace |
|---|---|
| `vigia-laboral` | Vigila vencimientos laborales: contratos a término fijo por renovar, periodos de prueba, incapacidades prolongadas y términos de descargos. |

Los agentes corren en la periodicidad que se configure y escriben en el
destino definido en el perfil de práctica. No radican, no firman y no deciden.

## Marco normativo que aplica

- **Código Sustantivo del Trabajo (Decretos 2663 y 3743 de 1950)** — Contrato de trabajo, jornada, salario, prestaciones, terminación (art. 62-64), prescripción (art. 488)
- **Ley 50 de 1990** — Cesantías con régimen anualizado, contrato a término fijo, salario integral
- **Ley 789 de 2002** — Indemnización por despido sin justa causa (art. 28, que modificó el art. 64 CST)
- **Ley 2466 de 2025** — Reforma laboral: contrato a término indefinido como regla, recargos, jornada y estabilidad `[verificar vigencia, reglamentación y transición]`
- **Ley 2101 de 2021** — Reducción gradual de la jornada máxima legal
- **Ley 2191 de 2022** — Desconexión laboral
- **Ley 1010 de 2006** — Acoso laboral: conductas, comité de convivencia, procedimiento y caducidad de 6 meses
- **Ley 100 de 1993 y Ley 797 de 2003** — Sistema general de pensiones, salud y riesgos

La tabla completa, con su estado de verificación, está en el `CLAUDE.md` del plugin.

## Lo que este plugin NO hace

- Emitir asesoría jurídica. Todo lo que produce es borrador para revisión de abogado
- Radicar, firmar, notificar o comunicarse con autoridades o contrapartes por su cuenta
- Afirmar que una cita está verificada cuando no la recuperó de fuente oficial
- Decidir por usted una calificación jurídica discutible: la marca y la escala

## Configuración

La configuración del usuario vive en
`~/.claude/plugins/config/claude-legal-colombia/laboral-seguridad-social-co/CLAUDE.md`,
fuera del control de versiones. El `CLAUDE.md` de este directorio es la **plantilla**
que la entrevista inicial copia allá.

El perfil de la organización, compartido por todos los plugins, vive en
`~/.claude/plugins/config/claude-legal-colombia/perfil-organizacion.md`.
