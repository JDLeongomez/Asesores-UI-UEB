---
title: "Estimador de Puntajes para Proyectos de Investigación"
date: 2026-01-20T00:00:00
lastmod: 2025-06-03T00:00:00
authors: ["juan-david-leongomez"]
summary: "Aplicación que calcula el puntaje requerido para proyectos de investigación según su categoría y duración del contrato, y también permite registrar los productos de investigación para verificar si se alcanzan los puntajes necesarios."
tags: ["App", "Aplicación", "Software", "R", "Puntaje", "Proyectos de investigación"]
editor_options: 
  markdown: 
    wrap: 80
# Opcionales útiles en Hugo Blox:
# featured: true
# show_date: true
# show_toc: true
# toc: true
# commentable: false
---

Esta aplicación calcula el puntaje requerido para proyectos de investigación según su categoría y duración del contrato, y también permite registrar los productos de investigación para verificar si se alcanzan los puntajes necesarios.

<p>
  <a href="https://shiny.jdl-svr.lat/Puntaje_Proyecto_Investigacion/"
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

## Descripción breve

### ¿Qué es esta aplicación?

Esta aplicación permite **estimar y verificar el cumplimiento de los puntajes exigidos para proyectos de investigación** según los criterios de la Facultad de Psicología de la Universidad El Bosque.

### ¿Qué hace?

- Calcula automáticamente el **puntaje total requerido** y su distribución por tipo de producto.
- Permite **registrar productos** y ver cómo se acumulan los puntos.
- **Compara** los puntajes requeridos con los obtenidos.
- Indica claramente **si el proyecto cumple o qué le hace falta**.
- Genera un **informe descargable en PDF** con el resumen de resultados.

### ¿Qué tiene en cuenta?

- La **categoría del proyecto** (A1, A2, B, C o D).
- El **tipo de contrato** de quien lidera el proyecto: 48 semanas (12 meses) o 42 semanas (11 meses).
- Los **productos de investigación** (nuevo conocimiento, divulgación, formación, etc.).
- Los **puntos excedentes** de años anteriores, si existen.
