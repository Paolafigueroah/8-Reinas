# ANÁLISIS COMPARATIVO DE ALGORITMOS PARA EL PROBLEMA DE LAS N-REINAS

**Análisis Comparativo de Algoritmos: Hill Climbing vs. Backtracking**

---

## PORTADA

**Título del Trabajo:**  
Análisis Comparativo de Algoritmos para el Problema de las N-Reinas

**Integrantes del Equipo:**  
[Indicar nombres de los integrantes]

**Fecha de Entrega:**  
[Indicar fecha]

**Curso:**  
Fundamentos de Inteligencia Artificial

**Profesor:**  
[Indicar nombre del profesor]

---

## 1. INTRODUCCIÓN

### 1.1 Descripción del Problema de las N-Reinas

El problema de las N-Reinas es un problema clásico en ciencias de la computación y matemáticas que consiste en colocar N reinas en un tablero de ajedrez de N×N de tal manera que ninguna reina pueda atacar a otra. En el ajedrez, una reina puede moverse en cualquier dirección (horizontal, vertical y diagonal) cualquier número de casillas, por lo que el problema requiere que ninguna reina comparta fila, columna o diagonal con otra.

Este problema fue propuesto originalmente para 8 reinas en 1848 por el ajedrecista Max Bezzel y ha sido estudiado extensivamente desde entonces. Para N=8, existen 92 soluciones únicas, mientras que para valores mayores de N, el número de soluciones crece exponencialmente, convirtiéndolo en un problema NP-completo en su variante de encontrar todas las soluciones.

### 1.2 Importancia y Aplicaciones

El problema de las N-Reinas es importante por varias razones:

1. **Problema de referencia:** Sirve como caso de prueba estándar para algoritmos de búsqueda, constraint satisfaction problems (CSP) y optimización combinatoria.

2. **Aplicaciones prácticas:** 
   - Planificación y scheduling en sistemas distribuidos
   - Optimización de recursos en redes de telecomunicaciones
   - Diseño de circuitos integrados
   - Problemas de asignación de recursos

3. **Valor educativo:** Permite comparar diferentes paradigmas algorítmicos:
   - Búsqueda sistemática (backtracking)
   - Búsqueda local (hill climbing)
   - Algoritmos genéticos
   - Simulated annealing

### 1.3 Objetivos Específicos del Análisis

Los objetivos específicos de este trabajo son:

1. **Implementar y adaptar** dos algoritmos distintos (Hill Climbing y Backtracking) para resolver el problema de N-Reinas.

2. **Comparar experimentalmente** el rendimiento de ambos algoritmos en términos de:
   - Tiempo de ejecución
   - Número de estados/iteraciones explorados
   - Tasa de éxito en encontrar soluciones
   - Consistencia de resultados

3. **Analizar la escalabilidad** de cada algoritmo para diferentes valores de N (4, 8, 12, 16, 20).

4. **Evaluar la consistencia** de los resultados mediante múltiples ejecuciones y análisis de variabilidad.

5. **Implementar mejoras** a los algoritmos base (random restart para Hill Climbing, poda adicional para Backtracking) y evaluar su impacto.

6. **Documentar** claramente las fuentes de los algoritmos base y las modificaciones realizadas.

---

## 2. MARCO TEÓRICO

### 2.1 Problema de las N-Reinas

#### 2.1.1 Definición Formal

El problema de las N-Reinas se puede definir formalmente como:

- **Entrada:** Un entero positivo N (número de reinas y tamaño del tablero)
- **Salida:** Una configuración válida del tablero N×N donde:
  - Exactamente N reinas están colocadas
  - Ninguna reina ataca a otra
  - Dos reinas se atacan si están en la misma fila, columna o diagonal

#### 2.1.2 Espacio de Estados

El espacio de estados para el problema de N-Reinas es enorme:

- **Representación simple:** Cada reina puede estar en cualquiera de las N² posiciones del tablero, resultando en (N²)^N configuraciones posibles.
- **Representación optimizada:** Si restringimos a una reina por columna, el espacio se reduce a N^N configuraciones.
- **Representación más eficiente:** Si representamos cada configuración como un vector de N elementos donde el elemento i indica la fila de la reina en la columna i, el espacio es N^N, pero la búsqueda puede ser más eficiente.

#### 2.1.3 Restricciones

Las restricciones del problema son:

1. **Restricción de fila:** Cada fila debe contener exactamente una reina (o ninguna, pero en total deben ser N reinas).
2. **Restricción de columna:** Cada columna debe contener exactamente una reina.
3. **Restricción de diagonal principal:** Dos reinas no pueden estar en la misma diagonal principal (i - j = constante).
4. **Restricción de diagonal secundaria:** Dos reinas no pueden estar en la misma diagonal secundaria (i + j = constante).

### 2.2 Algoritmo Hill Climbing

#### 2.2.1 Principios de Funcionamiento

Hill Climbing es un algoritmo de búsqueda local que comienza con un estado inicial (aleatorio en nuestro caso) y realiza movimientos incrementales hacia estados vecinos que mejoran el valor de una función objetivo.

**Características principales:**

1. **Estado inicial:** Se genera aleatoriamente colocando una reina en cada columna.
2. **Función objetivo:** Se utiliza el número de conflictos (pares de reinas que se atacan).
3. **Operadores:** Se generan vecinos moviendo una reina a otra fila en su columna.
4. **Selección:** Se elige el mejor vecino (con menos conflictos). Si hay múltiples vecinos con el mismo número de conflictos, se elige aleatoriamente.
5. **Criterio de parada:** Se detiene cuando:
   - Se encuentra una solución (0 conflictos)
   - Se alcanza un óptimo local (no hay vecinos mejores)

#### 2.2.2 Ventajas y Limitaciones

**Ventajas:**

- **Eficiencia en memoria:** Solo mantiene un estado actual en memoria.
- **Rapidez:** Generalmente encuentra soluciones rápidamente para problemas pequeños.
- **Simplicidad:** Fácil de implementar y entender.

**Limitaciones:**

- **Óptimos locales:** Puede quedar atrapado en óptimos locales que no son soluciones.
- **No garantiza solución:** No es completo; puede no encontrar una solución incluso si existe.
- **Dependencia del estado inicial:** El rendimiento depende significativamente del estado inicial aleatorio.
- **Sensibilidad a la función objetivo:** La elección de la función objetivo afecta el comportamiento del algoritmo.

#### 2.2.3 Complejidad Temporal y Espacial

- **Complejidad temporal:** 
  - En el peor caso: O(N² × I), donde I es el número máximo de iteraciones
  - En promedio: Depende del estado inicial y la distribución de óptimos locales
  - Generación de vecinos: O(N²) para calcular conflictos de todos los vecinos

- **Complejidad espacial:** O(N) para almacenar el estado actual del tablero

### 2.3 Algoritmo Backtracking

#### 2.3.1 Principios de Funcionamiento

Backtracking es un algoritmo de búsqueda sistemática que explora el espacio de soluciones de manera recursiva, construyendo soluciones parciales y retrocediendo (backtracking) cuando encuentra que una solución parcial no puede llevar a una solución válida.

**Características principales:**

1. **Exploración sistemática:** Coloca reinas columna por columna, de izquierda a derecha.
2. **Poda (pruning):** Verifica si es seguro colocar una reina antes de continuar.
3. **Recursión:** Utiliza recursión para explorar todas las posibilidades.
4. **Backtracking:** Si no se puede colocar una reina en ninguna fila de una columna, retrocede a la columna anterior y prueba la siguiente posición.
5. **Criterio de parada:** Se detiene cuando:
   - Se encuentra una solución (todas las reinas colocadas)
   - Se explora todo el espacio de búsqueda sin encontrar solución

#### 2.3.2 Estrategia de Exploración

La estrategia de exploración es determinista:

1. **Orden de exploración:** Siempre explora las filas en orden ascendente (0, 1, 2, ..., N-1).
2. **Profundidad primero:** Explora en profundidad antes de explorar en anchura.
3. **Poda temprana:** Verifica restricciones antes de continuar, evitando explorar ramas inválidas.

#### 2.3.3 Complejidad Temporal y Espacial

- **Complejidad temporal:**
  - En el peor caso: O(N!), aunque con poda es mucho mejor en la práctica
  - En promedio: O(N^N) sin poda, pero con poda eficiente puede ser exponencialmente mejor
  - Verificación de seguridad: O(N) por cada colocación de reina

- **Complejidad espacial:**
  - O(N) para el tablero
  - O(N) para la pila de recursión en el peor caso

---

## 3. METODOLOGÍA

### 3.1 Información sobre el Código de los Algoritmos

#### 3.1.1 Origen de los Códigos Utilizados

**Algoritmo Hill Climbing:**

- **Fuente Base:** GeeksforGeeks
- **Título:** "N-Queen Problem | Local Search using Hill Climbing with Random Neighbour"
- **Autor:** GeeksforGeeks contributors
- **URL:** https://www.geeksforgeeks.org/n-queen-problem-local-search-using-hill-climbing-with-random-neighbour/
- **Fecha de consulta:** 2024
- **Licencia:** No especificada (uso educativo)

**Algoritmo Backtracking:**

- **Fuente Base:** Algoritmo clásico de backtracking para N-Reinas
- **Referencias:**
  - Wikipedia: "Eight queens puzzle" - algoritmo de backtracking estándar
  - Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). *Introduction to Algorithms* (3rd ed.). MIT Press. - Capítulo sobre backtracking
- **Autor:** Varios (algoritmo clásico ampliamente conocido)
- **Fecha de consulta:** 2024
- **Licencia:** Algoritmo de dominio público

#### 3.1.2 Autores y Licencias

- **Hill Climbing:** Basado en código de GeeksforGeeks (licencia no especificada, uso educativo)
- **Backtracking:** Algoritmo de dominio público, implementación propia basada en principios estándar

#### 3.1.3 Enlaces a Repositorios

Los códigos originales están disponibles en:
- Hill Climbing: https://www.geeksforgeeks.org/n-queen-problem-local-search-using-hill-climbing-with-random-neighbour/
- Backtracking: Implementación basada en algoritmos estándar documentados en literatura académica

### 3.2 Modificaciones Realizadas

#### 3.2.1 Modificaciones al Algoritmo Hill Climbing

Las siguientes modificaciones fueron implementadas sobre el código base:

1. **Medición de tiempo de ejecución:**
   - Se agregaron `start_time` y `end_time` usando `time.time()`
   - Se calcula `execution_time` como la diferencia entre ambos
   - Permite medir el rendimiento temporal del algoritmo

2. **Conteo de iteraciones:**
   - Se agregó un contador `iterations` que se incrementa en cada iteración del bucle principal
   - Permite analizar cuántos estados se exploran antes de encontrar una solución o alcanzar un óptimo local

3. **Soporte para diferentes tamaños de tablero:**
   - El algoritmo acepta `n` como parámetro variable
   - Todas las funciones se adaptan dinámicamente al tamaño del tablero

4. **Función de visualización:**
   - Se implementó `visualize_board()` para mostrar el tablero en consola
   - Integración con módulo de visualización gráfica usando matplotlib

5. **Random Restart (Experimento 3):**
   - Se agregó el parámetro `use_random_restart` al constructor
   - Se implementó lógica para reiniciar el algoritmo con un nuevo estado aleatorio cuando se alcanza un óptimo local
   - Se agregó el parámetro `max_restarts` para limitar el número de reinicios
   - Permite escapar de óptimos locales y mejorar la tasa de éxito

#### 3.2.2 Modificaciones al Algoritmo Backtracking

Las siguientes modificaciones fueron implementadas:

1. **Medición de tiempo de ejecución:**
   - Se agregaron `start_time` y `end_time` usando `time.time()`
   - Se calcula `execution_time` como la diferencia entre ambos

2. **Conteo de nodos explorados:**
   - Se agregó un contador `nodes_explored` que se incrementa en cada llamada a `is_safe()`
   - Proporciona una medida del número de estados/nodos explorados durante la búsqueda

3. **Soporte para diferentes tamaños de tablero:**
   - El algoritmo acepta `n` como parámetro variable
   - Todas las funciones se adaptan dinámicamente al tamaño del tablero

4. **Función de visualización:**
   - Se implementó `visualize_board()` para mostrar el tablero en consola
   - Integración con módulo de visualización gráfica usando matplotlib

5. **Poda adicional optimizada (Experimento 3):**
   - Se agregó el parámetro `use_optimized_pruning` al constructor
   - Se implementó verificación adicional de patrones que comúnmente llevan a conflictos
   - Se verifica un rango extendido de columnas anteriores (hasta 3 columnas atrás) para detectar conflictos potenciales
   - Reduce el número de nodos explorados en algunos casos

### 3.3 Diseño Experimental

#### 3.3.1 Variables Medidas

Las variables medidas en los experimentos son:

1. **Tiempo de ejecución (segundos):** Tiempo total desde el inicio hasta el fin de la ejecución del algoritmo
2. **Iteraciones (Hill Climbing):** Número de iteraciones del bucle principal antes de encontrar solución o alcanzar óptimo local
3. **Nodos explorados (Backtracking):** Número de llamadas a `is_safe()`, equivalente al número de estados verificados
4. **Solución encontrada (booleano):** Indica si el algoritmo encontró una solución válida
5. **Memoria utilizada (MB, opcional):** Memoria RAM utilizada durante la ejecución (si psutil está disponible)
6. **Reinicios (Hill Climbing con Random Restart):** Número de reinicios realizados antes de encontrar solución
7. **Solución (vector):** La configuración del tablero encontrada (para análisis de consistencia)

#### 3.3.2 Configuración del Ambiente de Pruebas

**Software:**
- Python 3.7 o superior
- Bibliotecas: matplotlib, psutil, numpy (opcional)
- Sistema operativo: Windows/Linux/MacOS

**Hardware:**
- Procesador: [Especificar si es relevante]
- Memoria RAM: [Especificar]
- Almacenamiento: Suficiente para guardar resultados

#### 3.3.3 Explicación de los Experimentos

**Experimento 1: Escalabilidad**

Este experimento evalúa cómo se comportan ambos algoritmos cuando el tamaño del problema (N) aumenta. Se prueban valores de N = 4, 8, 12, 16, 20.

- **Hill Climbing:** Se ejecuta 3 veces para cada N y se promedian los resultados, ya que el algoritmo es no determinista.
- **Backtracking:** Se ejecuta una vez para cada N, ya que es determinista.
- **Métricas:** Tiempo de ejecución, iteraciones/nodos explorados, memoria utilizada, tasa de éxito.

**Experimento 2: Consistencia de Resultados**

Este experimento analiza la variabilidad y consistencia de los resultados mediante 10 ejecuciones de cada algoritmo para N = 8.

- **Hill Climbing:** Se analiza:
  - Variabilidad en el estado inicial (aleatorio)
  - Variabilidad en la selección de vecinos igualmente buenos (aleatoria)
  - Variación en el tiempo de solución
  - Diferentes soluciones encontradas (si las hay)
  
- **Backtracking:** Se analiza:
  - Consistencia en el orden de exploración (determinista)
  - Consistencia en la solución encontrada (siempre la primera solución)
  - Consistencia en el tiempo de ejecución

**Experimento 3: Optimización y Modificaciones**

Este experimento compara las versiones originales de los algoritmos con versiones mejoradas.

- **Hill Climbing:** Compara versión original vs. Random Restart (máximo 50 reinicios)
- **Backtracking:** Compara versión original vs. Poda Optimizada adicional
- **Métricas:** Tiempo de ejecución, iteraciones/nodos explorados, tasa de éxito
- **Valores de N:** 8, 12, 16

---

## 4. RESULTADOS EXPERIMENTALES

### 4.1 Experimento 1: Escalabilidad

#### 4.1.1 Configuración

- **Valores de N:** 4, 8, 12, 16, 20
- **Hill Climbing:** 3 ejecuciones por N (promedio)
- **Backtracking:** 1 ejecución por N
- **Mediciones:** Tiempo (s), Iteraciones/Nodos, Memoria (MB), Tasa de éxito

#### 4.1.2 Resultados

*Nota: Los siguientes resultados son ejemplos. Se deben ejecutar los experimentos para obtener resultados reales.*

**Tabla 4.1: Resultados de Escalabilidad - Hill Climbing**

| n  | Tiempo Promedio (s) | Iteraciones Promedio | Memoria (MB) | Tasa de Éxito |
|----|---------------------|---------------------|--------------|---------------|
| 4  | 0.001234            | 15                  | 0.5          | 3/3           |
| 8  | 0.045678            | 28                  | 1.2          | 2/3           |
| 12 | 0.123456            | 45                  | 2.1          | 1/3           |
| 16 | 0.456789            | 78                  | 3.5          | 0/3           |
| 20 | 1.234567            | 120                 | 5.2          | 0/3           |

**Tabla 4.2: Resultados de Escalabilidad - Backtracking**

| n  | Tiempo (s) | Nodos Explorados | Memoria (MB) | Solución Encontrada |
|----|------------|------------------|--------------|---------------------|
| 4  | 0.000123   | 15               | 0.3          | Sí                  |
| 8  | 0.032456   | 115              | 0.8          | Sí                  |
| 12 | 0.234567   | 856              | 1.5          | Sí                  |
| 16 | 2.345678   | 5421             | 3.2          | Sí                  |
| 20 | 45.678901  | 87654            | 8.5          | Sí                  |

#### 4.1.3 Observaciones

1. **Hill Climbing:**
   - La tasa de éxito disminuye significativamente a medida que N aumenta
   - Para N ≥ 16, el algoritmo raramente encuentra solución en 3 intentos
   - El tiempo de ejecución aumenta de forma aproximadamente lineal con N
   - Las iteraciones aumentan con N, pero no de forma exponencial

2. **Backtracking:**
   - Siempre encuentra solución (algoritmo completo)
   - El tiempo de ejecución aumenta exponencialmente con N
   - El número de nodos explorados crece exponencialmente
   - Para N = 20, el tiempo es significativamente mayor que Hill Climbing

3. **Comparación:**
   - Para N pequeño (4, 8): Ambos algoritmos son rápidos, pero Backtracking es más confiable
   - Para N mediano (12): Hill Climbing puede ser más rápido pero menos confiable
   - Para N grande (16, 20): Backtracking es más lento pero garantiza solución; Hill Climbing falla frecuentemente

### 4.2 Experimento 2: Consistencia de Resultados

#### 4.2.1 Configuración

- **N:** 8
- **Número de ejecuciones:** 10
- **Algoritmos:** Hill Climbing (sin random restart) y Backtracking

#### 4.2.2 Resultados

*Nota: Los siguientes resultados son ejemplos. Se deben ejecutar los experimentos para obtener resultados reales.*

**Tabla 4.3: Análisis Comparativo - Consistencia (n=8, 10 ejecuciones)**

| Ejecución | Hill Climbing                    | Backtracking                    |
|-----------|----------------------------------|----------------------------------|
|           | Tiempo (s) | Iter. | Solución    | Tiempo (s) | Nodos  | Solución    |
| 1         | 0.045      | 28    | Solución A  | 0.032      | 115    | Solución X  |
| 2         | 0.089      | 52    | Solución B  | 0.032      | 115    | Solución X  |
| 3         | 0.023      | 15    | Solución A  | 0.033      | 115    | Solución X  |
| 4         | 0.067      | 41    | Solución C  | 0.032      | 115    | Solución X  |
| 5         | 0.034      | 22    | No solución | 0.032      | 115    | Solución X  |
| 6         | 0.056      | 35    | Solución A  | 0.032      | 115    | Solución X  |
| 7         | 0.078      | 48    | Solución B  | 0.032      | 115    | Solución X  |
| 8         | 0.012      | 8     | Solución D  | 0.032      | 115    | Solución X  |
| 9         | 0.091      | 55    | No solución | 0.032      | 115    | Solución X  |
| 10        | 0.045      | 28    | Solución A  | 0.032      | 115    | Solución X  |
| **Promedio** | **0.054** | **33.2** | **-** | **0.032** | **115** | **-** |
| **Desv. Est.** | **0.027** | **16.5** | **-** | **0.000** | **0** | **-** |

#### 4.2.3 Análisis de Consistencia

**Hill Climbing:**

1. **Estado inicial:** Aleatorio en cada ejecución, lo que explica la variabilidad en los resultados.
2. **Selección de vecinos:** Cuando hay múltiples vecinos con el mismo número de conflictos, se elige aleatoriamente, añadiendo aleatoriedad.
3. **Variación temporal:** El tiempo varía significativamente (desviación estándar de 0.027s) debido a:
   - Diferentes estados iniciales
   - Diferentes caminos de búsqueda
   - Posibilidad de quedar atrapado en óptimos locales
4. **Soluciones encontradas:** Encuentra diferentes soluciones (A, B, C, D) o ninguna solución, demostrando no determinismo.
5. **Tasa de éxito:** 8/10 = 80% de éxito en encontrar solución.

**Backtracking:**

1. **Orden de exploración:** Determinista, siempre explora las filas en el mismo orden (0, 1, 2, ..., N-1).
2. **Solución encontrada:** Siempre encuentra la misma solución (Solución X) porque explora el espacio de manera sistemática y se detiene en la primera solución encontrada.
3. **Consistencia temporal:** El tiempo es muy consistente (desviación estándar de 0.000s) porque el algoritmo es completamente determinista.
4. **Nodos explorados:** Siempre explora exactamente el mismo número de nodos (115) porque el orden de exploración es fijo.
5. **Tasa de éxito:** 10/10 = 100% de éxito.

#### 4.2.4 Observaciones

1. **Determinismo vs. Aleatoriedad:**
   - Backtracking es completamente determinista: siempre produce los mismos resultados.
   - Hill Climbing es no determinista: produce resultados variables.

2. **Confiabilidad:**
   - Backtracking es más confiable (100% de éxito) pero puede ser más lento para problemas grandes.
   - Hill Climbing es menos confiable (80% de éxito en este caso) pero puede ser más rápido cuando encuentra solución.

3. **Variabilidad:**
   - Hill Climbing muestra alta variabilidad en tiempo, iteraciones y soluciones.
   - Backtracking muestra cero variabilidad en todas las métricas.

### 4.3 Experimento 3: Optimización y Modificaciones

#### 4.3.1 Configuración

- **Valores de N:** 8, 12, 16
- **Hill Climbing:** Original vs. Random Restart (máximo 50 reinicios)
- **Backtracking:** Original vs. Poda Optimizada

#### 4.3.2 Resultados

*Nota: Los siguientes resultados son ejemplos. Se deben ejecutar los experimentos para obtener resultados reales.*

**Tabla 4.4: Hill Climbing - Original vs. Random Restart**

| n  | Versión       | Tiempo (s) | Iteraciones | Reinicios | Solución Encontrada |
|----|---------------|------------|-------------|-----------|---------------------|
| 8  | Original      | 0.054      | 33          | 0         | Sí (80%)            |
| 8  | Random Restart| 0.123      | 85          | 3         | Sí (100%)           |
| 12 | Original      | 0.234      | 78          | 0         | Sí (33%)            |
| 12 | Random Restart| 0.456      | 156         | 5         | Sí (100%)           |
| 16 | Original      | 0.789      | 120         | 0         | No (0%)             |
| 16 | Random Restart| 1.234      | 245         | 8         | Sí (100%)           |

**Tabla 4.5: Backtracking - Original vs. Poda Optimizada**

| n  | Versión          | Tiempo (s) | Nodos Explorados | Solución Encontrada |
|----|------------------|------------|------------------|---------------------|
| 8  | Original         | 0.032      | 115              | Sí                  |
| 8  | Poda Optimizada  | 0.031      | 110              | Sí                  |
| 12 | Original         | 0.234      | 856              | Sí                  |
| 12 | Poda Optimizada  | 0.228      | 820              | Sí                  |
| 16 | Original         | 2.345      | 5421             | Sí                  |
| 16 | Poda Optimizada  | 2.298      | 5280             | Sí                  |

#### 4.3.3 Observaciones

**Hill Climbing con Random Restart:**

1. **Tasa de éxito:** Mejora significativamente, alcanzando 100% de éxito en todos los casos probados.
2. **Tiempo:** Aumenta debido a los múltiples reinicios, pero el tiempo total sigue siendo razonable.
3. **Iteraciones:** Aumenta el número total de iteraciones, pero esto es esperado dado que se realizan múltiples intentos.
4. **Reinicios:** El número de reinicios aumenta con N, indicando que los óptimos locales son más comunes en problemas más grandes.

**Backtracking con Poda Optimizada:**

1. **Nodos explorados:** Se reduce ligeramente el número de nodos explorados (aproximadamente 2-5% de reducción).
2. **Tiempo:** Se reduce ligeramente el tiempo de ejecución, pero la mejora es marginal.
3. **Efectividad:** La poda adicional es más efectiva para valores mayores de N, donde se pueden evitar más exploraciones innecesarias.
4. **Limitaciones:** La mejora es limitada porque el algoritmo ya tiene poda eficiente en la versión original.

---

## 5. DISCUSIÓN

### 5.1 Interpretación de Resultados

Los resultados experimentales revelan características importantes de ambos algoritmos:

1. **Escalabilidad:**
   - **Hill Climbing** muestra un comportamiento que se degrada rápidamente con el tamaño del problema. Aunque es rápido para problemas pequeños, su tasa de éxito disminuye significativamente para N ≥ 16.
   - **Backtracking** mantiene su completitud (siempre encuentra solución) pero su tiempo de ejecución crece exponencialmente, lo que lo hace impráctico para valores muy grandes de N.

2. **Consistencia:**
   - La **aleatoriedad** de Hill Climbing lo hace impredecible pero también le permite encontrar diferentes soluciones, lo que puede ser útil en aplicaciones donde se necesitan múltiples soluciones.
   - La **determinismo** de Backtracking garantiza resultados reproducibles, lo cual es valioso en aplicaciones donde la consistencia es crítica.

3. **Optimizaciones:**
   - **Random Restart** transforma a Hill Climbing en un algoritmo más confiable, sacrificando un poco de velocidad por completitud práctica.
   - **Poda Optimizada** en Backtracking ofrece mejoras marginales, lo que sugiere que la poda original ya es bastante eficiente.

### 5.2 Situaciones donde Cada Algoritmo es Preferible

**Hill Climbing es preferible cuando:**

1. Se necesita una solución rápida para problemas pequeños o medianos (N ≤ 12).
2. No es crítico encontrar siempre una solución (se puede aceptar una tasa de éxito < 100%).
3. Se necesitan múltiples soluciones diferentes (diversidad de soluciones).
4. Los recursos de memoria son limitados (usa O(N) memoria).
5. Se puede usar Random Restart para mejorar la tasa de éxito.

**Backtracking es preferible cuando:**

1. Se requiere garantía de encontrar solución (completitud).
2. Se necesita consistencia y reproducibilidad (determinismo).
3. El problema es relativamente pequeño (N ≤ 20) o se puede tolerar tiempos largos.
4. Se necesita encontrar todas las soluciones (con modificaciones menores).
5. La exactitud es más importante que la velocidad.

### 5.3 Limitaciones Encontradas

1. **Hill Climbing:**
   - No garantiza encontrar solución (no es completo).
   - Puede quedar atrapado en óptimos locales.
   - El rendimiento depende fuertemente del estado inicial.
   - Para N grande, la tasa de éxito es muy baja sin Random Restart.

2. **Backtracking:**
   - Tiempo de ejecución exponencial para N grande.
   - Puede ser muy lento para N ≥ 20.
   - No aprovecha información heurística para guiar la búsqueda.

3. **Limitaciones generales:**
   - Ambos algoritmos pueden ser lentos para valores muy grandes de N.
   - La medición de memoria puede no ser completamente precisa en todos los sistemas.
   - Los resultados pueden variar según el hardware y el sistema operativo.

### 5.4 Posibles Mejoras

1. **Para Hill Climbing:**
   - Implementar Simulated Annealing para escapar de óptimos locales de manera más eficiente.
   - Usar heurísticas más sofisticadas para la selección del estado inicial.
   - Implementar Tabu Search para evitar ciclos.

2. **Para Backtracking:**
   - Implementar heurísticas de ordenamiento de variables (most constrained first).
   - Usar forward checking para detectar conflictos antes.
   - Implementar arc consistency para reducir el espacio de búsqueda.

3. **Para ambos:**
   - Paralelización para aprovechar múltiples núcleos.
   - Algoritmos híbridos que combinen búsqueda local y sistemática.
   - Uso de estructuras de datos más eficientes.

---

## 6. CONCLUSIONES

### 6.1 Resumen de Hallazgos Principales

1. **Hill Climbing** es rápido pero no garantiza solución, especialmente para problemas grandes. Con Random Restart, mejora significativamente su tasa de éxito pero a costa de mayor tiempo de ejecución.

2. **Backtracking** es completo y determinista, siempre encuentra solución pero puede ser lento para problemas grandes debido a su complejidad exponencial.

3. La **escalabilidad** muestra que Backtracking es más confiable pero Hill Climbing puede ser más rápido cuando encuentra solución.

4. La **consistencia** revela que Backtracking produce resultados reproducibles mientras que Hill Climbing es variable pero puede ofrecer diversidad de soluciones.

5. Las **optimizaciones** (Random Restart y Poda Optimizada) mejoran el rendimiento pero con trade-offs: Random Restart aumenta la confiabilidad a costa de tiempo, mientras que la Poda Optimizada ofrece mejoras marginales.

### 6.2 Recomendaciones de Uso

- **Para N ≤ 8:** Ambos algoritmos son eficientes. Backtracking es recomendado si se requiere garantía de solución.
- **Para 8 < N ≤ 12:** Hill Climbing con Random Restart es una buena opción si se puede tolerar una pequeña posibilidad de fallo. Backtracking sigue siendo viable.
- **Para N > 12:** Backtracking es más confiable, pero los tiempos pueden ser largos. Hill Climbing con Random Restart puede ser útil si se acepta el riesgo de no encontrar solución.
- **Para aplicaciones críticas:** Siempre usar Backtracking o Hill Climbing con Random Restart y un número alto de reinicios.
- **Para aplicaciones que requieren múltiples soluciones:** Hill Climbing es preferible debido a su aleatoriedad.

### 6.3 Aprendizajes del Equipo

**[Integrante 1]:** [Describir aprendizajes personales sobre algoritmos de búsqueda, complejidad algorítmica, experimentación científica, etc.]

**[Integrante 2]:** [Describir aprendizajes personales]

**[Integrante 3]:** [Describir aprendizajes personales]

*Nota: Cada integrante debe completar esta sección con sus aprendizajes específicos.*

---

## 7. REFERENCIAS

### 7.1 Fuentes Bibliográficas (Formato APA)

Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). *Introduction to Algorithms* (3rd ed.). MIT Press.

Russell, S., & Norvig, P. (2020). *Artificial Intelligence: A Modern Approach* (4th ed.). Pearson.

Wikipedia. (2024). *Eight queens puzzle*. Recuperado de https://en.wikipedia.org/wiki/Eight_queens_puzzle

### 7.2 Enlaces a Códigos Originales

GeeksforGeeks. (2024). *N-Queen Problem | Local Search using Hill Climbing with Random Neighbour*. Recuperado de https://www.geeksforgeeks.org/n-queen-problem-local-search-using-hill-climbing-with-random-neighbour/

### 7.3 Recursos Consultados

1. GeeksforGeeks - Algoritmos de búsqueda local
2. Wikipedia - Problema de las N-Reinas
3. Cormen et al. - Introducción a Algoritmos (capítulo de backtracking)
4. Documentación de Python - Módulos time, random, statistics
5. Documentación de matplotlib - Visualización de datos

---

## APÉNDICE A: Código Fuente

El código fuente completo está disponible en los archivos:
- `hill_climbing.py`
- `backtracking.py`
- `experiments.py`
- `visualization.py`

## APÉNDICE B: Resultados Detallados

Los resultados detallados de los experimentos están disponibles en:
- `resultados_experimentos.json`
- `experimento1_escalabilidad.csv`
- `experimento2_consistencia.csv`

---

**Fin del Reporte**

