from typing import List, Tuple
from collections import deque

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

GRN = '.'
WALL = '#'

DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def load_file(filename: str) -> List[str]:
    rv = []
    with open(filename, 'r') as f:
        for line in f:
            striped = line.strip('\n')
            if striped != "":
                rv.append(striped)
    return rv

def parse_line(line: str) -> Tuple[int, int, str]:
    line_lst = line.split()
    dir = NORTH
    if line[0] == 'R':
        dir = EAST
    elif line[0] == 'D':
        dir = SOUTH
    elif line[0] == 'L':
        dir = WEST

    return (dir, int(line_lst[1]), line_lst[2][1:-1])

def flood_fill(field: List[List[str]], sy: int, sx: int):
    if field[sy][sx] == WALL:
        return 0
    que = deque([])
    que.append((sy, sx))

    total = 0
    while (len(que) > 0):
        y, x = que.pop()

        for dy, dx in DIRS:
            if not (0 <= x + dx and x + dx < len(field[0]) and 0 <= y + dy and y + dy < len(field)):
               continue
            if field[y+dy][x+dx] == WALL:
                continue
            field[y+dy][x+dx] = WALL

            total += 1
            que.append((y+dy, x+dx))
    return total
    
def main() -> int:
    lst = load_file("day18_input.txt")
    instructions = []
    for line in lst:
        instructions.append(parse_line(line))
        
    for ins in instructions:
        print(ins)

    max_dirs = [0, 0, 0, 0]
    x, y = 0, 0
    occupied = set()
    for dir, step, _ in instructions:
        dy, dx = DIRS[dir]
        for _ in range(step):
            occupied.add((y, x))
            y = y + dy
            x = x + dx
        if y < max_dirs[NORTH]:
            max_dirs[NORTH] = y
        if y > max_dirs[SOUTH]:
            max_dirs[SOUTH] = y
        if x > max_dirs[EAST]:
            max_dirs[EAST] = x
        if x < max_dirs[WEST]:
            max_dirs[WEST] = x

    print(max_dirs)

    width = max_dirs[EAST] - max_dirs[WEST]
    height = max_dirs[SOUTH] - max_dirs[NORTH]

    print(height, width)
    #terrain = [['.' for _ in range(width + 1)] for _ in range(height + 1)]
    #for y, x in occupied:
    #    terrain[y - max_dirs[NORTH]][x - max_dirs[WEST]] = '#'
        
    #for line in terrain:
    #    print(''.join(line))

    #total = 0

    #for y in [0, height]:
    #    for x in range(width+1):
    #        total += flood_fill(terrain, y, x)

    #for y in range(1, height):
    #    for x in [0, width]:
    #        total += flood_fill(terrain, y, x)
    #print(total)

    return 0

print(f"result: {main()}")

