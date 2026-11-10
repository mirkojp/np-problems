# Algoritmos de Coloración de Grafos

Este proyecto contiene dos implementaciones en Python para abordar el problema de la coloración de grafos y la obtención del número cromático utilizando grafos aleatorios $G(n, p)$.

## Archivos Incluidos

### `cnumber-heuristic.py`

Este script implementa una heurística voraz secuencial (Greedy Coloring) para obtener una aproximación del número cromático utilizando listas de adyacencia con una complejidad temporal de $O(\vert{}V\vert{} + \vert{}E\vert{})$ y espacial de $O(\vert{}V\vert{})$.

**Funciones:**
*   `generar_grafo_lista_adyacencia(n, p, seed)`: Genera un grafo aleatorio $G(n, p)$ y lo representa mediante listas de adyacencia.
*   `greedy_coloring_lista(n, adj_list, p, seed)`: Ejecuta el algoritmo voraz. Recorre secuencialmente cada vértice y le asigna el primer color libre (el menor entero disponible) que no esté ocupado por ninguno de sus vecinos. Retorna la cantidad total de colores ($k$) y la lista de asignación por vértice.

### `cnumber-bf.py`

Este script calcula de forma exacta el número cromático óptimo ($\chi(G)$) utilizando fuerza bruta exhaustiva sobre una representación en matriz de adyacencia de tamaño $n \times n$.

**Funciones:**
*   `generar_grafo_aleatorio(n, p, seed)`: Genera un grafo no dirigido simple $G(n, p)$ y devuelve su matriz de adyacencia.
*   `es_coloracion_valida(adj_matrix, asignacion, n)`: Verifica en $O(n^2)$ si una asignación particular de colores respeta la restricción fundamental de que ningún par de vértices adyacentes comparta el mismo color.
*   `chromatic_number_exacto(n, p, seed)`: Evalúa incrementalmente el número de colores $k$ (desde $1$ hasta $n$). Utiliza el producto cartesiano para generar todas las asignaciones posibles de colores (de tamaño $k^n$) y usa `es_coloracion_valida` para encontrar la asignación óptima. Retorna el número cromático y la tupla de asignación.

## Ejecución

Ambos scripts funcionan con la biblioteca estándar de Python y pueden ser ejecutados de forma independiente.

```bash
python cnumber-heuristic.py
python cnumber-bf.py
```