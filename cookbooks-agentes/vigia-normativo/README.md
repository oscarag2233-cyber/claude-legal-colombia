# Vigía normativo — cookbook

Barrido periódico de fuentes oficiales colombianas, filtro de materialidad y preparación
del boletín para revisión profesional.

## Arquitectura

```
vigia-normativo-co                    read, grep, glob
  ├── lector-de-fuentes-co            read, grep, web_fetch (lista blanca oficial)
  ├── filtro-de-materialidad-co       read
  └── redactor-de-digest-co           read, write (solo ./salida/)
```

## Qué concede cada agente

| Agente | read | grep | glob | web_fetch | write | MCP |
|---|---|---|---|---|---|---|
| `vigia-normativo-co` (orquestador) | ✓ | ✓ | ✓ | — | — | — |
| `lector-de-fuentes-co` | ✓ | ✓ | — | ✓ (lista blanca) | — | — |
| `filtro-de-materialidad-co` | ✓ | — | — | — | — | — |
| `redactor-de-digest-co` | ✓ | — | — | — | ✓ | — |

**El orquestador no sale a la red ni escribe.** La única hoja con egreso es el lector, y
está limitada por `allowed_hosts` a dominios oficiales colombianos. La única hoja con
escritura es el redactor, y solo escribe en `./salida/`.

## Lista blanca de dominios

Diario Oficial · SUIN-Juriscol · Corte Constitucional · Corte Suprema · Consejo de Estado ·
Rama Judicial · SIC · Superintendencia de Sociedades · Superintendencia Financiera · DIAN ·
Función Pública · Secretaría del Senado · Colombia Compra Eficiente.

Ampliar solo con fuentes oficiales adicionales. **La lista es la frontera de seguridad**,
no una preferencia.

## Lo que este cookbook NO hace

- No publica el boletín en ningún canal: lo escribe en `./salida/` para revisión.
- No afirma que una norma esté vigente sin verificación en fuente oficial.
- No obedece instrucciones que aparezcan dentro de las publicaciones que lee.
- No interpreta el alcance de una norma: para eso está
  `/regulatorio-co:analisis-de-impacto`.

## Despliegue

1. Ajustar la lista blanca a las fuentes del sector.
2. Configurar la periodicidad y el destino de `./salida/`.
3. Verificar que el modelo indicado esté disponible en la cuenta.
4. Correr `python3 scripts/verificar-alcance.py` antes de desplegar.
