#!/usr/bin/env

def problem1and2(reverse=True):
    stacks = [[] for i in range(9)]
    move_flag = False
    with open('input.txt', 'r') as f:
        for i, line in enumerate(f):
            line = line.rstrip()
            if line == '':
                move_flag = True
                stacks = [stack[:-1] for stack in stacks]
            elif not move_flag: #we read the stack
                crates = [line[ii: ii+3].strip() for ii in range(0, len(line), 4)]
                for ii, crate in enumerate(crates):
                    if not crate == '':
                        stacks[ii].append(crate)
            else: #we move the crates 
                for ii, stack in enumerate(stacks):
                    print(f"STACK {ii+1}: {stack}")
                num_items, start_l, end_l = [int(word) for word in line.split(' ') if word.isnumeric()]
                if reverse:
                    stacks[end_l-1] = stacks[start_l-1][:num_items][::-1] + stacks[end_l-1]
                else:
                    stacks[end_l-1] = stacks[start_l-1][:num_items] + stacks[end_l-1]

                stacks[start_l-1] = stacks[start_l-1][num_items:]

    for ii, stack in enumerate(stacks):
        print(f"STACK {ii+1}: {stack}")
    return ''.join([stack[0][1] for stack in stacks])

if __name__ == '__main__':
    print(problem1and2())
    print(problem1and2(reverse=False))