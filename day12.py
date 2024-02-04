from typing import List, Tuple

def load_file(filename: str):
    rv = []
    with open(filename, 'r') as f:
        for line in f:
            striped = line.strip('\n')
            if striped != "":
                rv.append(striped)
    return rv

POS = ['.', '#']
UNKNOWN = '?'
WORKS = '.'
NO_WORKS = '#'


def gen_rec(cnt, curr: str, res: List[str]) -> None:
    if cnt == 0:
        res.append(curr)
        return
    for char in POS:
        gen_rec(cnt - 1, curr + char, res)

def gen_possible_inputs(cnt) -> List[str]:
    res = []
    gen_rec(cnt, "", res)
    return res

def gen_possible_lines(line: str) -> List[str]:
    gens = gen_possible_inputs(line.count(UNKNOWN))
    rv = []
    for gen in gens:
        work_line = ""
        gen_index = 0
        for char in line:
            if char == UNKNOWN:
                work_line += gen[gen_index]
                gen_index += 1
            else:
                work_line += char
        rv.append(work_line)
    return rv

def line_match(line: str, pos: List[int]) -> bool:
    pos_index = 0
    i = 0
    inside = False
    while i < len(line):
        if line[i] == WORKS:
            if inside:
                return False
            i += 1
            continue
        inside = True
        pos[pos_index] -= 1
        if pos[pos_index] == 0:
            inside = False
            if i + 1 >= len(line):
                return sum(pos) == 0
            if line[i+1] != WORKS:
                return False

            pos_index += 1

            if pos_index >= len(pos):
                return line[i+1::].count(NO_WORKS) == 0
        i += 1

    return sum(pos) == 0


def combinations(line: str, pos: List[int]) -> int:
    total = 0
    gen_lines = gen_possible_lines(line)
    for gen_line in gen_lines:
        if line_match(gen_line, pos.copy()):
            total += 1
    return total

def main() -> int:
    filename = "day12_input.txt"
    lst = load_file(filename)
    
    lines = []
    pos = []

    for line in lst:
        lines.append(line[0:line.find(' ')])
        pos.append([int(x) for x in (line[line.find(' ')+1::].split(','))])


    total = 0
    for i in range(len(lines)):
        print(lines[i])
        #print(pos[i])
        cnt = combinations(lines[i], pos[i])
        #print(cnt)
        total += cnt


    return total


print(f"result: {main()}")
