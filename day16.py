from collections import deque

SPLITER_VER = '|'
SPLITER_HOR = '-'
MIRROR_SW = '\\'
MIRROR_SE = '/'
GROUND = '.'

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3
ORIENTATION = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def load_file(filename: str):
    rv = []
    with open(filename, 'r') as f:
        for line in f:
            striped = line.strip('\n')
            if striped != "":
                rv.append(striped)
    return rv


def main() -> int:
    filename = "day16_input.txt"
    field = load_file(filename)
    total = -1

    indexes = []
    for i in range(len(field)):
        indexes.append((i, 0, EAST))
        indexes.append((i, len(field[0]) - 1, WEST))
    for i in range(len(field[0])):
        indexes.append((0, i, SOUTH))
        indexes.append((len(field) - 1, i, NORTH))

    for index in indexes:
        beams = deque([])
        beams.append(index)
        energized = set()
        energized_no_dir = set()
        a, b, _ = index
        energized_no_dir.add((a, b))

        while len(beams) > 0:
            y, x, dir = beams.pop()

            if not (0 <= x and x < len(field[0]) and 0 <= y and y < len(field)):
                continue

            if (y, x, dir) in energized:
                continue

            energized.add((y, x, dir))
            energized_no_dir.add((y, x))

            if field[y][x] == SPLITER_VER and (dir == WEST or dir == EAST):
                beams.append((y, x, SOUTH))
                beams.append((y, x, NORTH))
            elif field[y][x] == SPLITER_HOR and (dir == SOUTH or dir == NORTH):
                beams.append((y, x, EAST))
                beams.append((y, x, WEST))
            elif (field[y][x] == MIRROR_SW and (dir == SOUTH or dir == NORTH)) or\
                (field[y][x] == MIRROR_SE and (dir == WEST or dir == EAST)):
                dy, dx = ORIENTATION[(dir - 1) % 4]
                beams.append((y + dy, x + dx, (dir - 1) % 4))
            elif (field[y][x] == MIRROR_SE and (dir == SOUTH or dir == NORTH)) or\
                (field[y][x] == MIRROR_SW and (dir == WEST or dir == EAST)):
                dy, dx = ORIENTATION[(dir + 1) % 4]
                beams.append((y + dy, x + dx, (dir + 1) % 4))
            else:
                dy, dx = ORIENTATION[dir]
                beams.append((y + dy, x + dx, dir))
        if len(energized_no_dir) > total:
            total = len(energized_no_dir)
    return total

print(f"result: {main()}")

