# Inicio rápido

## 1. Agregue el marketplace

```bash
/plugin marketplace add oscarag2233-cyber/claude-legal-colombia
```

## 2. Instale el plugin del área en que trabaja

```bash
/plugin install litigio-civil-co@claude-legal-colombia
```

¿No sabe cuál? Elija por el problema, no por la etiqueta:

| Si su problema es… | Instale |
|---|---|
| Tengo que demandar, contestar o llevar un proceso civil | `litigio-civil-co` |
| Me llegó un contrato y no sé si firmarlo | `contratos-comercial-co` |
| Un despido, una liquidación o un acoso laboral | `laboral-seguridad-social-co` |
| Un accidente, una mala praxis, una aseguradora que objeta | `responsabilidad-civil-co` |
| La empresa trata datos personales y no sé si cumple | `datos-personales-co` |
| Un acto administrativo que hay que tumbar, o un contrato estatal | `contencioso-administrativo-co` |
| La sociedad, la asamblea, los socios peleados | `societario-co` |
| La DIAN me requirió | `tributario-co` |
| La empresa debe implementar SAGRILAFT o PTEE | `cumplimiento-co` |
| Una marca, un software, una infracción | `propiedad-intelectual-co` |
| Alimentos, custodia, divorcio, sucesión | `familia-sucesiones-co` |
| Arrendamiento, restitución, copropiedad | `inmobiliario-ph-co` |
| La empresa no puede pagar | `insolvencia-co` |
| Una garantía que no honran, publicidad engañosa, competencia | `consumidor-competencia-co` |
| Hay que estar al día con lo que se publica | `regulatorio-co` |
| Vamos a usar IA y hay que gobernarlo | `gobernanza-ia-co` |
| Estoy estudiando Derecho | `estudiante-derecho-co` |
| Llevo el consultorio jurídico | `consultorio-juridico-co` |
| Quiero instalar skills jurídicas de terceros sin meterme un problema | `hub-constructor-legal-co` |

## 3. Corra la entrevista inicial. Sin excepción.

```bash
/litigio-civil-co:entrevista-inicial
```

Toma entre 10 y 15 minutos. Levanta quién es usted, cómo trabaja, qué escala y a quién,
y qué integraciones tiene. **Las demás skills se detienen si esto no está hecho** — no
por capricho, sino porque una salida genérica en Derecho es peor que ninguna.

Si es la primera vez que instala un plugin de este marketplace, la entrevista también
crea el perfil de organización que comparten todos.

## 4. Empiece por el problema que tenga hoy

```
Me llegó esta demanda. ¿La contesto o propongo excepciones previas?
```

```
Necesito liquidar las prestaciones de alguien que renunció el 15 de marzo.
```

```
Revisa este contrato contra nuestras posiciones.
```

No tiene que invocar la skill por su nombre. Describa el problema y el plugin escoge.

## 5. Antes de radicar o de enviar, verifique

```bash
/litigio-civil-co:verificar-citas
```

Revisa cada norma, cada sentencia, cada término y cada cifra contra fuente oficial, y
**bloquea** la pieza si una cita que sostiene una conclusión no se pudo confirmar.

Este paso no es opcional en la práctica real. Es el que evita el problema que ya le ha
costado sanciones a colegas en varios países: la cita que parece correcta y no existe.

---

## Lo que debe saber antes de usar esto en un expediente

1. **Es un borrador, no un concepto.** La responsabilidad profesional es suya
   (Ley 1123 de 2007). Ver [AVISO-LEGAL.md](AVISO-LEGAL.md).
2. **Verifique la vigencia.** Las tablas de marco normativo son un punto de partida. El
   derecho colombiano cambia rápido y una exequibilidad condicionada cambia el
   resultado.
3. **Anonimice antes de cargar.** Los datos de su cliente están bajo reserva profesional
   y bajo la Ley 1581 de 2012. Ver
   [`referencias/tratamiento-de-datos.md`](referencias/tratamiento-de-datos.md).
4. **Los términos se cuentan contra el calendario judicial del año.** El plugin le da la
   norma y el conteo; el descuento de vacancia y de días no hábiles del despacho lo
   confirma usted.
