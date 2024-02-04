from gettext import find
from typing import List, Tuple
import math

def load_file(filename: str) -> List[str]:
    rv = []
    with open(filename, 'r') as f:
        for line in f:
            striped = line.strip('\n')
            if striped != "":
                rv.append(striped)
    return rv


def into_tuples(lst: List[Tuple[int, int, int]], line: str) -> None:
    nums = line.split()
    # from to rng
    lst.append((int(nums[1]), int(nums[0]), int(nums[2])))

def find_in_tuples(lst_tuples, val):
    for a, b, c in lst_tuples:
        if a <= val <= a + c:
            return (a, b, c)
    return None

def parse_matrix(change_matrix):
    out = []
    for i in range(len(change_matrix) - 1):
        for tup in change_matrix[i]:
            in_start, in_to, in_rng = tup
            val = find_in_tuples(change_matrix[i+1], )


def main():
    filename = 'day5_test1.txt'

    lst = load_file(filename)
    names = ["soil", "fertilizer", "water", "light", "temp", "humidity", "location"]

    for line in lst:
        print(line)

    seeds = []
    only_seeds = lst[0][lst[0].index(":") + 1::].split()
    print(only_seeds)
    for i in range(0, len(only_seeds), 2):
        seeds.append((int(only_seeds[i]), int(only_seeds[i]) + int(only_seeds[i+1])))

    print("seeds")
    print(seeds)

    index = 2
    change_matrix = []
    for _ in range(7):
        matrix = []
        while (lst[index][0].isdigit() and index < len(lst) - 1):
            into_tuples(matrix, lst[index])
            index += 1
        change_matrix.append(matrix)
        index += 1

    for matrix in change_matrix:
        print(matrix)

    for seed in seeds:

    





print(f"result sum: {main()}")
