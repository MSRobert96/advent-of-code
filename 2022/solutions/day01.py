from utils import advent

YEAR = '2022'
DAY = '01'

def sol1():
    input = advent.read_input_as_lines(YEAR, DAY)

    print(input)

    elves = [[]]

    i = 0
    for row in input:
        if row == '':
            i += 1
            elves.append([])
        else:
            elves[i].append(int(row))

    return max([sum(e) for e in elves])


def sol2():
    input = advent.read_input_as_lines(YEAR, DAY)

    elves = [[]]

    i = 0
    for row in input:
        if row == '':
            i += 1
            elves.append([])
        else:
            elves[i].append(int(row))

    return sum(sorted([sum(e) for e in elves], reverse=True)[:3])


print(sol1()) # 72602
print(sol2()) # 207410