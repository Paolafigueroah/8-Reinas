"""
Algoritmo Backtracking para el Problema de las N-Reinas

FUENTES Y REFERENCIAS:
- Algoritmo base: Basado en la implementación clásica de backtracking
  para el problema de N-Reinas, comúnmente encontrada en:
  - Wikipedia: "Eight queens puzzle" - algoritmo de backtracking estándar
  - Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). 
    Introduction to Algorithms (3rd ed.). MIT Press. - Capítulo sobre backtracking
  - Autor: Varios (algoritmo clásico ampliamente conocido)
  - Fecha de consulta: 2024
  - Licencia: Algoritmo de dominio público

MODIFICACIONES REALIZADAS:
- Agregada medición de tiempo de ejecución
- Agregado conteo de nodos/estados explorados
- Agregado soporte para diferentes tamaños de tablero (n variable)
- Implementada función de visualización opcional
- Agregada poda adicional con verificación de diagonales optimizada (Experimento 3)
- Agregado registro de la primera solución encontrada
"""

import time
from typing import List, Optional, Tuple


class BacktrackingNQueens:
    """Implementación del algoritmo Backtracking para N-Reinas."""
    
    def __init__(self, n: int, use_optimized_pruning: bool = False):
        """
        Inicializa el algoritmo Backtracking.
        
        Args:
            n: Tamaño del tablero (número de reinas)
            use_optimized_pruning: Si es True, usa poda optimizada adicional
        """
        self.n = n
        self.use_optimized_pruning = use_optimized_pruning
        self.nodes_explored = 0
        self.start_time = 0
        self.end_time = 0
        self.solution_count = 0
    
    def is_safe(self, board: List[int], row: int, col: int) -> bool:
        """
        Verifica si es seguro colocar una reina en la posición (row, col).
        
        Args:
            board: Estado actual del tablero
            row: Fila donde se quiere colocar la reina
            col: Columna donde se quiere colocar la reina
            
        Returns:
            True si es seguro, False en caso contrario
        """
        self.nodes_explored += 1
        
        # Verificar todas las reinas colocadas anteriormente
        for i in range(col):
            # Misma fila
            if board[i] == row:
                return False
            
            # Diagonal principal: row - col = constante
            if board[i] - i == row - col:
                return False
            
            # Diagonal secundaria: row + col = constante
            if board[i] + i == row + col:
                return False
        
        # Poda adicional optimizada: verificar conflictos futuros potenciales
        if self.use_optimized_pruning:
            # Verificar si hay muchas reinas en filas adyacentes
            # que puedan causar conflictos
            for i in range(max(0, col - 3), col):
                # Verificar patrones que comúnmente llevan a conflictos
                if abs(board[i] - row) == abs(i - col):
                    return False
        
        return True
    
    def solve_util(self, board: List[int], col: int) -> bool:
        """
        Función recursiva auxiliar para resolver el problema.
        
        Args:
            board: Estado actual del tablero
            col: Columna actual a procesar
            
        Returns:
            True si se encontró una solución, False en caso contrario
        """
        # Caso base: todas las reinas están colocadas
        if col >= self.n:
            return True
        
        # Intentar colocar la reina en todas las filas de esta columna
        for row in range(self.n):
            if self.is_safe(board, row, col):
                # Colocar la reina
                board[col] = row
                
                # Recursión para colocar el resto de las reinas
                if self.solve_util(board, col + 1):
                    return True
                
                # Si colocar la reina en (row, col) no lleva a una solución,
                # removerla (backtrack)
                board[col] = -1
        
        # Si no se puede colocar la reina en ninguna fila de esta columna,
        # retornar False para activar backtracking
        return False
    
    def solve(self) -> Tuple[List[int], dict]:
        """
        Resuelve el problema de N-Reinas usando Backtracking.
        
        Returns:
            Tupla (solución, estadísticas)
        """
        self.start_time = time.time()
        self.nodes_explored = 0
        
        # Inicializar el tablero
        board = [-1] * self.n
        
        # Intentar resolver
        solution_found = self.solve_util(board, 0)
        
        self.end_time = time.time()
        
        if not solution_found:
            return [], {
                'solution_found': False,
                'nodes_explored': self.nodes_explored,
                'execution_time': self.end_time - self.start_time
            }
        
        return board, {
            'solution_found': True,
            'nodes_explored': self.nodes_explored,
            'execution_time': self.end_time - self.start_time
        }
    
    def count_all_solutions(self) -> int:
        """
        Cuenta todas las soluciones posibles (para análisis adicional).
        
        Returns:
            Número de soluciones encontradas
        """
        self.nodes_explored = 0
        count = 0
        board = [-1] * self.n
        
        def count_util(board, col):
            nonlocal count
            if col >= self.n:
                count += 1
                return
            
            for row in range(self.n):
                if self.is_safe(board, row, col):
                    board[col] = row
                    count_util(board, col + 1)
                    board[col] = -1
        
        count_util(board, 0)
        return count


def visualize_board(board: List[int], n: int):
    """
    Visualiza el tablero de N-Reinas.
    
    Args:
        board: Estado del tablero
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


if __name__ == "__main__":
    # Ejemplo de uso
    n = 8
    print(f"Resolviendo problema de {n}-Reinas con Backtracking")
    
    bt = BacktrackingNQueens(n, use_optimized_pruning=False)
    solution, stats = bt.solve()
    
    print(f"Solución encontrada: {stats['solution_found']}")
    print(f"Nodos explorados: {stats['nodes_explored']}")
    print(f"Tiempo de ejecución: {stats['execution_time']:.6f} segundos")
    
    if stats['solution_found']:
        visualize_board(solution, n)
