---
name: construir-linea-jurisprudencial
description: >
  Enseña y aplica el método completo de construcción de líneas jurisprudenciales:
  sentencia arquimédica, nicho citacional, patrón de sombra, puntos de quiebre y
  verificación de vigencia. Actívela ante «línea jurisprudencial», «cómo ha evolucionado
  la jurisprudencia sobre», «mapear las sentencias sobre un tema», «trabajo de
  investigación jurisprudencial», «cambió la Corte de posición».
---

# Construir una línea jurisprudencial

**Antes de empezar.** Leer el perfil. Y una advertencia que va en toda salida: **esta
skill no busca sentencias en las relatorías.** Enseña el método y organiza el material que
el estudiante recolecte. Las citas que aporte el modelo van marcadas
`[conocimiento del modelo — verificar]` y **deben confirmarse en la relatoría oficial**
antes de usarse en un trabajo.

Ver `referencias/precedente-y-jurisprudencia.md` y `referencias/fuentes-oficiales.md`.

## El método, paso por paso

### Paso 1 — Formular el problema jurídico

**Como pregunta cerrada, con dos respuestas posibles.** Este es el paso que más se
descuida y el que determina si la línea sirve.

| ❌ Mal formulado | ✅ Bien formulado |
|---|---|
| «La tutela contra providencias judiciales» | «¿Procede la acción de tutela contra una sentencia de casación cuando se alega desconocimiento del precedente?» |
| «El derecho a la salud» | «¿Puede el juez de tutela ordenar un tratamiento excluido del plan de beneficios?» |
| «Contrato realidad» | «¿La existencia de un contrato de prestación de servicios prolongado en el tiempo, por sí sola, acredita subordinación?» |

**Prueba:** si la pregunta no se puede responder con «sí» o «no», hay que reformularla.

### Paso 2 — La sentencia arquimédica

Es el punto de apoyo: **la sentencia más reciente y más pertinente** del órgano de cierre
sobre el problema formulado.

**Cómo se escoge:** la más reciente que resuelva exactamente el problema, no una que lo
toque de paso. Si hay una **sentencia de unificación**, esa es.

**Cómo se encuentra:** buscador de la relatoría con los términos del problema; también
sirve buscar la norma aplicable y filtrar.

### Paso 3 — El nicho citacional

Desde la arquimédica se construye la red:

```
        ┌── sentencias que la ARQUIMÉDICA cita  (hacia atrás)
ARQUIMÉDICA
        └── sentencias que CITAN a la arquimédica (hacia adelante)
```

**Hacia atrás:** se leen las citas de la arquimédica y se repite el ejercicio con las más
relevantes, hasta llegar a las **sentencias fundadoras** de la línea.

**Hacia adelante:** se buscan las posteriores que la citan. Es lo que revela si la línea
sigue viva o si cambió. En la relatoría de la Corte Constitucional esto se puede hacer
buscando la nomenclatura de la arquimédica.

**Criterio de corte:** cuando las nuevas sentencias solo reiteran sin agregar nada, la
red está completa. Una línea de veinte sentencias mal escogidas vale menos que una de seis
bien escogidas.

### Paso 4 — El patrón de sombra

Se ubica cada sentencia entre las dos respuestas posibles:

```
¿Procede la tutela contra sentencia de casación por desconocimiento del precedente?

  NO PROCEDE                                                    SÍ PROCEDE
      │                                                              │
      │  ●  C-543/1992  (fundadora)                                 │
      │        ╲                                                     │
      │         ╲                                                    │
      │          ●  T-XXX/199X                                       │
      │              ╲                                               │
      │               ─────────────●  SU-XXX/200X  (punto de quiebre)│
      │                                    ╲                         │
      │                                     ●  C-590/2005 (hito)     │
      │                                          ╲                   │
      │                                           ●  SU-XXX/20XX     │
      │                                                              │
```

**Cada punto lleva:** nomenclatura, año, y la *ratio* en una frase.

### Paso 5 — Identificar lo que importa

| Elemento | Qué es |
|---|---|
| **Sentencia fundadora** | La que abre la línea |
| **Sentencias hito** | Las que fijan o reformulan la regla |
| **Sentencias de unificación** | Las que consolidan |
| **Puntos de quiebre** | Donde la línea cambia de lado |
| **Sentencias confusas** | Las que no encajan; hay que explicarlas, no ignorarlas |
| **Salvamentos que anticipan el cambio** | Con frecuencia el salvamento de hoy es la mayoría de mañana |

**Las sentencias que no encajan son las más valiosas del trabajo.** Explicar por qué se
apartan —hechos distintos, sala distinta, contexto normativo distinto— es lo que
demuestra que se entendió la línea.

### Paso 6 — Verificar la vigencia

| Verificación | Cómo |
|---|---|
| ¿Hay unificación posterior? | Búsqueda en la relatoría |
| ¿La norma que aplicaban sigue vigente? | SUIN-Juriscol |
| ¿Hubo reforma constitucional o legal que cambie el marco? | |
| ¿Hay cambio de composición de la Corte con giro de línea? | |

**Una línea sin verificación de vigencia es un trabajo histórico, no jurídico.**

## La tabla, que es el entregable central

| # | Sentencia | Fecha | M.P. | Problema jurídico | Ratio (una frase) | Posición | Tipo | Fuente | Verificada |
|---|---|---|---|---|---|---|---|---|---|
| 1 | | | | | | NO / SÍ | fundadora / hito / reiteración / quiebre | relatoría | ✅ / ⚠️ |

**La columna «Verificada» es obligatoria.** Distingue lo que el estudiante confirmó en la
relatoría de lo que solo tiene de segunda mano.

## Salida

```markdown
## Línea jurisprudencial — [tema]

### ⚠️ Advertencia de método
Las sentencias que se sugieran aquí y que no provengan de la relatoría oficial van
marcadas `[conocimiento del modelo — verificar]`. **Antes de usar cualquiera en un
trabajo, confírmela en la relatoría de la corporación.** Ver
`referencias/verificacion-de-fuentes.md`.

### Problema jurídico
> [pregunta cerrada]

### Respuestas posibles
**A:** [ ] · **B:** [ ]

### Sentencia arquimédica
[cuál y por qué]

### Tabla de la línea
[la tabla completa]

### Patrón de sombra
[el gráfico]

### Narrativa de la evolución
[Tres o cuatro párrafos: dónde empezó, qué la hizo cambiar, dónde está hoy. **Con los
argumentos, no solo con las fechas**: lo que interesa no es que cambió, sino por qué]

### Estado actual
**Regla vigente:** [ ]
**Última sentencia relevante:** [ ] `[verificar]`
**Estabilidad de la línea:** [consolidada / en transición / con tensión interna]

### Vacíos y preguntas abiertas
[qué no ha resuelto la línea — es lo que hace interesante un trabajo de investigación]

### Cómo se usa en la práctica
| Si represento a… | Cito… | Para sostener… |
|---|---|---|

### Verificación pendiente
| Sentencia | Qué falta confirmar | Dónde |
|---|---|---|
```

## Compuertas

- **Ninguna sentencia se presenta como verificada si no se recuperó de la relatoría.**
- **No inventar nomenclatura, fecha ni magistrado ponente.** Si no se tienen, se dice.
- **Marcar siempre la necesidad de verificar la vigencia.**
- **Si el estudiante quiere entregar la línea como trabajo evaluado**, recordarle que las
  citas son su responsabilidad académica y que una cita inexistente en un trabajo
  universitario tiene consecuencias.

## Lo que esta skill NO hace

- No busca en las relatorías.
- No garantiza que las sentencias que sugiere existan: por eso la marca.
- No escribe el trabajo: enseña el método y organiza el material.
