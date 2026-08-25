---
name: mapa-de-obligaciones
description: >
  Construye y mantiene la matriz de obligaciones normativas por área, con norma,
  obligación, responsable, evidencia y periodicidad. Actívela ante «matriz de
  cumplimiento», «mapa de obligaciones», «qué obligaciones legales tenemos», «matriz de
  requisitos legales», «inventario normativo», «no sé qué nos aplica».
---

# Mapa de obligaciones

**Antes de empezar.** Leer el perfil. Este es un entregable que se construye una vez y se
mantiene siempre; la mitad del valor está en el mantenimiento.

> **Una matriz de obligaciones sin responsable con nombre y sin evidencia esperada no
> sirve para nada.** Es la diferencia entre un documento que se muestra en una auditoría y
> uno que efectivamente organiza el cumplimiento.

## Paso 1 — Delimitar el alcance

| Pregunta | Efecto |
|---|---|
| ¿Qué actividad económica desarrolla la organización? | Define el marco sectorial |
| ¿Qué autoridades la vigilan? | Define de quién vienen las obligaciones |
| ¿Dónde opera? | Obligaciones territoriales: impuestos municipales, usos del suelo, licencias |
| ¿Tiene trabajadores? ¿Cuántos? | Umbrales laborales, SG-SST, copasst, comité de convivencia |
| ¿Trata datos personales? | Ley 1581 |
| ¿Contrata con el Estado? | Ley 80, inhabilidades |
| ¿Exporta o importa? | Aduanero, cambiario |
| ¿Es sujeto obligado a SAGRILAFT o PTEE? | Ver `/cumplimiento-co:diagnostico-de-obligados` |
| ¿Maneja recursos públicos o parafiscales? | |

**Delimitar es lo primero porque una matriz sin límite crece hasta volverse inútil.**

## Paso 2 — La estructura de la matriz

Una fila por obligación, no por norma. Una norma puede generar diez obligaciones y cada
una tiene su propio responsable y su propia periodicidad.

| Campo | Contenido |
|---|---|
| **ID** | Consecutivo |
| **Área** | Laboral, tributario, datos, ambiental, societario, sectorial, consumidor, SST |
| **Norma** | Tipo, número, año, **artículo** |
| **Obligación** | En lenguaje operativo, empezando con un verbo |
| **¿Nos aplica y por qué?** | El criterio: umbral, actividad, número de trabajadores |
| **Periodicidad** | Única, diaria, mensual, anual, por evento |
| **Fecha o plazo** | La concreta cuando existe |
| **Responsable** | **Cargo y nombre** |
| **Evidencia esperada** | El documento que prueba el cumplimiento |
| **Dónde reposa la evidencia** | Ruta, sistema, carpeta |
| **Estado** | ✅ cumple / ⚠️ parcial / 🔴 no cumple / ⏳ no aplicable aún |
| **Riesgo de incumplir** | Sanción concreta, con norma |
| **Última verificación** | Fecha y quién |

**El campo «evidencia esperada» es el que convierte la matriz en herramienta.** «Cumplir
con la política de tratamiento de datos» no se puede auditar; «política publicada en la
web, con fecha de vigencia, y acta de aprobación» sí.

## Paso 3 — El catálogo de arranque

Punto de partida para una empresa colombiana promedio. **No es exhaustivo y debe
depurarse contra la actividad real:**

### Societario y registral
Renovación de matrícula mercantil (31 de marzo); reunión ordinaria de asamblea (primeros
3 meses); depósito de estados financieros; actualización del registro de beneficiarios
finales `[verificar el régimen y los plazos vigentes]`; libros societarios.

### Tributario
Declaraciones según calendario de la DIAN; información exógena; facturación electrónica;
retenciones; ICA y predial municipales; conservación de soportes.

### Laboral y seguridad social
Afiliaciones; pago de aportes; **SG-SST** (Decreto 1072 de 2015) con su plan anual;
COPASST; **comité de convivencia laboral** (Ley 1010 y resoluciones); reglamento interno
de trabajo; reporte de accidentes (FURAT, 2 días); exámenes médicos ocupacionales;
consignación de cesantías (14 de febrero); intereses a cesantías (31 de enero).

### Datos personales
Política de tratamiento; aviso de privacidad; autorizaciones y su prueba; **RNBD** si
aplica; canal de atención de titulares; reporte de incidentes; contratos de transmisión.

### Consumidor
Información al consumidor; garantía legal; publicidad; **SIC**: cláusulas abusivas;
cobranza (Ley 2300 de 2023).

### Cumplimiento
SAGRILAFT y PTEE si es sujeto obligado; reportes a la UIAF; capacitaciones anuales;
informes del oficial de cumplimiento.

### Ambiental y sectorial
Permisos, licencias, planes de manejo, posconsumo, según la actividad.

### Propiedad intelectual
Renovación de marcas; anualidades de patentes; licencias de software.

**Cada organización tiene además su bloque sectorial**, que es el que hay que construir
con el negocio: salud, financiero, transporte, alimentos, construcción, educación,
servicios públicos.

## Paso 4 — El mantenimiento

Una matriz desactualizada es peor que no tenerla: da falsa seguridad.

| Disparador | Acción |
|---|---|
| **Novedad normativa material** | Correr `/regulatorio-co:analisis-de-impacto` y actualizar las filas afectadas |
| **Cambio en el negocio** | Nueva línea, nueva ciudad, nuevo canal, crecimiento que cruza un umbral |
| **Cambio de responsables** | Reasignar; una obligación sin dueño es una obligación incumplida |
| **Revisión periódica** | Al menos anual, área por área |
| **Hallazgo de auditoría o requerimiento de autoridad** | Actualizar y registrar |

**Los umbrales son el punto ciego más frecuente:** una empresa que crece deja de estar
exenta de cosas sin que nadie lo note. Revisar los umbrales **con corte a 31 de diciembre**
de cada año.

## Salida

```markdown
[ENCABEZADO DE PRODUCTO DE TRABAJO]

## Mapa de obligaciones — [organización] — [fecha]

### Alcance
| Punto | Contenido |
|---|---|
| Actividad y CIIU | |
| Autoridades que vigilan | |
| Territorios de operación | |
| N.º de trabajadores | |
| Umbrales relevantes al corte 31-12-[año] | |
| Áreas cubiertas por este mapa | |
| **Áreas NO cubiertas** | [decirlo explícitamente] |

### Resumen
| Área | Obligaciones | ✅ | ⚠️ | 🔴 | Sin responsable |
|---|---|---|---|---|---|

### 🔴 Incumplimientos
| ID | Obligación | Norma | Riesgo | Responsable | Plazo de corrección |
|---|---|---|---|---|---|

### Matriz completa
| ID | Área | Norma y art. | Obligación | Aplica porque | Periodicidad | Plazo | Responsable | Evidencia esperada | Dónde reposa | Estado | Riesgo | Última verificación |
|---|---|---|---|---|---|---|---|---|---|---|---|---|

### Calendario del año
| Mes | Obligación | Responsable |
|---|---|---|

### Obligaciones sin responsable asignado
[sección propia — es el hallazgo más accionable de todos]

### Umbrales a revisar el próximo cierre
| Umbral | Valor actual | Límite | Consecuencia de superarlo |
|---|---|---|---|

Fuentes: […] | Marcas pendientes: [N] | Revisó: [PENDIENTE DE REVISIÓN PROFESIONAL]
```

## Compuertas

- **Ninguna obligación sin responsable con nombre.** Las que no lo tengan van en sección
  propia.
- **Ninguna obligación sin evidencia esperada.**
- **Decir explícitamente qué áreas NO cubre el mapa.** Un mapa presentado como completo
  cuando no lo es genera la falsa seguridad que después cuesta.
- **Marcar `[verificar]` las obligaciones cuya norma o umbral no se confirmó.**
- **Revisar umbrales con corte a 31 de diciembre.**

## Lo que esta skill NO hace

- No verifica el cumplimiento: registra lo que se le informe.
- No reemplaza la auditoría.
- No cubre obligaciones sectoriales que no se le indiquen.
