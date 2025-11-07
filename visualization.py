"""
Módulo de Visualización para el Problema de las N-Reinas

Este módulo proporciona funciones para visualizar los tableros de N-Reinas
de manera gráfica usando matplotlib.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from typing import List, Optional
import numpy as np


def visualize_board(board: List[int], n: int, title: str = "Tablero de N-Reinas", 
                   save_path: Optional[str] = None):
    """
    Visualiza el tablero de N-Reinas de forma gráfica.
    
    Args:
        board: Estado del tablero (board[i] = fila de la reina en columna i)
        n: Tamaño del tablero
        title: Título del gráfico
        save_path: Ruta donde guardar la imagen (opcional)
    """
    fig, ax = plt.subplots(figsize=(8, 8))
    
    # Crear el tablero (alternando colores)
    for row in range(n):
        for col in range(n):
            color = '#F0D9B5' if (row + col) % 2 == 0 else '#B58863'
            rect = patches.Rectangle((col, n - 1 - row), 1, 1, 
                                    linewidth=1, edgecolor='black', 
                                    facecolor=color)
            ax.add_patch(rect)
    
    # Colocar las reinas
    for col in range(n):
        if 0 <= board[col] < n:
            row = board[col]
            # Dibujar círculo para la reina
            circle = patches.Circle((col + 0.5, n - 1 - row + 0.5), 
                                  0.35, linewidth=2, 
                                  edgecolor='black', facecolor='gold')
            ax.add_patch(circle)
            # Agregar símbolo de corona
            ax.text(col + 0.5, n - 1 - row + 0.5, '♕', 
                   fontsize=20, ha='center', va='center')
    
    ax.set_xlim(0, n)
    ax.set_ylim(0, n)
    ax.set_aspect('equal')
    ax.set_xticks(range(n))
    ax.set_yticks(range(n))
    ax.set_xticklabels(range(1, n + 1))
    ax.set_yticklabels(range(n, 0, -1))
    ax.set_xlabel('Columnas')
    ax.set_ylabel('Filas')
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
        print(f"Imagen guardada en: {save_path}")
    
    plt.show()


def visualize_comparison(boards: List[List[int]], n: int, 
                        titles: List[str], save_path: Optional[str] = None):
    """
    Visualiza múltiples tableros lado a lado para comparación.
    
    Args:
        boards: Lista de estados de tableros
        n: Tamaño del tablero
        titles: Lista de títulos para cada tablero
        save_path: Ruta donde guardar la imagen (opcional)
    """
    num_boards = len(boards)
    fig, axes = plt.subplots(1, num_boards, figsize=(6 * num_boards, 6))
    
    if num_boards == 1:
        axes = [axes]
    
    for idx, (board, title) in enumerate(zip(boards, titles)):
        ax = axes[idx]
        
        # Crear el tablero
        for row in range(n):
            for col in range(n):
                color = '#F0D9B5' if (row + col) % 2 == 0 else '#B58863'
                rect = patches.Rectangle((col, n - 1 - row), 1, 1, 
                                        linewidth=1, edgecolor='black', 
                                        facecolor=color)
                ax.add_patch(rect)
        
        # Colocar las reinas
        for col in range(n):
            if 0 <= board[col] < n:
                row = board[col]
                circle = patches.Circle((col + 0.5, n - 1 - row + 0.5), 
                                      0.35, linewidth=2, 
                                      edgecolor='black', facecolor='gold')
                ax.add_patch(circle)
                ax.text(col + 0.5, n - 1 - row + 0.5, '♕', 
                       fontsize=20, ha='center', va='center')
        
        ax.set_xlim(0, n)
        ax.set_ylim(0, n)
        ax.set_aspect('equal')
        ax.set_xticks(range(n))
        ax.set_yticks(range(n))
        ax.set_title(title, fontsize=12, fontweight='bold')
        ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
        print(f"Imagen guardada en: {save_path}")
    
    plt.show()


if __name__ == "__main__":
    # Ejemplo de uso
    from backtracking import BacktrackingNQueens
    
    n = 8
    bt = BacktrackingNQueens(n)
    solution, _ = bt.solve()
    
    if solution:
        visualize_board(solution, n, f"Solución para {n}-Reinas (Backtracking)")
