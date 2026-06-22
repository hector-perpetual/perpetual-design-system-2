# Tokens — Tabla completa (lista para copiar)

Fuente de verdad de todos los valores. Si un valor cambia, se edita aquí y en `SKILL.md`.

## Bloque CSS (HTML / web)

```css
:root {
  /* Brand primitives (logo) */
  --brand-blue: #0032cb;
  --brand-blue-deep: #002ed6;
  --brand-orange: #f33d1f;
  --brand-yellow: #fbb900;

  /* Superficies (claro) */
  --bg: #ffffff;
  --surface: #f8f9fc;
  --surface2: #eef1f8;
  --border: #dde1ef;

  /* Acentos de interfaz */
  --accent: #1a56db;
  --accent2: #f97316;

  /* Texto */
  --text: #111827;
  --text-dim: #374151;
  --text-muted: #6b7280;

  /* Estado — semáforo 4 niveles */
  --ok: #059669;    --ok-bg: #ecfdf5;    --ok-border: #a7f3d0;
  --warn: #d97706;  --warn-bg: #fffbeb;  --warn-border: #fcd34d;
  --error: #dc2626; --error-bg: #fef2f2; --error-border: #fca5a5;
  --info: #1a56db;  --info-bg: #eff6ff;  --info-border: #93c5fd;

  /* Modo oscuro */
  --bg-dark: #0b1220;
  --surface-dark: #131c2e;
  --border-dark: #243047;
  --text-on-dark: #ffffff;
  --text-dim-dark: #9aa6bd;

  /* Espaciado */
  --space-1: 4px; --space-2: 8px; --space-3: 12px; --space-4: 16px;
  --space-5: 20px; --space-6: 24px; --space-8: 32px; --space-10: 40px;
  --pad-x: 40px;

  /* Radios */
  --radius-sm: 4px; --radius-md: 6px; --radius-lg: 8px; --radius-pill: 20px;

  /* Sombras */
  --shadow-card: 0 1px 4px rgba(0,0,0,.05);
  --shadow-focus: 0 0 0 3px rgba(26,86,219,.1);
}
* { margin: 0; padding: 0; box-sizing: border-box; }
body { background: var(--bg); color: var(--text); }
```

Gradiente de marca: `linear-gradient(90deg, #1a56db 0%, #3b82f6 50%, #f97316 100%)`

## Tabla RGB (para PPTX / DOCX / python-pptx / OOXML)

Los formatos de Office no usan CSS vars. Usar estos valores directos.

| Token | Hex | RGB | PowerPoint usa |
|---|---|---|---|
| brand-blue | 0032CB | 0,50,203 | Acento de marca, títulos de portada |
| brand-orange | F33D1F | 243,61,31 | Acento, highlights |
| brand-yellow | FBB900 | 251,185,0 | Acento secundario |
| accent (UI) | 1A56DB | 26,86,219 | Azul principal de slides |
| accent2 (UI) | F97316 | 249,115,22 | Naranja de datos/charts |
| text | 111827 | 17,24,39 | Texto principal |
| text-muted | 6B7280 | 107,114,128 | Texto secundario, notas |
| surface | F8F9FC | 248,249,252 | Fondo de tablas/cards |
| border | DDE1EF | 221,225,239 | Líneas, divisores |
| ok | 059669 | 5,150,105 | Estado positivo |
| warn | D97706 | 217,119,6 | Estado advertencia |
| error | DC2626 | 220,38,38 | Estado crítico |
| info | 1A56DB | 26,86,219 | Estado informativo |
| bg-dark | 0B1220 | 11,18,32 | Fondo oscuro de portada |
| text-on-dark | FFFFFF | 255,255,255 | Texto sobre oscuro |

## Paleta de datos para charts (orden recomendado)

Para series en gráficos, usar en este orden para máxima distinción:
1. `#1a56db` (accent)
2. `#f97316` (accent2)
3. `#059669` (ok)
4. `#fbb900` (brand-yellow)
5. `#7e22ce` (violeta de apoyo)
6. `#6b7280` (muted, para "otros")
