# Tratamiento de datos personales al usar estos plugins

Todo expediente contiene datos personales, y buena parte contiene datos sensibles
(salud, orientación sexual, datos de menores, datos biométricos, origen étnico). El
régimen aplicable es la **Ley 1581 de 2012** (estatutaria), el **Decreto 1074 de
2015** (que compiló el Decreto 1377 de 2013) y, para datos financieros y crediticios,
la **Ley 1266 de 2008** (modificada por la **Ley 2157 de 2021**). `[verificar]`

## Reglas operativas antes de procesar cualquier documento

1. **Anonimizar primero.** Si el documento identifica personas, reemplazar nombres,
   cédulas, direcciones, teléfonos y correos por seudónimos estables antes de
   analizarlo. Si hay un conector de anonimización disponible, usarlo — no pedirle al
   usuario que pegue el texto identificado en el chat.
2. **Datos sensibles** (art. 5 Ley 1581): salud, vida sexual, datos biométricos,
   origen racial o étnico, orientación política, convicciones religiosas, pertenencia
   a sindicatos. Su tratamiento está prohibido salvo las excepciones del art. 6.
   **Los datos de menores** solo pueden tratarse cuando responda al interés superior
   del niño y respete sus derechos fundamentales (art. 7).
3. **Finalidad.** El dato solo se usa para lo que se recogió. Analizar un expediente
   para el caso es legítimo; reutilizarlo para entrenar, para marketing o para otro
   cliente no lo es.
4. **Reserva profesional.** El secreto profesional (Const. art. 74; Ley 1123 de 2007,
   art. 34 lit. f) es más exigente que la ley de datos: rige aunque el titular
   consienta la divulgación, porque protege también la confianza en la profesión.
5. **Nunca subir un expediente a un repositorio público.**

## Cadena de responsabilidad

| Rol | Quién suele serlo | Deber principal |
|---|---|---|
| **Responsable** | La firma o la empresa que decide el tratamiento | Autorización, aviso de privacidad, política de tratamiento, registro en el RNBD, atención de consultas y reclamos |
| **Encargado** | El proveedor tecnológico que trata por cuenta del responsable | Tratar solo bajo instrucciones, seguridad, no usar para fines propios |

Si usa un servicio de IA para procesar datos de clientes, **usted es responsable y el
proveedor es encargado**: necesita contrato de transmisión de datos con las cláusulas
del art. 25 del Decreto 1074 de 2015, y si hay transferencia internacional, verificar
si el país está declarado con nivel adecuado por la SIC o si aplica una de las
excepciones del art. 26 de la Ley 1581. `[verificar circular y listado vigentes]`

## Registro Nacional de Bases de Datos (RNBD)

Obligación de registro para responsables con las características que define el
decreto y las circulares de la SIC (sociedades y entidades sin ánimo de lucro con
activos superiores a determinado número de UVT). `[verificar umbral vigente]`

## Incidentes de seguridad

La Ley 1581 (art. 17 lit. n) obliga a informar a la SIC las violaciones a los códigos
de seguridad y los riesgos en la administración de la información. La SIC ha fijado
el canal y el plazo por circular. `[verificar plazo vigente — se ha manejado como 15
días hábiles]`

## Qué hace este repositorio al respecto

- Ninguna skill escribe expedientes al repositorio; la configuración y los asuntos
  viven en `~/.claude/plugins/config/claude-legal-colombia/`, fuera del control de
  versiones.
- Los `.gitignore` excluyen `config/`, `asuntos/` y `expedientes/`.
- El plugin `datos-personales-co` tiene las skills de cumplimiento del régimen.
