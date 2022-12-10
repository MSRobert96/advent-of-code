import math
import re
from utils import advent

YEAR = '2022'
DAY = '05'


def init_stacks(raw_header):
    stacks = [[] for i in range(math.ceil(len(raw_header[0])/4))]

    for row in raw_header:
        for idx, el in enumerate(row[idx:idx+4].strip('[ ]') for idx in range(0, len(row), 4)):
            if el != '':
                stacks[idx].insert(0, el)

    return stacks


def init_moves(raw_moves):
    return (re.search(r'move (?P<amount>\d+?) from (?P<from>\d) to (?P<to>\d)', move).groupdict() for move in raw_moves)


def sol1():
    input = advent.read_input_as_lines(YEAR, DAY)
    stacks = init_stacks(input[:input.index('')-1])
    moves = init_moves(input[input.index('')+1:])

    for move in moves:
        amount = int(move['amount'])
        stack_from = int(move['from']) - 1
        stack_to = int(move['to']) - 1
        for i in range(amount):
            stacks[stack_to].append(stacks[stack_from].pop())

    return ''.join([stack[-1] for stack in stacks if len(stack) > 0])


def sol2():
    input = advent.read_input_as_lines(YEAR, DAY)
    stacks = init_stacks(input[:input.index('')-1])
    moves = init_moves(input[input.index('')+1:])

    for move in moves:
        amount = int(move['amount'])
        stack_from = int(move['from']) - 1
        stack_to = int(move['to']) - 1
        removed_crates = stacks[stack_from][-amount:]
        stacks[stack_from] = stacks[stack_from][:-amount]
        stacks[stack_to].extend(removed_crates)

    return ''.join([stack[-1] for stack in stacks if len(stack) > 0])


print(sol1())  # ZWHVFWQWW
print(sol2())  # HZFZCCWWV
