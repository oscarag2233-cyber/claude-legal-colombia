# Estudiante de Derecho

Acompaña el estudio del Derecho colombiano sin hacer la tarea: ficha sentencias separando ratio de obiter, interroga con método socrático, enseña a construir líneas jurisprudenciales, prepara exámenes y preparatorios por materia, y corrige escritura jurídica exigiendo estructura y cita correcta.

> **Todo lo que produce este plugin es un borrador sujeto a revisión profesional.**
> No es concepto jurídico ni asesoría, y no reemplaza a un abogado titulado e inscrito.
> Ver [AVISO-LEGAL.md](../AVISO-LEGAL.md).

**Ámbito:** Formación jurídica de pregrado y preparación de exámenes preparatorios.

## Instalación

```bash
/plugin marketplace add oscarag2233-cyber/claude-legal-colombia
/plugin install estudiante-derecho-co@claude-legal-colombia
```

Luego, sin excepción:

```bash
/estudiante-derecho-co:entrevista-inicial
```

Sin la entrevista, las skills se detienen: prefieren no responder a responder genérico.

## Skills

### Propias del área

| Skill | Qué hace |
|---|---|
| `/estudiante-derecho-co:ficha-de-sentencia` | Ficha la sentencia con problema jurídico, ratio, obiter, decisum, salvamentos y ubicación en la línea. |
| `/estudiante-derecho-co:metodo-socratico` | Interroga sobre la lectura hasta que la respuesta se sostenga; no entrega la respuesta hecha. |
| `/estudiante-derecho-co:construir-linea-jurisprudencial` | Enseña el método completo: sentencia arquimédica, nicho citacional, patrón de sombra y puntos de quiebre. |
| `/estudiante-derecho-co:preparacion-de-examen` | Arma el plan por materia con los temas que efectivamente se preguntan y ejercicios de aplicación. |
| `/estudiante-derecho-co:escritura-juridica` | Corrige el escrito exigiendo estructura, precisión y cita verificable, y explica cada corrección. |

### Comunes a todos los plugins

| Skill | Qué hace |
|---|---|
| `/estudiante-derecho-co:entrevista-inicial` | Entrevista de arranque. Levanta el perfil de práctica, los criterios de la casa y el estado de las integraciones. **Córrala primero.** |
| `/estudiante-derecho-co:personalizar` | Ajusta el perfil sin repetir la entrevista completa: cambiar una posición, un umbral, un destinatario. |
| `/estudiante-derecho-co:verificar-citas` | Compuerta de verificación: toma una pieza y revisa cada norma, sentencia y término citado contra fuente oficial, dejando marcado lo que no se pudo confirmar. |
| `/estudiante-derecho-co:espacio-de-asunto` | Crea, cambia y cierra espacios de asunto cuando se quiere aislar contexto y salidas por caso. |

## Marco normativo que aplica

- **Constitución Política de 1991** — Base del estudio de todas las materias
- **Ley 169 de 1896, art. 4** — Doctrina probable
- **Ley 270 de 1996** — Estatutaria de administración de justicia
- **Códigos vigentes** — CC, C.Co., CST, CP, CPP, CGP, CPACA, ET
- **Sentencias hito** — Ver `referencias/precedente-y-jurisprudencia.md`

La tabla completa, con su estado de verificación, está en el `CLAUDE.md` del plugin.

## Lo que este plugin NO hace

- Escribir el trabajo, el ensayo o el parcial por el estudiante
- Entregar respuestas de examen
- Resolver el caso sin que el estudiante haya intentado la respuesta primero

## Configuración

La configuración del usuario vive en
`~/.claude/plugins/config/claude-legal-colombia/estudiante-derecho-co/CLAUDE.md`,
fuera del control de versiones. El `CLAUDE.md` de este directorio es la **plantilla**
que la entrevista inicial copia allá.

El perfil de la organización, compartido por todos los plugins, vive en
`~/.claude/plugins/config/claude-legal-colombia/perfil-organizacion.md`.
