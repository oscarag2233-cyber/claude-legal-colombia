---
name: control-de-terminos
description: >
  Lleva el tablero de términos del consultorio con criterio de prevención del daño al
  usuario, y define el protocolo cuando un término está en riesgo. Actívela ante «tablero
  de términos», «qué se vence esta semana», «control de vencimientos del consultorio»,
  «se nos va a pasar un término», «revisión de plazos de los casos».
---

# Control de términos

> **En un consultorio jurídico, un término vencido no es un error administrativo: es un
> daño a una persona que no tenía otra opción de acceso a la justicia.** Ese es el criterio
> que gobierna esta skill.

**Antes de empezar.** Leer el perfil: quién es el docente responsable de cada área y cuál
es el protocolo de alerta.

## Por qué el consultorio es especialmente vulnerable

| Factor | Riesgo |
|---|---|
| **Rotación semestral** | El caso cambia de manos cada semestre y los términos se pierden en la entrega |
| **Carga académica** | Parciales y finales coinciden con vencimientos |
| **Vacaciones** | El consultorio cierra; los términos judiciales no siempre |
| **Estudiantes en formación** | El cálculo de términos es de las cosas que menos se enseñan y más se necesitan |
| **Usuarios sin alternativa** | Si aquí falla, no hay otro abogado |

**Diseñar el control asumiendo esos factores**, no ignorándolos.

## El registro

Cada término, una fila. Nada de tener los plazos en la cabeza del estudiante.

| Campo | Contenido |
|---|---|
| **Caso** | Número de ficha y usuario |
| **Área** | |
| **Actuación** | Qué hay que hacer |
| **Norma que fija el término** | **Obligatorio** |
| **Hábiles o calendario** | |
| **Hecho que lo dispara y su fecha** | Notificación, hecho dañoso, publicación |
| **Fecha de vencimiento** | |
| **Calendario judicial consultado** | Sí/No, y cuál acuerdo |
| **Estudiante responsable** | |
| **Docente responsable** | |
| **Estado** | Pendiente / en elaboración / en revisión docente / radicado |
| **Fecha de radicación** | Con constancia |

**El campo «calendario judicial consultado» existe porque es el error más frecuente:**
contar días hábiles sin descontar vacancia judicial ni días no laborables del despacho.
Ver `referencias/terminos-caducidad-prescripcion.md`.

## Las franjas y el protocolo

| Franja | Ventana | Protocolo |
|---|---|---|
| 🔴 **Crítico** | 0-3 días hábiles | **Alerta inmediata al docente responsable y al director del consultorio.** El caso se atiende hoy, con reasignación si el estudiante no está disponible |
| 🟠 **Urgente** | 4-7 días hábiles | Alerta al docente. La pieza debe estar en revisión ya |
| 🟡 **Próximo** | 8-15 días hábiles | En elaboración |
| 🟢 **En el horizonte** | Más de 15 días | Programado |

**Regla del margen docente:** la pieza debe llegar a revisión del docente con al menos
**3 días hábiles** de anticipación al vencimiento. Un memorial que llega el día del
vencimiento no se puede revisar bien, y revisarlo mal es peor que no revisarlo.

**Por eso el vencimiento operativo del estudiante es 3 días antes del vencimiento legal.**
El tablero muestra las dos fechas.

## Los términos que más se pasan

| Término | Plazo | Por qué se pasa |
|---|---|---|
| **Contestación de demanda** | 20 días (verbal) / 10 (verbal sumario) | Se cuenta desde la notificación, no desde que el usuario trae el papel |
| **Recursos** | 3 días | Plazo cortísimo; si el usuario avisa tarde, ya no hay |
| **Nulidad y restablecimiento** | 4 meses | Parece mucho y la conciliación consume tres |
| **Acción de protección al consumidor** | 1 año desde la terminación de la garantía | Se olvida el disparador |
| **Acoso laboral** | 6 meses | El usuario consulta cuando ya lleva un año |
| **Sociedad patrimonial (unión marital)** | **1 año desde la separación** | El más letal de todos |
| **Impugnación de decisiones sociales o de asamblea de PH** | 2 meses | |
| **Impugnación de fallo de tutela** | 3 días | |
| **Habeas data: consulta y reclamo** | 10 y 15 días hábiles | |
| **Prescripción laboral** | 3 años | |

## El protocolo cuando un término está en riesgo

**No hay que ocultarlo. Hay que escalarlo hoy.**

```
1. ALERTA INMEDIATA al docente responsable y al director. Por escrito, con la fecha y la
   situación real.
2. EVALUAR SI TODAVÍA ALCANZA. Si alcanza, reasignar y atender con prioridad absoluta.
3. SI NO ALCANZA:
   a) Informar al usuario **de inmediato**, con franqueza.
   b) Explicarle qué vías le quedan abiertas.
   c) Orientarlo hacia otra alternativa: defensoría pública, otro consultorio, remisión.
   d) Documentar todo lo actuado.
4. REGISTRAR Y ANALIZAR. Qué falló en el proceso, no quién falló. La causa suele ser
   estructural: el caso no se registró, la entrega de semestre no lo incluyó, la
   notificación no se preguntó en la entrevista.
```

**La regla más importante:** informar al usuario. Un usuario que sabe que su término venció
puede buscar otra vía; uno que no sabe, pierde también esa posibilidad.

## Verificación semanal

```
[ ] ¿Todos los casos abiertos tienen sus términos registrados?
[ ] ¿Todos los términos tienen la norma que los fija?
[ ] ¿Se consultó el calendario judicial vigente?
[ ] ¿Todos los términos tienen estudiante y docente asignados?
[ ] ¿Hay casos sin actuación en más de 30 días?
[ ] ¿Hay piezas en revisión docente hace más de 3 días?
[ ] ¿Se registraron los términos de los casos nuevos de la semana?
[ ] ¿Hay términos que caen en semana de parciales o en vacancia?
```

**La penúltima pregunta —casos nuevos— es donde nace la mayoría de los términos
perdidos.**

## Salida

```markdown
[NOTAS DE TRABAJO — CONSULTORIO JURÍDICO]

## Tablero de términos — semana del [fecha]

**Calendario judicial consultado:** [acuerdo n.º / **NO CONSULTADO — los conteos no
descuentan vacancia**]

### 🔴 Crítico (0-3 días hábiles)
| Caso | Usuario | Actuación | Vence | Vencimiento operativo | Estudiante | Docente | Estado |
|---|---|---|---|---|---|---|---|

### 🟠 Urgente (4-7 días)
### 🟡 Próximo (8-15 días)
### 🟢 En el horizonte

### En revisión docente hace más de 3 días
| Caso | Pieza | Docente | Días en revisión | Vence |
|---|---|---|---|---|

### Casos sin actuación en más de 30 días
| Caso | Última actuación | Estudiante | Estado |
|---|---|---|---|

### ⚠️ Casos sin términos registrados
[Sección propia: un caso sin términos registrados o no tiene términos, o tiene términos
que nadie está mirando. Hay que revisarlo caso por caso.]

### Alertas de calendario académico
[Términos que caen en semana de parciales, finales o vacaciones]

### Verificación semanal
[la lista, con sus respuestas]
```

## Compuertas

- **Ningún término sin norma y sin responsable.**
- **El vencimiento operativo (3 días antes) es el que se le comunica al estudiante.**
- **Si un término está en riesgo, se escala el mismo día.** No se espera a ver si alcanza.
- **Si un término se vence, se informa al usuario de inmediato.**
- **Los casos sin términos registrados van en sección propia** y se revisan uno por uno.

## Lo que esta skill NO hace

- No radica ni elabora las piezas.
- No consulta la Rama Judicial: trabaja con lo que se registre.
- No sustituye la supervisión docente.
