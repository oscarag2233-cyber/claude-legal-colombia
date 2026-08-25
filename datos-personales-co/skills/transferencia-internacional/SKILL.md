---
name: transferencia-internacional
description: >
  Determina si una operación es transferencia o transmisión internacional de datos, qué
  exige cada una, si el país de destino tiene nivel adecuado según la SIC y cómo se
  documenta el contrato de transmisión. Actívela ante «los datos se van a otro país»,
  «servidores en el exterior», «nube extranjera», «transferencia internacional»,
  «proveedor en Estados Unidos», «cláusulas contractuales de datos», o cuando cualquier
  dato personal salga de Colombia.
---

# Transferencia internacional

**Antes de empezar.** Leer el perfil. Presupone que ya se corrió
`/datos-personales-co:evaluacion-de-tratamiento` y se determinó el rol.

## Paso 1 — La distinción que decide todo

| Figura | Qué es | Régimen |
|---|---|---|
| **Transferencia** | El dato se envía a un **receptor que es responsable** del tratamiento | Ley 1581 **art. 26**: prohibida hacia países sin nivel adecuado de protección, salvo excepciones |
| **Transmisión** | El dato se comunica a un **encargado** que lo trata **por cuenta del responsable** | Decreto 1074 (compiló el Decreto 1377): **contrato de transmisión** con contenido mínimo; no exige declaración de nivel adecuado |

**Prueba práctica:** ¿quién decide para qué se usa el dato en el destino?
Si el receptor decide → **transferencia**. Si solo ejecuta instrucciones → **transmisión**.

**La mayoría de los servicios en la nube son transmisión.** Un proveedor de
infraestructura que aloja datos bajo instrucciones del cliente es encargado. Tratarlo
como transferencia complica sin necesidad; tratar como transmisión lo que es
transferencia deja la operación sin cobertura.

## Paso 2 — Si es transferencia: el artículo 26

**Regla:** se prohíbe la transferencia a países que no proporcionen niveles adecuados de
protección.

**Excepciones (art. 26):**

a) **Autorización expresa e inequívoca del titular** para la transferencia.
b) **Intercambio de datos médicos**, cuando lo exija el tratamiento del titular por
   razones de salud o higiene pública.
c) **Transferencias bancarias o bursátiles**, conforme a la legislación aplicable.
d) Transferencias acordadas en **tratados internacionales** de los que Colombia sea
   parte, con fundamento en reciprocidad.
e) Transferencias necesarias para la **ejecución de un contrato** entre el titular y el
   responsable, o de medidas precontractuales, con autorización del titular.
f) Transferencias legalmente exigidas para la **salvaguardia del interés público** o para
   el reconocimiento, ejercicio o defensa de un derecho en un proceso judicial.

**Nivel adecuado:** la SIC ha fijado por circular los criterios y el listado de países
considerados con nivel adecuado, además de un mecanismo de **declaración de conformidad**
para casos no cubiertos. `[verificar circular y listado vigentes]`

**Lo más práctico en operaciones comerciales:** obtener la **autorización expresa e
inequívoca**, informando país de destino y finalidad. Debe ser específica, no una mención
genérica en la política.

## Paso 3 — Si es transmisión: el contrato

Contenido mínimo `[verificar el texto vigente del Decreto 1074, art. 2.2.2.25.5.2]`:

1. **Alcances y finalidades** del tratamiento.
2. **Actividades** que el encargado realizará por cuenta del responsable.
3. **Obligaciones** del encargado frente al titular y al responsable.
4. Deber de **tratar los datos conforme a la finalidad** fijada por el responsable y a su
   política de tratamiento.
5. Obligación de **proteger** adecuadamente los datos y de guardar **confidencialidad**.
6. Obligación de **devolver o suprimir** los datos al terminar la relación.

**Cláusulas que conviene añadir aunque la norma no las exija:**

- Prohibición de usar los datos para fines propios, **incluido el entrenamiento de
  modelos de IA**.
- **Subencargados**: autorización previa, lista, y traslado de las mismas obligaciones.
- **Notificación de incidentes** en 24-48 horas y deber de colaboración.
- **Auditoría** o entrega de certificaciones e informes.
- Localización de los datos y aviso previo de cambio de ubicación.
- Colaboración en la atención de derechos, con plazos que permitan cumplir los 10 y 15
  días hábiles de la Ley 1581.
- Responsabilidad e indemnidad.
- Deber de informar requerimientos de autoridades extranjeras.

## Paso 4 — Riesgos que hay que mirar aunque la norma no los exija

| Riesgo | Pregunta |
|---|---|
| Acceso de autoridades extranjeras | ¿La ley del país de destino permite acceso gubernamental? |
| Subencargados en cadena | ¿A dónde llegan realmente los datos? |
| **Entrenamiento de modelos** | Si es un servicio de IA, esta es la pregunta central |
| Retención tras la terminación | ¿En cuánto borra? ¿Copias de respaldo? |
| Cambio unilateral de términos | ¿Puede cambiar la política sin aviso? |
| Datos sensibles | ¿Salen datos de salud, biométricos o de menores? Eleva todo |

## Salida

```markdown
[ENCABEZADO DE PRODUCTO DE TRABAJO]

## Flujo internacional — [proveedor / destinatario]

### Calificación
**Figura:** [TRANSFERENCIA / TRANSMISIÓN] — **Razón:** [quién decide la finalidad en destino]

### Mapa del flujo
| Elemento | Detalle |
|---|---|
| Datos que salen | |
| ¿Sensibles o de menores? | |
| País(es) de destino | |
| Subencargados conocidos | |
| Finalidad en destino | |
| Conservación | |

### Si es transferencia
| Punto | Estado |
|---|---|
| ¿País con nivel adecuado según la SIC? | `[verificar listado vigente]` |
| Excepción del art. 26 aplicable | [cuál] |
| Autorización específica del titular | [texto y canal] |
| ¿Requiere declaración de conformidad? | |

### Si es transmisión
| Cláusula | ¿Está en el contrato? | Observación |
|---|---|---|

### 🔴 Brechas
| Brecha | Riesgo | Cómo se cierra |
|---|---|---|

### Recomendación
[puede proceder / con estas condiciones / no puede proceder]

---
[CLÁUSULAS DE TRANSMISIÓN, si se pidieron]
---

Fuentes: […] | Marcas pendientes: [N] | Revisó: [PENDIENTE DE REVISIÓN PROFESIONAL]
```

## Compuertas

- **No afirmar que un país tiene nivel adecuado sin verificar la circular vigente.**
- **No calificar como transmisión lo que es transferencia** para eludir el art. 26.
- **Datos sensibles saliendo del país sin autorización específica es 🔴.**
- **Si el proveedor usa los datos para entrenar modelos, ya no es encargado**: trata para
  fin propio y hay que rehacer el análisis.

## Lo que esta skill NO hace

- No tramita declaraciones de conformidad ante la SIC.
- No audita al proveedor.
- No mantiene el listado de países con nivel adecuado: remite a la circular vigente.
