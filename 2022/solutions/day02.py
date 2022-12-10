from utils import advent

YEAR = '2022'
DAY = '02'


def sol1():
    WIN = 6
    DRAW = 3
    LOSE = 0

    SCORES = {'X': 1, 'Y': 2, 'Z': 3}

    WIN_CONDITIONS = {('A', 'Y'), ('B', 'Z'), ('C', 'X')}
    DRAW_CONDITIONS = {('A', 'X'), ('B', 'Y'), ('C', 'Z')}
    LOSE_CONDITIONS = {('A', 'Z'), ('B', 'X'), ('C', 'Y')}

    total_score = 0

    input = advent.read_input_as_lines(YEAR, DAY)
    for line in input:
        pair = tuple(line.replace('\n', '').split(' '))
        total_score += SCORES[pair[1]]
        if pair in WIN_CONDITIONS:
            total_score += 6
        elif pair in DRAW_CONDITIONS:
            total_score += 3

    return total_score


def sol2():
    WIN = 6
    DRAW = 3
    LOSE = 0

    ENDINGS = {'X': 0, 'Y': 3, 'Z': 6}
    MOVES = {'R': 1, 'P': 2, 'S': 3}

    WIN_CONDITIONS = {'A': 'P', 'B': 'S', 'C': 'R'}
    DRAW_CONDITIONS = {'A': 'R', 'B': 'P', 'C': 'S'}
    LOSE_CONDITIONS = {'A': 'S', 'B': 'R', 'C': 'P'}

    total_score = 0

    input = advent.read_input_as_lines(YEAR, DAY)
    for line in input:
        pair = tuple(line.replace('\n', '').split(' '))
        move = pair[0]
        ending = pair[1]
        if ending == 'X':
            answer = LOSE_CONDITIONS[move]
        elif ending == 'Y':
            answer = DRAW_CONDITIONS[move]
        elif ending == 'Z':
            answer = WIN_CONDITIONS[move]
        total_score += ENDINGS[ending] + MOVES[answer]

    return total_score


print(sol1())  # 11906
print(sol2())  # 11186
