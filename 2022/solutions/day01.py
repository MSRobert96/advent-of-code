from utils import advent

YEAR = '2022'
DAY = '01'


def load_elves():
    input = advent.read_input(YEAR, DAY)
    return [sum(map(int, elf.splitlines())) for elf in input.split('\n\n')]


def sol1():
    return max(load_elves())


def sol2():
    return sum(sorted(load_elves())[-3:])


print(sol1())  # 72602
print(sol2())  # 207410
