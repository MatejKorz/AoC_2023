from collections import namedtuple
import sys

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

PATH = '.'
FOREST = '#'
SLOPES = '^>v<'

Pos = namedtuple('Pos', 'y x') 

class Field():
    def __init__(self, field) -> None:
        self.map: list[str] = field
        self.height: int = len(field)
        self.width: int = len(field[0])
        self.start: 'Pos' = Pos(0, 1)
        self.end: 'Pos' = Pos(self.height - 1, self.width - 2)

    def inside(self, y: int, x: int) -> bool:
        return 0 <= y and y < self.height and 0 <= x and x < self.width


def load_file(filename: str) -> list[str]:
    rv = []
    with open(filename, 'r') as f:
        for line in f:
            striped = line.strip('\n')
            rv.append(striped)
    return rv

def dfs_maze(field: 'Field', visited: set[tuple[int,int]], pos: 'Pos', length: int) -> int:
    if pos.x == field.end.x and pos.y == field.end.y:
        return length

    is_sloped = SLOPES.find(field.map[pos.y][pos.x])

    if is_sloped != -1:
        dy, dx = DIRS[is_sloped]
        if (pos.y+dy, pos.x+dx) not in visited:
            visited.add((pos.y+dy,pos.x+dx))
            rv = dfs_maze(field, visited, Pos(pos.y + dy, pos.x + dx), length + 1)
            visited.remove((pos.y+dy,pos.x+dx))
            return rv
    else:
        rv = -1
        for dy, dx in DIRS:
            nx = pos.x + dx
            ny = pos.y + dy
            if field.inside(ny, nx) and field.map[ny][nx] != FOREST and (ny,nx) not in visited:
                visited.add((ny,nx))
                rv = max(rv, dfs_maze(field, visited, Pos(ny, nx), length + 1))
                visited.remove((ny,nx))
        return rv
    return -1     

def main() -> int:
    field: 'Field' = Field(load_file("day23_input.txt"))
    for line in field.map:
        print(line)
    sys.setrecursionlimit(20000) 
    return dfs_maze(field, set(), Pos(0, 1), 0)
    
print(f"result: {main()}")
    
