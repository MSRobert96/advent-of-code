from utils import advent

YEAR = '2022'
DAY = '06'


def sol1():
    input = advent.read_input(YEAR, DAY)

    for idx in range(0, len(input)-4):
        if len(set(input[idx:idx+4])) == 4:
            return idx+4


def sol2():
    input = advent.read_input(YEAR, DAY)

    for idx in range(0, len(input)-14):
        if len(set(input[idx:idx+14])) == 14:
            return idx+14


print(sol1())  # 1542
print(sol2())  # 3153
