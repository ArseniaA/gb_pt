# Написать программу, которая обходит не взвешенный ориентированный граф без петель, в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).
# Примечания:
# a. граф должен храниться в виде списка смежности;
# b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.

import random


def G(n):
    G = {}
    for i in range(n):
        G[i] = set()
        edges = random.randrange(0, n - 1)
        while len(G[i]) < edges:
            edge = random.randrange(0, n)
            if edge != i:
                G[i].add(edge)
    return G


def dfs(start, G):
    is_visited = [False] * n
    is_visited[start] = True

    for i in G[start]:
        if is_visited[i] == False:
            dfs(i, G)


G(5)