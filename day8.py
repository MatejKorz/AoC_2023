from typing import Dict, Tuple
from math import lcm

def load_file(filename: str):
    rv = []
    with open(filename, 'r') as f:
        for line in f:
            striped = line.strip('\n')
            if striped != "":
                rv.append(striped)
    return rv


def lcm_list(lst):
    rv = lst[0]
    for item in lst:
        rv = lcm(rv, item)
    return rv

def main():
    filename = 'day8_input.txt'

    lst = load_file(filename)
    sequence = lst[0].strip()
    print(f"sequence: {sequence}")

    nodes: Dict[str, Tuple[str, str]] = {}
    for i, line in enumerate(lst[1::]):
        key: str = line[0:3]
        val: Tuple[str, str] = (line[7:10], line[12:15])
        nodes[key] = val

    print(f"nodes: {nodes}")


    curr = [key for key in nodes if key[2] == "A"]
    step_cnt = [ 0 for _ in curr ]
    print(f"start nodes: {curr}")
    for i, _ in enumerate(curr):
        while curr[i][-1] != "Z":
            for char in sequence:
                dirs = nodes.get(curr[i])
                if dirs is None:
                    return -1
                left, right = dirs
                curr[i] = (left if char == 'L' else right)
                step_cnt[i] += 1
        print(f"step_cnt[{i}]: {step_cnt}")
    print(f"end nodes: {curr}")
    print(f"step_cnt: {step_cnt}")


    return lcm_list(step_cnt)

print(f"result: {main()}")
