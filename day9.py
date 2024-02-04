def load_file(filename: str):
    rv = []
    with open(filename, 'r') as f:
        for line in f:
            striped = line.strip('\n')
            if striped != "":
                rv.append(striped)
    return rv

def all_zero(lst):
    for item in lst:
        if item != 0:
            return False
    return True

def parse_data(data):
    data_mem = []
    while len(data) != 0 and not all_zero(data):
        data_mem.append(data)
        new_data = [data[i+1] - data[i] for i in range(len(data)-1)]
        data = new_data
    data_mem.append(data)
    data.append(0)

    for i in range(len(data_mem)):
        data_mem[i].reverse()

    for i in range(len(data_mem) - 1, 0, -1):
        val = data_mem[i-1][-1]-data_mem[i][-1]
        data_mem[i-1].append(val)
    print(data_mem)
    return data_mem[0][-1]

def main():
    filename = "day9_input.txt"
    lst = load_file(filename)
    total = 0
    for line in lst:
        data = [int(x) for x in line.split()]
        print(data)
        total += parse_data(data)
    return total

print(f"result: {main()}")
