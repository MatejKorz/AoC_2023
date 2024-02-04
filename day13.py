def load_file(filename: str):
    rv = []
    with open(filename, 'r') as f:
        tmp = []
        for line in f:
            striped = line.strip('\n')
            if striped != "":
                tmp.append(striped)
            else:
                rv.append(tmp)
                tmp = []
    return rv


def cmp_rows(area, index) -> bool:
    low_index = index
    high_index = index + 1
    while low_index >= 0 and high_index < len(area):
        if area[low_index] != area[high_index]:
            return False
        low_index -= 1
        high_index += 1
    return True


def parse_area(area) -> int:
    column = 0
    row = 0
    for i in range(len(area) - 1): #row mirroring
        if cmp_rows(area, i) == True: row += i + 1

    new_area = []
    for i in range(len(area[0])):
        tmp = []
        for j in range(len(area)):
            tmp.append(area[j][i])
        new_area.append(tmp)

    for i in range(len(new_area) - 1): #coll mirroring
        if cmp_rows(new_area, i) == True: column += i + 1

    return 100 * row + column

def main() -> int:
    filename = "day13_input.txt"
    lst = load_file(filename)

    total = 0

    for area in lst:
        print(area)
        total += parse_area(area)

    return total

print(f"result: {main()}")
