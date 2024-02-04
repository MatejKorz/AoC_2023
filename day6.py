def load_file(filename: str):
    rv = []
    with open(filename, 'r') as f:
        for line in f:
            striped = line.strip('\n')
            if striped != "":
                rv.append(striped)
    return rv

def main():
    filename = 'day6_input.txt'

    lst = load_file(filename)
    times = lst[0][lst[0].index(":") + 1::].split()
    dist = lst[1][lst[1].index(":") + 1::].split()

    print(f"times: {times}")
    print(f"distances: {dist}")
    times = ["44707080"]
    dist = ["283113411341491"]
    rv = 1
    for i, time in enumerate(times):
        #print(f"{i}. time -> {time}")
        traveled = []
        for hold_time in range(int(time)):
            speed = 0 if hold_time == 0 else (hold_time)
            total = (int(time) - hold_time) * speed
            #print(f"{total} = ({time} - {hold_time}) * {speed}")
            traveled.append(total)
        #print(f"pos_dist: {traveled}")
        higher = [x for x in traveled if x > int(dist[i])]
        #print(f"winning: {higher} -> {len(higher)}")
        rv *= len(higher)
        #print(rv)

    return rv

print(f"result: {main()}")



