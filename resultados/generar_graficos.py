"""
Script para generar gráficos a partir de los resultados de los experimentos.
Este script lee los resultados de experimentos/resultados_brutos/ y genera gráficos
comparativos para incluir en el reporte técnico.
"""

import sys
import json
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# Agregar el directorio raíz al path
sys.path.insert(0, str(Path(__file__).parent.parent))

from codigo.utils import ensure_dir

# Rutas
BASE_DIR = Path(__file__).parent.parent
RESULTS_DIR = BASE_DIR / "experimentos" / "resultados_brutos"
GRAPHS_DIR = BASE_DIR / "resultados" / "graficas"
ensure_dir(str(GRAPHS_DIR))


def cargar_resultados():
    """Carga los resultados desde los archivos JSON."""
    resultados = {}
    
    # Cargar Experimento 1
    exp1_path = RESULTS_DIR / "exp1_resultados.json"
    if exp1_path.exists():
        with open(exp1_path, 'r', encoding='utf-8') as f:
            exp1 = json.load(f)
            resultados.update(exp1)
    
    # Cargar Experimento 2
    exp2_path = RESULTS_DIR / "exp2_resultados.json"
    if exp2_path.exists():
        with open(exp2_path, 'r', encoding='utf-8') as f:
            exp2 = json.load(f)
            resultados.update(exp2)
    
    # Cargar Experimento 3
    exp3_path = RESULTS_DIR / "exp3_resultados.json"
    if exp3_path.exists():
        with open(exp3_path, 'r', encoding='utf-8') as f:
            exp3 = json.load(f)
            resultados.update(exp3)
    
    # Si existe archivo combinado, intentar cargarlo
    combined_path = RESULTS_DIR / "resultados_combinados.json"
    if combined_path.exists():
        with open(combined_path, 'r', encoding='utf-8') as f:
            resultados = json.load(f)
    
    return resultados if resultados else None


def grafico_escalabilidad(resultados):
    """Genera gráfico de escalabilidad (Experimento 1)."""
    if not resultados or 'experimento1' not in resultados:
        print("No hay datos del Experimento 1")
        return
    
    exp1 = resultados['experimento1']
    hc_data = exp1['hill_climbing']
    bt_data = exp1['backtracking']
    
    # Extraer datos
    n_values = [d['n'] for d in hc_data]
    hc_times = [d['tiempo_promedio'] for d in hc_data]
    bt_times = [d['tiempo'] for d in bt_data]
    
    # Crear gráfico
    plt.figure(figsize=(10, 6))
    plt.plot(n_values, hc_times, 'o-', label='Hill Climbing', linewidth=2, markersize=8)
    plt.plot(n_values, bt_times, 's-', label='Backtracking', linewidth=2, markersize=8)
    plt.xlabel('Tamaño del Tablero (N)', fontsize=12)
    plt.ylabel('Tiempo de Ejecución (segundos)', fontsize=12)
    plt.title('Experimento 1: Escalabilidad - Tiempo de Ejecución', fontsize=14, fontweight='bold')
    plt.legend(fontsize=11)
    plt.grid(True, alpha=0.3)
    plt.yscale('log')  # Escala logarítmica para mejor visualización
    plt.tight_layout()
    plt.savefig(GRAPHS_DIR / 'tiempo_vs_n.png', dpi=300, bbox_inches='tight')
    print(f"Gráfico guardado: {GRAPHS_DIR / 'tiempo_vs_n.png'}")
    plt.close()
    
    # Gráfico de iteraciones/nodos
    hc_iters = [d['iteraciones_promedio'] for d in hc_data]
    bt_nodes = [d['nodos_explorados'] for d in bt_data]
    
    plt.figure(figsize=(10, 6))
    plt.plot(n_values, hc_iters, 'o-', label='Hill Climbing (Iteraciones)', linewidth=2, markersize=8)
    plt.plot(n_values, bt_nodes, 's-', label='Backtracking (Nodos)', linewidth=2, markersize=8)
    plt.xlabel('Tamaño del Tablero (N)', fontsize=12)
    plt.ylabel('Iteraciones / Nodos Explorados', fontsize=12)
    plt.title('Experimento 1: Escalabilidad - Estados Explorados', fontsize=14, fontweight='bold')
    plt.legend(fontsize=11)
    plt.grid(True, alpha=0.3)
    plt.yscale('log')
    plt.tight_layout()
    plt.savefig(GRAPHS_DIR / 'iteraciones_vs_n.png', dpi=300, bbox_inches='tight')
    print(f"Gráfico guardado: {GRAPHS_DIR / 'iteraciones_vs_n.png'}")
    plt.close()


def grafico_consistencia(resultados):
    """Genera gráfico de consistencia (Experimento 2)."""
    if not resultados or 'experimento2' not in resultados:
        print("No hay datos del Experimento 2")
        return
    
    exp2 = resultados['experimento2']
    hc_data = exp2['hill_climbing']
    bt_data = exp2['backtracking']
    
    # Extraer datos
    ejecuciones = [d['ejecucion'] for d in hc_data]
    hc_times = [d['tiempo'] for d in hc_data]
    bt_times = [d['tiempo'] for d in bt_data]
    
    # Crear gráfico
    plt.figure(figsize=(12, 6))
    plt.plot(ejecuciones, hc_times, 'o-', label='Hill Climbing', linewidth=2, markersize=6, alpha=0.7)
    plt.plot(ejecuciones, bt_times, 's-', label='Backtracking', linewidth=2, markersize=6, alpha=0.7)
    plt.axhline(y=exp2['estadisticas_hc']['tiempo_promedio'], 
                color='blue', linestyle='--', alpha=0.5, label='Promedio HC')
    plt.axhline(y=exp2['estadisticas_bt']['tiempo_promedio'], 
                color='orange', linestyle='--', alpha=0.5, label='Promedio BT')
    plt.xlabel('Ejecución', fontsize=12)
    plt.ylabel('Tiempo de Ejecución (segundos)', fontsize=12)
    plt.title('Experimento 2: Consistencia - Variabilidad Temporal (n=8)', fontsize=14, fontweight='bold')
    plt.legend(fontsize=11)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(GRAPHS_DIR / 'consistencia_tiempo.png', dpi=300, bbox_inches='tight')
    print(f"Gráfico guardado: {GRAPHS_DIR / 'consistencia_tiempo.png'}")
    plt.close()


def grafico_optimizacion(resultados):
    """Genera gráfico de optimización (Experimento 3)."""
    if not resultados or 'experimento3' not in resultados:
        print("No hay datos del Experimento 3")
        return
    
    exp3 = resultados['experimento3']
    hc_data = exp3['hill_climbing']
    bt_data = exp3['backtracking']
    
    # Hill Climbing
    n_values = [d['n'] for d in hc_data]
    hc_orig_times = [d['original']['execution_time'] for d in hc_data]
    hc_rr_times = [d['random_restart']['execution_time'] for d in hc_data]
    
    plt.figure(figsize=(10, 6))
    x = np.arange(len(n_values))
    width = 0.35
    
    plt.bar(x - width/2, hc_orig_times, width, label='Original', alpha=0.7, edgecolor='black')
    plt.bar(x + width/2, hc_rr_times, width, label='Random Restart', alpha=0.7, edgecolor='black')
    plt.xlabel('Tamaño del Tablero (N)', fontsize=12)
    plt.ylabel('Tiempo de Ejecución (segundos)', fontsize=12)
    plt.title('Experimento 3: Hill Climbing - Original vs. Random Restart', fontsize=14, fontweight='bold')
    plt.xticks(x, n_values)
    plt.legend(fontsize=11)
    plt.grid(True, alpha=0.3, axis='y')
    plt.tight_layout()
    plt.savefig(GRAPHS_DIR / 'optimizacion_hc.png', dpi=300, bbox_inches='tight')
    print(f"Gráfico guardado: {GRAPHS_DIR / 'optimizacion_hc.png'}")
    plt.close()
    
    # Backtracking
    bt_orig_times = [d['original']['execution_time'] for d in bt_data]
    bt_opt_times = [d['optimizada']['execution_time'] for d in bt_data]
    bt_orig_nodes = [d['original']['nodes_explored'] for d in bt_data]
    bt_opt_nodes = [d['optimizada']['nodes_explored'] for d in bt_data]
    
    plt.figure(figsize=(10, 6))
    plt.bar(x - width/2, bt_orig_times, width, label='Original', alpha=0.7, edgecolor='black')
    plt.bar(x + width/2, bt_opt_times, width, label='Poda Optimizada', alpha=0.7, edgecolor='black')
    plt.xlabel('Tamaño del Tablero (N)', fontsize=12)
    plt.ylabel('Tiempo de Ejecución (segundos)', fontsize=12)
    plt.title('Experimento 3: Backtracking - Original vs. Poda Optimizada', fontsize=14, fontweight='bold')
    plt.xticks(x, n_values)
    plt.legend(fontsize=11)
    plt.grid(True, alpha=0.3, axis='y')
    plt.tight_layout()
    plt.savefig(GRAPHS_DIR / 'optimizacion_bt.png', dpi=300, bbox_inches='tight')
    print(f"Gráfico guardado: {GRAPHS_DIR / 'optimizacion_bt.png'}")
    plt.close()


def main():
    """Función principal."""
    print("="*60)
    print("GENERADOR DE GRÁFICOS PARA EXPERIMENTOS N-REINAS")
    print("="*60)
    
    resultados = cargar_resultados()
    if not resultados:
        print("Error: No se encontraron archivos de resultados")
        print(f"Busca en: {RESULTS_DIR}")
        return
    
    print("\nGenerando gráficos...")
    grafico_escalabilidad(resultados)
    grafico_consistencia(resultados)
    grafico_optimizacion(resultados)
    
    print("\n" + "="*60)
    print("TODOS LOS GRÁFICOS GENERADOS EXITOSAMENTE")
    print(f"Gráficos guardados en: {GRAPHS_DIR}")
    print("="*60)


if __name__ == "__main__":
    main()

