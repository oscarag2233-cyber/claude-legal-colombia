---
name: verificar-citas
description: >
  Compuerta de verificación de fuentes para Propiedad Intelectual. Toma una pieza ya redactada —un
  concepto, una demanda, un memorando, un contrato, un boletín— y revisa una por una
  cada norma, sentencia, término y umbral citado, dejando explícito qué se confirmó
  contra fuente oficial y qué quedó marcado. Actívela antes de radicar, antes de enviar
  al cliente, o cuando el usuario pregunte si las citas están bien.
---

# Verificar citas — Propiedad Intelectual

> Esta es la skill que evita el problema más caro del uso de IA en Derecho: **la cita
> que parece correcta y no existe**. Nada sale de este plugin hacia una autoridad, un
> cliente o una contraparte sin pasar por aquí.

## Qué hace

1. **Extrae** toda cita de la pieza: leyes, artículos, decretos, sentencias,
   circulares, conceptos, términos, umbrales y cifras.
2. **Clasifica** cada una por el tipo de verificación que necesita.
3. **Verifica** lo que se pueda con las herramientas disponibles en la sesión.
4. **Marca** lo que no se pudo verificar, sin excepción.
5. **Entrega** una tabla de verificación y una versión de la pieza con las marcas
   puestas donde corresponde.

## Regla de oro

**Una cita solo se declara verificada si en esta sesión apareció en un resultado de una
fuente oficial.** No se asciende una cita porque suene bien, porque el modelo esté
seguro o porque «esa norma existe seguro». Ver `referencias/verificacion-de-fuentes.md`.

## Qué se verifica de cada tipo de cita

### Normas

| Punto | Pregunta |
|---|---|
| Existencia | ¿La ley/decreto con ese número y año existe? |
| Artículo | ¿El artículo citado dice lo que la pieza afirma? |
| Vigencia | ¿Está vigente? ¿Derogado expresa, orgánica o tácitamente? |
| Constitucionalidad | ¿Hay inexequibilidad total o parcial? ¿Exequibilidad **condicionada**? |
| Reglamentación | ¿Hay decreto reglamentario o circular que cambie su aplicación? |
| Compilación | ¿Está compilado en un decreto único? Citar el DUR además de la norma origen |

Fuente preferida: SUIN-Juriscol; en su defecto, Diario Oficial o la edición de la
Secretaría del Senado.

### Jurisprudencia

| Punto | Pregunta |
|---|---|
| Existencia | ¿La sentencia con esa nomenclatura existe? |
| Corporación y sala | ¿Es de la corporación que se dice? |
| Ratio | ¿Lo que se cita es la *ratio decidendi* o es *obiter dictum*? |
| Vigencia de la línea | ¿Hay sentencia de unificación o cambio de línea posterior? |
| M.P. y radicado | ¿Coinciden? Si no se tienen, **no se inventan** |

Ver `referencias/precedente-y-jurisprudencia.md`.

### Términos y caducidades

| Punto | Pregunta |
|---|---|
| Norma que lo fija | ¿Cuál artículo? |
| Hábiles o calendario | ¿Cuál de los dos? |
| Día de inicio | ¿Desde qué hecho corre y por qué? |
| Suspensión o interrupción | ¿Conciliación, reclamo escrito, recurso? |
| Calendario judicial | ¿Se descontó vacancia y días no hábiles? |

### Cifras y umbrales

SMLMV, UVT, cuantías de competencia, topes indemnizatorios, umbrales de obligados:
**siempre con el año**. Un SMLMV sin año es una cifra sin sentido. Ver
`referencias/valores-anuales.md`.

## Fuentes oficiales de esta área

- Superintendencia de Industria y Comercio — Delegatura para la Propiedad Industrial
- Dirección Nacional de Derecho de Autor (DNDA)
- Tribunal de Justicia de la Comunidad Andina (interpretación prejudicial)
- Jueces civiles del circuito y SIC en función jurisdiccional

Catálogo completo en `referencias/fuentes-oficiales.md`.

## Salida

```markdown
## Verificación de citas — [nombre de la pieza]

**Conector de investigación:** [respondió / no disponible]
**Citas encontradas:** [N] — **verificadas:** [N] — **marcadas:** [N]

| # | Cita | Tipo | Lo que afirma la pieza | Resultado | Fuente consultada |
|---|---|---|---|---|---|
| 1 | Ley 1564 de 2012, art. 90 | Norma | Inadmisión de la demanda | ✅ Confirmado | SUIN-Juriscol |
| 2 | C-836 de 2001 | Sentencia | Doctrina probable | ⚠️ No verificado | sin conector |
| 3 | 2 años de caducidad | Término | Reparación directa | ✅ Confirmado | CPACA art. 164 |
| 4 | 100 SMLMV | Umbral | Tope de perjuicio moral | ⚠️ Verificar unificación vigente | — |

### 🔴 No usar sin verificar
[Citas que sostienen una conclusión y no se pudieron confirmar. Estas bloquean la radicación.]

### 🟠 Verificar antes de enviar
[Citas accesorias sin confirmar.]

### ✏️ Correcciones propuestas
[Cita | lo que dice la pieza | lo que dice la fuente | texto corregido]

### Pieza marcada
[La pieza con las marcas insertadas donde corresponde.]
```

## Compuerta

Si hay al menos una cita en 🔴, cerrar con:

> Hay [N] cita(s) que sostienen conclusiones y no pude confirmar. **No radique ni envíe
> esta pieza hasta resolverlas.** Puedo (a) intentar de nuevo con otra fuente,
> (b) reformular el argumento sin esa cita, o (c) dejarlas marcadas para que las
> verifique usted. ¿Cuál prefiere?

## Bitácora

Toda cita confirmada se anota en `~/.claude/plugins/config/claude-legal-colombia/propiedad-intelectual-co/bitacora-verificacion.md` para que la
siguiente pieza no la vuelva a verificar desde cero.

## Lo que esta skill NO hace

- No declara verificada una cita que no recuperó.
- No corrige el argumento jurídico: corrige la cita y señala si el argumento se cae.
- No sustituye la lectura del abogado.
