---
name: politica-de-uso-de-ia
description: >
  Redacta la política interna de uso de inteligencia artificial: usos permitidos,
  prohibidos, revisión humana obligatoria, régimen de datos y gobierno. Actívela ante
  «política de uso de IA», «reglamento interno de IA», «lineamientos para usar ChatGPT en
  la empresa», «los empleados están usando IA sin control», «norma interna sobre IA»,
  «capacitación en uso de IA».
---

# Política de uso de IA

**Antes de empezar.** Correr `/gobernanza-ia-co:inventario-de-ia`. **Una política escrita
sin conocer lo que la gente ya usa se incumple desde el primer día.**

> **La política que funciona no es la que prohíbe: es la que habilita con condiciones.**
> Una política puramente restrictiva empuja el uso a la clandestinidad, que es exactamente
> el escenario de mayor riesgo: datos de clientes en herramientas gratuitas sin contrato,
> sin registro y sin control.

## Paso 1 — Las decisiones de fondo, antes de redactar

| Decisión | Opciones | Consecuencia |
|---|---|---|
| **Postura general** | Prohibir salvo autorización / Permitir salvo prohibición / Permitir herramientas aprobadas | La tercera es la que mejor funciona |
| **Herramientas aprobadas** | Lista cerrada, con contrato y con controles | Requiere mantenerla actualizada |
| **Qué datos pueden entrar** | Públicos / internos / confidenciales / de clientes / personales / sensibles | Es la regla más importante de toda la política |
| **Revisión humana** | Siempre / según el uso / según el riesgo | |
| **Transparencia** | ¿Se declara el uso de IA a clientes, contrapartes, autoridades? | |
| **Quién autoriza excepciones** | | |
| **Consecuencias del incumplimiento** | Disciplinarias, en los términos del reglamento interno | Sin esto la política es una sugerencia |

## Paso 2 — La regla de datos, que es el corazón

Una tabla de clasificación que cualquiera pueda aplicar en cinco segundos:

| Clasificación | Ejemplos | ¿Puede entrar a una herramienta de IA? |
|---|---|---|
| **Público** | Normas, jurisprudencia publicada, información del sitio web | ✅ En cualquier herramienta aprobada |
| **Interno** | Procesos, plantillas, comunicaciones internas sin datos personales | ✅ Solo en herramientas aprobadas con contrato |
| **Confidencial** | Estrategia, información financiera no pública, negociaciones | ⚠️ Solo con autorización y en herramientas con contrato y sin uso para entrenamiento |
| **Datos personales** | De empleados, clientes, terceros | ⚠️ Solo con base de legitimación, en herramientas con contrato de transmisión, y preferiblemente **anonimizados** |
| **Datos sensibles y de menores** | Salud, biométricos, origen étnico, orientación | 🔴 **No**, salvo autorización expresa del comité y con evaluación de impacto |
| **🔴 Información de clientes bajo reserva profesional** | Expedientes, estrategia procesal, documentos del cliente | 🔴 **No**, salvo herramientas contratadas por la firma con contrato de tratamiento y con autorización informada del cliente cuando corresponda |
| **Credenciales y secretos** | Contraseñas, llaves, tokens | 🔴 **Nunca** |

**La regla operativa que la gente recuerda:** *si no lo publicarías en el sitio web de la
empresa, no lo pegues en una herramienta que no está aprobada.*

**Anonimizar primero.** Ver `referencias/tratamiento-de-datos.md`.

## Paso 3 — Estructura de la política

```markdown
POLÍTICA DE USO DE INTELIGENCIA ARTIFICIAL
[Organización] — Versión [ ] — Vigente desde [fecha]

1. OBJETO Y ÁMBITO
   A quién aplica: empleados, contratistas, practicantes, proveedores con acceso.

2. DEFINICIONES
   Sistema de IA, IA generativa, herramienta aprobada, dato de entrada, salida.

3. PRINCIPIOS
   Legalidad · Responsabilidad humana · Protección de datos · No discriminación ·
   Transparencia · Confidencialidad y reserva profesional · Verificación · Trazabilidad.

4. HERRAMIENTAS APROBADAS
   Lista, con el uso permitido de cada una. Cómo se solicita la aprobación de una nueva.

5. CLASIFICACIÓN DE INFORMACIÓN Y REGLAS DE ENTRADA
   [La tabla del Paso 2]

6. USOS PERMITIDOS
   [Lista concreta, con ejemplos del trabajo real]

7. 🔴 USOS PROHIBIDOS
   a) Ingresar información de clientes bajo reserva profesional a herramientas no
      aprobadas.
   b) Ingresar datos sensibles o de menores sin autorización del comité.
   c) Ingresar credenciales, llaves o secretos.
   d) Usar la salida sin verificación cuando el uso lo exija.
   e) Tomar decisiones sobre personas —contratación, desvinculación, evaluación,
      acceso a servicios— con base únicamente en una salida de IA.
   f) Suplantar personas o generar contenido engañoso.
   g) Presentar como propia una salida de IA cuando el destinatario espera trabajo humano
      y el contexto lo exige.
   h) Eludir controles de seguridad o de acceso.
   i) [Los propios de la organización]

8. REVISIÓN HUMANA
   Qué usos exigen revisión, en qué consiste y quién responde.
   **La responsabilidad por la salida es siempre de la persona que la usa.**

9. VERIFICACIÓN DE CONTENIDO
   Toda cita normativa, jurisprudencial, dato numérico o referencia debe verificarse en
   fuente oficial antes de usarse. Ver `referencias/verificacion-de-fuentes.md`.

10. TRANSPARENCIA
    Cuándo se informa el uso de IA: a clientes, a contrapartes, a autoridades, a
    destinatarios de contenido.

11. PROPIEDAD INTELECTUAL
    Titularidad de las salidas; respeto de derechos de terceros en las entradas.

12. GOBIERNO
    Comité, responsable de la política, inventario, evaluaciones, revisión periódica.

13. INCUMPLIMIENTO
    Consecuencias disciplinarias conforme al reglamento interno de trabajo.

14. CANAL DE CONSULTAS
    A quién preguntar antes de usar algo en caso de duda.

15. VIGENCIA Y ACTUALIZACIÓN
```

## Paso 4 — Lo que hace que se cumpla

| Factor | Cómo |
|---|---|
| **Que sea corta** | Dos o tres páginas. Un anexo con la tabla de datos y la lista de herramientas |
| **Que dé alternativas** | Por cada prohibición, decir qué sí se puede hacer |
| **Que haya un canal fácil** | «Pregúntele a [ ] antes de usarlo» resuelve más que diez páginas |
| **Que la lista de herramientas esté al día** | Una lista desactualizada empuja al uso no autorizado |
| **Que haya capacitación con casos reales** | No con teoría: con los casos de esta organización |
| **Que la dirección la cumpla** | Si la alta dirección usa herramientas no aprobadas, la política muere |
| **Que se actualice** | Semestral. El campo cambia rápido |

## Paso 5 — Anexo para firmas de abogados

Si la organización es una firma o un departamento jurídico, la política incorpora:

- **Reserva profesional** (Const. art. 74; Ley 1123 de 2007, art. 34 lit. f): la
  información del cliente no entra a herramientas sin contrato de tratamiento.
- **Deber de diligencia** (art. 33): **verificación obligatoria de toda cita** antes de
  radicar o entregar. Ver `/gobernanza-ia-co:ia-en-la-practica-juridica`.
- **Información al cliente**: cuándo se le informa el uso de IA en su asunto, y si hay
  que pedirle autorización.
- **Uso en actuaciones judiciales**: Ley 2213 de 2022 y lineamientos del Consejo Superior
  de la Judicatura `[verificar]`.
- **Facturación**: si la IA reduce el tiempo, cómo se refleja en los honorarios pactados
  por hora. Es una conversación incómoda y es mejor tenerla en la política que con el
  cliente.

## Salida

```markdown
[ENCABEZADO DE PRODUCTO DE TRABAJO]

## Política de uso de IA — [organización]

### Decisiones de fondo adoptadas
| Decisión | Opción | Justificación |
|---|---|---|

---
[TEXTO DE LA POLÍTICA]
---

### Anexo 1 — Herramientas aprobadas
| Herramienta | Uso permitido | Datos permitidos | Contrato | Vence |
|---|---|---|---|---|

### Anexo 2 — Clasificación de información
[la tabla]

### Plan de implementación
| Acción | Responsable | Plazo |
|---|---|---|
| Aprobación por [órgano] | | |
| Comunicación | | |
| Capacitación con casos propios | | |
| Actualización del reglamento interno de trabajo | | |
| Canal de consultas | | |
| Primera revisión | | |

### Puntos que quedaron pendientes de decisión
| Punto | Opciones | Quién decide |
|---|---|---|

Fuentes: […] | Marcas pendientes: [N] | Revisó: [PENDIENTE DE REVISIÓN PROFESIONAL]
```

## Compuertas

- **No redactar una política sin inventario previo.**
- **Por cada prohibición, dar la alternativa.**
- **Si la política va a un reglamento interno de trabajo con efectos disciplinarios,
  verificar el procedimiento de adopción y publicidad** (CST arts. 104 y ss.). Una
  política no divulgada no sostiene una sanción.
- **En firmas, la reserva profesional manda sobre cualquier conveniencia operativa.**
- **Fijar fecha de revisión.** Una política de IA sin fecha de vencimiento nace obsoleta.

## Lo que esta skill NO hace

- No adopta la política: la redacta para aprobación.
- No evalúa herramientas técnicamente.
- No sustituye la capacitación.
