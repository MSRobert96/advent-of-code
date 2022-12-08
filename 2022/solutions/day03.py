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

    for r in rucksacks:
        half = len(r) // 2
        items.append(*set(r[:half]).intersection(set(r[half:])))
    
    return sum([priority(item) for item in items])


def sol2() -> int:
    rucksacks = advent.read_input_as_lines(YEAR, DAY)
    items = []

    for idx in range(0, len(rucksacks), 3):
        a = set(rucksacks[idx+0])
        b = set(rucksacks[idx+1])
        c = set(rucksacks[idx+2])
        items.append(*a.intersection(b).intersection(c))
    
    return sum([priority(item) for item in items])

print(sol1()) # 7980
print(sol2()) # 2881