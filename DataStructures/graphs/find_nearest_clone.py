#!/bin/python3

# https://www.hackerrank.com/challenges/find-the-nearest-clone/copy-from/174694788
# TC:O(E+V)
# SC:O(E+V)

import math
import os
import random
import re
import sys

# Complete the findShortest function below.

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] to <name>_to[i].
#
#
from collections import defaultdict, deque


def bfs(graph, visited, source, destination):
    visited.add(source)
    distance = [0] * len(graph)
    que = deque()
    que.append(source)

    while que:
        node = que.popleft()
        for neigh in graph[node]:
            if neigh not in visited:
                if neigh == destination:
                    return 1 + distance[node]
                que.append(neigh)
                distance[neigh] = distance[node] + 1


def findShortest(graph_nodes, graph_from, graph_to, ids, val):

    graph = defaultdict(list)
    color_map = defaultdict(int)

    for i in range(len(graph_from)):
        u = graph_from[i]
        v = graph_to[i]
        graph[u].append(v)
        graph[v].append(u)

        if graph_from[i] not in color_map:
            color_map[u] = ids[u - 1]
        if graph_to[i] not in color_map:
            color_map[v] = ids[v - 1]

    print(graph)
    print(color_map)

    visited = set()
    start_color = color_map[val]

    que = deque()
    que.append((val, 0))

    while que:
        node, dist = que.popleft()
        visited.add(node)
        for neigh in graph[node]:
            if neigh not in visited:
                if color_map[neigh] == val:
                    return 1 + dist
                que.append((neigh, dist + 1))
                visited.add(neigh)

    return -1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    graph_nodes, graph_edges = map(int, input().split())

    graph_from = [0] * graph_edges
    graph_to = [0] * graph_edges

    for i in range(graph_edges):
        graph_from[i], graph_to[i] = map(int, input().split())

    ids = list(map(int, input().rstrip().split()))

    val = int(input())

    ans = findShortest(graph_nodes, graph_from, graph_to, ids, val)

    fptr.write(str(ans) + '\n')

    fptr.close()
