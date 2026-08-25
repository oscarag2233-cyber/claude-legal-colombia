# Uso de IA en actuaciones judiciales y administrativas

## Marco

- **Ley 2213 de 2022** — adoptó de forma permanente el uso de las TIC en las
  actuaciones judiciales (origen: Decreto 806 de 2020). Notificaciones y memoriales
  electrónicos, presunción de autenticidad de los mensajes de datos remitidos desde
  las direcciones inscritas.
- **Lineamientos del Consejo Superior de la Judicatura** sobre uso de inteligencia
  artificial en la Rama Judicial. `[verificar acuerdo/circular vigente]`
- **Jurisprudencia de la Corte Constitucional** sobre uso de IA generativa por parte
  de jueces —debido proceso, juez natural, motivación y transparencia—. La Corte se
  ha pronunciado sobre el uso de IA en providencias judiciales; **verificar la
  sentencia y su alcance antes de citarla.** `[conocimiento del modelo — verificar]`
- **CONPES sobre política nacional de inteligencia artificial** `[verificar número y
  fecha]`.
- **Ley 1581 de 2012** y decisiones automatizadas: el titular tiene derecho a conocer
  el uso que se da a sus datos.

## Reglas de conducta profesional

1. **Verificar toda cita antes de radicar.** Presentar autoridad inexistente o
   tergiversada puede constituir falta a la lealtad y a la debida diligencia
   (Ley 1123 de 2007, arts. 33 y 34) y, según el caso, conducta sancionable
   procesalmente (CGP art. 78).
2. **La IA no firma.** El memorial lo suscribe un abogado con tarjeta profesional
   vigente, que asume la responsabilidad.
3. **Transparencia.** Cuando el despacho lo exija o cuando la herramienta haya
   incidido de manera relevante, informarlo. Varios despachos ya lo requieren.
4. **Reserva.** No cargar expedientes con datos personales a servicios sin contrato de
   tratamiento. Ver `tratamiento-de-datos.md`.
5. **No delegar el juicio.** La calificación jurídica, la estrategia y la decisión de
   radicar son del abogado.

## Lo que este repositorio hace para reducir el riesgo

| Riesgo | Control incorporado |
|---|---|
| Citas fabricadas | Etiquetado obligatorio de procedencia + skill `verificar-citas` en cada plugin |
| Norma derogada o inexequible | Disparador de actualidad + tabla de vigencia en cada perfil |
| Término mal contado | Salida obligatoria con norma, tipo de días, día de inicio y advertencia de calendario judicial |
| Fuga de datos del cliente | Anonimización previa y exclusión de `config/` y `asuntos/` del control de versiones |
| Salida presentada como concepto | Encabezado de producto de trabajo en toda pieza + compuerta de revisión profesional |
| Pérdida de trazabilidad | Bitácora de verificación por plugin |
