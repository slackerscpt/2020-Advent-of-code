import re
maskRe = re.compile(r"mask = ([X01]+)")
memRe = re.compile(r"mem\[(\d+)\] = (\d+)")
all_binaries = lambda n: [list(("{:0" + str(n) + "b}").format(v)) for v in range(2**n)]

def readData():
    with open('input.txt', "r") as read_file:
        inputData = [line.rstrip() for line in read_file]

        return inputData


def part1():
    data = readData()

    bitmask = None # it is guaranteed that it will be set beforehand
    memory = dict()

    for line in data:
        mask = maskRe.match(line)
        if mask:
            bitmask = mask.groups()[0]
            continue

        index, value = memRe.match(line).groups()
        #Let's put the value in binary and replace the values of X
        #Line by line
        memory[index] = "".join(
            (c if d == "X" else d)
            for c, d in zip("{:036b}".format(int(value)), bitmask)
        )
    
    print(sum(int(v, 2) for v in memory.values()))


def part2():
    data = readData()
    memory = dict()
    bitmask = None

    for line in data:
        mask = maskRe.match(line)
        if mask:
            bitmask = mask.groups()[0]
            continue
        index, value = memRe.match(line).groups()
        new_index = "".join(
            (c if m == "0" else m)
            for c, m in zip("{:036b}".format(int(index)), bitmask)
        )
        indices = replace_x(new_index)
        for i in indices:
            memory[i] = value

    print(sum(int(v) for v in memory.values()))
    

def replace_x(s):
    addresses = []
    n = s.count("X")
    for binary_string in all_binaries(n):
        new_string = ""
        for c in s:
            if c == "X":
                new_string += binary_string.pop(0)
            else:
                new_string += c
        addresses.append(new_string)
    return addresses


part1()
part2()