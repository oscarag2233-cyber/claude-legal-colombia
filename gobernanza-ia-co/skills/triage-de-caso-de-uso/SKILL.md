---
name: triage-de-caso-de-uso
description: >
  Clasifica un caso de uso de IA propuesto por nivel de riesgo y decide qué controles y qué
  aprobaciones se activan antes de autorizarlo. Actívela ante «queremos usar IA para…»,
  «podemos usar esta herramienta», «aprobación de un caso de uso de IA», «riesgo de este
  proyecto de IA», «¿esto se puede automatizar?», «un área quiere implementar un modelo».
---

# Triage de caso de uso de IA

**Antes de empezar.** Leer el perfil, incluido quién aprueba y qué usos están prohibidos.

> Esta skill existe para que la respuesta a «¿podemos usar IA para esto?» no dependa de
> quién pregunte ni de qué día sea. **Mismo caso, mismo resultado.**

## Paso 1 — Entender el caso de uso de verdad

Cinco preguntas, y ninguna se salta:

1. **¿Qué decisión se va a tomar o a apoyar?** No «qué hace el sistema», sino qué cambia
   en el mundo por su salida.
2. **¿Sobre quién recae esa decisión?** Clientes, empleados, aspirantes, usuarios,
   ciudadanos, proveedores.
3. **¿Con qué datos?** Origen, categorías, si hay sensibles o de menores.
4. **¿Hay revisión humana, y es efectiva?** Un humano que aprueba doscientas
   recomendaciones por hora no está revisando: está firmando.
5. **¿Qué pasa si el sistema se equivoca?** En el peor caso, no en el promedio.

**La quinta pregunta es la que clasifica.** Un error en un asistente de redacción interna
cuesta una corrección; un error en un modelo que decide a quién se le da un crédito o a
quién se despide, afecta derechos.

## Paso 2 — Los niveles de riesgo

| Nivel | Criterio | Qué se activa |
|---|---|---|
| **🔴 Prohibido** | Cae en la lista de usos vedados del perfil, o vulnera derechos fundamentales de forma que ningún control mitiga | No se autoriza. Se explica por qué y se ofrece alternativa |
| **🟠 Alto** | Afecta decisiones sobre personas en materias sensibles: crédito, empleo, salud, educación, acceso a servicios esenciales, seguridad, justicia; o usa datos sensibles o biométricos; o hay decisión automatizada sin intervención humana significativa | Evaluación de impacto completa + aprobación del comité + revisión humana obligatoria + monitoreo + documentación reforzada + revisión periódica |
| **🟡 Medio** | Trata datos personales sin decisiones sobre derechos; o apoya decisiones de negocio relevantes con revisión humana | Evaluación simplificada + controles de datos + revisión humana + registro en el inventario |
| **🟢 Bajo** | No trata datos personales ni afecta decisiones sobre personas: apoyo a tareas internas, generación de borradores sin datos, análisis de información pública | Registro en el inventario + reglas generales de uso |

### Criterios de riesgo alto — la lista de chequeo

Basta que uno se cumpla para clasificar 🟠 como mínimo:

- [ ] Determina o influye en el **acceso a crédito**, seguros o servicios financieros.
- [ ] Interviene en **selección, evaluación, promoción o desvinculación** de personas.
- [ ] Interviene en **diagnóstico, triage o acceso a servicios de salud**.
- [ ] Interviene en **acceso a educación** o en evaluación académica.
- [ ] Trata **datos biométricos** para identificación.
- [ ] Trata **datos sensibles** o de **menores**.
- [ ] Interviene en **decisiones de autoridad pública** o en la administración de justicia.
- [ ] Produce **decisiones automatizadas sin intervención humana significativa**.
- [ ] Determina **precios personalizados** con base en características de la persona.
- [ ] Se usa en **vigilancia** de trabajadores o de personas.
- [ ] Puede producir **discriminación** por raza, sexo, género, edad, discapacidad, origen,
      religión u opinión política.
- [ ] Genera contenido que **suplanta identidad** o puede confundirse con contenido real.
- [ ] Trata **información de clientes bajo reserva profesional**.

## Paso 3 — El análisis jurídico

| Frente | Preguntas |
|---|---|
| **Datos personales** | ¿Base de legitimación? ¿La finalidad del tratamiento original cubre este uso? ¿Hay autorización para entrenar? ¿Transferencia internacional? → `/datos-personales-co:evaluacion-de-tratamiento` |
| **No discriminación** | ¿El sistema puede producir resultados diferenciados por características protegidas? ¿Se puede medir? |
| **Debido proceso** | Si la salida afecta derechos, ¿la persona puede conocer los criterios, controvertir y pedir revisión humana? |
| **Transparencia** | ¿Se le informa a la persona que hay un sistema automatizado de por medio? |
| **Consumidor** | ¿La IA interviene en la relación de consumo? ¿Hay deber de información? |
| **Propiedad intelectual** | ¿Los datos de entrenamiento están licenciados? ¿De quién es la salida? → `/propiedad-intelectual-co:derecho-de-autor-y-software` |
| **Reserva profesional** | Si es una firma: ¿se van a procesar datos de clientes? ¿Con qué contrato? |
| **Sectorial** | ¿La superintendencia del sector tiene exigencias? |
| **Responsabilidad** | Si el sistema causa un daño, ¿quién responde? ¿Qué dice el contrato del proveedor? |

## Paso 4 — Los controles por nivel

| Control | 🟢 | 🟡 | 🟠 |
|---|---|---|---|
| Registro en el inventario | ✓ | ✓ | ✓ |
| Reglas generales de uso | ✓ | ✓ | ✓ |
| Evaluación de impacto | | Simplificada | **Completa** |
| Aprobación del comité | | | **✓** |
| Base de legitimación documentada | | ✓ | ✓ |
| **Revisión humana efectiva** | | ✓ | **✓, con criterios y tiempo suficiente** |
| Información a las personas afectadas | | ✓ | ✓ |
| Mecanismo de reclamación y revisión | | | ✓ |
| Pruebas de desempeño y de resultados diferenciados | | | ✓ |
| Monitoreo continuo y métricas | | | ✓ |
| Plan de contingencia y apagado | | | ✓ |
| Revisión periódica | Anual | Anual | **Semestral** |
| Documentación técnica del proveedor | | ✓ | ✓ |

**«Revisión humana efectiva» tiene requisitos:** la persona debe tener competencia,
información suficiente, tiempo real para revisar, autoridad para apartarse de la
recomendación, y no debe ser evaluada por seguirla. Si falta cualquiera de esos, no hay
revisión humana: hay un sello.

## Salida

```markdown
[ENCABEZADO DE PRODUCTO DE TRABAJO]

## Triage — [caso de uso] — [área solicitante]

### Decisión
**[🟢 AUTORIZADO / 🟡 AUTORIZADO CON CONTROLES / 🟠 REQUIERE EVALUACIÓN Y APROBACIÓN /
🔴 NO AUTORIZADO]**

### El caso de uso
| Pregunta | Respuesta |
|---|---|
| Decisión que se toma o apoya | |
| Sobre quién recae | |
| Datos que usa | |
| ¿Sensibles o de menores? | |
| ¿Hay revisión humana? ¿Es efectiva? | |
| **Qué pasa si se equivoca (peor caso)** | |
| Proveedor y modalidad | |

### Clasificación
**Nivel:** [ ] — **Criterios que se cumplen:** [de la lista de chequeo]

### Análisis jurídico
| Frente | Estado | Observación |
|---|---|---|

### 🔴 Condiciones para autorizar
1. [condición concreta, verificable, con responsable]

### Controles que se activan
| Control | Responsable | Evidencia | Periodicidad |
|---|---|---|---|

### Si no se autoriza
**Razón:** [ ]
**Alternativa que sí se puede hacer:** [ ]

### Aprobaciones requeridas
| Aprobador | Estado |
|---|---|

Fuentes: […] | Marcas pendientes: [N] | Revisó: [PENDIENTE DE REVISIÓN PROFESIONAL]
```

## Compuertas

- **Ante duda entre dos niveles, se redondea hacia arriba.**
- **Si el caso cae en la lista de prohibidos del perfil, no se negocia:** se explica y se
  ofrece alternativa.
- **No aceptar «hay revisión humana» sin verificar que sea efectiva.**
- **Datos de clientes bajo reserva profesional en herramientas sin contrato es 🔴.**
- **Documentar la decisión, incluso las autorizaciones:** el registro de por qué se
  autorizó es lo que defiende la decisión después.

## Lo que esta skill NO hace

- No evalúa el desempeño técnico del modelo.
- No aprueba: prepara la decisión para quien tiene la competencia según el perfil.
- No sustituye la evaluación de impacto completa en los casos de riesgo alto.
