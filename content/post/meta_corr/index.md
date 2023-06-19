---
title: "Meta-análisis de correlaciones y meta-regresión en R: Guía práctica [Guía en PDF]"
date: 2023-04-07T00:00:00
authors: ["juan-david-leongomez"]
summary: Este documento contiene todo el código explicaciones básicas, paso a paso, para hacer un meta-análisis en R. 
tags: ["Estadística", "Software", "Guía", "R", "Meta-análisis", "Correlación", "Tamaño de muestra"]
---

El meta-análisis es un método ampliamente utilizado para sintetizar los datos de diferentes estudios. Sin embargo, a menudo estudiantes, profesionales e investigadores carecemos de conocimientos prácticos para hacer e interpretar un meta-análisis. Esta guía presenta una batería de herramientas para realizar meta-análisis de correlaciones en R, ilustradas a partir de un ejemplo real. Incluye desde análisis simples y su interpretación hasta análisis con moderadores (meta-regresión), usando los paquetes [`metafor`](https://www.metafor-project.org/doku.php) (Viechtbauer, 2010) y [`metaviz`](https://cran.r-project.org/web/packages/metaviz/vignettes/metaviz.html) (Kossmeier et al., 2020). También incluye explicaciones para la transformación de coeficientes *r* de Pearson a *z* de Fisher (y viceversa), creación de gráficos de bosque (*forest plots*) y gráficos de embudo (*funnel plots*), análisis de heterogeneidad y diagnósticos de influencia, así como estrategias para detectar posibles sesgos de publicación utilizando el paquete [`weightr`](https://www.r-pkg.org/pkg/weightr) (Coburn & Vevea, 2019), y para determinar el poder estadístico de un meta-análisis utilizando [`metameta`](https://www.dsquintana.blog/metameta-r-package-meta-analysis/) (Quintana, 2022).

**Cita:**
> Leongómez, J.D. (2023). Meta-análisis de correlaciones y meta-regresión en R: Guía práctica. *MetaArXiv*. https://doi.org/10.31222/osf.io/yaxd4

{{< cta cta_text="Descargar documento PDF" cta_link="https://asesores-psic.netlify.app/post/meta_corr/meta_corr.pdf" cta_new_tab="true" >}}

### Fuentes citadas en el resumen:

> Coburn, K. M., & Vevea, J. L. (2019). *Weightr: Estimating weight-function models for publication bias*. https://CRAN.R-project.org/package=weightr

> Kossmeier, M., Tran, U. S., & Voracek, M. (2020). *metaviz: Forest Plots, Funnel Plots, and Visual Funnel Plot Inference for Meta-Analysis*. https://CRAN.R-project.org/package=metaviz

> Quintana, D. S. (2022). *Metameta: A suite of tools to re-evaluate published meta-analyses*. https://github.com/dsquintana/metameta

> Viechtbauer, W. (2010). Conducting Meta-Analyses in R with the metafor Package. *Journal of Statistical Software, 36* (3). https://doi.org/10.18637/jss.v036.i03
