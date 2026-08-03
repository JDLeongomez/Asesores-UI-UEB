---
title: "Intercepto, pendiente y residuos [App]"
subtitle: "Cómo se elige la mejor recta de ajuste"
date: 2026-08-03T00:00:00
lastmod: 2026-04-14T00:00:00
authors: ["juan-david-leongomez"]
summary: "Aplicación web creada con R Shiny para explicar de forma interactiva el intercepto, la pendiente, los residuos y por qué se usa la suma de residuos al cuadrado (SSR) para elegir la mejor recta de ajuste."
tags: ["Estadística", "Métodos cuantitativos", "Apps"]
editor_options: 
  markdown: 
    wrap: 80
---

App de R Shiny para explicar de forma interactiva el intercepto, la pendiente,
los residuos y por qué se usa la suma de residuos al cuadrado (SSR) para
elegir la mejor recta de ajuste.

<p>
  <a href="https://shiny.jdl-svr.lat/intercepto_pendiente/"
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
    ▶️ Acceder a la aplicación
  </a>
</p>

## Cómo usarla

1. **Tus variables**: define el nombre, media, desviación estándar y
   correlación (r) de X e Y, y genera una muestra simulada.
2. **Ajusta la recta y mira los residuos**: mueve los sliders de intercepto
   y pendiente para intentar ajustar la recta a mano; observa los residuos
   y cómo cambia la suma de residuos al cuadrado (SSR).
3. **La superficie de error (SSR)**: visualiza el SSR para muchas
   combinaciones de intercepto/pendiente y comprueba que la solución de
   mínimos cuadrados (OLS) es el único mínimo de esa superficie.
   
## Instalación (para correrla localmente)

```r
install.packages(c("shiny", "ggplot2", "MASS"))
```

(`MASS` normalmente ya viene incluido con R.)

## Ejecutar la app

Primero, debes descargar la [carpeta del proyecto](http://localhost:4321/post/intercepto_pendiente) a tu computador.

Una vez la descargues, y desde la carpeta del proyecto:

```r
shiny::runApp("app.R")
```

o desde la terminal:

```sh
Rscript -e "shiny::runApp('app.R')"
```
   
## Citar

> Leongómez, J. D. (2026). *Intercepto, pendiente y residuos*. GitHub. [https://github.com/JDLeongomez/intercepto_pendiente](https://github.com/JDLeongomez/intercepto_pendiente)
