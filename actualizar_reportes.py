"""
Script auxiliar para actualizar el reporte técnico con los resultados reales
de los experimentos. Este script lee los resultados de resultados_experimentos.json
y genera tablas en formato Markdown que se pueden copiar al reporte.
"""

import json
import statistics
from typing import Dict, List

def cargar_resultados(archivo='resultados_experimentos.json'):
    """Carga los resultados desde un archivo JSON."""
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {archivo}")
        print("Ejecuta primero los experimentos con: python experiments.py")
        return None

def generar_tabla_experimento1(resultados):
    """Genera tabla Markdown para el Experimento 1."""
    if not resultados or 'experimento1' not in resultados:
        return "No hay datos del Experimento 1"
    
    exp1 = resultados['experimento1']
    hc_data = exp1['hill_climbing']
    bt_data = exp1['backtracking']
    
    tabla = "\n**Tabla 4.1: Resultados de Escalabilidad - Hill Climbing**\n\n"
    tabla += "| n  | Tiempo Promedio (s) | Iteraciones Promedio | Memoria (MB) | Tasa de Éxito |\n"
    tabla += "|----|---------------------|---------------------|--------------|---------------|\n"
    
    for hc in hc_data:
        memoria = f"{hc['memoria_promedio']:.2f}" if hc.get('memoria_promedio') else "N/A"
        tasa = f"{hc['soluciones_encontradas']}/3"
        tabla += f"| {hc['n']}  | {hc['tiempo_promedio']:.6f} | {hc['iteraciones_promedio']:.0f} | {memoria} | {tasa} |\n"
    
    tabla += "\n**Tabla 4.2: Resultados de Escalabilidad - Backtracking**\n\n"
    tabla += "| n  | Tiempo (s) | Nodos Explorados | Memoria (MB) | Solución Encontrada |\n"
    tabla += "|----|------------|------------------|--------------|---------------------|\n"
    
    for bt in bt_data:
        memoria = f"{bt['memoria']:.2f}" if bt.get('memoria') else "N/A"
        solucion = "Sí" if bt['solucion_encontrada'] else "No"
        tabla += f"| {bt['n']}  | {bt['tiempo']:.6f} | {bt['nodos_explorados']} | {memoria} | {solucion} |\n"
    
    return tabla

def generar_tabla_experimento2(resultados):
    """Genera tabla Markdown para el Experimento 2."""
    if not resultados or 'experimento2' not in resultados:
        return "No hay datos del Experimento 2"
    
    exp2 = resultados['experimento2']
    hc_data = exp2['hill_climbing']
    bt_data = exp2['backtracking']
    hc_stats = exp2['estadisticas_hc']
    bt_stats = exp2['estadisticas_bt']
    
    tabla = "\n**Tabla 4.3: Análisis Comparativo - Consistencia (n=8, 10 ejecuciones)**\n\n"
    tabla += "| Ejecución | Hill Climbing                    | Backtracking                    |\n"
    tabla += "|-----------|----------------------------------|----------------------------------|\n"
    tabla += "|           | Tiempo (s) | Iter. | Solución    | Tiempo (s) | Nodos  | Solución    |\n"
    
    for i in range(len(hc_data)):
        hc = hc_data[i]
        bt = bt_data[i]
        hc_sol = "Sí" if hc['solucion_encontrada'] else "No"
        bt_sol = "Sí" if bt['solucion_encontrada'] else "No"
        
        # Truncar solución si es muy larga
        hc_sol_detalle = hc['solucion'][:20] + "..." if len(hc['solucion']) > 20 else hc['solucion']
        bt_sol_detalle = bt['solucion'][:20] + "..." if len(bt['solucion']) > 20 else bt['solucion']
        
        tabla += f"| {hc['ejecucion']} | {hc['tiempo']:.6f} | {hc['iteraciones']} | {hc_sol} | {bt['tiempo']:.6f} | {bt['nodos_explorados']} | {bt_sol} |\n"
    
    tabla += f"| **Promedio** | **{hc_stats['tiempo_promedio']:.6f}** | **{hc_stats['iteraciones_promedio']:.0f}** | **-** | **{bt_stats['tiempo_promedio']:.6f}** | **{bt_stats['nodos_promedio']:.0f}** | **-** |\n"
    tabla += f"| **Desv. Est.** | **{hc_stats['tiempo_desv_est']:.6f}** | **{hc_stats['iteraciones_desv_est']:.0f}** | **-** | **{bt_stats['tiempo_desv_est']:.6f}** | **{bt_stats['nodos_desv_est']:.0f}** | **-** |\n"
    
    return tabla

def generar_tabla_experimento3(resultados):
    """Genera tabla Markdown para el Experimento 3."""
    if not resultados or 'experimento3' not in resultados:
        return "No hay datos del Experimento 3"
    
    exp3 = resultados['experimento3']
    hc_data = exp3['hill_climbing']
    bt_data = exp3['backtracking']
    
    tabla = "\n**Tabla 4.4: Hill Climbing - Original vs. Random Restart**\n\n"
    tabla += "| n  | Versión       | Tiempo (s) | Iteraciones | Reinicios | Solución Encontrada |\n"
    tabla += "|----|---------------|------------|-------------|-----------|---------------------|\n"
    
    for hc in hc_data:
        orig = hc['original']
        rr = hc['random_restart']
        orig_sol = "Sí" if orig['solution_found'] else "No"
        rr_sol = "Sí" if rr['solution_found'] else "No"
        
        tabla += f"| {hc['n']}  | Original      | {orig['execution_time']:.6f} | {orig['iterations']} | 0 | {orig_sol} |\n"
        tabla += f"| {hc['n']}  | Random Restart| {rr['execution_time']:.6f} | {rr['iterations']} | {rr.get('restarts', 0)} | {rr_sol} |\n"
    
    tabla += "\n**Tabla 4.5: Backtracking - Original vs. Poda Optimizada**\n\n"
    tabla += "| n  | Versión          | Tiempo (s) | Nodos Explorados | Solución Encontrada |\n"
    tabla += "|----|------------------|------------|------------------|---------------------|\n"
    
    for bt in bt_data:
        orig = bt['original']
        opt = bt['optimizada']
        orig_sol = "Sí" if orig['solution_found'] else "No"
        opt_sol = "Sí" if opt['solution_found'] else "No"
        
        tabla += f"| {bt['n']}  | Original         | {orig['execution_time']:.6f} | {orig['nodes_explored']} | {orig_sol} |\n"
        tabla += f"| {bt['n']}  | Poda Optimizada  | {opt['execution_time']:.6f} | {opt['nodes_explored']} | {opt_sol} |\n"
    
    return tabla

def generar_analisis_experimento2(resultados):
    """Genera análisis detallado del Experimento 2."""
    if not resultados or 'experimento2' not in resultados:
        return ""
    
    exp2 = resultados['experimento2']
    hc_data = exp2['hill_climbing']
    bt_data = exp2['backtracking']
    hc_stats = exp2['estadisticas_hc']
    bt_stats = exp2['estadisticas_bt']
    
    # Analizar soluciones únicas de Hill Climbing
    hc_solutions = [tuple(eval(hc['solucion'])) for hc in hc_data if hc['solucion_encontrada'] and hc['solucion'] != "No solución"]
    unique_solutions_hc = len(set(hc_solutions)) if hc_solutions else 0
    
    # Analizar soluciones de Backtracking
    bt_solutions = [tuple(eval(bt['solucion'])) for bt in bt_data if bt['solucion_encontrada'] and bt['solucion'] != "No solución"]
    unique_solutions_bt = len(set(bt_solutions)) if bt_solutions else 0
    
    analisis = "\n#### 4.2.3 Análisis de Consistencia\n\n"
    analisis += "**Hill Climbing:**\n\n"
    analisis += f"1. **Estado inicial:** Aleatorio en cada ejecución, lo que explica la variabilidad en los resultados.\n"
    analisis += f"2. **Selección de vecinos:** Cuando hay múltiples vecinos con el mismo número de conflictos, se elige aleatoriamente, añadiendo aleatoriedad.\n"
    analisis += f"3. **Variación temporal:** El tiempo varía significativamente (desviación estándar de {hc_stats['tiempo_desv_est']:.6f}s) debido a:\n"
    analisis += "   - Diferentes estados iniciales\n"
    analisis += "   - Diferentes caminos de búsqueda\n"
    analisis += "   - Posibilidad de quedar atrapado en óptimos locales\n"
    analisis += f"4. **Soluciones encontradas:** Se encontraron {unique_solutions_hc} soluciones únicas diferentes, demostrando no determinismo.\n"
    analisis += f"5. **Tasa de éxito:** {hc_stats['tasa_exito']*100:.0f}% de éxito en encontrar solución.\n\n"
    
    analisis += "**Backtracking:**\n\n"
    analisis += f"1. **Orden de exploración:** Determinista, siempre explora las filas en el mismo orden (0, 1, 2, ..., N-1).\n"
    analisis += f"2. **Solución encontrada:** Siempre encuentra la misma solución porque explora el espacio de manera sistemática y se detiene en la primera solución encontrada.\n"
    analisis += f"3. **Consistencia temporal:** El tiempo es muy consistente (desviación estándar de {bt_stats['tiempo_desv_est']:.6f}s) porque el algoritmo es completamente determinista.\n"
    analisis += f"4. **Nodos explorados:** Siempre explora exactamente el mismo número de nodos ({bt_stats['nodos_promedio']:.0f}) porque el orden de exploración es fijo.\n"
    analisis += f"5. **Tasa de éxito:** {bt_stats['tasa_exito']*100:.0f}% de éxito.\n"
    
    return analisis

def main():
    """Función principal."""
    print("="*60)
    print("GENERADOR DE TABLAS PARA REPORTE TÉCNICO")
    print("="*60)
    
    resultados = cargar_resultados()
    if not resultados:
        return
    
    print("\nGenerando tablas...")
    
    # Generar tablas
    tabla1 = generar_tabla_experimento1(resultados)
    tabla2 = generar_tabla_experimento2(resultados)
    tabla3 = generar_tabla_experimento3(resultados)
    analisis2 = generar_analisis_experimento2(resultados)
    
    # Guardar en archivo
    with open('tablas_reporte.md', 'w', encoding='utf-8') as f:
        f.write("# TABLAS PARA EL REPORTE TÉCNICO\n\n")
        f.write("## Experimento 1: Escalabilidad\n")
        f.write(tabla1)
        f.write("\n\n## Experimento 2: Consistencia\n")
        f.write(tabla2)
        f.write(analisis2)
        f.write("\n\n## Experimento 3: Optimización\n")
        f.write(tabla3)
    
    print("\nTablas generadas en: tablas_reporte.md")
    print("\nPuedes copiar las tablas de este archivo al REPORTE_TECNICO.md")
    print("="*60)

if __name__ == "__main__":
    main()

