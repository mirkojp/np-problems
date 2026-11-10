import random
import time
from typing import List, Tuple, Optional


def generar_grafo_lista_adyacencia(
    n: int, p: float = 0.5, seed: Optional[int] = 1
):
    """
    Genera un grafo G(n, p) representado mediante listas de adyacencia.
    """
    if seed is not None:
        random.seed(seed)

    adj_list: List[List[int]] = [[] for _ in range(n)]
    for u in range(n):
        for v in range(u + 1, n):
            if random.random() < p:
                adj_list[u].append(v)
                adj_list[v].append(u)
    return adj_list


def greedy_coloring_lista(
    n: int,
    adj_list: Optional[List[List[int]]] = None,
    p: float = 0.5,
    seed: Optional[int] = 1,
):
    """
    Heurística voraz secuencial (Greedy Coloring) sobre listas de adyacencia.
    Complejidad temporal: O(|V| + |E|).
    Complejidad espacial auxiliar: O(|V|).

    Retorna:
      - k_colores: cantidad total de colores utilizados.
      - asignacion: lista donde asignacion[v] es el color asignado al vértice v.
    """
    if adj_list is None:
        adj_list = generar_grafo_lista_adyacencia(n, p, seed=seed)

    if n == 0:
        return 0, []

    # asignacion[v] = -1 significa que el vértice no fue coloreado aún
    asignacion = [-1] * n
    asignacion[0] = 0

    # Arreglo para registrar qué colores ya fueron tomados por los vecinos inmediatos
    colores_ocupados = [False] * n

    for u in range(1, n):
        # 1. Marcar colores ocupados solo por los vecinos reales de u
        for vecino in adj_list[u]:
            color_vecino = asignacion[vecino]
            if color_vecino != -1:
                colores_ocupados[color_vecino] = True

        # 2. Encontrar el primer color libre (el menor entero disponible)
        color_libre = 0
        while colores_ocupados[color_libre]:
            color_libre += 1

        asignacion[u] = color_libre

        # 3. Limpiar marcas únicamente para los colores de sus vecinos
        for vecino in adj_list[u]:
            color_vecino = asignacion[vecino]
            if color_vecino != -1:
                colores_ocupados[color_vecino] = False

    k_colores = max(asignacion) + 1
    return k_colores, asignacion


if __name__ == "__main__":
    n = 10000
    print(f"Generando y coloreando grafo para n = {n}")

    
    t0 = time.perf_counter()
    k, sol = greedy_coloring_lista(n=n, p=0.5, seed=42+n)
    t1 = time.perf_counter()

    print(f"Colores utilizados (k): {k}")
    print(f"Tiempo total de ejecución: {t1 - t0:.4f} segundos")
