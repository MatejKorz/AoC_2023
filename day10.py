from typing import List, Tuple
from collections import deque

VERTICAL = '|'
HORIZONTAL = '-'
NORTHEAST = 'L'
NORTHWEST = 'J'
SOUTHWEST = '7'
SOUTHEAST = 'F'
GROUND = '.'
START = 'S'
UNKNOWN = 'x'

class Pipe:
    def __init__(self, x: int, y: int, kind) -> None:
        self.x = x
        self.y = y
        self.dist = -1
        self.kind = kind

    def connections(self) -> List[Tuple[int, int]]:
        if self.kind == VERTICAL:
            return [(-1, 0), (1, 0)]
        elif self.kind == HORIZONTAL:
            return [(0, -1), (0, 1)]
        elif self.kind == NORTHEAST:
            return [(-1, 0), (0, 1)]
        elif self.kind == NORTHWEST:
            return [(-1, 0), (0, -1)]
        elif self.kind == SOUTHEAST:
            return [(1, 0), (0, 1)]
        elif self.kind == SOUTHWEST:
            return [(1, 0), (0, -1)]
        elif self.kind == START:
            return [(-1, 0), (1, 0), (0, -1), (0, 1)]
        return []


class PipeMap:
    def __init__(self, height: int, width: int) -> None:
        self.height = height
        self.width = width
        self.field: List[List[Pipe]] = [[Pipe(x, y, UNKNOWN) for x in range(width)] for y in range(height)]

    def show(self) -> None:
        for row in self.field:
            for item in row:
                print(item.kind, end='')
            print()
        print()

    def show_dist(self) -> None:
        for row in self.field:
            for item in row:
                print(item.dist if item.kind != GROUND else '_', end='')
            print()
        print()

    def connected_neighbours(self, x: int, y:int) -> List[Pipe]:
        connencted = self.field[y][x].connections()
        rv = []
        for dy, dx in connencted:
            if 0 <= x + dx and x + dx < self.width and 0 <= y + dy and y + dy < self.height:
                neigh_connect = self.field[y+dy][x+dx].connections()
                is_connected = False
                for neigh_dy, neigh_dx in neigh_connect:
                    if dx + neigh_dx == 0 and dy + neigh_dy == 0:
                        is_connected = True
                        break
                if is_connected:
                    rv.append(self.field[y+dy][x+dx])
        return rv


def load_file(filename: str) -> List[str]:
    rv = []
    with open(filename, 'r') as f:
        for line in f:
            striped = line.strip('\n')
            if striped != "":
                rv.append(striped)
    return rv


def eval_pipes(pipe_map: PipeMap, start: Tuple[int, int]) -> int:
    start_y, start_x = start
    pipe_map.field[start_y][start_x].dist = 0
    que = deque([])
    que.append(pipe_map.field[start_y][start_x])

    max_eval = 0

    while len(que) > 0:
        pipe = que.popleft()
        neightbours = pipe_map.connected_neighbours(pipe.x, pipe.y)

        for neihg in neightbours:
            if neihg.dist == -1:
                neihg.dist = pipe.dist + 1
                if (pipe.dist + 1 > max_eval):
                    max_eval = pipe.dist + 1
                que.append(neihg)

    #pipe_map.show_dist()
    return max_eval

def main() -> int:
    filename = "day10_input.txt"
    lst = load_file(filename)
    pipe_map = PipeMap(len(lst), len(lst[0]))
    start_pos = (-1, -1)
    for y, line in enumerate(lst):
        for x, char in enumerate(line):
            pipe_map.field[y][x].kind = char
            if char == START:
                start_pos = (y, x)

    pipe_map.show()
    print(start_pos)

    return eval_pipes(pipe_map, start_pos)

print(f"result: {main()}")
