"""
Algoritmo Hill Climbing para el Problema de las N-Reinas

FUENTES Y REFERENCIAS:
- Algoritmo base: Basado en el algoritmo de búsqueda local Hill Climbing
  para el problema de N-Reinas descrito en:
  - GeeksforGeeks: "N-Queen Problem | Local Search using Hill Climbing with Random Neighbour"
    URL: https://www.geeksforgeeks.org/n-queen-problem-local-search-using-hill-climbing-with-random-neighbour/
  - Autor: GeeksforGeeks contributors
  - Fecha de consulta: 2024
  - Licencia: No especificada (uso educativo)

MODIFICACIONES REALIZADAS:
- Agregada medición de tiempo de ejecución
- Agregado conteo de iteraciones/estados explorados
- Agregado soporte para diferentes tamaños de tablero (n variable)
- Implementada función de visualización opcional
- Agregado random restart como mejora (Experimento 3)
"""

import random
import time
import copy
from typing import List, Tuple, Optional


class HillClimbingNQueens:
    """Implementación del algoritmo Hill Climbing para N-Reinas."""
    
    def __init__(self, n: int, use_random_restart: bool = False, max_restarts: int = 100):
        """
        Inicializa el algoritmo Hill Climbing.
        
        Args:
            n: Tamaño del tablero (número de reinas)
            use_random_restart: Si es True, usa random restart
            max_restarts: Número máximo de reinicios aleatorios
        """
        self.n = n
        self.use_random_restart = use_random_restart
        self.max_restarts = max_restarts
        self.iterations = 0
        self.restarts = 0
        self.start_time = 0
        self.end_time = 0
    
    def generate_random_state(self) -> List[int]:
        """
        Genera un estado inicial aleatorio.
        Cada columna tiene una reina en una fila aleatoria.
        
        Returns:
            Lista donde board[i] = fila de la reina en la columna i
        """
        return [random.randint(0, self.n - 1) for _ in range(self.n)]
    
    def calculate_conflicts(self, board: List[int]) -> int:
        """
        Calcula el número de conflictos (pares de reinas que se atacan).
        
        Args:
            board: Estado del tablero
            
        Returns:
            Número de conflictos
        """
        conflicts = 0
        for i in range(self.n):
            for j in range(i + 1, self.n):
                # Misma fila
                if board[i] == board[j]:
                    conflicts += 1
                # Diagonal principal
                if board[i] - board[j] == i - j:
                    conflicts += 1
                # Diagonal secundaria
                if board[i] - board[j] == j - i:
                    conflicts += 1
        return conflicts
    
    def get_neighbors(self, board: List[int]) -> List[Tuple[List[int], int, int]]:
        """
        Genera todos los vecinos del estado actual.
        Un vecino se obtiene moviendo una reina a otra fila en su columna.
        
        Args:
            board: Estado actual del tablero
            
        Returns:
            Lista de tuplas (nuevo_estado, columna_movida, conflicto_nuevo)
        """
        neighbors = []
        current_conflicts = self.calculate_conflicts(board)
        
        for col in range(self.n):
            for row in range(self.n):
                if board[col] != row:
                    new_board = board.copy()
                    new_board[col] = row
                    new_conflicts = self.calculate_conflicts(new_board)
                    neighbors.append((new_board, col, new_conflicts))
        
        return neighbors
    
    def hill_climbing(self, initial_state: Optional[List[int]] = None) -> Tuple[List[int], bool]:
        """
        Ejecuta el algoritmo Hill Climbing.
        
        Args:
            initial_state: Estado inicial (si es None, se genera aleatoriamente)
            
        Returns:
            Tupla (mejor_estado_encontrado, encontro_solucion)
        """
        if initial_state is None:
            current_state = self.generate_random_state()
        else:
            current_state = initial_state.copy()
        
        current_conflicts = self.calculate_conflicts(current_state)
        self.iterations = 0
        
        # Si ya es solución
        if current_conflicts == 0:
            return current_state, True
        
        max_iterations = 10000  # Límite para evitar bucles infinitos
        
        while self.iterations < max_iterations:
            self.iterations += 1
            
            # Obtener vecinos
            neighbors = self.get_neighbors(current_state)
            
            # Hill Climbing: solo acepta mejoras estrictas
            # Filtrar solo vecinos mejores (menos conflictos)
            better_neighbors = [n for n in neighbors if n[2] < current_conflicts]
            if not better_neighbors:
                # No hay mejoras, estamos en un óptimo local
                break
            # Elegir aleatoriamente entre los mejores vecinos
            best_conflict = min(n[2] for n in better_neighbors)
            best_neighbors = [n for n in better_neighbors if n[2] == best_conflict]
            next_state, _, next_conflicts = random.choice(best_neighbors)
            
            # Actualizar estado
            current_state = next_state
            current_conflicts = next_conflicts
            
            # Verificar si encontramos solución
            if current_conflicts == 0:
                return current_state, True
        
        return current_state, False
    
    def solve(self, initial_state: Optional[List[int]] = None) -> Tuple[List[int], dict]:
        """
        Resuelve el problema de N-Reinas usando Hill Climbing.
        
        Args:
            initial_state: Estado inicial (opcional)
            
        Returns:
            Tupla (solución, estadísticas)
        """
        self.start_time = time.time()
        
        if self.use_random_restart:
            # Random Restart Hill Climbing
            best_solution = None
            best_conflicts = float('inf')
            total_iterations = 0
            
            for restart in range(self.max_restarts):
                self.restarts = restart + 1
                solution, found = self.hill_climbing()
                total_iterations += self.iterations
                conflicts = self.calculate_conflicts(solution)
                
                if conflicts == 0:
                    self.end_time = time.time()
                    self.iterations = total_iterations
                    return solution, {
                        'solution_found': True,
                        'iterations': total_iterations,
                        'restarts': self.restarts,
                        'execution_time': self.end_time - self.start_time,
                        'conflicts': conflicts
                    }
                
                if conflicts < best_conflicts:
                    best_conflicts = conflicts
                    best_solution = solution
            
            self.end_time = time.time()
            self.iterations = total_iterations
            return best_solution, {
                'solution_found': False,
                'iterations': total_iterations,
                'restarts': self.restarts,
                'execution_time': self.end_time - self.start_time,
                'conflicts': best_conflicts
            }
        else:
            # Hill Climbing estándar
            solution, found = self.hill_climbing(initial_state)
            self.end_time = time.time()
            
            return solution, {
                'solution_found': found,
                'iterations': self.iterations,
                'restarts': 0,
                'execution_time': self.end_time - self.start_time,
                'conflicts': self.calculate_conflicts(solution)
            }


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
    print(f"Resolviendo problema de {n}-Reinas con Hill Climbing")
    
    # Hill Climbing estándar
    hc = HillClimbingNQueens(n, use_random_restart=False)
    solution, stats = hc.solve()
    
    print(f"Solución encontrada: {stats['solution_found']}")
    print(f"Iteraciones: {stats['iterations']}")
    print(f"Tiempo de ejecución: {stats['execution_time']:.6f} segundos")
    print(f"Conflictos: {stats['conflicts']}")
    
    if stats['solution_found']:
        visualize_board(solution, n)
