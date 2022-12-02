#!/usr/bin/env
SYMBOLS = {'X':1, 'Y':2, 'Z':3}

def problem1():
    scores = []
    matchups = {}
    matchups['A'] = {'X': 3, 'Y':6, 'Z':0}
    matchups['B'] = {'X': 0, 'Y':3, 'Z':6}
    matchups['C'] = {'X': 6, 'Y':0, 'Z':3}

    with open("input.txt", 'r') as f:
        for line in f:
            op_symbol, my_symbol = line.rstrip().split(" ")
            symbol_score = SYMBOLS[my_symbol]
            matchhup_score = matchups[op_symbol][my_symbol]
            scores.append(symbol_score + matchhup_score)
                
    return sum(scores)

def problem2():
    scores = []
    lookup = {}
    lookup['A'] = {'X':3+0, 'Y':1+3, 'Z':2+6}
    lookup['B'] = {'X':1+0, 'Y':2+3, 'Z':3+6}
    lookup['C'] = {'X':2+0, 'Y':3+3, 'Z':1+6}
    with open("input.txt", 'r') as f:
        for line in f:
            op_symbol, my_symbol = line.rstrip().split(" ")
            scores.append(lookup[op_symbol][my_symbol])

    return sum(scores)

if __name__ == "__main__":
    print(f"Problem 1:{problem1()}")
    print(f"Problem 2:{problem2()}")