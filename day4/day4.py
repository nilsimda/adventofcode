#!/usr/bin/env

def problem1():
    count = 0
    with open('input.txt', 'r') as f:
        for line in f:
            line = line.rstrip()
            first, second = line.split(',')

            first1, first2 = first.split('-')
            first_set = set(range(int(first1), int(first2)+1))

            second1, second2 = second.split('-')
            second_set = set(range(int(second1), int(second2)+1))

            if first_set <= second_set or second_set <= first_set:
                count+=1

    return count

def problem2():
    count = 0
    with open('input.txt', 'r') as f:
        for line in f:
            line = line.rstrip()
            first, second = line.split(',')

            first1, first2 = first.split('-')
            first_set = set(range(int(first1), int(first2)+1))

            second1, second2 = second.split('-')
            second_set = set(range(int(second1), int(second2)+1))

            if len(first_set & second_set) > 0:
                count+=1

    return count

if __name__ == '__main__':
    print(problem1())
    print(problem2())