# Actividad 1 – Sistema de Evaluación de Feria de Ciencias

## Descripción

Este programa implementa un **sistema de evaluación** para equipos que participan en una feria de ciencias.

Cumple con:

1. Calcula puntajes por ronda.
2. Determina el **Mejor Equipo de la Ronda (MER)**.
3. Mantiene un acumulado de métricas: innovacion, presentacion, errores, MER y total.
4. Muestra una tabla ordenada por puntaje total (descendente) tras cada ronda y al final de la competencia.

## Estructura de carpetas

```

Actividad-1-
│
├── notebooks/
│   ├── actividad\_1.ipynb      # Jupyter Notebook principal
│   ├── evaluaciones.py        # Datos de entrada (las rondas)
│   ├── README.md              # Documentación del proyecto
│   └── src/                   # Código fuente en módulos
│       ├── **init**.py        # Marca el paquete
│       └── scoring.py         # Funciones principales (puntajes, acumulado, etc.)

```
## Instalación

1. Se requiere **Python 3.12.9**

## 🧩 Uso del programa

* El programa lee los datos desde `evaluaciones.py`.
* Cada ronda contiene los equipos y sus métricas (`innovacion`, `presentacion`, `errores`).
* El sistema imprime:

  * El mejor equipo de cada ronda.
  * Una tabla acumulada ordenada.
  * Los resultados finales y la tabla final definitiva.

## Ejemplo de salida

```

Resultados de la Feria de Ciencias - Sistema de Evaluación

Ronda 1
Mejor Equipo de la Ronda: EquipoA (6 puntos)

Ranking Actualizado
Equipo     Innovación  Presentación  Errores MER   Total
--------------------------------------------------------

EquipoA    2           1             1       1     6
EquipoB    1           0             0       0     3

```

## 🛠️ Funciones principales

* `puntaje_equipo(datos_equipo)` → calcula el puntaje de un equipo en una ronda.
* `puntajes_ronda(ronda)` → genera los puntajes de todos los equipos en la ronda.
* `mejor_equipo_ronda(ronda)` → determina el Mejor Equipo de la Ronda (MER).
* `inicializar_acumulado(equipos)` → crea el diccionario acumulado con métricas en cero.
* `actualizar_acumulado(acumulado, ronda, equipo_mer)` → actualiza métricas tras cada ronda.
* `mostrar_tabla(acumulado, titulo)` → imprime la tabla ordenada.

## 👩‍💻 Autoría

Trabajo práctico realizado por Maria Araujo, Materia: Taller de Lenguaje - CDO - UNLP.
