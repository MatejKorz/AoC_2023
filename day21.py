from collections import deque, namedtuple

ROCK = '#'
SOIL = '.'
START = 'S'

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

Pos = namedtuple('Pos', 'y x step') 

def load_file(filename: str) -> list[str]:
    rv = []
    with open(filename, 'r') as f:
        for line in f:
            striped = line.strip('\n')
            rv.append(striped)
    return rv

def main() -> int:
    field: list[str] = load_file("day21_input.txt")
    steps = 0
    que = deque([])
    odd: set[tuple[int, int]] = set()
    even: set[tuple[int, int]] = set()
    height = len(field)
    width = len(field[0])

    for line in field:
        print(line)
    print()

    for y in range(len(field)):
        x = field[y].find(START)
        if x != -1:
            que.append(Pos(y, x, 0))
            break

    while len(que) > 0 and steps <= 63:
        pos = que.popleft()
        steps = pos.step
        for dy, dx in DIRS:
            ny = pos.y + dy
            nx = pos.x + dx
            if not (0 <= nx and nx < width and 0 <= ny and ny < height) or field[ny][nx] == ROCK:
                continue
            
            if pos.step % 2 == 0 and (ny, nx) not in odd:
                odd.add((ny, nx))
                que.append(Pos(ny, nx, pos.step + 1))
            elif pos.step % 2 == 1 and (ny, nx) not in even:
                even.add((ny, nx))
                que.append(Pos(ny, nx, pos.step + 1))


    for y, line in enumerate(field):
        for x, char in enumerate(line):
            if (y, x) in even:
                print('O', end='')
            else:
                print(char, end='')
        print()
    print(f"even: {len(even)}")


    for y, line in enumerate(field):
        for x, char in enumerate(line):
            if (y, x) in odd:
                print('O', end='')
            else:
                print(char, end='')
        print()
    print(f"odd: {len(odd)}")

    return len(even)

print(f"result: {main()}")
