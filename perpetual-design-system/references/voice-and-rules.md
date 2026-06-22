# Voz y reglas duras

## Idioma y voz

- **Español latinoamericano**, sin voseo.
- Tono: directo, técnico-comercial, profesional. Sin relleno ni adornos.
- Justificaciones siempre respaldadas por dato, no por opinión.
- En deliverables formales para cliente, registro corporativo. En internos, más conciso.
- Inglés solo cuando el deliverable es para audiencia angloparlante (p. ej. Google-facing); en ese caso, inglés profesional equivalente.

## Reglas duras — NUNCA hagas esto

1. **Nunca** uses em-dash (—) en texto de marca. Usa coma, paréntesis o reescribe.
2. **Nunca** uses emojis en documentos formales.
3. **Nunca** uses otra tipografía que no sea ArminGrotesk (mono JetBrains solo para footer/código/metadatos).
4. **Nunca** recolorees el logo fuera de sus dos variantes oficiales (color / dark). Nada de logo en un solo color plano, gradiente sobre el logo, sombra o contorno.
5. **Nunca** distorsiones la proporción del logo ni lo pongas por debajo del tamaño mínimo (90px de ancho).
6. **Nunca** uses fondo que no sea blanco en deliverables claros; para secciones oscuras usa `--bg-dark` (no negro puro #000).
7. **Nunca** mezcles brand primitives y semantic tokens sin intención (el logo usa brand-blue/orange; la interfaz usa accent/accent2).
8. **Nunca** dejes texto de relleno tipo "lorem ipsum" ni placeholders sin resolver en un entregable final.
9. **Nunca** generes artefactos típicos de IA en la redacción (frases vacías, triplas retóricas forzadas, "en resumen", "es importante notar que"). Escribe como consultor, no como modelo.
10. **Nunca** uses color como único portador de significado: los badges de estado siempre llevan texto + punto, no solo color.

## Sí, siempre

- Fondo blanco en claro, `--bg-dark` en oscuro.
- Logo correcto según contraste del fondo.
- Padding horizontal global de 40px (`--pad-x`) en deliverables.
- Sistema de semáforo de 4 niveles para estados.
- Footer con confidencialidad + crédito Perpetual + año.
- Contraste suficiente para legibilidad (texto sobre fondo, mín. AA).
