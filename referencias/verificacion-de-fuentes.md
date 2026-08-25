# Verificación de fuentes y etiquetado de citas

**Esta es la regla dura del repositorio.** Cualquier skill que cite una norma, una
sentencia, un concepto de autoridad, un término o un umbral se somete a lo siguiente.

## 1. Tres valores, no dos

Cuando falta información (el texto de una norma, la posición de una autoridad, una
fecha de entrada en vigencia), hay **tres** respuestas válidas:

1. **Complementar con marca.** Traer el dato de búsqueda web, del conocimiento del
   modelo o de otra fuente inspeccionable, etiquetarlo (`[web — verificar]`,
   `[conocimiento del modelo — verificar]`) y continuar.
2. **Callar y detenerse.** Pedir al usuario que pegue la fuente o señale el
   documento primario, y no continuar hasta tenerlo.
3. **Marcar sin usar.** Si se conoce algo que cambiaría si la norma aplica o está
   vigente —demanda de inconstitucionalidad en curso, proyecto de derogatoria,
   suspensión provisional, reglamentación pendiente— se advierte como salvedad
   marcada `[conocimiento del modelo — verificar]` aunque no se use para modificar
   el análisis.

> Ejemplo: «Nota: entiendo que esta norma pudo haber sido demandada o modificada con
> posterioridad `[conocimiento del modelo — verificar]`. El análisis siguiente asume
> que está vigente en su texto original. Confirme el estado en SUIN-Juriscol antes de
> radicar.»

Callar sobre una duda conocida engaña tanto como afirmar con falsa seguridad.

## 2. Disparador de actualidad

La regla anterior *permite* buscar; en estos casos la búsqueda es **obligatoria**
antes de apoyarse en el conocimiento del modelo:

- Jurisprudencia reciente o cambio de línea (especialmente sentencias de unificación).
- Vigencia, exequibilidad o entrada en aplicación de una ley reciente.
- Reforma tributaria, laboral, pensional o de salud en trámite o recién expedida.
- Umbrales que se actualizan cada año (SMLMV, UVT, topes de competencia por cuantía,
  topes de contratación estatal, montos de SAGRILAFT/PTEE).
- Posición de una superintendencia (circulares externas, conceptos).

Prueba práctica: ¿un boletín de firma sobre este tema tendría sección de
«novedades»? Si sí, hay que mirar qué pasó últimamente.

## 3. Etiquetas de procedencia

La etiqueta describe **de dónde salió la cita**, no cuánta confianza le tiene.

| Etiqueta | Cuándo se usa |
|---|---|
| `[Corte Constitucional]` | La sentencia apareció en un resultado de la relatoría oficial o del buscador de la Corte **en esta sesión** |
| `[Corte Suprema]` / `[Consejo de Estado]` | Ídem, relatoría oficial de la corporación |
| `[SUIN-Juriscol]` | El texto normativo se recuperó de SUIN-Juriscol en esta sesión |
| `[Diario Oficial]` | Se verificó publicación y número de Diario Oficial |
| `[sitio de la autoridad]` | Circular, resolución o concepto recuperado del sitio de la SIC, DIAN, SuperSociedades, MinTrabajo, etc. |
| `[aportado por el usuario]` | El usuario pegó o adjuntó el texto |
| `[conocimiento del modelo — verificar]` | **Todo lo demás. Es el valor por defecto.** Si no se recuperó, es conocimiento del modelo por seguro que suene |
| `[estable — última confirmación AAAA-MM-DD]` | Norma estructural confirmada contra fuente primaria en esa fecha (p. ej. «CGP, Ley 1564 de 2012, art. 90») |

**No se asciende una etiqueta porque la cita «se ve bien».**

Una cita sin etiqueta se lee como verificada. Si no la verificó, etiquétela.

## 4. Vocabulario de marcas de revisión

- `[verificar]` — dato fáctico (cita, fecha, término, umbral, radicado) que el lector
  debe confirmar contra fuente primaria antes de usar.
- `[revisar]` — juicio profesional que le corresponde decidir al abogado, no un vacío
  de información.
- `[VERIFICAR: …]` / `[INCIERTO: …]` — formas expandidas, con el punto concreto
  explicitado, para memoriales y cronologías.

## 5. Chequeo previo (pre-flight)

Antes de correr cualquier skill que cite autoridad, comprobar si hay un conector de
investigación **respondiendo**, no solo configurado. Si no lo hay, registrarlo en la
línea **Fuentes:** de la nota al revisor:

`Fuentes: sin conector de jurisprudencia — las citas provienen del conocimiento del modelo; verificar antes de usar`

## 6. Fabricación de citas: qué hacer cuando no se tiene el texto

Si el usuario, la contraparte o un documento cita una norma para una proposición que
no parece correcta, y no se tiene el texto:

> «Ese artículo no corresponde a lo que yo esperaría. Necesitaría el texto para
> decirle qué dice realmente `[norma no recuperada — verificar]`.»

Luego: (a) recuperar el texto y citarlo literal, (b) pedir que lo peguen, o (c)
marcar para revisión del abogado. **Una descripción segura y equivocada de una norma
real es peor que un vacío**: es más difícil de desmentir y es la vía por la que
termina autoridad inventada en un memorial radicado.

## 7. Bitácora de verificación

Cuando alguien verifica un ítem marcado, se registra para que el siguiente no repita
el trabajo. Una línea en
`~/.claude/plugins/config/claude-legal-colombia/<plugin>/bitacora-verificacion.md`:

`[AAAA-MM-DD] [cita o dato] verificado por [nombre] contra [fuente] — [resultado: confirmado / corregido a X / no se pudo verificar]`
