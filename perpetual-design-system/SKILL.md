---
name: perpetual-design-system
description: >
  Fuente de verdad del sistema de diseño de Perpetual Technologies: tokens de
  color, tipografía ArminGrotesk, logos (color y fondo oscuro), espaciado,
  componentes y reglas de marca. Aplicar SIEMPRE que cualquier miembro de
  Perpetual genere un deliverable de marca en CUALQUIER formato: HTML, PPTX,
  DOCX, PDF, dashboards, reportes, auditorías, propuestas, plantillas o assets
  visuales. Se activa con "genera", "crea", "reporte", "dashboard", "propuesta",
  "presentación", "deck", "documento", "plantilla", "logo", "marca", "branding",
  "on-brand", "colores Perpetual", "design system". Esta skill define los tokens;
  las skills de formato (perpetual-html-design, perpetual-pptx-design) los
  consumen. No esperar confirmación: aplicar la marca por defecto.
---

# Perpetual Technologies — Design System (Fuente de Verdad)

Esta skill es la **única fuente de verdad** de la marca Perpetual. Define tokens, assets y reglas de forma **agnóstica al formato**. Las skills de salida (HTML, PPTX, DOCX) traducen estos tokens a su medio. Cuando un valor de marca cambie, se edita **aquí** y se propaga a todos los formatos.

Si trabajas un formato específico, lee primero esta skill y luego la skill de ese formato:
- HTML → `perpetual-html-design`
- PPTX → `perpetual-pptx-design`
- Otros formatos → aplica estos tokens directamente.

---

## 1. Color

Hay dos capas de color. **No las mezcles sin intención.**

### 1a. Brand primitives (colores reales del logo)

Estos son los colores oficiales de la marca. Se usan en el **logo** y en contextos puramente de marca (portadas, sellos, branding). No se alteran nunca.

| Token | Hex | Uso |
|---|---|---|
| `brand-blue` | `#0032cb` | Azul principal del logotipo |
| `brand-blue-deep` | `#002ed6` | Azul del segundo ícono |
| `brand-orange` | `#f33d1f` | Acento naranja del ícono |
| `brand-yellow` | `#fbb900` | Acento amarillo del ícono |

### 1b. UI / semantic tokens (interfaz)

Estos son los tokens que se usan dentro de reportes, dashboards y deliverables. Son **estables** y dan continuidad a todo lo ya producido. El azul de interfaz (`accent`) es ligeramente distinto al `brand-blue` a propósito: rinde mejor en pantalla y texto. Ver nota de decisión al final de esta sección.

```
--bg:        #ffffff   /* fondo: siempre blanco en deliverables claros */
--surface:   #f8f9fc
--surface2:  #eef1f8
--border:    #dde1ef
--accent:    #1a56db   /* azul de interfaz */
--accent2:   #f97316   /* naranja de interfaz */
--text:      #111827
--text-dim:  #374151
--text-muted:#6b7280
```

Estado (semáforo de 4 niveles):

```
--ok:    #059669   --ok-bg:    #ecfdf5   --ok-border:    #a7f3d0
--warn:  #d97706   --warn-bg:  #fffbeb   --warn-border:  #fcd34d
--error: #dc2626   --error-bg: #fef2f2   --error-border: #fca5a5
--info:  #1a56db   --info-bg:  #eff6ff   --info-border:  #93c5fd
```

Gradiente decorativo de marca (header / barras de acento):
`linear-gradient(90deg, #1a56db 0%, #3b82f6 50%, #f97316 100%)`

> **Nota de decisión (confirmar con el equipo):** hoy `accent` (#1a56db) y `accent2` (#f97316) NO son idénticos a `brand-blue` (#0032cb) y `brand-orange` (#f33d1f). Se mantienen separados para no romper los deliverables existentes. Si Perpetual quiere alinear interfaz y marca al 100%, cambiar `accent → #0032cb` y `accent2 → #f33d1f` **solo aquí** y se propaga. Hasta entonces, brand primitives = logo; semantic tokens = interfaz.

### Modo oscuro

Para fondos oscuros (portadas de deck, secciones dark):

```
--bg-dark:      #0b1220
--surface-dark: #131c2e
--border-dark:  #243047
--text-on-dark: #ffffff
--text-dim-dark:#9aa6bd
```

En modo oscuro los acentos `brand-orange` y `brand-yellow` se mantienen (alto contraste); el azul de texto pasa a blanco. El logo usa su variante dark (ver sección 3).

---

## 2. Tipografía — ArminGrotesk

**ArminGrotesk** es la única tipografía de marca. Está embebida en base64 en `assets/fonts/`. Para formatos web (HTML), leer los `.b64` e inyectarlos en `@font-face`. Para PPTX/DOCX, instalar/incrustar el OTF o usar la fuente del sistema equivalente declarada por la skill de formato.

| Archivo | font-weight | Uso |
|---|---|---|
| `assets/fonts/ArminGrotesk_Normal.b64`     | `300` | Texto ligero, subtítulos |
| `assets/fonts/ArminGrotesk_Regular.b64`    | `400` | Cuerpo de texto, celdas |
| `assets/fonts/ArminGrotesk_Semi_Bold.b64`  | `600` | Labels, chips, badges |
| `assets/fonts/ArminGrotesk_Black.b64`      | `800` | Números grandes (stats), énfasis |
| `assets/fonts/ArminGrotesk_Ultra_Bold.b64` | `900` | Títulos H1, headers principales |

Fuente monoespaciada secundaria (solo footer, código, metadatos): `'JetBrains Mono', monospace`.

Escala tipográfica de referencia (deliverables):
- H1 / título principal: peso 900, `letter-spacing: -.02em`
- H2 / sección: peso 800
- Label / badge / chip: peso 600, `text-transform: uppercase`, `letter-spacing: .06em`
- Cuerpo: peso 400, line-height 1.5
- Número destacado (stat): peso 800

---

## 3. Logo

Hay **dos variantes oficiales**. Elegir según el fondo. Nunca recolorear fuera de estas dos definiciones, nunca distorsionar la proporción, nunca poner sombra o contorno.

| Variante | Archivo | Cuándo usar |
|---|---|---|
| Color | `assets/logo/perpetual-color.svg` | Fondos claros (blanco, `--surface`). Azul de marca + ícono naranja/amarillo. |
| Dark | `assets/logo/perpetual-dark.svg` | Fondos oscuros (`--bg-dark`, portadas dark, fotos). Todo blanco **excepto** el ícono naranja y amarillo, que se mantienen. |

Reglas de uso:
- **Web (HTML):** copiar el SVG **inline** (no `<img src>`). Dimensionar por CSS: header `height: 36px`, footer `height: 22px`.
- **PPTX/DOCX:** insertar el SVG/PNG como imagen; mantener proporción (viewBox `0 0 1140.5 136.32`, ratio ~8.36:1).
- **Espacio de protección:** margen libre mínimo alrededor del logo = altura de la letra "p" del logotipo.
- **Tamaño mínimo legible:** 90px de ancho en pantalla.
- Elegir variante por **contraste real del fondo**, no por preferencia. Fondo claro → color. Fondo oscuro o con imagen → dark.

---

## 4. Espaciado, radios y sombras

```
/* Espaciado base (múltiplos de 4) */
--space-1: 4px;  --space-2: 8px;  --space-3: 12px; --space-4: 16px;
--space-5: 20px; --space-6: 24px; --space-8: 32px; --space-10: 40px;

/* Padding horizontal global de deliverables */
--pad-x: 40px;

/* Radios */
--radius-sm: 4px;   /* badges, chips */
--radius-md: 6px;   /* botones, inputs */
--radius-lg: 8px;   /* tablas, cards */
--radius-pill: 20px;/* badges de sección */

/* Sombras */
--shadow-card: 0 1px 4px rgba(0,0,0,.05);
--shadow-focus: 0 0 0 3px rgba(26,86,219,.1);
```

---

## 5. Componentes y reglas

Las especificaciones detalladas de componentes (header, stats bar, badges de semáforo, tablas, chips, footer, portadas de deck) están en los archivos de referencia. **Léelos según el formato que estés produciendo:**

- `references/tokens.md` — Tabla completa de tokens lista para copiar (CSS vars + tabla PPTX/DOCX).
- `references/components.md` — Anatomía y specs de cada componente, agnóstico al formato.
- `references/voice-and-rules.md` — Voz, idioma y la lista de **reglas duras** ("nunca hagas esto").

Estructura típica de un deliverable de marca:
```
header   → logo + badge de sección + H1 + metadatos (cliente, fecha)
stats    → métricas numéricas clave
legend   → badges de estado (semáforo)
body     → tablas / contenido / slides
footer   → logo + confidencialidad + Perpetual Technologies © [año]
```

---

## 6. Anatomía de esta skill

```
perpetual-design-system/
├── SKILL.md                      (este archivo: tokens + índice)
├── assets/
│   ├── logo/
│   │   ├── perpetual-color.svg   (fondos claros)
│   │   └── perpetual-dark.svg    (fondos oscuros: blanco + naranja/amarillo)
│   └── fonts/                    (ArminGrotesk, 5 pesos en base64)
└── references/
    ├── tokens.md
    ├── components.md
    └── voice-and-rules.md
```

Esta skill no genera archivos por sí sola: provee el lenguaje de marca. Para producir un deliverable, combínala con la skill de formato correspondiente.
