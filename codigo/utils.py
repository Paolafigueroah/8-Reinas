"""
Utilidades comunes para el proyecto N-Reinas
Funciones compartidas para medir tiempo, memoria, visualización, etc.
"""

import time
import os
import sys
from typing import List, Optional, Tuple

try:
    import psutil
    MEMORY_AVAILABLE = True
except ImportError:
    MEMORY_AVAILABLE = False

try:
    import matplotlib.pyplot as plt
    import matplotlib.patches as patches
    MATPLOTLIB_AVAILABLE = True
except ImportError:
    MATPLOTLIB_AVAILABLE = False


def measure_memory(func, *args, **kwargs):
    """
    Mide el uso de memoria de una función.
    
    Args:
        func: Función a medir
        *args: Argumentos posicionales
        **kwargs: Argumentos nombrados
        
    Returns:
        Tupla (resultado, memoria_usada_mb) o (resultado, None) si no está disponible
    """
    if not MEMORY_AVAILABLE:
        return func(*args, **kwargs), None
    
    process = psutil.Process(os.getpid())
    mem_before = process.memory_info().rss / 1024 / 1024  # MB
    result = func(*args, **kwargs)
    mem_after = process.memory_info().rss / 1024 / 1024  # MB
    mem_used = mem_after - mem_before
    
    return result, max(0, mem_used)


def visualize_board_console(board: List[int], n: int):
    """
    Visualiza el tablero de N-Reinas en consola.
    
    Args:
        board: Estado del tablero (board[i] = fila de la reina en columna i)
        n: Tamaño del tablero
    """
    print("\n" + "=" * (2 * n + 1))
    for row in range(n):
        print("|", end="")
        for col in range(n):
            if board[col] == row:
                print("Q|", end="")
            else:
                print(" |", end="")
        print()
    print("=" * (2 * n + 1) + "\n")


def visualize_board_graphic(board: List[int], n: int, title: str = "Tablero de N-Reinas", 
                           save_path: Optional[str] = None):
    """
    Visualiza el tablero de N-Reinas de forma gráfica usando matplotlib.
    
    Args:
        board: Estado del tablero (board[i] = fila de la reina en columna i)
        n: Tamaño del tablero
        title: Título del gráfico
        save_path: Ruta donde guardar la imagen (opcional)
    """
    if not MATPLOTLIB_AVAILABLE:
        print("Matplotlib no está disponible. Usando visualización en consola.")
        visualize_board_console(board, n)
        return
    
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


def get_project_root():
    """
    Obtiene la ruta raíz del proyecto.
    
    Returns:
        Ruta absoluta del directorio raíz del proyecto
    """
    # Esta función asume que estamos en la estructura organizada
    # Si el archivo está en codigo/utils.py, la raíz está dos niveles arriba
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Si estamos en codigo/, subir un nivel
    if os.path.basename(current_dir) == 'codigo':
        return os.path.dirname(current_dir)
    return current_dir


def ensure_dir(directory: str):
    """
    Asegura que un directorio existe, lo crea si no existe.
    
    Args:
        directory: Ruta del directorio
    """
    os.makedirs(directory, exist_ok=True)

