#!/usr/bin/env python3
"""
Genera un reporte-infografia HTML autocontenido con el layout del informe
"BCG AI at Work", reinterpretado con la marca Perpetual Technologies:
paleta de tokens, tipografia Armin Grotesk (embebida en base64) y logo oficial
(SVG inline). Mismo layout y graficas, llevado a Perpetual.

Salida: report/perpetual-ai-at-work.html  (abrir en navegador).
"""
import os, base64

HERE = os.path.dirname(os.path.abspath(__file__))
DS = os.path.join(HERE, "..", "perpetual-design-system", "assets")
OUT = os.path.join(HERE, "perpetual-ai-at-work.html")

# --- fuentes: .b64 (OTF) -> @font-face data URIs ---
FONTS = [("Normal", 300), ("Regular", 400), ("Semi_Bold", 600), ("Black", 800)]
faces = []
for name, weight in FONTS:
    b64 = open(os.path.join(DS, "fonts", f"ArminGrotesk_{name}.b64")).read().strip()
    faces.append(
        "@font-face{font-family:'Armin Grotesk';font-style:normal;font-weight:%d;"
        "font-display:swap;src:url(data:font/otf;base64,%s) format('opentype');}" % (weight, b64)
    )
FONT_FACES = "\n".join(faces)

# --- logos SVG inline (ya con fills inline tras el fix) ---
def svg(path):
    return open(os.path.join(DS, "logo", path)).read().split("?>", 1)[-1].strip()
LOGO_COLOR = svg("perpetual-color.svg")
LOGO_DARK = svg("perpetual-dark.svg")


# ---------------------------------------------------------------------------
# Helpers de graficas (HTML/CSS/SVG, sin librerias)
# ---------------------------------------------------------------------------
def donut(pct, size, stroke, color, track, label_top, label_bot, text_color):
    import math
    r = (size - stroke) / 2
    circ = 2 * math.pi * r
    dash = circ * pct / 100
    return f"""
<div class="donut" style="width:{size}px;height:{size}px">
  <svg width="{size}" height="{size}" viewBox="0 0 {size} {size}">
    <circle cx="{size/2}" cy="{size/2}" r="{r}" fill="none" stroke="{track}" stroke-width="{stroke}"/>
    <circle cx="{size/2}" cy="{size/2}" r="{r}" fill="none" stroke="{color}" stroke-width="{stroke}"
      stroke-dasharray="{dash:.1f} {circ:.1f}" stroke-linecap="round"
      transform="rotate(-90 {size/2} {size/2})"/>
  </svg>
  <div class="donut-c" style="color:{text_color}">
    <div class="donut-n">{label_top}</div><div class="donut-l">{label_bot}</div>
  </div>
</div>"""


def hbars(rows, maxv, color, value_fmt=lambda v: f"{v:,}"):
    """rows: list[(label, value)] -> barras horizontales."""
    out = ['<div class="hbars">']
    for lbl, v in rows:
        w = v / maxv * 100
        out.append(
            f'<div class="hbar"><span class="hbar-l">{lbl}</span>'
            f'<span class="hbar-track"><span class="hbar-fill" style="width:{w:.1f}%;background:{color}"></span></span>'
            f'<span class="hbar-v">{value_fmt(v)}</span></div>')
    out.append("</div>")
    return "".join(out)


def group_hbars(title, sub, rows, delta):
    """Bloque tipo BCG: titulo + barras horizontales 3-series + delta pp."""
    series_colors = ["var(--accent)", "var(--accent-2b)", "var(--muted)"]
    bars = []
    for lbl, vals in rows:
        segs = "".join(
            f'<div class="gb"><span class="gb-fill" style="width:{val}%;background:{series_colors[i]}"></span>'
            f'<span class="gb-v">{val}%</span></div>'
            for i, val in enumerate(vals))
        bars.append(f'<div class="gbrow"><span class="gb-l">{lbl}</span><div class="gb-set">{segs}</div></div>')
    return f"""
<div class="mini">
  <div class="mini-h">{title}</div>
  <div class="mini-s">{sub}</div>
  {''.join(bars)}
  <div class="delta">{delta}</div>
</div>"""


def vstack(title, segs):
    """Barra vertical apilada (edad, ingresos)."""
    parts = "".join(
        f'<div class="vseg" style="height:{p}%;background:{c}"><span>{p}%</span></div>'
        for p, c in segs)
    return f'<div class="vstack-w"><div class="vstack">{parts}</div><div class="vstack-t">{title}</div></div>'


def legend(items):
    return '<div class="legend">' + "".join(
        f'<div class="lg"><span class="dot" style="background:{c}"></span>{t}</div>' for t, c in items) + '</div>'


# ---------------------------------------------------------------------------
# Datos (placeholder realista Perpetual, es-LatAm)
# ---------------------------------------------------------------------------
BLUE_SHADES = ["#0b2a8f", "#1a56db", "#4f86f7", "#9dbcfb"]  # graduado para imperativos

mercados = [("Peru", 1031), ("Mexico", 1015), ("Colombia", 1013), ("Brasil", 1012),
            ("Chile", 1010), ("Argentina", 1009), ("Espana", 1002), ("Otros", 543)]

industria = [("Tecnologia", 23), ("Servicios financieros", 18), ("Retail", 14),
             ("Salud", 12), ("Manufactura", 10), ("Energia", 8), ("Sector publico", 8), ("Otros", 7)]

ingresos = [("<5M", 23, BLUE_SHADES[2]), ("5-18M", 30, BLUE_SHADES[1]),
            ("18-50M", 27, BLUE_SHADES[0]), (">50M", 20, "var(--muted)")]

edad = [("18-24", 12, BLUE_SHADES[3]), ("25-34", 27, BLUE_SHADES[2]),
        ("35-44", 24, BLUE_SHADES[1]), ("45-54", 20, BLUE_SHADES[0]), ("55+", 17, "var(--muted)")]

confianza = [
    ("Optimismo", [52, 41, 35]),
    ("Curiosidad", [54, 61, 60]),
    ("Confianza", [39, 26, 17]),
    ("Preocupacion", [28, 36, 40]),
    ("Ansiedad", [11, 12, 18]),
]

imperativos = [
    ("Mide el valor", "No subestimes la capacitacion. Asigna inversion, tiempo y respaldo de liderazgo."),
    ("Rastrea el impacto", "Cuantifica las mejoras de la IA en productividad, calidad y satisfaccion del equipo."),
    ("Invierte en tu gente", "Rediseña flujos y desarrolla capacidades de upskilling para soportar el despliegue."),
    ("Experimenta con rigor", "Acelera la curva de experiencia. Mide impacto y riesgos con pruebas A/B."),
]

# bloques de entrenamiento (mini charts)
mini1 = group_hbars("Al menos cinco horas", "% de usuarios segun volumen de capacitacion",
                    [("Sin capacitacion", [18]), ("1-5 horas", [32]), ("5+ horas", [39])], "+13pp")
mini2 = group_hbars("Presencial", "% de usuarios segun formacion presencial",
                    [("Sin presencial", [22]), ("Presencial", [67])], "+12pp")
mini3 = group_hbars("Coaching", "% de usuarios con acceso a coach",
                    [("Sin coach", [29]), ("Con coach", [70])], "+14pp")

# confianza: horizontal multi-serie
conf_rows = []
sc = ["var(--accent)", "var(--accent-2b)", "var(--muted)"]
for lbl, vals in confianza:
    segs = "".join(
        f'<div class="cb"><span class="cb-fill" style="width:{v*1.4}%;background:{sc[i]}"></span><span class="cb-v">{v}%</span></div>'
        for i, v in enumerate(vals))
    conf_rows.append(f'<div class="cbrow"><span class="cb-l">{lbl}</span><div class="cb-set">{segs}</div></div>')
CONF = "".join(conf_rows)

# tono claro (#9dbcfb) requiere texto oscuro para contraste AA
IMP_TEXT = ["#fff", "#fff", "#fff", "#0b2a8f"]
IMP = "".join(
    f'<div class="imp" style="background:{BLUE_SHADES[i]};color:{IMP_TEXT[i]}"><div class="imp-n">{i+1}</div>'
    f'<div class="imp-t">{t}</div><div class="imp-d">{d}</div></div>'
    for i, (t, d) in enumerate(imperativos))

DONUT_ROLE = donut(34, 120, 22, "var(--accent)", "var(--surface-2)", "34%", "", "var(--text)")
DONUT_36 = donut(36, 190, 26, "#ffffff", "rgba(255,255,255,.25)", "36%", "", "#fff")

MERCADOS = hbars(mercados, 1031, "var(--accent)")
INDUSTRIA = "".join(
    f'<div class="ind"><span>{t}</span><b>{v}%</b></div>' for t, v in industria)
EDAD = vstack("Edad", [(p, c) for _, p, c in edad])
INGRESOS = vstack("Ingresos", [(p, c) for _, p, c in ingresos])

# ---------------------------------------------------------------------------
# HTML
# ---------------------------------------------------------------------------
HTML = f"""<!doctype html>
<html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Perpetual · IA en el trabajo</title>
<style>
{FONT_FACES}
:root{{
  --bg:#fff; --surface:#f8f9fc; --surface-2:#eef1f8; --border:#dde1ef;
  --accent:#1a56db; --accent-2b:#4f86f7; --accent2:#f97316;
  --text:#111827; --dim:#374151; --muted:#6b7280;
  --bg-dark:#0b1220; --on-dark:#fff; --dim-dark:#9aa6bd;
  --yellow:#fbb900;
}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{font-family:'Armin Grotesk',system-ui,sans-serif;color:var(--text);background:#c9ccd6;
  -webkit-font-smoothing:antialiased;padding:28px 0}}
.page{{width:940px;margin:0 auto;background:var(--bg);box-shadow:0 8px 40px rgba(0,0,0,.18)}}
h1,h2,h3{{font-weight:800;letter-spacing:-.02em;line-height:1.05}}
.label{{font-weight:600;text-transform:uppercase;letter-spacing:.12em;font-size:11px;color:var(--accent)}}
section{{padding:30px 40px}}

/* header */
.top{{display:flex;align-items:center;justify-content:space-between;padding:26px 40px 20px}}
.top .logo{{height:42px}} .top .logo svg{{height:42px;width:auto}}
.top .tag{{font-weight:600;font-size:13px;color:var(--muted);border:1px solid var(--border);
  border-radius:20px;padding:7px 16px}}

/* hero */
.hero{{background:var(--bg-dark);color:var(--on-dark);display:grid;grid-template-columns:1.1fr .9fr;
  min-height:340px;position:relative;overflow:hidden}}
.hero-l{{padding:42px 40px;display:flex;flex-direction:column;justify-content:center}}
.hero .chip{{display:inline-flex;gap:8px;align-items:center;font-weight:800;font-size:15px;margin-bottom:26px}}
.hero .chip b{{background:#fff;color:var(--bg-dark);padding:3px 9px;border-radius:4px}}
.hero .chip span{{opacity:.6}}
.hero h1{{font-size:40px;margin:6px 0 0}}
.hero .ed{{margin-top:30px;font-weight:600;font-size:12px;letter-spacing:.14em;color:var(--dim-dark);text-transform:uppercase}}
.hero-r{{position:relative}}
.orb{{position:absolute;right:-60px;top:50%;transform:translateY(-50%);width:430px;height:430px;border-radius:50%;
  background:radial-gradient(circle at 38% 38%, #cde0ff 0%, var(--accent-2b) 16%, var(--accent) 40%, #0a2c8c 70%, #06155a 100%);
  box-shadow:0 0 120px 20px rgba(26,86,219,.55);}}
.orb::after{{content:"";position:absolute;inset:0;border-radius:50%;
  background:radial-gradient(rgba(255,255,255,.85) .6px,transparent .7px);background-size:9px 9px;
  mix-blend-mode:overlay;opacity:.5;-webkit-mask:radial-gradient(circle at 38% 38%,#000 55%,transparent 78%);
          mask:radial-gradient(circle at 38% 38%,#000 55%,transparent 78%)}}

/* survey band */
.survey{{display:grid;grid-template-columns:auto auto 1fr auto;gap:26px;background:var(--surface);align-items:start}}
.big-num{{font-size:46px;font-weight:800;color:var(--accent);line-height:1}}
.big-sub{{font-size:12px;color:var(--muted);margin-top:4px;max-width:120px}}
.block-h{{font-size:12px;font-weight:600;text-transform:uppercase;letter-spacing:.06em;color:var(--dim);margin-bottom:10px}}
.cols{{display:flex;gap:22px}}
.donut{{position:relative;display:grid;place-items:center}}
.donut svg{{position:absolute;inset:0}}
.donut-c{{text-align:center}} .donut-n{{font-size:22px;font-weight:800}} .donut-l{{font-size:10px}}
.legend{{margin-top:8px}} .lg{{display:flex;align-items:center;gap:6px;font-size:11px;color:var(--dim);margin:3px 0}}
.dot{{width:9px;height:9px;border-radius:50%;display:inline-block}}
.vstack-w{{text-align:center}} .vstack{{width:44px;height:150px;display:flex;flex-direction:column-reverse;
  border-radius:5px;overflow:hidden;margin:0 auto}}
.vseg{{display:flex;align-items:center;justify-content:center}} .vseg span{{font-size:9px;color:#fff;font-weight:600}}
.vstack-t{{font-size:11px;color:var(--muted);margin-top:6px}}
.ind{{display:flex;justify-content:space-between;font-size:11.5px;color:var(--dim);padding:3px 0;border-bottom:1px solid var(--border)}}
.ind b{{color:var(--text)}}
.hbars{{min-width:230px}} .hbar{{display:flex;align-items:center;gap:8px;margin:4px 0;font-size:11px}}
.hbar-l{{width:74px;color:var(--dim)}} .hbar-track{{flex:1;background:var(--surface-2);border-radius:3px;height:13px}}
.hbar-fill{{display:block;height:100%;border-radius:3px}} .hbar-v{{width:42px;text-align:right;font-weight:600}}

/* accent panel */
.accent{{background:var(--accent);color:#fff;display:grid;grid-template-columns:1fr auto;gap:30px;align-items:center}}
.accent h2{{font-size:26px;max-width:340px}}
.accent .sub{{margin-top:10px;font-size:12px;opacity:.85;max-width:330px}}

/* training */
.train-h{{font-size:18px;font-weight:800;margin-bottom:4px}}
.train-s{{font-size:12px;color:var(--muted);margin-bottom:18px;max-width:560px}}
.minis{{display:grid;grid-template-columns:repeat(3,1fr);gap:22px}}
.mini-h{{font-weight:600;font-size:13px;margin-bottom:2px}} .mini-s{{font-size:10px;color:var(--muted);margin-bottom:12px;min-height:26px}}
.gbrow{{margin:7px 0}} .gb-l{{font-size:10px;color:var(--dim);display:block;margin-bottom:3px}}
.gb{{position:relative;background:var(--surface-2);border-radius:3px;height:15px;margin:2px 0}}
.gb-fill{{display:block;height:100%;border-radius:3px}}
.gb-v{{position:absolute;right:6px;top:0;line-height:15px;font-size:9px;font-weight:600;color:var(--text)}}
.delta{{margin-top:10px;display:inline-block;background:var(--surface-2);color:var(--accent);font-weight:800;
  font-size:12px;padding:4px 10px;border-radius:20px}}

/* dark confidence */
.conf{{background:var(--bg-dark);color:#fff;display:grid;grid-template-columns:.8fr 1.2fr;gap:30px}}
.conf h2{{font-size:24px;max-width:240px}}
.cbrow{{margin:10px 0}} .cb-l{{font-size:12px;font-weight:600;display:block;margin-bottom:5px}}
.cb{{position:relative;height:14px;margin:3px 0;background:rgba(255,255,255,.08);border-radius:3px}}
.cb-fill{{display:block;height:100%;border-radius:3px}} .cb-v{{position:absolute;right:6px;top:-1px;font-size:9px;font-weight:600;line-height:16px}}
.conf .leg{{display:flex;gap:16px;margin-top:14px;font-size:11px;color:var(--dim-dark)}}
.conf .leg .dot{{margin-right:5px}}

/* imperativos */
.imps{{display:grid;grid-template-columns:repeat(4,1fr);gap:0}}
.imp{{color:#fff;padding:24px 18px;min-height:200px}}
.imp-n{{font-size:34px;font-weight:800;line-height:1;margin-bottom:14px}}
.imp-t{{font-weight:600;font-size:14px;margin-bottom:10px}} .imp-d{{font-size:11.5px;line-height:1.45;opacity:.92}}
.imps-h{{font-size:18px;font-weight:800;padding:0 40px 14px}}

/* footer */
.foot{{display:flex;justify-content:space-between;align-items:center;padding:16px 40px 22px;
  font-size:10px;color:var(--muted);font-family:ui-monospace,monospace}}
.foot .logo svg{{height:18px}}
</style></head>
<body>
<div class="page">

  <div class="top">
    <span class="logo">{LOGO_COLOR}</span>
    <span class="tag">Reporte · perpetual.pe</span>
  </div>

  <div class="hero">
    <div class="hero-l">
      <div class="chip"><b>Perpetual X</b><span>|</span><b style="background:transparent;color:#fff;padding-left:0">Perpetual</b></div>
      <div class="label" style="color:var(--accent-2b)">Perpetual · IA en el trabajo</div>
      <h1>El impulso crece,<br>pero quedan brechas.</h1>
      <div class="ed">Tercera edicion · Junio 2026</div>
    </div>
    <div class="hero-r"><div class="orb"></div></div>
  </div>

  <section class="survey">
    <div>
      <div class="big-num">10,635</div>
      <div class="big-sub">encuestados a nivel regional</div>
    </div>
    <div>
      <div class="block-h">Rol</div>
      {DONUT_ROLE}
      {legend([("Primera linea", "var(--accent)"), ("Gerentes", "var(--accent-2b)"), ("Lideres", "var(--surface-2)")])}
    </div>
    <div>
      <div class="block-h">Mercados clave</div>
      {MERCADOS}
    </div>
    <div>
      <div class="cols">
        <div><div class="block-h">Edad</div>{EDAD}</div>
        <div><div class="block-h">Ingresos</div>{INGRESOS}</div>
        <div style="min-width:170px"><div class="block-h">Industria</div>{INDUSTRIA}</div>
      </div>
    </div>
  </section>

  <section class="accent">
    <div>
      <h2>Solo 36% de los empleados se siente bien capacitado</h2>
      <div class="sub">Porcentaje que afirma: "Si, mi capacitacion fue suficiente." El resto pide mas horas y mejor calidad de formacion en IA.</div>
    </div>
    {DONUT_36}
  </section>

  <section>
    <div class="train-h">Cinco horas de instruccion, sesiones presenciales y coaching son claves</div>
    <div class="train-s">Tres componentes que elevan de forma significativa la confianza de los empleados en la IA y mejoran la calidad de los entregables asistidos por IA.</div>
    <div class="minis">{mini1}{mini2}{mini3}</div>
  </section>

  <section class="conf">
    <div>
      <h2>A medida que la IA se vuelve mainstream, la confianza sube y las preocupaciones bajan.</h2>
      <div class="leg"><span><span class="dot" style="background:var(--accent)"></span>2026</span>
        <span><span class="dot" style="background:var(--accent-2b)"></span>2024</span>
        <span><span class="dot" style="background:var(--muted)"></span>2019</span></div>
    </div>
    <div>{CONF}</div>
  </section>

  <div class="imps-h">Imperativos estrategicos para lideres</div>
  <div class="imps">{IMP}</div>

  <div class="foot">
    <span class="logo">{LOGO_COLOR}</span>
    <span>Fuente: encuesta Perpetual 2026 (n=10,635). Confidencial · Perpetual Technologies © 2026</span>
  </div>

</div>
</body></html>"""

with open(OUT, "w", encoding="utf-8") as f:
    f.write(HTML)
print("OK:", OUT, "|", round(len(HTML) / 1024), "KB")
