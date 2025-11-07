# Instrucciones de Uso - Análisis Comparativo N-Reinas

## Instalación Rápida

```bash
pip install -r requirements.txt
```

## Ejecución de Experimentos

### Ejecutar Todos los Experimentos

```bash
python experiments.py
```

Esto ejecutará:
- **Experimento 1:** Escalabilidad (n = 4, 8, 12, 16, 20)
- **Experimento 2:** Consistencia (10 ejecuciones para n = 8)
- **Experimento 3:** Optimización (versiones mejoradas)

### Ejecutar Experimentos Individuales

```bash
python run_experiments.py 1    # Solo Experimento 1
python run_experiments.py 2    # Solo Experimento 2
python run_experiments.py 3    # Solo Experimento 3
```

### Prueba Rápida

Para verificar que todo funciona:
```bash
python test_quick.py
```

## Archivos Generados

Después de ejecutar los experimentos, se generan:

1. **resultados_experimentos.json** - Todos los resultados en formato JSON
2. **experimento1_escalabilidad.csv** - Resultados del Experimento 1
3. **experimento2_consistencia.csv** - Resultados del Experimento 2

## Uso de los Algoritmos Individualmente

### Hill Climbing

```python
from hill_climbing import HillClimbingNQueens

n = 8
hc = HillClimbingNQueens(n, use_random_restart=False)
solution, stats = hc.solve()

print(f"Solución encontrada: {stats['solution_found']}")
print(f"Tiempo: {stats['execution_time']:.6f}s")
print(f"Iteraciones: {stats['iterations']}")
```

### Hill Climbing con Random Restart

```python
hc_rr = HillClimbingNQueens(n, use_random_restart=True, max_restarts=100)
solution, stats = hc_rr.solve()
```

### Backtracking

```python
from backtracking import BacktrackingNQueens

bt = BacktrackingNQueens(n, use_optimized_pruning=False)
solution, stats = bt.solve()

print(f"Solución encontrada: {stats['solution_found']}")
print(f"Tiempo: {stats['execution_time']:.6f}s")
print(f"Nodos explorados: {stats['nodes_explored']}")
```

### Visualización

```python
from visualization import visualize_board

if stats['solution_found']:
    visualize_board(solution, n, "Mi Solución")
```

## Estructura de los Resultados

### Experimento 1: Escalabilidad
- Tiempo de ejecución promedio
- Iteraciones/nodos explorados
- Memoria utilizada (si está disponible)
- Tasa de éxito

### Experimento 2: Consistencia
- 10 ejecuciones de cada algoritmo
- Tabla comparativa con:
  - Tiempo de cada ejecución
  - Iteraciones/nodos explorados
  - Soluciones encontradas
  - Promedio y desviación estándar

### Experimento 3: Optimización
- Comparación entre versión original y mejorada
- Para Hill Climbing: Original vs. Random Restart
- Para Backtracking: Original vs. Poda Optimizada

## Notas Importantes

1. **Hill Climbing:** Puede quedar atrapado en óptimos locales, por lo que no siempre encuentra solución. El Random Restart mejora esto.

2. **Backtracking:** Siempre encuentra solución (si existe) porque es un algoritmo completo.

3. **Tiempos de ejecución:** Para valores grandes de n (≥16), los tiempos pueden ser significativos.

4. **Memoria:** La medición de memoria requiere `psutil`. Si no está instalado, se mostrará "N/A" en los resultados.

## Solución de Problemas

### Error: "ModuleNotFoundError: No module named 'matplotlib'"
```bash
pip install matplotlib psutil numpy
```

### Los experimentos tardan mucho
- Reduce el valor de `max_restarts` en Hill Climbing
- Prueba con valores menores de n primero
- Ejecuta los experimentos individualmente en lugar de todos a la vez

### Hill Climbing no encuentra solución
- Esto es normal, especialmente para n grande
- Usa Random Restart para mejorar las probabilidades
- Backtracking siempre encontrará solución si existe

