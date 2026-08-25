# Aviso legal

## Esto no es asesoría jurídica

Todo lo que producen estos plugins es un **borrador de trabajo sujeto a revisión
profesional**. No es concepto jurídico, no es asesoría, no constituye ejercicio de
la abogacía y no reemplaza a un abogado titulado e inscrito.

En Colombia el ejercicio de la abogacía está reservado a quienes tienen tarjeta
profesional vigente (Decreto 196 de 1971 y Ley 1123 de 2007). Un modelo de lenguaje
no puede otorgar poder, no puede firmar, no puede comparecer y no puede asumir la
responsabilidad disciplinaria que el Estatuto del Abogado le impone al profesional.
**La responsabilidad profesional por cualquier pieza que salga de aquí es del abogado
que la revisa, la suscribe y la radica.**

## Deberes profesionales que estos plugins no relevan

| Deber | Fuente | Qué significa aquí |
|---|---|---|
| Diligencia y competencia | Ley 1123 de 2007, art. 28 num. 9 y art. 34 | Verificar cada norma, cada cita y cada término antes de radicar |
| Reserva profesional | Ley 1123 de 2007, art. 34 lit. f; Const. art. 74 | No cargar información de clientes en herramientas sin control ni contrato |
| Lealtad y no colisión de intereses | Ley 1123 de 2007, art. 34 lit. b y c | El modelo no detecta conflictos de interés; usted sí debe hacerlo |
| Información veraz al cliente | Ley 1123 de 2007, art. 33 | No presentar como concepto lo que es un borrador generado |
| Protección de datos del cliente | Ley 1581 de 2012 | Anonimizar antes de procesar; ver `referencias/tratamiento-de-datos.md` |

## Riesgo específico: fabricación de citas

Los modelos de lenguaje generan citas jurisprudenciales y normativas que **parecen
correctas y no existen**. En Colombia esto ya ha producido sanciones y llamados de
atención judiciales, y en cualquier caso configura falta a la lealtad procesal.

Por eso, todo el repositorio está construido sobre una regla dura:

> **Ninguna cita se presenta como verificada si no fue recuperada en esta sesión de
> una fuente oficial.** Toda cita que provenga del conocimiento del modelo se marca
> `[conocimiento del modelo — verificar]`. Ver `referencias/verificacion-de-fuentes.md`.

## Vigencia normativa

El derecho colombiano cambia rápido. Las normas citadas en este repositorio se
listan con su estado a la fecha de última revisión del archivo correspondiente, y
todas las skills están instruidas para **verificar vigencia antes de aplicar**:
derogatorias tácitas, inexequibilidades, exequibilidades condicionadas, decretos
reglamentarios posteriores y sentencias de unificación cambian el resultado.

## Uso de IA ante autoridades judiciales

Si va a usar salidas de estos plugins en actuaciones judiciales, revise:

- Ley 2213 de 2022 — uso de TIC en actuaciones judiciales.
- Los lineamientos del Consejo Superior de la Judicatura sobre uso de inteligencia
  artificial en la Rama Judicial y las reglas de la Corte Constitucional sobre el
  particular. `[verificar versión vigente]`
- El deber de transparencia frente al despacho cuando la herramienta incidió en la
  elaboración de la pieza.

Ver el plugin `gobernanza-ia-co` y `referencias/ia-y-judicatura.md`.
