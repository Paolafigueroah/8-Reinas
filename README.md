# Análisis Comparativo de Algoritmos para el Problema de las N-Reinas

## Descripción del Proyecto

Este proyecto implementa y compara experimentalmente dos enfoques algorítmicos para resolver el problema de las N-Reinas:

1. **Algoritmo Hill Climbing** (búsqueda local)
2. **Algoritmo Backtracking** (búsqueda sistemática)

## Fuentes y Referencias

### Algoritmo Hill Climbing

**Fuente Base:**
- **Título:** "N-Queen Problem | Local Search using Hill Climbing with Random Neighbour"
- **Autor:** GeeksforGeeks contributors
- **Sitio:** GeeksforGeeks
- **URL:** https://www.geeksforgeeks.org/n-queen-problem-local-search-using-hill-climbing-with-random-neighbour/
- **Fecha de consulta:** 2024
- **Licencia:** No especificada (uso educativo)

**Modificaciones realizadas:**
- Agregada medición de tiempo de ejecución usando `time.time()`
- Agregado conteo de iteraciones/estados explorados
- Agregado soporte para diferentes tamaños de tablero (n variable)
- Implementada función de visualización opcional usando matplotlib
- Implementado Random Restart como mejora (Experimento 3)

### Algoritmo Backtracking

**Fuente Base:**
- **Título:** "Eight queens puzzle" - algoritmo de backtracking estándar
- **Autor:** Varios (algoritmo clásico ampliamente conocido)
- **Referencia:** Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). 
  *Introduction to Algorithms* (3rd ed.). MIT Press. - Capítulo sobre backtracking
- **Fecha de consulta:** 2024
- **Licencia:** Algoritmo de dominio público

**Modificaciones realizadas:**
- Agregada medición de tiempo de ejecución usando `time.time()`
- Agregado conteo de nodos/estados explorados durante la búsqueda
- Agregado soporte para diferentes tamaños de tablero (n variable)
- Implementada función de visualización opcional usando matplotlib
- Agregada poda adicional optimizada con verificación de diagonales mejorada (Experimento 3)

## Estructura del Proyecto

```
8-Reinas/
├── hill_climbing.py          # Implementación del algoritmo Hill Climbing
├── backtracking.py           # Implementación del algoritmo Backtracking
├── visualization.py          # Módulo de visualización de tableros
├── experiments.py            # Script principal de experimentación
├── requirements.txt          # Dependencias del proyecto
└── README.md                # Este archivo
```

## Instalación

1. Asegúrate de tener Python 3.7 o superior instalado.

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

## Uso

### Ejecutar un algoritmo individual

#### Hill Climbing:
```bash
python hill_climbing.py
```

#### Backtracking:
```bash
python backtracking.py
```

### Ejecutar todos los experimentos

El script `experiments.py` ejecuta los tres experimentos requeridos:

```bash
python experiments.py
```

Esto generará:
- **Experimento 1:** Escalabilidad (n = 4, 8, 12, 16, 20)
- **Experimento 2:** Consistencia (10 ejecuciones para n = 8)
- **Experimento 3:** Optimización (versión original vs. mejorada)

Los resultados se guardan en:
- `resultados_experimentos.json` (formato JSON)
- `experimento1_escalabilidad.csv`
- `experimento2_consistencia.csv`

### Visualización

Para visualizar una solución:
```python
from backtracking import BacktrackingNQueens
from visualization import visualize_board

n = 8
bt = BacktrackingNQueens(n)
solution, stats = bt.solve()

if stats['solution_found']:
    visualize_board(solution, n, f"Solución para {n}-Reinas")
```

## Experimentos

### Experimento 1: Escalabilidad
- Prueba con n = 4, 8, 12, 16, 20 reinas
- Mide tiempo de ejecución, iteraciones/nodos explorados y memoria utilizada
- Identifica si algún algoritmo falla en tamaños específicos

### Experimento 2: Consistencia de Resultados
- Ejecuta cada algoritmo 10 veces para n = 8
- Registra variabilidad en tiempo y soluciones encontradas
- Analiza determinismo vs. aleatoriedad:
  - **Hill Climbing:** Analiza variación en estado inicial, selección aleatoria de vecinos, variación temporal y soluciones diferentes
  - **Backtracking:** Analiza consistencia en orden de exploración, soluciones encontradas y tiempo de ejecución

### Experimento 3: Optimización y Modificaciones
- **Hill Climbing:** Compara versión original vs. Random Restart
- **Backtracking:** Compara versión original vs. Poda Optimizada adicional

## Características Implementadas

### Mediciones
- ✅ Tiempo de ejecución (precisión microsegundos)
- ✅ Número de iteraciones/estados explorados
- ✅ Memoria utilizada (opcional, requiere psutil)
- ✅ Tasa de éxito en encontrar soluciones

### Visualización
- ✅ Visualización de tableros en consola
- ✅ Visualización gráfica usando matplotlib
- ✅ Comparación lado a lado de múltiples soluciones

### Experimentación
- ✅ Script automatizado para los 3 experimentos
- ✅ Exportación de resultados a JSON y CSV
- ✅ Tablas comparativas formateadas
- ✅ Análisis estadístico (promedio, desviación estándar)

## Consideraciones Éticas

- **Citación de fuentes:** Todas las fuentes utilizadas están documentadas en este README y en los comentarios de los archivos fuente.
- **Claridad en modificaciones:** Los archivos fuente contienen secciones claramente marcadas indicando qué partes son originales y cuáles son modificaciones realizadas.
- **Licencias:** Se respetan las licencias de los códigos base utilizados (uso educativo).

## Autores

Este proyecto fue desarrollado como parte de la asignación de Fundamentos de IA.

## Licencia

Este proyecto es para uso educativo. Los algoritmos base tienen sus respectivas licencias como se indica en las referencias.
