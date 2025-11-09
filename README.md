# Análisis Comparativo de Algoritmos para el Problema de las N-Reinas

## Descripción del Proyecto

Este proyecto implementa y compara experimentalmente dos enfoques algorítmicos para resolver el problema de las N-Reinas:

1. **Algoritmo Hill Climbing** (búsqueda local)
2. **Algoritmo Backtracking** (búsqueda sistemática)

## Estructura del Proyecto

```
NReinas_Comparativo/
│
├── 📄 README.md
│
├── 🧠 codigo/
│   ├── hill_climbing.py          # Algoritmo Hill Climbing
│   ├── backtracking.py           # Algoritmo Backtracking
│   ├── utils.py                  # Funciones comunes (medir tiempo, contar nodos, etc.)
│   ├── main.py                   # Script principal que ejecuta los experimentos
│   └── test_quick.py             # Pruebas rápidas
│
├── 🧪 experimentos/
│   ├── experimento1_escalabilidad.py
│   ├── experimento2_consistencia.py
│   ├── experimento3_optimizacion.py
│   └── resultados_brutos/        # CSV, logs, JSON con datos de salida
│       ├── exp1_resultados.json
│       ├── exp2_resultados.json
│       ├── exp3_resultados.json
│       └── resultados_combinados.json
│
├── 📊 resultados/
│   ├── tablas/                   # Tablas procesadas
│   ├── graficas/                 # Gráficos generados
│   │   ├── tiempo_vs_n.png
│   │   ├── iteraciones_vs_n.png
│   │   └── ...
│   └── generar_graficos.py       # Script para generar gráficos
│
└── 🗃️ docs/
    └── REPORTE_TECNICO.md        # Reporte técnico completo
```

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

## Instalación

1. Asegúrate de tener Python 3.7 o superior instalado.

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

## Uso

### Prueba rápida
```bash
python codigo/test_quick.py
```

### Ejecutar todos los experimentos
```bash
python codigo/main.py
```

### Ejecutar experimentos individuales
```bash
python experimentos/experimento1_escalabilidad.py
python experimentos/experimento2_consistencia.py
python experimentos/experimento3_optimizacion.py
```

### Generar gráficos
```bash
python resultados/generar_graficos.py
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
