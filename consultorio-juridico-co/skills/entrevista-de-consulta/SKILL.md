---
name: entrevista-de-consulta
description: >
  Guía la entrevista con el usuario del consultorio para levantar los hechos completos,
  identificar el problema jurídico y detectar términos que corran. Actívela ante «llegó un
  usuario», «entrevista de consulta», «ficha de atención», «no sé qué preguntarle»,
  «primera cita en el consultorio», «cómo levanto los hechos».
---

# Entrevista de consulta

**Antes de empezar.** Leer `~/.claude/plugins/config/claude-legal-colombia/consultorio-juridico-co/CLAUDE.md`.

> **La entrevista es la única fuente de hechos que va a tener el caso.** Lo que no se
> pregunte hoy, se descubre tarde. Y en un consultorio, «tarde» suele significar «después
> de que venció el término».

**Datos personales:** la ficha contiene datos personales y con frecuencia sensibles.
Aplica la Ley 1581 de 2012 y `referencias/tratamiento-de-datos.md`. **Tomar autorización
de tratamiento** en la primera atención.

## Paso 0 — Antes de que el usuario hable

| Verificación | Por qué |
|---|---|
| **Competencia del consultorio** | La Ley 2113 de 2021 delimita en qué asuntos puede actuar el consultorio. Si el asunto está fuera, hay que decirlo hoy, no en tres semanas `[verificar el ámbito vigente]` |
| **Conflicto de interés** | ¿La contraparte ya es usuaria del consultorio? Verificar antes de oír el caso |
| **Docente responsable del área** | Quién supervisa |
| **Autorización de tratamiento de datos** | |

## Paso 1 — El relato libre

**Primero se escucha, sin interrumpir y sin encasillar.** Dos o tres minutos de relato
libre dan más información que veinte preguntas cerradas, y muestran qué es lo que al
usuario le importa —que no siempre coincide con el problema jurídico—.

Cuando termine: **«¿Hay algo más que deba saber?»**. Esa pregunta abre lo que el usuario
no contó por vergüenza, por miedo o porque no le pareció importante.

## Paso 2 — Los datos que nunca pueden faltar

### Del usuario
Nombre completo, documento, fecha de nacimiento, dirección, teléfono, **correo
electrónico** (indispensable para notificaciones electrónicas), ocupación, ingresos
aproximados, personas a cargo.

### De la contraparte
Nombre o razón social, documento o NIT, dirección conocida, teléfono, correo, **relación
con el usuario**. Si es persona jurídica: representante legal.

**La dirección de la contraparte decide si el proceso avanza o se estanca en la
notificación.** Insistir en ella y en cualquier dato que ayude: lugar de trabajo, nombre
de familiares, redes sociales.

### De los hechos
**Cada hecho con su fecha.** Si el usuario no recuerda la fecha exacta, ubicarla: «¿fue
antes o después de tal cosa?», «¿qué mes?», «¿hacía frío?». Una cronología con fechas
aproximadas ubicadas es mucho mejor que una sin fechas.

### De los documentos
Qué tiene, qué no tiene, y **dónde podría conseguir lo que falta**.

## Paso 3 — 🔴 La detección de términos

**Esta es la parte que no se puede omitir, aunque el usuario tenga afán o la entrevista se
acabe.** Preguntas de barrido:

| Pregunta | Qué detecta |
|---|---|
| ¿Le llegó **algún papel**? ¿Cuándo? ¿Lo trajo? | Notificaciones, demandas, actos administrativos, requerimientos |
| ¿Lo **notificaron** de algo? ¿Firmó algo al recibirlo? | Términos corriendo |
| ¿Hay un **proceso** en curso? ¿En qué juzgado? | Términos procesales |
| ¿Cuándo ocurrió el hecho? | Caducidad y prescripción |
| ¿Ya **reclamó** por escrito? ¿Cuándo? ¿Le respondieron? | Requisitos de procedibilidad, silencio administrativo |
| ¿Hay **audiencia** programada? | |
| ¿Le hicieron alguna **oferta** con plazo? | |
| ¿Está pagando algo, o dejó de pagar? Desde cuándo | Mora, reportes, ejecutivos |

**Si aparece cualquier término, se calcula el mismo día y se registra**, aunque el resto
de la entrevista quede pendiente. Ver
`/consultorio-juridico-co:control-de-terminos`.

## Paso 4 — Las preguntas por área

Guías cortas de barrido. **Se usan después del relato libre**, no en lugar de él.

### Familia
Estado civil y fecha; hijos, edades, con quién viven; unión marital: fechas de inicio y de
separación **(🔴 prescripción de un año para la sociedad patrimonial)**; bienes y a nombre
de quién; ingresos de ambos; ¿hay acuerdo previo, conciliación o proceso?; **¿hay
violencia?** (preguntar siempre, con cuidado y sin insistir si la persona no quiere hablar).

### Laboral
Fechas de ingreso y de retiro; cargo y funciones reales; salario y su composición; tipo de
contrato y si hay documento; forma de terminación y si hubo carta; ¿le liquidaron?;
¿estaba afiliado a seguridad social?; ¿hay incapacidades, embarazo, condición de salud o
fuero? **(estabilidad reforzada)**; **🔴 prescripción de 3 años**.

### Civil y consumidor
Qué se pactó y con quién; ¿hay documento?; qué se incumplió y cuándo; qué se pagó y cómo
se prueba; ¿reclamó?; valor de lo pretendido; **🔴 caducidad de la acción de protección al
consumidor**.

### Arrendamiento y vivienda
¿Es vivienda urbana? ; canon y forma de pago; ¿hay contrato escrito?; ¿se dio preaviso?;
¿hay depósito? (prohibido en vivienda); estado del inmueble.

### Administrativo
Qué acto lo afecta; **fecha exacta de notificación** 🔴; ¿interpuso recursos?; ¿pidió algo
por escrito y no le respondieron?; **🔴 caducidad de 4 meses** en nulidad y
restablecimiento.

### Penal (víctima)
Qué pasó, cuándo, dónde; ¿denunció?; ¿hay lesiones? ¿valoración de Medicina Legal?; ¿hay
riesgo actual? **Si hay riesgo, eso va primero.**

## Paso 5 — Cerrar bien la entrevista

**Nunca cerrar sin:**

1. **Decirle al usuario qué sigue**, con fecha: «lo llamamos el [día] con el concepto».
2. **La lista de documentos que debe traer**, escrita y entregada.
3. **Advertencia sobre términos**, si los hay: «esto vence el [fecha]; si no alcanzamos, le
   avisamos para que consulte otra opción».
4. **Advertir el alcance del consultorio**: qué puede hacer y qué no.
5. **Datos de contacto** del consultorio y del estudiante.

**Lo que nunca se hace en la primera entrevista:** dar un concepto definitivo, prometer un
resultado, o decir «eso lo ganamos». El concepto sale después de la revisión del docente.
Ver `/consultorio-juridico-co:cola-de-revision-docente`.

## Salida — la ficha

```markdown
[NOTAS DE TRABAJO — NO ES ASESORÍA JURÍDICA — PENDIENTE DE REVISIÓN DOCENTE]

## Ficha de consulta n.º [ ] — [fecha]

### Verificaciones previas
| Punto | Estado |
|---|---|
| Asunto dentro de la competencia del consultorio | |
| Conflicto de interés verificado | |
| Autorización de tratamiento de datos | |
| Área y docente responsable | |

### Usuario
| Dato | Contenido |
|---|---|
| Nombre y documento | |
| Contacto (teléfono y **correo**) | |
| Dirección | |
| Ocupación e ingresos aproximados | |
| Personas a cargo | |

### Contraparte
| Dato | Contenido |
|---|---|
| Nombre / razón social e identificación | |
| Dirección y contacto | |
| Relación con el usuario | |

### Hechos
| # | Fecha | Hecho | ¿Cómo se prueba? |
|---|---|---|---|

### 🔴 Términos detectados
| Actuación | Hecho que lo dispara | Fecha | Vence | Norma | Estado |
|---|---|---|---|---|---|

### Problema jurídico
[Formulado como pregunta]

### Área y ruta preliminar
| Punto | Contenido |
|---|---|
| Área | |
| Vía probable | |
| ¿Requisito de procedibilidad? | |
| ¿Está dentro de la competencia del consultorio? | |

### Documentos
| Documento | ¿Lo trajo? | Quién lo consigue | Para cuándo |
|---|---|---|---|

### Lo que se le dijo al usuario
[textual, para que quede constancia de lo que se prometió y lo que no]

### Pendiente de revisión docente
| Punto | Duda concreta |
|---|---|

### Próxima cita
[fecha, hora, qué debe traer]
```

## Compuertas

- **Los términos se detectan y se calculan en la primera entrevista**, sin excepción.
- **No dar concepto definitivo en la entrevista.**
- **Verificar competencia y conflicto de interés antes de oír el caso.**
- **Si el asunto está fuera de la competencia del consultorio, decirlo el mismo día** y
  orientar hacia dónde acudir.
- **Si hay riesgo para la integridad de una persona, eso va primero** y activa la ruta de
  protección.
- **Tomar autorización de tratamiento de datos.**

## Lo que esta skill NO hace

- No emite el concepto — para eso está `/consultorio-juridico-co:concepto-para-usuario`.
- No asume la representación: eso lo decide el consultorio conforme a su reglamento.
- No reemplaza la supervisión docente.
