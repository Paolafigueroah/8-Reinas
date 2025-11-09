"""
Experimento 1: Escalabilidad
Prueba con n = 4, 8, 12, 16, 20 reinas
Mide tiempo de ejecución y memoria utilizada
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
from codigo.utils import measure_memory, ensure_dir, MEMORY_AVAILABLE

# Rutas
BASE_DIR = Path(__file__).parent.parent
RESULTS_DIR = BASE_DIR / "experimentos" / "resultados_brutos"
ensure_dir(str(RESULTS_DIR))


def experimento1_escalabilidad():
    """
    Experimento 1: Escalabilidad
    Prueba con n = 4, 8, 12, 16, 20 reinas
    Mide tiempo de ejecución y memoria utilizada
    """
    print("\n" + "="*80)
    print("EXPERIMENTO 1: ESCALABILIDAD")
    print("="*80)
    
    n_values = [4, 8, 12, 16, 20]
    results_hc = []
    results_bt = []
    
    for n in n_values:
        print(f"\nProbando con n = {n}...")
        
        # Hill Climbing (3 intentos para obtener mejor resultado)
        hc_times = []
        hc_iterations = []
        hc_solutions_found = 0
        hc_memory = []
        
        for attempt in range(3):
            hc = HillClimbingNQueens(n, use_random_restart=False)
            if MEMORY_AVAILABLE:
                (solution, stats), mem = measure_memory(hc.solve)
                hc_memory.append(mem)
            else:
                solution, stats = hc.solve()
                mem = None
            
            hc_times.append(stats['execution_time'])
            hc_iterations.append(stats['iterations'])
            if stats['solution_found']:
                hc_solutions_found += 1
        
        results_hc.append({
            'n': n,
            'tiempo_promedio': statistics.mean(hc_times),
            'tiempo_min': min(hc_times),
            'tiempo_max': max(hc_times),
            'iteraciones_promedio': statistics.mean(hc_iterations),
            'iteraciones_min': min(hc_iterations),
            'iteraciones_max': max(hc_iterations),
            'soluciones_encontradas': hc_solutions_found,
            'memoria_promedio': statistics.mean(hc_memory) if hc_memory else None
        })
        
        # Backtracking
        bt = BacktrackingNQueens(n, use_optimized_pruning=False)
        if MEMORY_AVAILABLE:
            (solution, stats), mem = measure_memory(bt.solve)
        else:
            solution, stats = bt.solve()
            mem = None
        
        results_bt.append({
            'n': n,
            'tiempo': stats['execution_time'],
            'nodos_explorados': stats['nodes_explored'],
            'solucion_encontrada': stats['solution_found'],
            'memoria': mem
        })
        
        print(f"  Hill Climbing: tiempo={statistics.mean(hc_times):.6f}s, "
              f"iteraciones={statistics.mean(hc_iterations):.0f}, "
              f"soluciones={hc_solutions_found}/3")
        print(f"  Backtracking: tiempo={stats['execution_time']:.6f}s, "
              f"nodos={stats['nodes_explored']}, "
              f"solucion={'Sí' if stats['solution_found'] else 'No'}")
    
    # Guardar resultados
    results = {
        'experimento1': {
            'hill_climbing': results_hc,
            'backtracking': results_bt
        }
    }
    
    # Guardar JSON
    json_path = RESULTS_DIR / "exp1_resultados.json"
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"\nResultados guardados en: {json_path}")
    
    # Guardar CSV
    csv_path = RESULTS_DIR / "exp1_resultados.csv"
    with open(csv_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['n', 'algoritmo', 'tiempo_promedio', 'iteraciones_nodos', 
                       'memoria_mb', 'solucion_encontrada'])
        for hc in results_hc:
            writer.writerow([hc['n'], 'Hill Climbing', hc['tiempo_promedio'], 
                           hc['iteraciones_promedio'], hc['memoria_promedio'] or 0,
                           hc['soluciones_encontradas'] > 0])
        for bt in results_bt:
            writer.writerow([bt['n'], 'Backtracking', bt['tiempo'], 
                           bt['nodos_explorados'], bt['memoria'] or 0,
                           bt['solucion_encontrada']])
    print(f"Resultados CSV guardados en: {csv_path}")
    
    # Imprimir tabla
    print("\n" + "-"*80)
    print("TABLA EXPERIMENTO 1: ESCALABILIDAD")
    print("-"*80)
    print(f"{'n':<5} {'Algoritmo':<20} {'Tiempo (s)':<15} {'Iter/Nodos':<15} {'Memoria (MB)':<15}")
    print("-"*80)
    
    for hc, bt in zip(results_hc, results_bt):
        print(f"{hc['n']:<5} {'Hill Climbing':<20} {hc['tiempo_promedio']:<15.6f} "
              f"{hc['iteraciones_promedio']:<15.0f} "
              f"{hc['memoria_promedio'] if hc['memoria_promedio'] else 'N/A':<15}")
        print(f"{bt['n']:<5} {'Backtracking':<20} {bt['tiempo']:<15.6f} "
              f"{bt['nodos_explorados']:<15} "
              f"{bt['memoria'] if bt['memoria'] else 'N/A':<15}")
        print("-"*80)
    
    return results


if __name__ == "__main__":
    experimento1_escalabilidad()

