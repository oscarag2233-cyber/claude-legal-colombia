# Contencioso Administrativo y Contratación Estatal

Trabaja frente al Estado bajo el CPACA: escoge el medio de control y controla la caducidad, agota vía gubernativa y conciliación prejudicial, arma nulidad y restablecimiento y reparación directa, redacta derechos de petición que obligan, sustenta apelaciones ante tribunal y Consejo de Estado, y maneja el ciclo de la contratación estatal bajo la Ley 80, la Ley 1150 y el Decreto 1082.

> **Todo lo que produce este plugin es un borrador sujeto a revisión profesional.**
> No es concepto jurídico ni asesoría, y no reemplaza a un abogado titulado e inscrito.
> Ver [AVISO-LEGAL.md](../AVISO-LEGAL.md).

**Ámbito:** Derecho administrativo, contencioso administrativo y contratación estatal.

## Instalación

```bash
/plugin marketplace add oscarag2233-cyber/claude-legal-colombia
/plugin install contencioso-administrativo-co@claude-legal-colombia
```

Luego, sin excepción:

```bash
/contencioso-administrativo-co:entrevista-inicial
```

Sin la entrevista, las skills se detienen: prefieren no responder a responder genérico.

## Skills

### Propias del área

| Skill | Qué hace |
|---|---|
| `/contencioso-administrativo-co:medio-de-control` | Escoge el medio de control correcto, fija la caducidad con su norma y define qué hay que agotar antes de demandar. |
| `/contencioso-administrativo-co:derecho-de-peticion` | Redacta la petición con objeto concreto, término aplicable y ruta cuando la autoridad no responde o responde mal. |
| `/contencioso-administrativo-co:nulidad-y-restablecimiento` | Ataca el acto administrativo por causal, con cargos separados y pretensión de restablecimiento cuantificada. |
| `/contencioso-administrativo-co:reparacion-directa` | Estructura la falla del servicio, el daño especial o el riesgo excepcional, con imputación y liquidación conforme a la unificación de 2014. |
| `/contencioso-administrativo-co:contratacion-estatal` | Acompaña el proceso de selección, la ejecución y la liquidación, con control de inhabilidades, riesgos y garantías. |
| `/contencioso-administrativo-co:apelacion-contenciosa` | Sustenta la apelación con reparos concretos, no con la repetición de la demanda. |

### Comunes a todos los plugins

| Skill | Qué hace |
|---|---|
| `/contencioso-administrativo-co:entrevista-inicial` | Entrevista de arranque. Levanta el perfil de práctica, los criterios de la casa y el estado de las integraciones. **Córrala primero.** |
| `/contencioso-administrativo-co:personalizar` | Ajusta el perfil sin repetir la entrevista completa: cambiar una posición, un umbral, un destinatario. |
| `/contencioso-administrativo-co:verificar-citas` | Compuerta de verificación: toma una pieza y revisa cada norma, sentencia y término citado contra fuente oficial, dejando marcado lo que no se pudo confirmar. |
| `/contencioso-administrativo-co:espacio-de-asunto` | Crea, cambia y cierra espacios de asunto cuando se quiere aislar contexto y salidas por caso. |

## Agentes

| Agente | Qué hace |
|---|---|
| `vigia-caducidad` | Vigila la caducidad de los medios de control en los asuntos abiertos y avisa con antelación suficiente para conciliar antes de demandar. |

Los agentes corren en la periodicidad que se configure y escriben en el
destino definido en el perfil de práctica. No radican, no firman y no deciden.

## Marco normativo que aplica

- **Ley 1437 de 2011 (CPACA), modificada por la Ley 2080 de 2021** — Procedimiento administrativo, medios de control (art. 137 y ss.), caducidad (art. 164), extensión de jurisprudencia, recurso de unificación
- **Ley 1755 de 2015** — Derecho de petición (sustituyó el Título II del CPACA)
- **Ley 80 de 1993** — Estatuto General de Contratación de la Administración Pública
- **Ley 1150 de 2007** — Modalidades de selección, riesgos, garantías, interventoría
- **Decreto 1082 de 2015** — DUR del sector Planeación: reglamentación de la contratación estatal, SECOP
- **Ley 2022 de 2020** — Documentos tipo obligatorios
- **Ley 1474 de 2011** — Estatuto Anticorrupción: inhabilidades, supervisión e interventoría, responsabilidad fiscal
- **Ley 610 de 2000** — Proceso de responsabilidad fiscal

La tabla completa, con su estado de verificación, está en el `CLAUDE.md` del plugin.

## Lo que este plugin NO hace

- Emitir asesoría jurídica. Todo lo que produce es borrador para revisión de abogado
- Radicar, firmar, notificar o comunicarse con autoridades o contrapartes por su cuenta
- Afirmar que una cita está verificada cuando no la recuperó de fuente oficial
- Decidir por usted una calificación jurídica discutible: la marca y la escala

## Configuración

La configuración del usuario vive en
`~/.claude/plugins/config/claude-legal-colombia/contencioso-administrativo-co/CLAUDE.md`,
fuera del control de versiones. El `CLAUDE.md` de este directorio es la **plantilla**
que la entrevista inicial copia allá.

El perfil de la organización, compartido por todos los plugins, vive en
`~/.claude/plugins/config/claude-legal-colombia/perfil-organizacion.md`.
