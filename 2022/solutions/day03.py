from utils import advent

YEAR = '2022'
DAY = '03'


def priority(chr):
    if chr >= 'a' and chr <= 'z':
        return ord(chr) - ord('a') + 1
    return ord(chr) - ord('A') + 27


def sol1() -> int:
    rucksacks = advent.read_input_as_lines(YEAR, DAY)
    items = []

    for r1, r2 in ((set(r[:len(r)//2]), set(r[len(r)//2:])) for r in rucksacks):
        items.append(*r1.intersection(r2))

    return sum([priority(item) for item in items])


def sol2() -> int:
    rucksacks = advent.read_input_as_lines(YEAR, DAY)
    items = []

    for a, b, c in (map(set, rucksacks[idx:idx+3]) for idx in range(0, len(rucksacks), 3)):
        items.append(*a.intersection(b).intersection(c))

    return sum([priority(item) for item in items])


print(sol1())  # 7980
print(sol2())  # 2881
