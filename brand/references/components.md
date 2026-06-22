# Componentes — Specs agnósticas al formato

Cada componente se describe por su **intención y proporciones**, no por su implementación. Cada skill de formato lo traduce a su medio (CSS para HTML, shapes/placeholders para PPTX, estilos para DOCX).

## Header / cabecera

- Fondo blanco (`--bg`), borde inferior 2px `--border`.
- Barra de acento de 3px en el borde inferior con el gradiente de marca.
- Contenido: logo (color, ~36px alto) a la izquierda + badge de sección + H1 + subtítulo. Metadatos (cliente, fecha, contenedor) alineados a la derecha.
- Padding: `20px` vertical, `--pad-x` (40px) horizontal.

## Badge de sección

- Forma pill (`--radius-pill`), padding `4px 12px`, fondo `--info-bg`, texto `--accent`.
- `font-size: 10px`, peso 600, mayúsculas, `letter-spacing: .06em`.
- Punto decorativo 8×8 circular en `--accent` a la izquierda del texto.

## H1

- Peso 900, `letter-spacing: -.02em`. En HTML: `font-size: clamp(20px, 2.5vw, 28px)`.
- La palabra a destacar va en `--accent` (sin cursiva real: `font-style: normal`).

## Stats bar

- Fila horizontal sobre `--surface`, borde inferior 1px `--border`.
- Cada stat: número (peso 800, ~22px, `--text`) + label (11px, `--text-muted`).
- Padding por stat: `14px 28px`.

## Badges de estado (semáforo 4 niveles)

Sistema central de Perpetual. Cuatro niveles: ok / warn / error / info.

- Forma: `--radius-sm`, padding `3px 10px`, `font-size: 10px`, peso 600, `letter-spacing: .04em`.
- Punto circular 7×7 a la izquierda en `currentColor`.
- Cada nivel usa su trío `--{estado}`, `--{estado}-bg`, `--{estado}-border` (texto / fondo / borde 1px).

| Nivel | Significado |
|---|---|
| ok | Correcto, aprobado, saludable |
| warn | Atención, riesgo medio, revisar |
| error | Crítico, bloqueante, fallo |
| info | Neutral, informativo, en proceso |

## Tablas

- `border-collapse`, ancho 100%, borde 1px `--border`, `--radius-lg`, `--shadow-card`.
- `thead th`: fondo `--surface`, 10px, mayúsculas, `letter-spacing: .08em`, color `--text-muted`, padding `10px 14px`.
- `td`: padding `11px 14px`, fondo blanco, borde superior 1px `--border`.
- Hover de fila: fondo `#f0f4ff`.
- Fila de categoría: fondo `--surface2`, 11px, peso 700, mayúsculas, color `--accent`.

## Chips

- Base: `--radius-sm` o 3px, padding `1px 7px`, `font-size: 10px`.
- Variantes por categoría (param azul, utm naranja, id verde, off rojo) usando fondo claro + borde + texto del mismo tono. Ver `perpetual-html-design` para los hex exactos de cada chip.

## Botones e inputs

- Botón filtro: `--radius-md`, borde 1px `--border`, fondo blanco, 12px, padding `6px 14px`. Hover → borde y texto `--accent`. Activo → fondo `--accent`, texto blanco.
- Input búsqueda: `--radius-md`, borde 1px `--border`, 12px, padding `6px 12px`. Focus → borde `--accent` + `--shadow-focus`.

## Footer

- Borde superior 1px `--border`, padding `16px --pad-x`, distribución space-between.
- Tipografía `'JetBrains Mono'`, 11px, color `--text-muted`.
- Contenido: logo (~20-22px) + texto de confidencialidad + `Perpetual Technologies © [año]`.

## Portada de deck (PPTX/HTML dark)

- Fondo `--bg-dark` (`#0b1220`).
- Logo variante **dark** (`perpetual-dark.svg`), ~120px de ancho.
- Título en `--text-on-dark` (peso 900) + subtítulo en `--text-dim-dark`.
- Acento opcional: barra/forma fina con gradiente de marca o en `--brand-orange`.
- Metadatos (cliente, fecha) en `--text-dim-dark`, tipografía mono.

## Slide de contenido (PPTX)

- Fondo blanco. Franja de título superior con H2 (peso 800, `--text`) y, opcional, regla de 3px con gradiente de marca.
- Cuerpo: bullets a 18-20pt cuerpo, números/stats en peso 800.
- Pie de slide: logo color pequeño + numeración en mono `--text-muted`.
