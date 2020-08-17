#!/bin/python3

# https://www.hackerrank.com/challenges/torque-and-development
# TC: O(E+V)
# SC: O(E+V)
import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the roadsAndLibraries function below.


def dfs(node, visited, graph):
    visited.add(node)
    ans = 1
    if node in graph:
        for neigh in graph[node]:
            if neigh not in visited:
                ans += dfs(neigh, visited, graph)
    return ans


def roadsAndLibraries(n, c_lib, c_road, cities):
    if c_lib < c_road:
        return n * c_lib

    visited = set()
    graph = defaultdict(list)

    for u, v in cities:
        graph[u].append(v)
        graph[v].append(u)

    connected_components = dict()
    """
    print(cities)
    print('graph is ' + str(graph))
    print('n is ' + str(n))
    print ('m is ' + str(m))
    """
    for i in range(1, n + 1):
        if i not in visited:
            print('doing dfs on ' + str(i))
            dfs_result = (dfs(i, visited, graph))
            connected_components[i] = dfs_result

    roads = 0

    for k, v in connected_components.items():
        roads = roads + v - 1

    cost_roads = roads * c_road
    cost_lib = len(connected_components) * c_lib
    """
    print('connected_component is ' + str(connected_components))
    print('roads' + str(roads))
    print('cost-roads ' + str(cost_roads) + ' cost_lib ' + str(cost_lib))
    """
    return cost_roads + cost_lib


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nmC_libC_road = input().split()

        n = int(nmC_libC_road[0])

        m = int(nmC_libC_road[1])

        c_lib = int(nmC_libC_road[2])

        c_road = int(nmC_libC_road[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        fptr.write(str(result) + '\n')

    fptr.close()
