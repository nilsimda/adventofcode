#!/usr/bin/env

def problem1and2(num_chars=4):
    with open('input.txt', 'r') as f:
        counter = 0 
        while True:
            chars = f.read(num_chars)

            if not chars:
                break

            if len(set(chars)) == num_chars:
                counter += num_chars
                return counter

            counter += 1
            f.seek(counter)

if __name__ == '__main__':
    print(problem1and2(4))
    print(problem1and2(14))