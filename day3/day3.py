#!/usr/bin/env
import string

LETTERS = string.ascii_lowercase + string.ascii_uppercase
PRIORITY = dict(zip(LETTERS, range(1, len(LETTERS)+1)))

def problem1():
    scores = []
    with open("input.txt") as f:
        for line in f:
            line = line.rstrip()
            total_items = len(line)
            first_compartment = set(line[:total_items//2])
            second_compartment = set(line[total_items//2:])
            item = list(first_compartment & second_compartment)[0]
            scores.append(PRIORITY[item])

    return sum(scores)

def problem2():
    scores = []
    with open("input.txt") as f:
        for line in f:
            line1 = set(line.rstrip())
            line2 = set(next(f).rstrip())
            line3 = set(next(f).rstrip())
            badge = list(line1 & line2 & line3)[0]
            scores.append(PRIORITY[badge])

    return sum(scores)


if __name__ == "__main__":
    print(problem1())
    print(problem2())