"""
Script de prueba rápida para verificar que los algoritmos funcionan correctamente.
"""

import sys
from pathlib import Path

# Agregar el directorio padre al path
sys.path.insert(0, str(Path(__file__).parent.parent))

from codigo.hill_climbing import HillClimbingNQueens
from codigo.backtracking import BacktrackingNQueens

def test_algorithms():
    print("="*60)
    print("PRUEBA RÁPIDA DE ALGORITMOS")
    print("="*60)
    
    n = 4  # Tamaño pequeño para prueba rápida
    
    # Test Hill Climbing
    print("\n1. Probando Hill Climbing (n=4)...")
    hc = HillClimbingNQueens(n, use_random_restart=False)
    solution_hc, stats_hc = hc.solve()
    print(f"   Solución encontrada: {stats_hc['solution_found']}")
    print(f"   Tiempo: {stats_hc['execution_time']:.6f}s")
    print(f"   Iteraciones: {stats_hc['iterations']}")
    if stats_hc['solution_found']:
        print(f"   Solución: {solution_hc}")
    
    # Test Backtracking
    print("\n2. Probando Backtracking (n=4)...")
    bt = BacktrackingNQueens(n, use_optimized_pruning=False)
    solution_bt, stats_bt = bt.solve()
    print(f"   Solución encontrada: {stats_bt['solution_found']}")
    print(f"   Tiempo: {stats_bt['execution_time']:.6f}s")
    print(f"   Nodos explorados: {stats_bt['nodes_explored']}")
    if stats_bt['solution_found']:
        print(f"   Solución: {solution_bt}")
    
    # Test Random Restart
    print("\n3. Probando Hill Climbing con Random Restart (n=4)...")
    hc_rr = HillClimbingNQueens(n, use_random_restart=True, max_restarts=10)
    solution_hc_rr, stats_hc_rr = hc_rr.solve()
    print(f"   Solución encontrada: {stats_hc_rr['solution_found']}")
    print(f"   Tiempo: {stats_hc_rr['execution_time']:.6f}s")
    print(f"   Iteraciones: {stats_hc_rr['iterations']}")
    print(f"   Reinicios: {stats_hc_rr['restarts']}")
    
    # Test Backtracking Optimizado
    print("\n4. Probando Backtracking con Poda Optimizada (n=4)...")
    bt_opt = BacktrackingNQueens(n, use_optimized_pruning=True)
    solution_bt_opt, stats_bt_opt = bt_opt.solve()
    print(f"   Solución encontrada: {stats_bt_opt['solution_found']}")
    print(f"   Tiempo: {stats_bt_opt['execution_time']:.6f}s")
    print(f"   Nodos explorados: {stats_bt_opt['nodes_explored']}")
    
    print("\n" + "="*60)
    print("PRUEBAS COMPLETADAS")
    print("="*60)

if __name__ == "__main__":
    test_algorithms()

