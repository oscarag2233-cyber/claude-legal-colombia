---
name: revision-de-proveedor-ia
description: >
  Revisa el contrato y los términos de un proveedor de IA: entrenamiento con datos del
  cliente, subencargados, transferencias internacionales, propiedad de las salidas,
  auditoría, disponibilidad y responsabilidad. Actívela ante «revisa los términos de esta
  herramienta de IA», «contrato con proveedor de IA», «¿usan nuestros datos para
  entrenar?», «due diligence de un proveedor de IA», «términos y condiciones de un
  asistente».
---

# Revisión de proveedor de IA

**Antes de empezar.** Leer el perfil. Y **conseguir los documentos completos**: los
términos de servicio, la política de privacidad, el acuerdo de tratamiento de datos y la
documentación de seguridad. Revisar solo la página comercial no sirve.

> **La pregunta central de todo contrato de IA cabe en una línea: ¿qué hace el proveedor
> con nuestros datos?** Todo lo demás se ordena alrededor de esa respuesta.

## Bloque 1 — 🔴 Datos y entrenamiento

| Pregunta | Por qué importa | Qué se busca |
|---|---|---|
| **¿Usa los datos de entrada para entrenar o mejorar sus modelos?** | Si lo hace, ya no es encargado: trata para fin propio, y la información puede aparecer en salidas de otros usuarios | Exclusión expresa, o *opt-out* efectivo y documentado |
| **¿Hay diferencia entre el plan gratuito y el empresarial?** | Casi siempre sí: el gratuito entrena, el empresarial no | Verificar el plan contratado |
| **¿Qué pasa con las salidas?** ¿También se usan? | | |
| **¿Cuánto tiempo conserva los datos?** | Retención por «seguridad» o «prevención de abuso» de 30 días es común | Plazo definido y borrado verificable |
| **¿Puede revisar humanamente las conversaciones?** | Muchos proveedores lo hacen para moderación | Saber si aplica y con qué controles |
| **¿Dónde se almacenan y procesan?** | Transferencia internacional | → `/datos-personales-co:transferencia-internacional` |
| **¿Quiénes son los subencargados?** | Infraestructura, modelos de terceros, moderación | Lista, aviso previo de cambios, mismas obligaciones |
| **¿Hay contrato de transmisión de datos** con el contenido del Decreto 1074? | Obligatorio si tratan datos personales por nuestra cuenta | Cláusulas del art. 2.2.2.25.5.2 `[verificar]` |
| **¿Qué pasa al terminar?** | | Devolución o supresión certificada, y plazo |

**Bandera roja mayor:** términos que se reservan una licencia amplia, perpetua e
irrevocable sobre el contenido que se ingresa. En una firma de abogados eso es
incompatible con la reserva profesional.

## Bloque 2 — Propiedad intelectual

| Punto | Qué revisar |
|---|---|
| **Titularidad de las salidas** | ¿El proveedor las cede? ¿Se reserva derechos? En Colombia, la obra requiere autoría humana: una salida puramente generada puede no tener protección por derecho de autor `[verificar la posición vigente de la DNDA]` |
| **Exclusividad** | ¿Otro usuario puede recibir una salida idéntica? |
| **Indemnidad por infracción** | ¿El proveedor responde si la salida infringe derechos de un tercero? Es una cláusula que algunos proveedores ofrecen y que vale mucho |
| **Datos de entrenamiento del proveedor** | ¿Declara que están licenciados? |
| **Nuestro contenido** | ¿Qué licencia le damos sobre lo que ingresamos? Debe ser la mínima necesaria para prestar el servicio |

## Bloque 3 — Desempeño, disponibilidad y cambios

| Punto | Qué revisar |
|---|---|
| **Nivel de servicio** | Disponibilidad, tiempos de respuesta, compensación por incumplimiento |
| **Cambios del modelo** | ¿El proveedor puede cambiar el modelo subyacente sin aviso? Un cambio de versión puede alterar los resultados de un proceso validado |
| **Descontinuación** | ¿Con cuánto aviso? ¿Hay período de transición? |
| **Cambios de los términos** | ¿Unilaterales? ¿Con aviso? ¿Con derecho a terminar sin penalidad? |
| **Portabilidad y salida** | ¿Cómo se recuperan los datos y las configuraciones? |
| **Dependencia** | ¿Qué tan difícil sería cambiar de proveedor? |

**El riesgo de cambio silencioso de modelo se subestima:** un proceso validado con una
versión puede degradarse con otra sin que nadie lo note. Pedir aviso previo de cambios
mayores, o al menos registro de versiones.

## Bloque 4 — Seguridad

| Punto | Qué pedir |
|---|---|
| Certificaciones | ISO 27001, SOC 2 Tipo II, u otras — **con el informe, no solo el logo** |
| Cifrado | En tránsito y en reposo |
| Controles de acceso | Autenticación, roles, registro de auditoría |
| **Notificación de incidentes** | Plazo corto: 24-48 horas. Más corto que el legal |
| Pruebas de seguridad | Pentesting, *red teaming* del modelo |
| Segregación | ¿Nuestros datos están separados de los de otros clientes? |

## Bloque 5 — Responsabilidad

| Punto | Realidad del mercado | Qué pedir |
|---|---|---|
| **Límite de responsabilidad** | Suele ser bajísimo: lo pagado en 12 meses, a veces menos | Carveouts para violación de datos, incumplimiento de confidencialidad y dolo o culpa grave |
| **Exclusión de daños indirectos** | Estándar | Verificar que no vacíe la obligación |
| **Descargo sobre las salidas** | Casi todos declaran que la salida puede ser inexacta y que el usuario es responsable de verificarla | **Esta cláusula es correcta y hay que asumirla**: refuerza el deber interno de verificación |
| **Indemnidad** | | Por infracción de PI y por incumplimiento de datos |
| **Seguro** | | Verificar cobertura |

**Sobre el descargo de responsabilidad por las salidas:** no hay que pelearlo, hay que
**operacionalizarlo**. Si el proveedor dice que la salida puede ser inexacta y que la
verificación es del usuario, entonces la política interna tiene que exigir esa
verificación. Ver `/gobernanza-ia-co:ia-en-la-practica-juridica`.

## Bloque 6 — Cumplimiento y gobierno

| Punto | Qué revisar |
|---|---|
| **Documentación del modelo** | Propósito, limitaciones, datos de entrenamiento, desempeño conocido |
| **Derecho de auditoría** | O entrega de informes de terceros |
| **Cooperación en el ejercicio de derechos de titulares** | Con plazos que permitan cumplir los 10 y 15 días hábiles de la Ley 1581 |
| **Cooperación ante requerimientos de autoridades** | Y deber de informarnos de requerimientos de autoridades extranjeras |
| **Ley aplicable y foro** | Un contrato regido por ley extranjera con foro extranjero puede hacer inviable cualquier reclamación |
| **Cumplimiento sectorial** | Si aplica |

## Cláusulas mínimas que hay que negociar

```
1. NO ENTRENAMIENTO. El Proveedor no utilizará los datos de entrada, las salidas ni
   ningún contenido del Cliente para entrenar, ajustar o mejorar modelos propios o de
   terceros, ni para ningún fin distinto de la prestación del Servicio al Cliente.

2. CONFIDENCIALIDAD Y RESERVA. El Proveedor reconoce que la información del Cliente puede
   estar amparada por reserva profesional y se obliga a tratarla con ese estándar,
   incluso después de terminado el contrato.

3. TRATAMIENTO DE DATOS. El Proveedor actúa como encargado y trata los datos únicamente
   conforme a las instrucciones del Cliente, en los términos del artículo 2.2.2.25.5.2
   del Decreto 1074 de 2015. [Cláusulas de contenido mínimo.]

4. SUBENCARGADOS. El Proveedor mantendrá una lista actualizada, informará con [N] días de
   antelación cualquier cambio, e impondrá a los subencargados las mismas obligaciones.

5. LOCALIZACIÓN. Los datos se procesarán y almacenarán en [ ]. Cualquier cambio requiere
   aviso previo de [N] días y derecho de terminación sin penalidad.

6. INCIDENTES. El Proveedor notificará cualquier incidente de seguridad dentro de las
   [24/48] horas siguientes a su detección, y colaborará en la atención de los deberes
   legales del Cliente.

7. SALIDAS. Las salidas generadas a partir de las entradas del Cliente son de su
   propiedad, en la medida en que sean susceptibles de apropiación. El Proveedor no
   reclama derecho alguno sobre ellas.

8. CAMBIOS DEL MODELO. El Proveedor informará con [N] días de antelación los cambios
   mayores del modelo subyacente que puedan alterar materialmente los resultados.

9. TERMINACIÓN Y SALIDA. Al terminar, el Proveedor devolverá o suprimirá los datos dentro
   de [N] días y certificará la supresión por escrito.

10. AUDITORÍA. El Cliente podrá auditar el cumplimiento, directamente o por un tercero,
    o el Proveedor entregará anualmente su informe SOC 2 Tipo II vigente.
```

## Salida

```markdown
[ENCABEZADO DE PRODUCTO DE TRABAJO]

## Revisión de proveedor — [proveedor] — [herramienta]

### Semáforo
**[✅ SE PUEDE CONTRATAR / 🟡 CON ESTAS CONDICIONES / 🔴 NO SE PUEDE CONTRATAR PARA ESTE USO]**

### Uso previsto y datos que se procesarían
| Punto | Contenido |
|---|---|
| Uso | |
| Clasificación de los datos | |
| ¿Datos de clientes bajo reserva? | 🔴 si sí y no hay contrato adecuado |
| Volumen y frecuencia | |

### 🔴 Hallazgos bloqueantes
| # | Cláusula | Problema | Norma o riesgo | Qué se exige |
|---|---|---|---|---|

### Revisión por bloques
| Bloque | Hallazgos | Severidad |
|---|---|---|
| Datos y entrenamiento | | |
| Propiedad intelectual | | |
| Desempeño y cambios | | |
| Seguridad | | |
| Responsabilidad | | |
| Cumplimiento y gobierno | | |

### Cláusulas a negociar, por prioridad
| # | Cláusula | Texto propuesto | ¿Innegociable? |
|---|---|---|---|

### Si el proveedor no negocia
[qué usos quedan permitidos con los términos actuales y cuáles no]

### Controles compensatorios
[si no se logra la cláusula ideal: anonimización previa, restricción de datos, uso
limitado, revisión reforzada]

Fuentes: […] | Marcas pendientes: [N] | Revisó: [PENDIENTE DE REVISIÓN PROFESIONAL]
```

## Compuertas

- **Si el proveedor entrena con los datos del cliente y no hay *opt-out* efectivo, no se
  contrata para datos confidenciales, personales ni de clientes.** Sin excepción.
- **Los términos gratuitos no sirven para información de clientes.** Es la conclusión más
  frecuente y la más resistida.
- **Verificar el plan efectivamente contratado**, no el que aparece en la página comercial.
- **Si no se logran las cláusulas mínimas, proponer controles compensatorios y restringir
  el uso**, en lugar de aprobar sin condiciones.

## Lo que esta skill NO hace

- No negocia con el proveedor.
- No audita seguridad técnica.
- No aprueba: prepara la decisión.
