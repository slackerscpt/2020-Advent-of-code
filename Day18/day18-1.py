#!/usr/bin/env python3
import argparse
from collections import deque
import pathlib

def process_parens(data):
    paren_count = 1
    data2 = deque()
    while paren_count > 0:
        popped = data.popleft()
        if popped == "(":
            paren_count += 1
        elif popped == ")":
            paren_count -= 1
        data2.append(popped)
    data2.pop()
    while len(data2) > 1:
        math(data2)
    return int(data2[0])

def math(data):
    a = data.popleft()
    if a == "(":
        a = process_parens(data)
    else:
        a = int(a)
    b = data.popleft()
    c = data.popleft()
    if c == "(":
        c = process_parens(data)
    else:
        c = int(c)
    if b == "+":
        data.appendleft(a + c)
    elif b == "*":
        data.appendleft(a * c)

class AdvancedNum:
    def __init__(self, val):
        self.val = val
    def __add__(self, other):
        return AdvancedNum(self.val * other.val)
    def __mul__(self, other):
        return AdvancedNum(self.val + other.val)
    def __repr__(self):
        return f"{self.__class__.__name__}(val={self.val})"
    def __str__(self):
        return f"{self.__class__.__name__}(val={self.val})"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advent of Code 2020 Day 18")
    parser.add_argument("file", type=pathlib.Path, help="input file")
    args = parser.parse_args()

    print("Day 18")

    with args.file.open("r") as f:
        homework = [list(line.replace(" ", "").rstrip("\n")) for line in f]

    result = 0
    for x in homework:
        data = deque(x)
        while len(data) > 1:
            math(data)
        result += data[0]
    print(f"Part 1 result: {result}")

    result = 0
    for hw in homework:
        new_hw = []
        for x in hw:
            if x not in ["(", ")", "+", "*"]:
                new_hw.append(str(AdvancedNum(int(x))))
            elif x == "*":
                new_hw.append("+")
            elif x == "+":
                new_hw.append("*")
            else:
                new_hw.append(x)
        result += eval("".join(new_hw)).val
    print(f"Part 2 result: {result}")