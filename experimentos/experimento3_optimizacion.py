"""
Experimento 3: Optimización y Modificaciones
Compara versión original vs. mejorada
- Hill Climbing: random restart
- Backtracking: poda adicional optimizada
"""

import sys
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


def experimento3_optimizacion():
    """
    Experimento 3: Optimización y modificaciones
    Compara versión original vs. mejorada
    - Hill Climbing: random restart
    - Backtracking: poda adicional optimizada
    """
    print("\n" + "="*80)
    print("EXPERIMENTO 3: OPTIMIZACIÓN Y MODIFICACIONES")
    print("="*80)
    
    n_values = [8, 12, 16]
    results_hc = []
    results_bt = []
    
    for n in n_values:
        print(f"\nProbando con n = {n}...")
        
        # Hill Climbing: Original vs. Random Restart
        print("  Hill Climbing Original:")
        hc_original = HillClimbingNQueens(n, use_random_restart=False)
        solution_orig, stats_orig = hc_original.solve()
        
        print(f"    Tiempo: {stats_orig['execution_time']:.6f}s, "
              f"Iteraciones: {stats_orig['iterations']}, "
              f"Solución: {'Sí' if stats_orig['solution_found'] else 'No'}")
        
        print("  Hill Climbing con Random Restart:")
        hc_restart = HillClimbingNQueens(n, use_random_restart=True, max_restarts=50)
        solution_restart, stats_restart = hc_restart.solve()
        
        print(f"    Tiempo: {stats_restart['execution_time']:.6f}s, "
              f"Iteraciones: {stats_restart['iterations']}, "
              f"Reinicios: {stats_restart['restarts']}, "
              f"Solución: {'Sí' if stats_restart['solution_found'] else 'No'}")
        
        results_hc.append({
            'n': n,
            'original': stats_orig,
            'random_restart': stats_restart
        })
        
        # Backtracking: Original vs. Poda Optimizada
        print("  Backtracking Original:")
        bt_original = BacktrackingNQueens(n, use_optimized_pruning=False)
        solution_bt_orig, stats_bt_orig = bt_original.solve()
        
        print(f"    Tiempo: {stats_bt_orig['execution_time']:.6f}s, "
              f"Nodos: {stats_bt_orig['nodes_explored']}, "
              f"Solución: {'Sí' if stats_bt_orig['solution_found'] else 'No'}")
        
        print("  Backtracking con Poda Optimizada:")
        bt_optimized = BacktrackingNQueens(n, use_optimized_pruning=True)
        solution_bt_opt, stats_bt_opt = bt_optimized.solve()
        
        print(f"    Tiempo: {stats_bt_opt['execution_time']:.6f}s, "
              f"Nodos: {stats_bt_opt['nodes_explored']}, "
              f"Solución: {'Sí' if stats_bt_opt['solution_found'] else 'No'}")
        
        results_bt.append({
            'n': n,
            'original': stats_bt_orig,
            'optimizada': stats_bt_opt
        })
    
    # Guardar resultados
    results = {
        'experimento3': {
            'hill_climbing': results_hc,
            'backtracking': results_bt
        }
    }
    
    # Guardar JSON
    json_path = RESULTS_DIR / "exp3_resultados.json"
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"\nResultados guardados en: {json_path}")
    
    # Imprimir tablas
    print("\n" + "-"*80)
    print("TABLA EXPERIMENTO 3: HILL CLIMBING (Original vs. Random Restart)")
    print("-"*80)
    print(f"{'n':<5} {'Versión':<20} {'Tiempo (s)':<15} {'Iteraciones':<15} {'Solución':<10}")
    print("-"*80)
    
    for result in results_hc:
        print(f"{result['n']:<5} {'Original':<20} "
              f"{result['original']['execution_time']:<15.6f} "
              f"{result['original']['iterations']:<15} "
              f"{'Sí' if result['original']['solution_found'] else 'No':<10}")
        print(f"{result['n']:<5} {'Random Restart':<20} "
              f"{result['random_restart']['execution_time']:<15.6f} "
              f"{result['random_restart']['iterations']:<15} "
              f"{'Sí' if result['random_restart']['solution_found'] else 'No':<10}")
        print("-"*80)
    
    print("\n" + "-"*80)
    print("TABLA EXPERIMENTO 3: BACKTRACKING (Original vs. Poda Optimizada)")
    print("-"*80)
    print(f"{'n':<5} {'Versión':<20} {'Tiempo (s)':<15} {'Nodos':<15} {'Solución':<10}")
    print("-"*80)
    
    for result in results_bt:
        print(f"{result['n']:<5} {'Original':<20} "
              f"{result['original']['execution_time']:<15.6f} "
              f"{result['original']['nodes_explored']:<15} "
              f"{'Sí' if result['original']['solution_found'] else 'No':<10}")
        print(f"{result['n']:<5} {'Poda Optimizada':<20} "
              f"{result['optimizada']['execution_time']:<15.6f} "
              f"{result['optimizada']['nodes_explored']:<15} "
              f"{'Sí' if result['optimizada']['solution_found'] else 'No':<10}")
        print("-"*80)
    
    return results


if __name__ == "__main__":
    experimento3_optimizacion()

