---
name: politica-y-aviso
description: >
  Redacta la política de tratamiento de la información y el aviso de privacidad con el
  contenido mínimo del Decreto 1074 de 2015, y las cláusulas y textos de autorización que
  efectivamente sirvan como prueba. Actívela ante «política de tratamiento de datos»,
  «aviso de privacidad», «texto de autorización», «cláusula de datos personales»,
  «necesito la política de habeas data», o cuando haya que documentar el tratamiento
  frente a los titulares.
---

# Política y aviso de privacidad

**Antes de empezar.** Correr primero `/datos-personales-co:evaluacion-de-tratamiento`: la
política describe un tratamiento real. Una política redactada sin conocer el tratamiento
es una declaración falsa, y la SIC sanciona la discrepancia entre lo declarado y lo que
efectivamente ocurre.

## Los tres documentos y para qué sirve cada uno

| Documento | Qué es | Dónde vive |
|---|---|---|
| **Política de Tratamiento de la Información** | Documento completo y público con las reglas del responsable | Sitio web, disponible permanentemente |
| **Aviso de privacidad** | Comunicación breve al titular en el momento de la recolección, cuando no se puede poner la política a su disposición | Formulario, correo, punto de venta |
| **Autorización** | La manifestación del titular. **Es la prueba** | Registro con fecha, medio y contenido |

Confundirlos es la falla más común: una casilla que dice «acepto la política» **no es**
la política, y una política publicada **no reemplaza** la autorización.

## Contenido mínimo de la política (Decreto 1074 de 2015, art. 2.2.2.25.3.1) `[verificar]`

1. Nombre o razón social, **domicilio, dirección, correo electrónico y teléfono** del
   responsable.
2. **Tratamiento al cual serán sometidos los datos y su finalidad**, incluyendo cuando
   aplique las finalidades de los tratamientos de los encargados.
3. **Derechos que le asisten al titular.**
4. Persona o área responsable de la atención de peticiones, consultas y reclamos, ante
   la cual el titular puede ejercer sus derechos.
5. **Procedimiento** para que los titulares puedan ejercer sus derechos.
6. **Fecha de entrada en vigencia** de la política y período de vigencia de la base de
   datos.

**Toda modificación sustancial debe comunicarse al titular** antes de implementarla; si
el cambio es de finalidad, se requiere **nueva autorización**.

## Contenido mínimo del aviso de privacidad (art. 2.2.2.25.3.3) `[verificar]`

1. Nombre o razón social y datos de contacto del responsable.
2. **Tratamiento y finalidad.**
3. **Derechos del titular.**
4. **Mecanismo para conocer la política** de tratamiento y los cambios sustanciales.

El aviso es corto por diseño. **Debe poder leerse.** Un aviso de dos páginas en cuerpo 6
al pie de un formulario no cumple el principio de transparencia.

## La autorización — que sirva como prueba

**Requisitos:** previa, expresa e informada. **Y demostrable.**

Formas válidas de obtenerla: por escrito, de forma oral, o mediante conductas
inequívocas del titular que permitan concluir razonablemente que otorgó la autorización.

**No son autorización válida:**
- El silencio.
- La casilla premarcada.
- La continuación de la navegación.
- Un texto en letra menuda que el titular no pudo leer.

**Texto modelo de autorización general:**

```
Autorizo de manera previa, expresa e informada a [RESPONSABLE], NIT [ ], para
recolectar, almacenar, usar, circular, actualizar, suprimir y en general tratar mis
datos personales, con la(s) siguiente(s) finalidad(es): [enumerar de forma concreta,
una por una].

Declaro que conozco que puedo consultar la Política de Tratamiento de la Información en
[URL], que tengo derecho a conocer, actualizar y rectificar mis datos, a solicitar
prueba de esta autorización, a ser informado sobre el uso que se les ha dado, a
presentar quejas ante la Superintendencia de Industria y Comercio, a revocar esta
autorización y a solicitar la supresión de mis datos cuando proceda, y que el suministro
de datos sensibles es facultativo.

[  ] Autorizo          [  ] No autorizo
Nombre: ____  Documento: ____  Fecha: ____  Medio: ____
```

**Autorización para datos sensibles** — cláusula adicional obligatoria:

```
Se me ha informado que los siguientes datos son sensibles: [enumerar — p. ej. datos de
salud, huella dactilar]. Se me ha informado que NO ESTOY OBLIGADO A AUTORIZAR su
tratamiento y que su suministro es facultativo. Conociendo lo anterior:
[  ] Autorizo el tratamiento de mis datos sensibles para [finalidad específica]
[  ] No autorizo
```

**Autorización de menores:** la otorga el representante legal, previo ejercicio del
derecho del menor a ser escuchado. Documentar ambos.

## Finalidades — la sección que decide todo

Escribir finalidades **concretas y verificables**:

| ❌ No sirve | ✅ Sirve |
|---|---|
| «Fines comerciales» | «Enviar información sobre nuevos productos de [categoría] por correo electrónico y mensaje de texto» |
| «Mejorar nuestros servicios» | «Analizar patrones de uso agregados para priorizar el desarrollo de funcionalidades» |
| «Cumplir obligaciones legales» | «Reportar a la DIAN la información exógena exigida por [resolución]» |
| «Compartir con aliados» | «Transmitir a [proveedor de mensajería] los datos de envío para la entrega del pedido» |

**Regla:** si el titular no puede saber, leyendo la finalidad, qué va a pasar
concretamente con su dato, la finalidad no cumple.

## Retención y supresión

La política debe decir **cuánto tiempo se conservan los datos y por qué**. «Mientras sea
necesario» no es un plazo. Estructura útil:

| Categoría | Plazo | Fundamento |
|---|---|---|
| Datos de clientes con contrato | Vigencia + 10 años | Prescripción de la acción ordinaria (CC art. 2536) |
| Datos contables y facturación | 10 años | C.Co. art. 28 y 60 |
| Datos laborales | Vigencia + 3 años | Prescripción laboral (CST art. 488) |
| Datos de aspirantes no seleccionados | [plazo corto] | No hay obligación de conservación |
| Datos de marketing | Hasta la revocatoria | Autorización |

## Salida

```markdown
[ENCABEZADO DE PRODUCTO DE TRABAJO]

## Documentos de privacidad — [organización]

### Verificación de contenido mínimo
| Requisito | Norma | Política | Aviso |
|---|---|---|---|
[cada uno de los 6 y de los 4, con ✅/🔴]

---
[POLÍTICA DE TRATAMIENTO DE LA INFORMACIÓN — texto completo]
---
[AVISO DE PRIVACIDAD — texto completo]
---
[TEXTOS DE AUTORIZACIÓN — general, sensibles, menores]
---

### Cómo se prueba la autorización
| Canal de recolección | Mecanismo | Qué queda registrado | ✅/🔴 |
|---|---|---|---|

### Campos por diligenciar
### Implementación
| Acción | Responsable | Plazo |
|---|---|---|
| Publicar la política en [URL] | | |
| Incorporar el aviso en [canales] | | |
| Ajustar formularios | | |
| Registrar bases en el RNBD (si aplica) | | |

Fuentes: […] | Marcas pendientes: [N] | Revisó: [PENDIENTE DE REVISIÓN PROFESIONAL]
```

## Compuertas

- **No redactar una política que describa un tratamiento que no ocurre.** La discrepancia
  entre lo declarado y lo real es lo que sanciona la SIC.
- **Finalidades genéricas son 🔴.** Se devuelven para concretarlas.
- **Si no hay mecanismo para probar la autorización, es 🔴** aunque la política esté
  perfecta.
- **La política no reemplaza la autorización.** Decirlo siempre.

## Lo que esta skill NO hace

- No publica ni implementa.
- No registra bases ante la SIC.
- No audita si el tratamiento real corresponde a lo declarado: eso lo hace
  `/datos-personales-co:evaluacion-de-tratamiento`.
