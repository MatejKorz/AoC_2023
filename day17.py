from typing import List, Optional, Tuple
from collections import deque
import heapq


NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

class Node:
    def __init__(self, val: int, y: int, x: int):
        self.val: int = val
        self.dist: int = -1
        self.discovered_from: Optional['Node'] = None
        self.discovered_step: Tuple[int, int] = (SOUTH, 1)
        self.x = x
        self.y = y

class Field:
    def __init__(self, field: List[List['Node']]):
        self.field = field
        self.height = len(field)
        self.width = len(field[0])

    def inside(self, y: int, x: int) -> bool:
        return 0 <= y and y < self.height and 0 <= x and x < self.width


    def show_route(self):
        field = [[str(self.field[fy][fx].val) for fx in range(self.width)] for fy in range(self.height)]
        y, x = self.height - 1, self.width - 1
        while y != 0 or x != 0:
            field[y][x] = '*'
            ny = self.field[y][x].discovered_from.y
            nx = self.field[y][x].discovered_from.x
            y, x = ny, nx
        for line in field:
            print(''.join(line))


def load_file(filename: str) -> List[str]:
    rv = []
    with open(filename, 'r') as f:
        for line in f:
            striped = line.strip('\n')
            if striped != "":
                rv.append(striped)
    return rv

def main() -> int:
    plan = Field([[Node(int(i), y, x) for x, i in enumerate(line)]\
        for y, line in enumerate(load_file("day17_test1.txt"))])

    for line in plan.field:
        for node in line:
            print(node.val, end='')
        print()
    print()

    que = []
    heapq.heapify(que)
    heapq.heappush(que, (0, 0, 0, SOUTH, 0))

    while (len(que) > 0):
        dist, y, x, dir, step = heapq.heappop(que)
        curr_node = plan.field[y][x]
        nxt = [(y + dy, x + dx) for dy, dx in DIRECTIONS]

        for i, tup in enumerate(nxt):
            ny, nx = tup
            if (not plan.inside(ny, nx)) or (step == 3 and dir == i):
                continue
            nxt_node: 'Node' = plan.field[ny][nx]
            if nxt_node.dist == -1 or nxt_node.dist > dist + nxt_node.val:
                nxt_node.discovered_from = curr_node
                nxt_node.dist = dist + nxt_node.val
                nxt_node.discovered_step = (i, step + 1 if dir == i else 1)
                heapq.heappush(que, (nxt_node.dist, ny, nx, i, 1 if dir != i else step + 1))
            if nxt_node != -1 and step != 3:
                heapq.heappush(que, (nxt_node.val + dist, ny, nx, i, 1 if dir != i else step + 1))



    plan.show_route()
    print(plan.field[0][0].dist)
    return plan.field[plan.height - 1][plan.width - 1].dist

print(f"result: {main()}")

