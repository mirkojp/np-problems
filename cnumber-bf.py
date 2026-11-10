import itertools
import random
import time
from typing import List, Tuple


def generar_grafo_aleatorio(n: int, p: float = 0.5, seed: int = 1):
    """
    Genera un grafo no dirigido simple G(n, p)
    Representado como matriz de adyacencia n x n.
    """
    if seed is not None:
        random.seed(seed)
        
    adj_matrix = [[0] * n for _ in range(n)]
    for u in range(n):
        for v in range(u + 1, n):
            if random.random() < p:
                adj_matrix[u][v] = 1
                adj_matrix[v][u] = 1
    return adj_matrix


def es_coloracion_valida(adj_matrix: List[List[int]], asignacion: Tuple[int, ...], n: int):
    """
    Verifica en O(n^2) si una asignación particular de colores respeta
    la restricción de que vértices adyacentes tengan distinto color.
    """
    for u in range(n):
        for v in range(u + 1, n):
            if adj_matrix[u][v] == 1 and asignacion[u] == asignacion[v]:
                return False
    return True


def chromatic_number_exacto(n: int, p: float = 0.5, seed: int = 1) -> Tuple[int, Tuple[int, ...]]:
    """
    Calcula de forma exacta chi(G) mediante fuerza bruta exhaustiva.
    
    Parámetros:
      - n: número de vértices (parámetro mínimo requerido).
      - adj_matrix: matriz de adyacencia (opcional). Si es None, genera una aleatoria.
      - p: probabilidad de arista si se genera matriz aleatoria.
      
    Retorna:
      - chi: número cromático óptimo.
      - mejor_coloracion: tupla con los colores asignados a cada vértice (índices 0 a n-1).
    """

    adj_matrix = generar_grafo_aleatorio(n, p, seed)
        
    # El número cromático k varía entre 1 (grafo sin aristas) y n (grafo completo Kn)
    for k in range(1, n + 1):
        # itertools.product genera el producto cartesiano {0, ..., k-1}^n (tamaño k^n)
        for asignacion in itertools.product(range(k), repeat=n):
            if es_coloracion_valida(adj_matrix, asignacion, n):
                return k, asignacion

    return n, tuple(range(n))


if __name__ == "__main__":
    n = 5

    t0 = time.perf_counter()
    chi, coloracion = chromatic_number_exacto(n=n, p=0.5, seed=42+n)
    t1 = time.perf_counter()

    print(f"Número de vértices: {n}")
    print(f"Número cromático óptimo (chi): {chi}")
    print(f"Asignación de colores por vértice: {coloracion}")
    print(f"Tiempo total de ejecución: {t1 - t0:.4f} segundos")