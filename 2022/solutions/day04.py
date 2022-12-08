from utils import advent

YEAR = '2022'
DAY = '04'

def sol1() -> int:
    input = advent.read_input_as_lines(YEAR, DAY)
    score = 0
    for pair in input:
        e1, e2 = pair.split(',')
        min1, max1 = map(int, e1.split('-'))
        min2, max2 = map(int, e2.split('-'))
        r1 = set(range(min1, max1+1))
        r2 = set(range(min2, max2+1))
        if r1.issubset(r2) or r2.issubset(r1):
            score+=1
    return score

def sol2() -> int:
    input = advent.read_input_as_lines(YEAR, DAY)
    score = 0
    for pair in input:
        e1, e2 = pair.split(',')
        min1, max1 = map(int, e1.split('-'))
        min2, max2 = map(int, e2.split('-'))
        r1 = set(range(min1, max1+1))
        r2 = set(range(min2, max2+1))
        if len(r1.intersection(r2)) > 0:
            score+=1
    return score


print(sol1()) # 599
print(sol2()) # 928