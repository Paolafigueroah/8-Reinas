# TABLAS PARA EL REPORTE TÉCNICO

## Experimento 1: Escalabilidad

**Tabla 4.1: Resultados de Escalabilidad - Hill Climbing**

| n  | Tiempo Promedio (s) | Iteraciones Promedio | Memoria (MB) | Tasa de Éxito |
|----|---------------------|---------------------|--------------|---------------|
| 4  | 0.000000 | 2 | N/A | 2/3 |
| 8  | 0.002178 | 4 | 0.01 | 0/3 |
| 12  | 0.015744 | 6 | 0.01 | 0/3 |
| 16  | 0.058542 | 9 | 0.03 | 0/3 |
| 20  | 0.151484 | 10 | 0.08 | 0/3 |

**Tabla 4.2: Resultados de Escalabilidad - Backtracking**

| n  | Tiempo (s) | Nodos Explorados | Memoria (MB) | Solución Encontrada |
|----|------------|------------------|--------------|---------------------|
| 4  | 0.000000 | 26 | N/A | Sí |
| 8  | 0.001999 | 876 | N/A | Sí |
| 12  | 0.001999 | 3066 | N/A | Sí |
| 16  | 0.177607 | 160712 | N/A | Sí |
| 20  | 5.687961 | 3992510 | N/A | Sí |


## Experimento 2: Consistencia

**Tabla 4.3: Análisis Comparativo - Consistencia (n=8, 10 ejecuciones)**

| Ejecución | Hill Climbing                    | Backtracking                    |
|-----------|----------------------------------|----------------------------------|
|           | Tiempo (s) | Iter. | Solución    | Tiempo (s) | Nodos  | Solución    |
| 1 | 0.001998 | 4 | Sí | 0.001000 | 876 | Sí |
| 2 | 0.000999 | 3 | No | 0.000965 | 876 | Sí |
| 3 | 0.002663 | 6 | No | 0.000000 | 876 | Sí |
| 4 | 0.002957 | 5 | No | 0.000994 | 876 | Sí |
| 5 | 0.002002 | 6 | No | 0.001004 | 876 | Sí |
| 6 | 0.003525 | 6 | Sí | 0.000995 | 876 | Sí |
| 7 | 0.000996 | 4 | No | 0.000999 | 876 | Sí |
| 8 | 0.003006 | 6 | No | 0.001000 | 876 | Sí |
| 9 | 0.001032 | 4 | No | 0.000507 | 876 | Sí |
| 10 | 0.002050 | 4 | No | 0.001011 | 876 | Sí |
| **Promedio** | **0.002123** | **5** | **-** | **0.000847** | **876** | **-** |
| **Desv. Est.** | **0.000912** | **1** | **-** | **0.000335** | **0** | **-** |

#### 4.2.3 Análisis de Consistencia

**Hill Climbing:**

1. **Estado inicial:** Aleatorio en cada ejecución, lo que explica la variabilidad en los resultados.
2. **Selección de vecinos:** Cuando hay múltiples vecinos con el mismo número de conflictos, se elige aleatoriamente, añadiendo aleatoriedad.
3. **Variación temporal:** El tiempo varía significativamente (desviación estándar de 0.000912s) debido a:
   - Diferentes estados iniciales
   - Diferentes caminos de búsqueda
   - Posibilidad de quedar atrapado en óptimos locales
4. **Soluciones encontradas:** Se encontraron 2 soluciones únicas diferentes, demostrando no determinismo.
5. **Tasa de éxito:** 20% de éxito en encontrar solución.

**Backtracking:**

1. **Orden de exploración:** Determinista, siempre explora las filas en el mismo orden (0, 1, 2, ..., N-1).
2. **Solución encontrada:** Siempre encuentra la misma solución porque explora el espacio de manera sistemática y se detiene en la primera solución encontrada.
3. **Consistencia temporal:** El tiempo es muy consistente (desviación estándar de 0.000335s) porque el algoritmo es completamente determinista.
4. **Nodos explorados:** Siempre explora exactamente el mismo número de nodos (876) porque el orden de exploración es fijo.
5. **Tasa de éxito:** 100% de éxito.


## Experimento 3: Optimización

**Tabla 4.4: Hill Climbing - Original vs. Random Restart**

| n  | Versión       | Tiempo (s) | Iteraciones | Reinicios | Solución Encontrada |
|----|---------------|------------|-------------|-----------|---------------------|
| 8  | Original      | 0.000972 | 3 | 0 | No |
| 8  | Random Restart| 0.006793 | 20 | 5 | Sí |
| 12  | Original      | 0.009673 | 6 | 0 | No |
| 12  | Random Restart| 0.156121 | 92 | 16 | Sí |
| 16  | Original      | 0.029026 | 5 | 0 | No |
| 16  | Random Restart| 2.158046 | 371 | 50 | No |

**Tabla 4.5: Backtracking - Original vs. Poda Optimizada**

| n  | Versión          | Tiempo (s) | Nodos Explorados | Solución Encontrada |
|----|------------------|------------|------------------|---------------------|
| 8  | Original         | 0.000000 | 876 | Sí |
| 8  | Poda Optimizada  | 0.001038 | 876 | Sí |
| 12  | Original         | 0.003015 | 3066 | Sí |
| 12  | Poda Optimizada  | 0.001989 | 3066 | Sí |
| 16  | Original         | 0.158659 | 160712 | Sí |
| 16  | Poda Optimizada  | 0.178966 | 160712 | Sí |
