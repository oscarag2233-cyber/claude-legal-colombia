---
name: resumen-para-el-negocio
description: >
  Traduce una revisión jurídica a un resumen que quien decide sí lee: qué se puede
  firmar, qué hay que negociar, qué cuesta cada opción y qué pasa si no se hace nada.
  Sin perder las advertencias. Actívela ante «resúmelo para el gerente», «explícalo en
  cristiano», «necesito una versión para el comité», «un resumen ejecutivo», o cuando el
  destinatario de la salida no sea abogado.
---

# Resumen para el negocio

**Antes de empezar.** Leer el perfil, especialmente `## Salidas` y `## Estilo de la
casa`. Y hacer la **verificación de destinatario** de los guardarraíles: si el resumen
va a un canal amplio, a la contraparte o a un tercero, el encabezado de producto de
trabajo no lo protege. Ofrecer versión reservada y versión saneada.

## El problema que resuelve

Un análisis jurídico completo que nadie lee no protege a nadie. Quien decide en una
empresa lee tres cosas: **qué puedo hacer, qué me cuesta, y qué pasa si no hago nada.**
Todo lo demás lo delega.

Pero traducir no es diluir. Un resumen que borra las advertencias traslada el riesgo sin
que el destinatario lo sepa.

## Reglas de traducción

| En el análisis jurídico | En el resumen |
|---|---|
| «Cláusula de limitación de responsabilidad con tope al 30% del valor del contrato» | «Si algo sale mal, el proveedor solo responde hasta $X. El resto lo asumimos nosotros» |
| «Riesgo de declaratoria de agencia comercial» | «Si terminamos este contrato, podríamos tener que pagarle una prestación adicional equivalente a [X]. No está en el contrato: la pone la ley» |
| «Cláusula compromisoria ante centro de arbitraje» | «Los pleitos van a arbitraje: más rápido (12-18 meses) y más caro (desde $X)» |
| «Ineficacia de pleno derecho» | «Esa cláusula no vale, aunque esté firmada» |
| «Caducidad el 14 de marzo» | «**Después del 14 de marzo ya no podemos reclamar.** Nada» |

**Tres reglas duras:**

1. **No se elimina una advertencia por hacerla corta.** Se hace corta y se deja.
2. **Los números se traducen a plata y a fechas**, que es como se decide.
3. **Cada recomendación viene con lo que pasa si no se sigue.** Sin eso, es una opinión
   que se ignora.

## Estructura

```markdown
[ENCABEZADO DE PRODUCTO DE TRABAJO — o la versión saneada si el destino está fuera del
círculo de reserva]

## [Contrato / asunto] — resumen para decisión

### La decisión que hay que tomar
[Una frase. «¿Firmamos el contrato de X con Y como está, lo negociamos, o no lo
firmamos?»]

### Recomendación
[Una frase, sin condicionales apilados.]

### Lo que pasa si firmamos como está
| Riesgo | Qué significa en plata o en tiempo | Probabilidad |
|---|---|---|

### Lo que hay que negociar — en orden de prioridad
| # | Qué pedir | Por qué importa | Si no lo dan |
|---|---|---|---|
| 1 | [pedido concreto] | [consecuencia] | [aceptable / no aceptable / escalar] |

### Lo que se puede ceder
[Para que quien negocia sepa dónde tiene margen. Esto es lo que más agradece el área
comercial y lo que casi nunca se le da.]

### Fechas
| Qué | Cuándo | Qué pasa si se pasa |
|---|---|---|

### Lo que decide quién
| Decisión | Quién puede tomarla | Según el perfil |
|---|---|---|

---
*Este resumen no reemplaza el análisis completo, que está en [referencia]. Si va a tomar
una decisión distinta de la recomendada, avísenos: cambia lo que hay que hacer.*
```

## Extensión

- **Una página.** Si no cabe, el problema es que hay dos decisiones y hay que separarlas.
- **Sin citas normativas en el cuerpo.** Van al pie o al análisis completo. El gerente no
  necesita el artículo; necesita el efecto.
- **Sin latín, sin «prima facie», sin «sin perjuicio de».**
- **Las viñetas dicen qué hacer**, no qué existe. «El contrato tiene una cláusula penal»
  no sirve; «Si incumplimos, pagamos $X» sí.

## Variantes según destinatario

| Destinatario | Ajuste |
|---|---|
| **Gerente general / junta** | Plata, riesgo reputacional, decisión. Media página |
| **Área comercial** | Qué pueden ofrecer, qué no, cuál es el margen de negociación |
| **Financiera** | Exposición cuantificada, contingencias que provisionar |
| **Operaciones** | Obligaciones concretas y plazos que tienen que cumplir |
| **Cliente externo (firma)** | Se mantiene el encabezado y el lenguaje profesional; se traduce igual |

## Compuertas

- **Verificación de destinatario obligatoria** antes de generar. Si va fuera del círculo
  de reserva, ofrecer versión saneada.
- **Ninguna advertencia 🔴 del análisis puede desaparecer en el resumen.** Puede
  acortarse; no puede omitirse. Si el resumen no la incluye, hay que decir por qué.
- **Piso de severidad:** un hallazgo 🔴 aguas arriba llega 🔴 aquí, salvo que se diga
  expresamente que se baja y por qué.

## Lo que esta skill NO hace

- No suaviza para que la respuesta guste.
- No decide por el negocio.
- No sustituye el análisis: lo acompaña y remite a él.
