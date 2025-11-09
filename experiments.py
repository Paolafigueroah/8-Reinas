"""
Script de Experimentación para el Análisis Comparativo de Algoritmos N-Reinas

Este script realiza los tres experimentos requeridos:
1. Experimento 1: Escalabilidad (n = 4, 8, 12, 16, 20)
2. Experimento 2: Consistencia (10 ejecuciones para n = 8)
3. Experimento 3: Optimización (versión original vs. mejorada)

Las instrucciones especifican que se deben medir:
- Tiempo de ejecución
- Número de iteraciones/estados explorados
- Memoria utilizada (opcional, requiere psutil)
- Variabilidad en tiempo y soluciones
"""

import time
import statistics
import csv
import json
from typing import List, Dict, Tuple
import sys
import os

from hill_climbing import HillClimbingNQueens
from backtracking import BacktrackingNQueens

try:
    import psutil
    import tracemalloc
    MEMORY_AVAILABLE = True
except ImportError:
    MEMORY_AVAILABLE = False
    print("Advertencia: psutil o tracemalloc no disponibles. No se medirá memoria.")


class ExperimentRunner:
    """Ejecuta los experimentos comparativos."""
    
    def __init__(self):
        self.results = {
            'experimento1': [],
            'experimento2': [],
            'experimento3': []
        }
    
    def measure_memory(self, func, *args, **kwargs):
        """Mide el uso de memoria de una función."""
        if not MEMORY_AVAILABLE:
            return None
        
        process = psutil.Process(os.getpid())
        mem_before = process.memory_info().rss / 1024 / 1024  # MB
        result = func(*args, **kwargs)
        mem_after = process.memory_info().rss / 1024 / 1024  # MB
        mem_used = mem_after - mem_before
        
        return result, max(0, mem_used)
    
    def experimento1_escalabilidad(self):
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
                    (solution, stats), mem = self.measure_memory(hc.solve)
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
                (solution, stats), mem = self.measure_memory(bt.solve)
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
        self.results['experimento1'] = {
            'hill_climbing': results_hc,
            'backtracking': results_bt
        }
        
        # Generar tabla
        self._print_experimento1_table(results_hc, results_bt)
        
        return results_hc, results_bt
    
    def experimento2_consistencia(self):
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
        self.results['experimento2'] = {
            'hill_climbing': hc_results,
            'backtracking': bt_results,
            'estadisticas_hc': hc_stats,
            'estadisticas_bt': bt_stats
        }
        
        # Generar tabla comparativa
        self._print_experimento2_table(hc_results, bt_results, hc_stats, bt_stats)
        
        return hc_results, bt_results, hc_stats, bt_stats
    
    def experimento3_optimizacion(self):
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
        self.results['experimento3'] = {
            'hill_climbing': results_hc,
            'backtracking': results_bt
        }
        
        # Generar tablas
        self._print_experimento3_tables(results_hc, results_bt)
        
        return results_hc, results_bt
    
    def _print_experimento1_table(self, hc_results, bt_results):
        """Imprime tabla del Experimento 1."""
        print("\n" + "-"*80)
        print("TABLA EXPERIMENTO 1: ESCALABILIDAD")
        print("-"*80)
        print(f"{'n':<5} {'Algoritmo':<20} {'Tiempo (s)':<15} {'Iter/Nodos':<15} {'Memoria (MB)':<15}")
        print("-"*80)
        
        for hc, bt in zip(hc_results, bt_results):
            print(f"{hc['n']:<5} {'Hill Climbing':<20} {hc['tiempo_promedio']:<15.6f} "
                  f"{hc['iteraciones_promedio']:<15.0f} "
                  f"{hc['memoria_promedio'] if hc['memoria_promedio'] else 'N/A':<15}")
            print(f"{bt['n']:<5} {'Backtracking':<20} {bt['tiempo']:<15.6f} "
                  f"{bt['nodos_explorados']:<15} "
                  f"{bt['memoria'] if bt['memoria'] else 'N/A':<15}")
            print("-"*80)
    
    def _print_experimento2_table(self, hc_results, bt_results, hc_stats, bt_stats):
        """Imprime tabla comparativa del Experimento 2."""
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
    
    def _print_experimento3_tables(self, hc_results, bt_results):
        """Imprime tablas del Experimento 3."""
        print("\n" + "-"*80)
        print("TABLA EXPERIMENTO 3: HILL CLIMBING (Original vs. Random Restart)")
        print("-"*80)
        print(f"{'n':<5} {'Versión':<20} {'Tiempo (s)':<15} {'Iteraciones':<15} {'Solución':<10}")
        print("-"*80)
        
        for result in hc_results:
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
        
        for result in bt_results:
            print(f"{result['n']:<5} {'Original':<20} "
                  f"{result['original']['execution_time']:<15.6f} "
                  f"{result['original']['nodes_explored']:<15} "
                  f"{'Sí' if result['original']['solution_found'] else 'No':<10}")
            print(f"{result['n']:<5} {'Poda Optimizada':<20} "
                  f"{result['optimizada']['execution_time']:<15.6f} "
                  f"{result['optimizada']['nodes_explored']:<15} "
                  f"{'Sí' if result['optimizada']['solution_found'] else 'No':<10}")
            print("-"*80)
    
    def save_results_to_json(self, filename: str = "resultados_experimentos.json"):
        """Guarda los resultados en un archivo JSON."""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.results, f, indent=2, ensure_ascii=False)
        print(f"\nResultados guardados en: {filename}")
    
    def save_results_to_csv(self):
        """Guarda los resultados en archivos CSV."""
        # Experimento 1
        if self.results['experimento1']:
            with open('experimento1_escalabilidad.csv', 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['n', 'algoritmo', 'tiempo_promedio', 'iteraciones_nodos', 
                               'memoria_mb', 'solucion_encontrada'])
                for hc in self.results['experimento1']['hill_climbing']:
                    writer.writerow([hc['n'], 'Hill Climbing', hc['tiempo_promedio'], 
                                   hc['iteraciones_promedio'], hc['memoria_promedio'] or 0,
                                   hc['soluciones_encontradas'] > 0])
                for bt in self.results['experimento1']['backtracking']:
                    writer.writerow([bt['n'], 'Backtracking', bt['tiempo'], 
                                   bt['nodos_explorados'], bt['memoria'] or 0,
                                   bt['solucion_encontrada']])
        
        # Experimento 2
        if self.results['experimento2']:
            with open('experimento2_consistencia.csv', 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['ejecucion', 'algoritmo', 'tiempo', 'iteraciones_nodos', 
                               'solucion', 'solucion_encontrada'])
                for hc in self.results['experimento2']['hill_climbing']:
                    writer.writerow([hc['ejecucion'], 'Hill Climbing', hc['tiempo'], 
                                   hc['iteraciones'], hc['solucion'], hc['solucion_encontrada']])
                for bt in self.results['experimento2']['backtracking']:
                    writer.writerow([bt['ejecucion'], 'Backtracking', bt['tiempo'], 
                                   bt['nodos_explorados'], bt['solucion'], bt['solucion_encontrada']])
        
        print("\nResultados guardados en archivos CSV.")


def main():
    """Función principal que ejecuta todos los experimentos."""
    print("="*80)
    print("ANÁLISIS COMPARATIVO DE ALGORITMOS PARA EL PROBLEMA DE LAS N-REINAS")
    print("="*80)
    
    runner = ExperimentRunner()
    
    # Ejecutar experimentos
    try:
        runner.experimento1_escalabilidad()
        runner.experimento2_consistencia()
        runner.experimento3_optimizacion()
        
        # Guardar resultados
        runner.save_results_to_json()
        runner.save_results_to_csv()
        
        print("\n" + "="*80)
        print("TODOS LOS EXPERIMENTOS COMPLETADOS EXITOSAMENTE")
        print("="*80)
        
    except KeyboardInterrupt:
        print("\n\nExperimentos interrumpidos por el usuario.")
        runner.save_results_to_json()
        runner.save_results_to_csv()
    except Exception as e:
        print(f"\n\nError durante la ejecución: {e}")
        import traceback
        traceback.print_exc()
        runner.save_results_to_json()
        runner.save_results_to_csv()


if __name__ == "__main__":
    main()

