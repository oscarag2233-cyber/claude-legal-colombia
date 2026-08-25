# Tablero de práctica — plantilla

Plantilla de tablero que las skills de estado y de seguimiento pueden generar. Se
escribe en el directorio de configuración del usuario, nunca en el repositorio.

```markdown
# Tablero — [Área] — semana del [fecha]

## 🔴 Vence esta semana
| Asunto | Actuación | Vence | Responsable | Norma del término |
|---|---|---|---|---|

## 🟠 Vence en 8 a 30 días
| Asunto | Actuación | Vence | Responsable |
|---|---|---|---|

## 🟡 En curso sin término inminente
| Asunto | Estado | Próximo paso | Responsable |
|---|---|---|---|

## ⚖️ Pendientes de decisión profesional
| Asunto | Decisión que se requiere | Quién decide |
|---|---|---|

## 🔎 Ítems marcados para verificación
| Ítem | Marca | Quién verifica | Fuente a consultar |
|---|---|---|---|

## Novedades normativas y jurisprudenciales de la semana
| Fuente | Novedad | Impacto en nuestros asuntos | Acción |
|---|---|---|---|

---
Generado el [fecha]. Los términos se recalculan contra el calendario judicial
vigente antes de actuar. `[verificar]`
```

## Reglas

1. Nada entra al tablero sin **responsable con nombre**.
2. Todo término lleva la **norma que lo fija**.
3. Los ítems marcados `[verificar]` que lleven más de dos semanas sin resolver suben a
   🔴 automáticamente: una marca que nadie resuelve es una marca que alguien va a
   ignorar.
