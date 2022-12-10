from utils import advent

YEAR = '2022'
DAY = '04'


def init_group_pairs():
    input = advent.read_input_as_lines(YEAR, DAY)
    for g1, g2 in ([[int(val) for val in g.split('-')] for g in pair.split(',')] for pair in input):
        r1 = range(g1[0], g1[1]+1)
        r2 = range(g2[0], g2[1]+1)
        yield set(r1), set(r2)


def sol1():
    return [g1.issubset(g2) or g2.issubset(g1) for g1, g2 in init_group_pairs()].count(True)


def sol2():
    return [len(g1.intersection(g2)) > 0 for g1, g2 in init_group_pairs()].count(True)


print(sol1())  # 599
print(sol2())  # 928
