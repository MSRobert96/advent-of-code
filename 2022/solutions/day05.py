import math
import re
import numpy as np
from textwrap import wrap
from utils import advent

YEAR = '2022'
DAY = '05'

def init_stacks(raw_header):
    stacks = []
    n_stacks = math.ceil(len(raw_header[0])/4)
    for i in range(n_stacks):
        stacks.append([])

    for row in raw_header:
        data = [el.strip().replace('[', '').replace(']', '') for el in wrap(row, 4, drop_whitespace=False)]
        for idx, el in enumerate(data):
            if el != '':
                stacks[idx].insert(0, el)
    
    return stacks

def init_moves(raw_moves):
    moves = []
    for move in raw_moves:
        moves.append(re.search(r'move (?P<amount>\d+?) from (?P<from>\d) to (?P<to>\d)', move).groupdict())
        
    return moves

def sol1():
    input = advent.read_input_as_lines(YEAR, DAY)

    raw_header = input[:input.index('')-1]
    raw_moves = input[input.index('')+1:]
    
    stacks = init_stacks(raw_header)
    moves = init_moves(raw_moves)

    for move in moves:
        amount = int(move['amount'])
        stack_from = int(move['from']) - 1
        stack_to = int(move['to']) - 1
        for i in range(amount):
            stacks[stack_to].append(stacks[stack_from].pop())

    return ''.join([stack[-1] for stack in stacks if len(stack) > 0])

def sol2():
    input = advent.read_input_as_lines(YEAR, DAY)

    raw_header = input[:input.index('')-1]
    raw_moves = input[input.index('')+1:]
    
    stacks = init_stacks(raw_header)
    moves = init_moves(raw_moves)

    for move in moves:
        amount = int(move['amount'])
        stack_from = int(move['from']) - 1
        stack_to = int(move['to']) - 1
        removed_crates = stacks[stack_from][-amount:]
        stacks[stack_from] = stacks[stack_from][:-amount]
        stacks[stack_to].extend(removed_crates)

    return ''.join([stack[-1] for stack in stacks if len(stack) > 0])


print(sol1()) # ZWHVFWQWW
print(sol2()) # HZFZCCWWV