# https://leetcode.com/problems/course-schedule-ii/
# TC: O(V+E)
# SC: O(V+E)

from collections import deque


class Solution:
    def findOrder(self, numCourses: int,
                  prerequisites: List[List[int]]) -> List[int]:

        topological_sort_order = list()

        if numCourses <= 0:
            return topological_sort_order

        in_degree_map = {x: 0 for x in range(numCourses)}
        graph = {x: [] for x in range(numCourses)}

        # build graph
        for item in prerequisites:
            parent = item[1]
            child = item[0]
            graph[parent].append(child)
            in_degree_map[child] += 1

        # build the sources
        sources = deque()
        for i in in_degree_map:
            if in_degree_map[i] == 0:
                sources.append(i)

        while sources:
            pop_item = sources.popleft()
            topological_sort_order.append(pop_item)
            for child in graph[pop_item]:
                in_degree_map[child] -= 1
                if in_degree_map[child] == 0:
                    sources.append(child)

        if len(topological_sort_order) != numCourses:
            return []

        return topological_sort_order
