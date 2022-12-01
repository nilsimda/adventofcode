#!/usr/bin/env

if __name__ == "__main__":
    calories = []
    current_sum = 0
    with open("input.txt", "r") as f:
        for line in f:
            if line == '\n':
                calories.append(current_sum)
                current_sum = 0
            else:
                current_sum += int(line.rstrip())

    calories = sorted(calories)
    print(f"Top three: {calories[-3:]}")
    print(f"Sum of top three: {sum(calories[-3:])}")
            