"""
Script para generar gráficos a partir de los resultados de los experimentos.
Este script lee los resultados de resultados_experimentos.json y genera gráficos
comparativos para incluir en el reporte técnico.
"""

import json
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

def cargar_resultados(archivo='resultados_experimentos.json'):
    """Carga los resultados desde un archivo JSON."""
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {archivo}")
        print("Ejecuta primero los experimentos con: python experiments.py")
        return None

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
    plt.savefig('grafico_escalabilidad_tiempo.png', dpi=300, bbox_inches='tight')
    print("Gráfico guardado: grafico_escalabilidad_tiempo.png")
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
    plt.savefig('grafico_escalabilidad_estados.png', dpi=300, bbox_inches='tight')
    print("Gráfico guardado: grafico_escalabilidad_estados.png")
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
    plt.savefig('grafico_consistencia_tiempo.png', dpi=300, bbox_inches='tight')
    print("Gráfico guardado: grafico_consistencia_tiempo.png")
    plt.close()
    
    # Gráfico de barras para comparar variabilidad
    hc_std = exp2['estadisticas_hc']['tiempo_desv_est']
    bt_std = exp2['estadisticas_bt']['tiempo_desv_est']
    hc_mean = exp2['estadisticas_hc']['tiempo_promedio']
    bt_mean = exp2['estadisticas_bt']['tiempo_promedio']
    
    plt.figure(figsize=(8, 6))
    algorithms = ['Hill Climbing', 'Backtracking']
    means = [hc_mean, bt_mean]
    stds = [hc_std, bt_std]
    colors = ['blue', 'orange']
    
    bars = plt.bar(algorithms, means, yerr=stds, capsize=10, color=colors, alpha=0.7, edgecolor='black')
    plt.ylabel('Tiempo de Ejecución (segundos)', fontsize=12)
    plt.title('Experimento 2: Comparación de Consistencia Temporal', fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3, axis='y')
    plt.tight_layout()
    plt.savefig('grafico_consistencia_comparacion.png', dpi=300, bbox_inches='tight')
    print("Gráfico guardado: grafico_consistencia_comparacion.png")
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
    plt.savefig('grafico_optimizacion_hc.png', dpi=300, bbox_inches='tight')
    print("Gráfico guardado: grafico_optimizacion_hc.png")
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
    plt.savefig('grafico_optimizacion_bt_tiempo.png', dpi=300, bbox_inches='tight')
    print("Gráfico guardado: grafico_optimizacion_bt_tiempo.png")
    plt.close()
    
    plt.figure(figsize=(10, 6))
    plt.bar(x - width/2, bt_orig_nodes, width, label='Original', alpha=0.7, edgecolor='black')
    plt.bar(x + width/2, bt_opt_nodes, width, label='Poda Optimizada', alpha=0.7, edgecolor='black')
    plt.xlabel('Tamaño del Tablero (N)', fontsize=12)
    plt.ylabel('Nodos Explorados', fontsize=12)
    plt.title('Experimento 3: Backtracking - Nodos Explorados', fontsize=14, fontweight='bold')
    plt.xticks(x, n_values)
    plt.legend(fontsize=11)
    plt.grid(True, alpha=0.3, axis='y')
    plt.tight_layout()
    plt.savefig('grafico_optimizacion_bt_nodos.png', dpi=300, bbox_inches='tight')
    print("Gráfico guardado: grafico_optimizacion_bt_nodos.png")
    plt.close()

def main():
    """Función principal."""
    print("="*60)
    print("GENERADOR DE GRÁFICOS PARA EXPERIMENTOS N-REINAS")
    print("="*60)
    
    resultados = cargar_resultados()
    if not resultados:
        return
    
    print("\nGenerando gráficos...")
    grafico_escalabilidad(resultados)
    grafico_consistencia(resultados)
    grafico_optimizacion(resultados)
    
    print("\n" + "="*60)
    print("TODOS LOS GRÁFICOS GENERADOS EXITOSAMENTE")
    print("="*60)

if __name__ == "__main__":
    main()

