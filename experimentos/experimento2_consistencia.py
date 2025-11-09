"""
Experimento 2: Consistencia de Resultados
Ejecuta cada algoritmo 10 veces para n = 8
Analiza variabilidad en tiempo y soluciones
"""

import sys
import os
import statistics
import json
import csv
from pathlib import Path

# Agregar el directorio padre al path para importar módulos
sys.path.insert(0, str(Path(__file__).parent.parent))

from codigo.hill_climbing import HillClimbingNQueens
from codigo.backtracking import BacktrackingNQueens
from codigo.utils import ensure_dir

# Rutas
BASE_DIR = Path(__file__).parent.parent
RESULTS_DIR = BASE_DIR / "experimentos" / "resultados_brutos"
ensure_dir(str(RESULTS_DIR))


def experimento2_consistencia():
    """
    Experimento 2: Consistencia de resultados
    Ejecuta cada algoritmo 10 veces para n = 8
    Analiza variabilidad en tiempo y soluciones
    """
    print("\n" + "="*80)
    print("EXPERIMENTO 2: CONSISTENCIA DE RESULTADOS")
    print("="*80)
    
    n = 8
    num_runs = 10
    
    print(f"\nEjecutando cada algoritmo {num_runs} veces para n = {n}...\n")
    
    # Hill Climbing
    hc_results = []
    hc_solutions = []
    
    for run in range(1, num_runs + 1):
        hc = HillClimbingNQueens(n, use_random_restart=False)
        solution, stats = hc.solve()
        
        solution_str = str(solution) if stats['solution_found'] else "No solución"
        hc_results.append({
            'ejecucion': run,
            'tiempo': stats['execution_time'],
            'iteraciones': stats['iterations'],
            'solucion': solution_str,
            'solucion_encontrada': stats['solution_found']
        })
        if stats['solution_found']:
            hc_solutions.append(tuple(solution))
        
        print(f"HC Ejecución {run}: tiempo={stats['execution_time']:.6f}s, "
              f"iteraciones={stats['iterations']}, "
              f"solución={'Sí' if stats['solution_found'] else 'No'}")
    
    # Backtracking
    bt_results = []
    bt_solutions = []
    
    for run in range(1, num_runs + 1):
        bt = BacktrackingNQueens(n, use_optimized_pruning=False)
        solution, stats = bt.solve()
        
        solution_str = str(solution) if stats['solution_found'] else "No solución"
        bt_results.append({
            'ejecucion': run,
            'tiempo': stats['execution_time'],
            'nodos_explorados': stats['nodes_explored'],
            'solucion': solution_str,
            'solucion_encontrada': stats['solution_found']
        })
        if stats['solution_found']:
            bt_solutions.append(tuple(solution))
        
        print(f"BT Ejecución {run}: tiempo={stats['execution_time']:.6f}s, "
              f"nodos={stats['nodes_explored']}")
    
    # Calcular estadísticas
    hc_times = [r['tiempo'] for r in hc_results]
    hc_iterations = [r['iteraciones'] for r in hc_results]
    bt_times = [r['tiempo'] for r in bt_results]
    bt_nodes = [r['nodos_explorados'] for r in bt_results]
    
    hc_stats = {
        'tiempo_promedio': statistics.mean(hc_times),
        'tiempo_desv_est': statistics.stdev(hc_times) if len(hc_times) > 1 else 0,
        'iteraciones_promedio': statistics.mean(hc_iterations),
        'iteraciones_desv_est': statistics.stdev(hc_iterations) if len(hc_iterations) > 1 else 0,
        'soluciones_unicas': len(set(hc_solutions)),
        'tasa_exito': sum(r['solucion_encontrada'] for r in hc_results) / num_runs
    }
    
    bt_stats = {
        'tiempo_promedio': statistics.mean(bt_times),
        'tiempo_desv_est': statistics.stdev(bt_times) if len(bt_times) > 1 else 0,
        'nodos_promedio': statistics.mean(bt_nodes),
        'nodos_desv_est': statistics.stdev(bt_nodes) if len(bt_nodes) > 1 else 0,
        'soluciones_unicas': len(set(bt_solutions)),
        'tasa_exito': sum(r['solucion_encontrada'] for r in bt_results) / num_runs
    }
    
    # Guardar resultados
    results = {
        'experimento2': {
            'hill_climbing': hc_results,
            'backtracking': bt_results,
            'estadisticas_hc': hc_stats,
            'estadisticas_bt': bt_stats
        }
    }
    
    # Guardar JSON
    json_path = RESULTS_DIR / "exp2_resultados.json"
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"\nResultados guardados en: {json_path}")
    
    # Guardar CSV
    csv_path = RESULTS_DIR / "exp2_resultados.csv"
    with open(csv_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['ejecucion', 'algoritmo', 'tiempo', 'iteraciones_nodos', 
                       'solucion', 'solucion_encontrada'])
        for hc in hc_results:
            writer.writerow([hc['ejecucion'], 'Hill Climbing', hc['tiempo'], 
                           hc['iteraciones'], hc['solucion'], hc['solucion_encontrada']])
        for bt in bt_results:
            writer.writerow([bt['ejecucion'], 'Backtracking', bt['tiempo'], 
                           bt['nodos_explorados'], bt['solucion'], bt['solucion_encontrada']])
    print(f"Resultados CSV guardados en: {csv_path}")
    
    # Imprimir tabla
    print("\n" + "-"*100)
    print("TABLA EXPERIMENTO 2: CONSISTENCIA (n=8, 10 ejecuciones)")
    print("-"*100)
    print(f"{'Ejec.':<7} {'Hill Climbing':<50} {'Backtracking':<50}")
    print(f"{'':<7} {'Tiempo (s)':<15} {'Iter.':<10} {'Solución':<20} "
          f"{'Tiempo (s)':<15} {'Nodos':<15} {'Solución':<20}")
    print("-"*100)
    
    for i in range(len(hc_results)):
        hc = hc_results[i]
        bt = bt_results[i]
        hc_sol = "Sí" if hc['solucion_encontrada'] else "No"
        bt_sol = "Sí" if bt['solucion_encontrada'] else "No"
        
        print(f"{hc['ejecucion']:<7} {hc['tiempo']:<15.6f} {hc['iteraciones']:<10} "
              f"{hc_sol:<20} {bt['tiempo']:<15.6f} {bt['nodos_explorados']:<15} {bt_sol:<20}")
    
    print("-"*100)
    print(f"{'Promedio':<7} {hc_stats['tiempo_promedio']:<15.6f} "
          f"{hc_stats['iteraciones_promedio']:<10.0f} "
          f"{hc_stats['soluciones_unicas']} únicas{'':<13} "
          f"{bt_stats['tiempo_promedio']:<15.6f} "
          f"{bt_stats['nodos_promedio']:<15.0f} "
          f"{bt_stats['soluciones_unicas']} únicas{'':<13}")
    print(f"{'Desv. Est.':<7} {hc_stats['tiempo_desv_est']:<15.6f} "
          f"{hc_stats['iteraciones_desv_est']:<10.0f} {'':<20} "
          f"{bt_stats['tiempo_desv_est']:<15.6f} "
          f"{bt_stats['nodos_desv_est']:<15.0f} {'':<20}")
    print("-"*100)
    
    return results


if __name__ == "__main__":
    experimento2_consistencia()

