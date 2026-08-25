---
name: instalar-skill
description: >
  Instala únicamente lo que pasó la revisión de seguridad, deja registro de la instalación
  y explica qué quedó habilitado y con qué límites. Actívela ante «instala esta skill»,
  «agregar un plugin», «ya la revisamos, instálala», «registro de skills instaladas»,
  «cómo desinstalo algo».
---

# Instalar skill

> **Solo se instala lo que pasó `/hub-constructor-legal-co:revisar-seguridad`.** Si no hay
> constancia de revisión, esta skill se detiene y remite a la revisión.

**Antes de empezar.** Leer el perfil: **quién autoriza instalaciones**. Si el usuario no
es el autorizado, se pide la autorización antes de proceder.

## Paso 1 — Verificaciones previas

| # | Verificación | Si falla |
|---|---|---|
| 1 | **Constancia de revisión de seguridad**, con veredicto, nombre y fecha | Se detiene y remite a la revisión |
| 2 | Veredicto: aprobada o aprobada con restricciones | Si fue rechazada, no se instala |
| 3 | **Autorización de quien decide** según el perfil | Se pide |
| 4 | La skill no duplica una funcionalidad propia | Se advierte |
| 5 | Se sabe qué restricciones aplican | Se documentan antes |
| 6 | Se sabe **cómo desinstalarla** | Se documenta antes de instalar |

**El punto 6 se omite siempre y es el que más molesta después.** Antes de instalar hay que
saber cómo revertir.

## Paso 2 — Alcance de la instalación

| Alcance | Cuándo | Efecto |
|---|---|---|
| **De usuario** | La skill se usa en varios proyectos | Disponible en todo el entorno del usuario |
| **De proyecto** | La skill es específica de un asunto o de un cliente | Solo en ese directorio |

**Para skills que tocan información de clientes, el alcance de proyecto es preferible:**
limita la superficie y facilita el aislamiento por asunto.

## Paso 3 — La instalación

Los comandos concretos dependen del origen. Los del marketplace propio:

```bash
/plugin marketplace add oscarag2233-cyber/claude-legal-colombia
```

```bash
/plugin install <nombre-del-plugin>@claude-legal-colombia
```

**Para skills de terceros:** seguir el procedimiento que indique el registro
correspondiente, **con el alcance decidido en el Paso 2** y **sin ejecutar scripts de
instalación que no se hayan leído**.

**Regla dura:** si la instalación exige ejecutar un script, ese script se lee completo
antes. Un script de instalación es código que corre con los permisos del usuario, y la
revisión de seguridad debió cubrirlo; si no lo cubrió, se vuelve a la revisión.

## Paso 4 — La verificación posterior

Después de instalar, y antes de usarla con información real:

| # | Verificación |
|---|---|
| 1 | La skill aparece disponible y con el nombre esperado |
| 2 | **Probarla con información ficticia**, nunca con un expediente real |
| 3 | Revisar sus salidas: ¿marca las citas? ¿tiene compuerta de revisión? |
| 4 | Verificar que no pidió permisos adicionales al ejecutarse |
| 5 | Verificar que no se conectó a destinos no declarados, si hay forma de observarlo |
| 6 | Documentar el resultado de la prueba |

**La prueba con información ficticia es obligatoria.** Es el último control antes de que
la skill vea datos reales.

## Paso 5 — El registro

Cada instalación se registra. Es lo que permite auditar el entorno y saber qué hay que
revisar cuando algo cambie.

```markdown
## Registro de skills instaladas

| Skill | Origen | Versión | Alcance | Instalada el | Instaló | Revisión de seguridad | Veredicto | Restricciones | Última verificación |
|---|---|---|---|---|---|---|---|---|---|
```

**Campos que no se pueden dejar vacíos:** origen, quién instaló, constancia de revisión y
restricciones.

## Paso 6 — Comunicar qué quedó habilitado

A quien la va a usar se le dice, en lenguaje concreto:

```markdown
### Se instaló: [nombre]

**Qué hace:** [una frase]
**Cómo se invoca:** [ ]
**🔴 Restricciones:**
- [p. ej.: no usarla con información de clientes]
- [p. ej.: verificar todas sus citas antes de usar sus salidas]
**Qué NO hace:** [ ]
**A quién preguntar si algo se ve raro:** [ ]
**Cómo desinstalarla:** [ ]
```

## Desinstalación

| Cuándo se desinstala | |
|---|---|
| Ya no se usa | Una skill sin uso es superficie de riesgo sin beneficio |
| Apareció una alternativa propia | |
| El autor la abandonó | Sin actualizaciones tras una reforma de la materia |
| Cambió su comportamiento tras una actualización | |
| Se detectó un problema | Desinstalar **primero**, investigar después |
| Auditoría periódica la marcó | Ver `/hub-constructor-legal-co:control-de-calidad` |

**Al desinstalar:** registrar la fecha y la razón, verificar que no queden archivos de
configuración con datos, y avisar a quienes la usaban.

## Salida

```markdown
[NOTAS DE TRABAJO]

## Instalación — [skill]

### Verificaciones previas
| # | Verificación | Estado |
|---|---|---|

### Decisión de alcance
[usuario / proyecto] — porque [ ]

### Instalación
[comandos ejecutados]

### Verificación posterior
| # | Verificación | Resultado |
|---|---|---|
| Prueba con información ficticia | |

### Registro
[la fila del registro]

### Comunicación a los usuarios
[el bloque de arriba]

### Reversión
[cómo desinstalar, documentado antes de necesitarlo]
```

## Compuertas

- **Sin constancia de revisión de seguridad, no se instala.**
- **Sin autorización de quien decide según el perfil, no se instala.**
- **No se ejecutan scripts de instalación sin leerlos.**
- **La primera prueba es con información ficticia.**
- **Toda instalación queda registrada con sus restricciones.**

## Lo que esta skill NO hace

- No revisa la seguridad — para eso está
  `/hub-constructor-legal-co:revisar-seguridad`.
- No autoriza: ejecuta lo autorizado.
- No garantiza que la skill funcione bien.
