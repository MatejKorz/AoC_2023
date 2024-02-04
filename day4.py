from typing import List, Tuple

def load_file(filename: str) -> List[str]:
    rv = []
    with open(filename, 'r') as f:
        for line in f:
            striped = line.strip('\n')
            if striped != "":
                rv.append(striped)
    return rv


def parse_list(lst: List[str]) -> int:
    cards = [ 1 for i in range(len(lst))]
    for i, line in enumerate(lst):
        my_nums = line[line.index(":") + 1:line.index("|")].split()
        win_nums = line[line.index("|") + 1::].split()
        print(my_nums)
        print(win_nums)
        curr = 0
        for num in my_nums:
            if num in win_nums:
                curr += 1
        for j in range(curr):
            if (i + j < len(cards)):
                cards[i + j + 1] += cards[i]
        print(cards)

    rv = 0
    for num in cards:
        rv += num
    return rv



def main() -> int:
    filename = 'day4_input.txt'

    lst = load_file(filename)
    for line in lst:
        print(line)

    return parse_list(lst)


print(f"result sum: {main()}")
