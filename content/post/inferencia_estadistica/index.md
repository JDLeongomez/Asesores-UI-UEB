---
title: "Inferencia Estadística: tres aproximaciones [Presentación]"
date: 2026-04-14T00:00:00
lastmod: 2026-04-14T00:00:00
authors: ["juan-david-leongomez"]
summary: "Presentación introductoria sobre los tres enfoques principales de inferencia estadística (frecuentista, verosimilitud y bayesiano) ilustrados con un ejemplo sencillo en R: lanzar una moneda 20 veces y observar 14 caras."
tags: ["Estadística", "Inferencia", "Frecuentista", "Verosimilitud", "Bayesiana", "R", "Presentación", "Quarto", "Métodos cuantitativos"]
editor_options: 
  markdown: 
    wrap: 80
---

Presentación introductoria sobre los tres enfoques principales de inferencia estadística: **frecuentista**, **verosimilitud** y **bayesiano**, ilustrados con un ejemplo sencillo: lanzar una moneda 20 veces y observar 14 caras. Todo el código R está integrado y es completamente reproducible.

<p style="display: flex; gap: 0.8em; flex-wrap: wrap; margin-bottom: 1.5em;">
  <a href="https://jdleongomez.github.io/Inferencia_estadistica"
     target="_blank"
     style="
       display: inline-block;
       padding: 0.7em 1.4em;
       background-color: #2D2D2C;
       color: #ffffff;
       font-size: 1.05em;
       font-weight: 600;
       border-radius: 8px;
       text-decoration: none;
     ">
    ▶️ Abrir presentación
  </a>
  <a href="https://github.com/JDLeongomez/Inferencia_estadistica"
     target="_blank"
     style="
       display: inline-block;
       padding: 0.7em 1.4em;
       background-color: #24292e;
       color: #ffffff;
       font-size: 1.05em;
       font-weight: 600;
       border-radius: 8px;
       text-decoration: none;
     ">
    📂 Repositorio en GitHub
  </a>
</p>

<iframe
  src="https://jdleongomez.github.io/Inferencia_estadistica"
  width="100%"
  height="540"
  style="border: 1px solid #e0e0e0; border-radius: 8px;"
  allowfullscreen>
</iframe>

## Contenido

- Probabilidad y parámetros: qué es θ y cómo se distribuyen los resultados
- El problema de la inferencia: cómo pasar de los datos al parámetro
- **Frecuentista**: hipótesis nula, valor *p* e intervalos de confianza
- **Verosimilitud**: la función L(θ), el MLE y la razón de verosimilitud
- **Bayesiana**: prior, verosimilitud y posterior — actualización paso a paso
- Comparación de los tres enfoques

## Reproducibilidad

La presentación está escrita en [Quarto](https://quarto.org) con formato RevealJS.
Todo el código R está integrado en `index.qmd` y también disponible como script independiente en `codigo.R`.

**Dependencias en R:**

```r
install.packages(c("tidyverse", "patchwork"))
```

**Para renderizar localmente:**

```bash
quarto render index.qmd
```
