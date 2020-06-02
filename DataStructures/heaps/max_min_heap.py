from heapq import *


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_point(self):
        print("[" + str(self.x) + ", " + str(self.y) + "] ", end='')

    def distance_from_origin(self):
        # ignoring sqrt to calculate the distance
        return (self.x * self.x) + (self.y * self.y)


def find_closest_points(points, k):
    result = []

    for p in range(k):
        dist = points[p].distance_from_origin()
        heappush(result, (dist, points[p]))
        print(result)
        import pdb
        pdb.set_trace()

    for p in range(k, len(points) - 1):
        d1 = p.distance_from_origin()
        if d1 < result[0][0]:
            heappop(result)
            heappush(result, (d1, p))

    return result


def main():
    result = find_closest_points([Point(1, 3), Point(3, 4), Point(2, -1)], 2)
    print("Here are the k points closest the origin: ", end='')
    for point in result:
        point.print_point()


main()
