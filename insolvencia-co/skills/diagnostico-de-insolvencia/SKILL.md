---
name: diagnostico-de-insolvencia
description: >
  Determina si se configuran cesación de pagos o incapacidad de pago inminente, cuál es el
  régimen aplicable y quién es el juez del concurso, y compara reorganización con
  liquidación y con acuerdos extrajudiciales. Actívela ante «la empresa no puede pagar»,
  «insolvencia», «Ley 1116», «reorganización o liquidación», «me van a embargar todo»,
  «¿califico para insolvencia?», «acuerdo con acreedores», «cesación de pagos».
---

# Diagnóstico de insolvencia

**Antes de empezar.** Leer `~/.claude/plugins/config/claude-legal-colombia/insolvencia-co/CLAUDE.md`.

> **La pregunta que hay que hacer primero no es «¿podemos entrar a insolvencia?» sino
> «¿el negocio es viable?».** Un proceso de reorganización que termina en liquidación
> cuesta dos años y destruye más valor que una liquidación oportuna.

## Paso 1 — ¿Qué régimen aplica?

| Sujeto | Régimen | Juez |
|---|---|---|
| **Sociedad comercial, empresa unipersonal, sucursal de sociedad extranjera, patrimonio autónomo con actividad empresarial** | **Ley 1116 de 2006** | Superintendencia de Sociedades (a prevención con el juez civil del circuito) |
| **Persona natural comerciante** | Ley 1116 de 2006 | Ídem |
| **Persona natural NO comerciante** | **CGP, arts. 531 a 576** | Centro de conciliación o notaría → juez civil municipal | Ver `/insolvencia-co:insolvencia-persona-natural` |
| **Entidades vigiladas por la Superintendencia Financiera, bolsas, entidades de seguridad social, entidades públicas del art. 3** | **Excluidas** de la Ley 1116 | Regímenes especiales `[verificar el listado del art. 3]` |

**Primera verificación: ¿el deudor es comerciante?** (C.Co. arts. 10 y 20). La respuesta
cambia el régimen, el juez, los tiempos y los costos.

## Paso 2 — Los supuestos de admisión (Ley 1116, art. 9)

Se requiere **al menos uno**:

### Cesación de pagos

El deudor incumple el pago por más de **noventa (90) días** de **dos (2) o más
obligaciones** a favor de **dos (2) o más acreedores**, contraídas en desarrollo de su
actividad; **o** tiene por lo menos **dos (2) procesos de ejecución** presentados por dos
o más acreedores.

**Y en cualquier caso**, el valor acumulado de esas obligaciones debe representar **no
menos del diez por ciento (10%) del pasivo total** a la fecha de los estados financieros
de la solicitud. `[verificar el texto vigente]`

### Incapacidad de pago inminente

El deudor acredita **circunstancias en el respectivo mercado o dentro de su organización
o estructura** que afecten o razonablemente puedan afectar en forma grave el cumplimiento
normal de sus obligaciones, con un **plazo no mayor a un año**.

**La incapacidad de pago inminente es la puerta que casi nadie usa y la que más valor
preserva:** permite entrar al proceso **antes** del colapso, cuando todavía hay flujo de
caja, clientes y proveedores. Requiere sustentarla con proyecciones, no con afirmaciones.

## Paso 3 — Requisitos de admisión (art. 10)

Además del supuesto, el deudor debe acreditar `[verificar el texto vigente]`:

| Requisito | Contenido |
|---|---|
| **No estar en mora con trabajadores, pensionados y parafiscales** | Por más de 90 días. **Este es el requisito que más solicitudes tumba** |
| **Llevar contabilidad regular** de sus negocios conforme a las normas legales | |
| Estar cumpliendo las obligaciones de reporte a las autoridades de supervisión | |

**Consecuencia operativa:** si la empresa está en mora con la seguridad social o con la
nómina, **antes de solicitar hay que ponerse al día en eso**. Y si no hay contabilidad
regular, hay que reconstruirla. Ambas cosas toman tiempo y hay que planearlas.

## Paso 4 — Los efectos, que son la razón de entrar

| Efecto | Contenido | Norma |
|---|---|---|
| **Suspensión de procesos ejecutivos** | Los procesos de ejecución y de restitución en curso se **suspenden** y se incorporan al concurso; no se pueden iniciar nuevos | Art. 20 |
| **Levantamiento de medidas cautelares** | Las medidas sobre bienes del deudor se levantan, salvo las de créditos por alimentos `[verificar]` | |
| **Prohibición de pagos** | El deudor **no puede pagar obligaciones anteriores** al inicio, ni hacer compensaciones, daciones en pago, arreglos o conciliaciones, sin autorización del juez | Art. 17 |
| **🔴 Continuidad de los contratos** | **No se puede terminar unilateralmente un contrato por la sola causa del inicio del proceso.** Las cláusulas que lo permitan son **ineficaces** | Art. 21 |
| **Continuidad de servicios públicos** | No pueden suspenderse por deudas anteriores `[verificar]` | |
| **Administración** | El deudor conserva la administración, bajo supervisión del promotor y del juez | |

**El art. 21 es el que salva empresas.** Cuando un cliente o un proveedor amenaza con
terminar por «la situación de la compañía», hay que citarlo: la cláusula de terminación
por insolvencia es ineficaz.

## Paso 5 — Reorganización, liquidación o acuerdo extrajudicial

| Vía | Cuándo conviene | Costo | Tiempo |
|---|---|---|---|
| **Reorganización** | El negocio es viable: hay operación, márgenes y demanda; el problema es de estructura de pasivo o de caja | Alto: promotor, honorarios, tiempo de administración | Meses a años |
| **Liquidación judicial** | El negocio no es viable, o la reorganización fracasó | Menor, pero destruye la empresa | |
| **Validación judicial de acuerdo extrajudicial de reorganización** | Ya hay acuerdo con la mayoría de acreedores y se busca hacerlo oponible a todos | Bajo y rápido | Semanas |
| **Acuerdo privado sin concurso** | Pocos acreedores, todos dispuestos | El más bajo | Inmediato |
| **Reestructuración operativa sin insolvencia** | El problema es operativo, no de pasivo | | |

**Prueba de viabilidad, antes de decidir:**

1. ¿El **EBITDA** es o puede volverse positivo en un horizonte razonable?
2. ¿El problema es de **estructura de pasivo** (deuda cara, corto plazo) o de **modelo de
   negocio**?
3. ¿Hay **clientes** y **proveedores** dispuestos a seguir operando?
4. ¿El **flujo de caja proyectado** paga los gastos de administración del proceso, que son
   créditos de la masa?
5. ¿Los socios están dispuestos a **capitalizar** o a diluirse?

**Si la respuesta a 1 y 3 es no, la reorganización solo aplaza la liquidación** y consume
el patrimonio que habría servido para pagar. Decirlo con claridad: es el consejo más
valioso y el más incómodo de esta materia.

## Paso 6 — Riesgos personales que hay que advertir

| Riesgo | Contenido |
|---|---|
| **Responsabilidad de administradores** | Por el deterioro patrimonial y por no solicitar oportunamente el proceso. Puede haber **inhabilidad** y responsabilidad subsidiaria `[verificar los supuestos del art. 82 y concordantes]` |
| **Acción revocatoria y de simulación** (arts. 74-77) | Los actos del deudor en el **período de sospecha** anterior al inicio —daciones en pago, garantías otorgadas, ventas a vinculados— pueden revocarse |
| **Deber de los administradores** | Ley 222 de 1995, art. 23: velar por el cumplimiento legal y actuar con diligencia de un buen hombre de negocios |
| **Penal** | Alzamiento de bienes, ocultamiento, falsedad en documentos contables |
| **Garantías personales** | Los avales y codeudas de socios y administradores **no se afectan** por el concurso del deudor principal `[verificar]` |

**Advertencia que se hace siempre:** los socios que avalaron créditos siguen obligados
personalmente. Muchos entran a reorganización creyendo que su patrimonio personal queda
cubierto, y no es así.

## Salida

```markdown
[ENCABEZADO DE PRODUCTO DE TRABAJO]

## Diagnóstico de insolvencia — [deudor]

### Régimen aplicable
**[Ley 1116 de 2006 / CGP arts. 531 y ss. / régimen especial — excluido]**
**Juez del concurso:** [ ]

### Supuesto de admisión
| Supuesto | ¿Se configura? | Sustento |
|---|---|---|
| Cesación de pagos — 2+ obligaciones, 2+ acreedores, +90 días | | |
| Cesación de pagos — 2+ procesos ejecutivos | | |
| **¿Representan al menos el 10% del pasivo total?** | | |
| Incapacidad de pago inminente | | Proyecciones a [N] meses |

### Requisitos de admisión (art. 10)
| Requisito | Estado | 🔴 |
|---|---|---|
| Sin mora superior a 90 días con trabajadores, pensionados y parafiscales | | |
| Contabilidad regular | | |
| Reportes a autoridades al día | | |

### Fotografía financiera
| Concepto | Valor |
|---|---|
| Activo total | |
| Pasivo total | |
| Pasivo corriente | |
| Pasivo laboral y parafiscal | |
| Pasivo fiscal | |
| Pasivo con garantía real | |
| Pasivo con vinculados | |
| Caja disponible | |
| EBITDA últimos 12 meses | |

### Prueba de viabilidad
| Pregunta | Respuesta | Fuente |
|---|---|---|

### Recomendación
**[REORGANIZACIÓN / LIQUIDACIÓN JUDICIAL / ACUERDO EXTRAJUDICIAL VALIDADO / ACUERDO PRIVADO / NO ENTRAR A CONCURSO]**
Razón: [ ]

### 🔴 Antes de solicitar
| Acción | Por qué | Plazo |
|---|---|---|
| [ponerse al día en parafiscales, reconstruir contabilidad, preparar flujo] | | |

### Riesgos personales de socios y administradores
| Riesgo | Exposición | Mitigación |
|---|---|---|

### Actos en período de sospecha
| Acto | Fecha | ¿Revocable? | Riesgo |
|---|---|---|---|

Fuentes: […] | Marcas pendientes: [N] | Revisó: [PENDIENTE DE REVISIÓN PROFESIONAL]
```

## Compuertas

- **Verificar la mora con trabajadores y parafiscales antes de recomendar la solicitud.**
  Es el requisito que más solicitudes tumba.
- **No recomendar reorganización sin prueba de viabilidad.** Si el negocio no es viable,
  decirlo.
- **Advertir siempre que los avales personales no se cubren.**
- **Revisar los actos del período de sospecha** antes de entrar: pueden revocarse y pueden
  comprometer a los administradores.
- **Verificar si el deudor está excluido del régimen** antes de todo lo demás.

## Lo que esta skill NO hace

- No prepara estados financieros ni proyecciones.
- No radica ante la Superintendencia de Sociedades.
- No garantiza la admisión.
