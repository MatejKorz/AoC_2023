from typing import List

GALAXY = '#'
EMPTY = '.'

def load_file(filename: str) -> List[str]:
    rv = []
    with open(filename, 'r') as f:
        for line in f:
            striped = line.strip('\n')
            if striped != "":
                rv.append(striped)
    return rv

def main() -> int:
    filename = "day11_input.txt"
    lst = load_file(filename)
    empty_rows = []
    empty_cols = []
    
    for line in lst:
        print(line)

    for i, row in enumerate(lst):
        if row.find(GALAXY) == -1:
            empty_rows.append(i)

    for x in range(len(lst[0])):
        empty = True
        for y in range(len(lst)):
            if lst[y][x] == GALAXY:
                empty = False
        if empty:
            empty_cols.append(x)

    print(f"empty_rows: {empty_rows}")
    print(f"empty_cols: {empty_cols}")

    growth = 999999

    galaxy_coords = []
    real_x = 0
    for x, row in enumerate(lst):
        real_y = 0
        for y, char in enumerate(row):
            if y in empty_cols:
                real_y += growth
            if char == GALAXY:
                galaxy_coords.append((real_x, real_y))
            real_y += 1
        if x in empty_rows:
            real_x += growth
        real_x += 1

    print(f"galaxy_coords: {galaxy_coords}")
    total = 0

    while len(galaxy_coords) > 0:
        x,y = galaxy_coords.pop()
        dist = 0
        for x2,y2 in galaxy_coords:
            dist += abs(x2-x)+abs(y2-y)
        total += dist

    return total

print(f"result {main()}")

