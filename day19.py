from typing import Dict, List
from collections import namedtuple

SMALLER = 0
BIGGER = 1

ACCEPTED = 'A'
REJECTED = 'R'
Rule = namedtuple('Rule', 'attr diff val nxt')

X = 0
M = 1
A = 2
S = 3

class Part:
    def __init__(self, vals: List[int]) -> None:
        self.values = vals
        self.x = self.values[0]
        self.m = self.values[1]
        self.a = self.values[2]
        self.s = self.values[3]

def load_file(filename: str) -> List[str]:
    rv = []
    with open(filename, 'r') as f:
        for line in f:
            striped = line.strip('\n')
            rv.append(striped)
    return rv

def parse_rules(dic: Dict[str, List[Rule]], line: str) -> None:
    name = line[0:line.index('{')]
    rules = []
    for item in line[line.index('{')::].strip('{}').split(','):
        if ':' not in item:
            rules.append(Rule(None, None, None, item))
        else:
            diff = SMALLER if item.find('<') != -1 else BIGGER
            attr_str = item[0:item.index('<' if diff == SMALLER else '>')]
            if attr_str == 'x':
                attr = X
            elif attr_str == 'm':
                attr = M
            elif attr_str == 'a':
                attr = A
            else:
                attr = S

            val = int(item[item.index('<' if diff == SMALLER else '>')+1:item.index(':')])
            nxt = item[item.index(':')+1::]
            rules.append(Rule(attr, diff, val, nxt))

    dic[name] = rules

def eval_rule(part: Part, rule: Rule) -> bool:
    if rule.diff is None:
        return True
    elif rule.diff == SMALLER:
        return part.values[rule.attr] < rule.val
    else:
        return part.values[rule.attr] > rule.val
        
        

def eval_part(dic: Dict[str, List[Rule]], part: Part) -> int:
    curr = "in"

    while curr != ACCEPTED and curr != REJECTED:
        rule_list = dic.get(curr, [Rule(None, None, None, REJECTED)])

        print(rule_list)
        for rule in rule_list:
            print(rule)
            if eval_rule(part, rule):
                curr = rule.nxt
                break
    if curr == ACCEPTED:
        return sum(part.values)
    else:
        return 0


def main() -> int:
    lst = load_file("day19_input.txt")

    dic: Dict[str, List[Rule]] = {}
    parts: List[Part] = []
    rules = True
    total = 0

    for line in lst:
        print(line)
        if line == "":
            rules = False
        elif rules:
            parse_rules(dic, line)
        else:
            line_split = line.strip('{}').split(',')
            values = []
            for i in range(4):
                values.append(int(line_split[i][line_split[i].index('=')+1::]))
            parts.append(Part(values))

    print(dic)

    for part in parts:
        print(part.x, part.m, part.a, part.s)
        total += eval_part(dic, part)

    return total

print(f"result:{main()}")
