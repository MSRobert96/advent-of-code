from utils import advent

YEAR = '2022'
DAY = '06'


def find_token_end(input, size):
    return [len(set(input[idx-size:idx])) for idx in range(size, len(input))].index(size)+size


def sol1():
    input = advent.read_input(YEAR, DAY)
    return find_token_end(input, 4)


def sol2():
    input = advent.read_input(YEAR, DAY)
    return find_token_end(input, 14)


print(sol1())  # 1542
print(sol2())  # 3153
