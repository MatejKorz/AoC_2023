from typing import List, Tuple

def load_file(filename: str) -> List[str]:
    rv = []
    with open(filename, 'r') as f:
        for line in f:
            striped = line.strip('\n')
            if striped != "":
                rv.append(striped)
    return rv


def check_sides(lst: List[str], pos: Tuple[int, int]) -> int:
    y, x = pos
    rv = 0
    if x > 0 and lst[y][x - 1] != '.':
        index = [i for i in range(x - 1, -1, -1) if lst[y][i] == '.']
        num = int(lst[y][(index[0] + 1 if (index != []) else 0):x])
        print(num)
        rv += num
    if x < len(lst[y]) - 1 and lst[y][x + 1] != '.':
        index = [i for i in range(x + 1, len(lst[y])) if lst[y][i] == '.']
        num = int(lst[y][x + 1:(index[0] if (index != []) else len(lst[y]))])
        print(num)
        rv += num

    return rv

def find_nums(lst: List[str], pos: Tuple[int, int]) -> int:
    y, x = pos
    rv = check_sides(lst, (y, x))

    if y > 0:
        left_index = [i for i in range(x - 1, -1, -1) if lst[y - 1][i] == '.']
        right_indx = [i for i in range(x + 1, len(lst[y - 1])) if lst[y - 1][i] == '.']
        if lst[y - 1][x] != '.':
            num = int(lst[y - 1][(left_index[0] + 1 if (left_index != []) else 0):(right_indx[0] if (right_indx != []) else len(lst[y - 1]))])
            print(num)
            rv += num
        else:
            rv += check_sides(lst, (y - 1, x))

    if y < len(lst) - 1:
        left_index = [i for i in range(x - 1, -1, -1) if lst[y + 1][i] == '.']
        right_indx = [i for i in range(x + 1, len(lst[y - 1])) if lst[y + 1][i] == '.']
        if lst[y + 1][x] != '.':
            num = int(lst[y + 1][(left_index[0] + 1 if (left_index != []) else 0):(right_indx[0] if (right_indx != []) else len(lst[y + 1]))])
            print(num)
            rv += num
        else:
            rv += check_sides(lst, (y + 1, x))

    return rv


def check_sides2(lst: List[str], pos: Tuple[int, int], gears) -> int:
    y, x = pos
    rv = 0
    if x > 0 and lst[y][x - 1] != '.':
        index = [i for i in range(x - 1, -1, -1) if lst[y][i] == '.']
        num = int(lst[y][(index[0] + 1 if (index != []) else 0):x])
        # print(num)
        gears.append(num)
        rv += num
    if x < len(lst[y]) - 1 and lst[y][x + 1] != '.':
        index = [i for i in range(x + 1, len(lst[y])) if lst[y][i] == '.']
        num = int(lst[y][x + 1:(index[0] if (index != []) else len(lst[y]))])
        # print(num)
        rv += num
        gears.append(num)

    return rv

def find_nums2(lst: List[str], pos: Tuple[int, int], gears) -> int:
    y, x = pos
    rv = check_sides2(lst, (y, x), gears)

    if y > 0:
        left_index = [i for i in range(x - 1, -1, -1) if lst[y - 1][i] == '.']
        right_indx = [i for i in range(x + 1, len(lst[y - 1])) if lst[y - 1][i] == '.']
        if lst[y - 1][x] != '.':
            num = int(lst[y - 1][(left_index[0] + 1 if (left_index != []) else 0):(right_indx[0] if (right_indx != []) else len(lst[y - 1]))])
            # print(num)
            rv += num
            gears.append(num)
        else:
            rv += check_sides2(lst, (y - 1, x), gears)

    if y < len(lst) - 1:
        left_index = [i for i in range(x - 1, -1, -1) if lst[y + 1][i] == '.']
        right_indx = [i for i in range(x + 1, len(lst[y - 1])) if lst[y + 1][i] == '.']
        if lst[y + 1][x] != '.':
            num = int(lst[y + 1][(left_index[0] + 1 if (left_index != []) else 0):(right_indx[0] if (right_indx != []) else len(lst[y + 1]))])
            # print(num)
            rv += num
            gears.append(num)
        else:
            rv += check_sides2(lst, (y + 1, x), gears)

    return rv


def parse_list(lst: List[str]) -> int:
    rv = 0
    gears_ratio = 0
    for i, line in enumerate(lst):
        for j, char in enumerate(line):
            if char == '*':
                gears = []
                rv += find_nums2(lst, (i, j), gears)
                print(gears)
                if len(gears) == 2:
                    gears_ratio += gears[0] * gears[1]
    return gears_ratio


def main() -> int:
    filename = 'day3_input.txt'

    lst = load_file(filename)
    for line in lst:
        print(line)

    return parse_list(lst)


print(f"result sum: {main()}")
