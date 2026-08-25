---
name: cronologia-del-caso
description: >
  Construye la línea de tiempo del asunto con la fuente y el folio de cada hecho,
  distinguiendo lo probado de lo alegado y marcando los vacíos. Sirve para preparar
  audiencia, interrogatorios, alegatos y para entregarle el caso a otro abogado.
  Actívela ante «arma la cronología», «línea de tiempo del caso», «ordena los hechos»,
  «prepara la audiencia», «resume el expediente», o cuando el usuario aporte varios
  documentos de un mismo asunto.
---

# Cronología del caso

**Antes de empezar.** Leer el perfil. Si hay asunto activo, cargar su contexto. Si el
usuario aporta documentos con datos personales, aplicar
`referencias/tratamiento-de-datos.md`: anonimizar antes de procesar cuando corresponda.

## Para qué sirve una cronología bien hecha

- **Audiencia:** llegar sabiendo qué fecha está probada con qué folio.
- **Interrogatorio:** cada pregunta apoyada en un documento con fecha.
- **Alegatos:** los indicios se construyen sobre secuencias, y la secuencia hay que
  tenerla.
- **Entrega del caso:** que el siguiente abogado no reconstruya desde cero.
- **Detección de vacíos:** los huecos de la línea de tiempo son los huecos del caso.

## Estructura

| Fecha | Hecho | Fuente | Estado | Relevancia |
|---|---|---|---|---|
| 03-02-2024 | Se celebra el contrato | Contrato, anexo 1, fl. 12 | ✅ Probado | Elemento 1 de la pretensión |
| 14-03-2024 | Se entrega la mercancía | Remisión 4521, fl. 34 | ✅ Probado | |
| ~abril 2024 | Reclamos verbales del comprador | Dicho del cliente | ⚠️ Solo alegado | Cierra el vacío entre marzo y mayo |
| 02-05-2024 | Correo de reclamación formal | Correo, fl. 41 | ✅ Probado | Interrumpe prescripción |
| 15-07-2024 | Vence el plazo de garantía | Cláusula 8 del contrato | ✅ Documental | 🔴 Término |

### Columna «Estado» — la que hace útil la tabla

| Marca | Significa |
|---|---|
| ✅ Probado | Hay documento o prueba en el expediente que lo acredita |
| 📄 Documental sin controvertir | Consta en documento, pero la contraparte no se ha pronunciado |
| ⚠️ Solo alegado | Lo dice una parte y no hay respaldo |
| ❌ Controvertido | Las partes afirman versiones distintas |
| ❓ Vacío | Hay un salto de tiempo sin explicar |

**Nunca poner ✅ sobre lo que dijo el cliente sin documento.** Es exactamente la
confusión que después se cae en audiencia.

## Cómo se construye

1. **Inventariar las fuentes.** Cada documento con su identificación y folio.
2. **Extraer todo hecho con fecha.** Incluidos los que no favorecen: una cronología que
   solo trae lo bueno es inútil para preparar la audiencia, porque el juez va a ver todo.
3. **Ordenar y detectar saltos.** Un vacío de tres meses sin ningún hecho suele ser el
   lugar donde está el problema.
4. **Marcar los hitos jurídicos:**
   - 🔴 Fechas que activan términos: exigibilidad, notificación, vencimiento de plazo,
     inicio de prescripción o caducidad, interrupciones.
   - ⚖️ Hechos que corresponden a un elemento de la pretensión o de una excepción.
5. **Cruzar con la teoría del caso.** Cada elemento jurídico debe poder señalar una
   fila.

## Vistas derivadas

Ofrecer, según lo que el usuario necesite:

- **Cronología procesal** — solo actuaciones del expediente: demanda, admisión,
  notificación, contestación, audiencias, autos, recursos. Con sus términos.
- **Cronología sustancial** — solo los hechos del conflicto.
- **Cronología por actor** — qué hizo cada parte, en paralelo. Útil para mostrar
  conducta procesal o mala fe.
- **Cronología de una sola cuestión** — por ejemplo, solo lo relativo al pago.

## Salida

```markdown
[ENCABEZADO DE PRODUCTO DE TRABAJO]

## Cronología — [asunto, radicado]

### Resumen en cinco líneas
[qué pasó, en el orden en que un tercero lo entendería]

### Línea de tiempo
[la tabla completa]

### 🔴 Fechas críticas
| Fecha | Qué activa | Norma | Estado |
|---|---|---|---|

### ❓ Vacíos
| Período sin hechos | Qué habría que conseguir | Quién lo tiene |
|---|---|---|

### ❌ Hechos controvertidos
| Hecho | Versión nuestra | Versión contraria | Qué inclina |
|---|---|---|---|

### Cruce con la teoría del caso
| Elemento jurídico | Fila de la cronología | Estado probatorio |
|---|---|---|

Fuentes: […] | Marcas pendientes: [N] | Revisó: [PENDIENTE DE REVISIÓN PROFESIONAL]
```

## Compuertas

- **No inventar fechas.** Si un documento no tiene fecha cierta, se dice: «sin fecha en
  el documento; se ubica en [período] por [razón]».
- **No convertir el dicho del cliente en hecho probado.**
- **Las fechas que activan términos van marcadas 🔴** aunque el usuario no haya
  preguntado por términos.

## Lo que esta skill NO hace

- No valora la prueba: ordena y marca.
- No decide la teoría del caso: la contrasta con lo que hay.
- No reemplaza la lectura del expediente por el abogado.
