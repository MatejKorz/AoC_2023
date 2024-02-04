ROUND = 'O'
CUBE = '#'
GROUND = '.' 

def load_file(filename: str):
    rv = []
    with open(filename, 'r') as f:
        for line in f:
            striped = line.strip('\n')
            if striped != "":
                rv.append(striped)
    return rv

def count_column(col) -> int:
    total = 0
    max_index = len(col)
    round = 0
    for i, stone in enumerate(col):
        if stone == ROUND:
            round += 1
        if stone == CUBE:
            total += sum([x for x in range(max_index, max_index - round, -1)])
            round = 0
            max_index = len(col) - i - 1
    total += sum([x for x in range(max_index, max_index - round, -1)])

    return total


def main() -> int:
    filename = "day14_input.txt"

    lst = load_file(filename)

    total = 0
    for i in range(len(lst[0])):
        tmp = ""
        for j in range(len(lst)):
            tmp += lst[j][i]
        val = count_column(tmp)
        print(f"{tmp} -> {val}")
        total += val

    return total


print(f"result: {main()}")

