import numpy as np
from utils import advent

YEAR = '2022'
DAY = '08'

def sol1():
    grid = advent.read_input_as_grid(YEAR, DAY).astype(int)
    visible = np.full_like(grid, False, bool)

    for (r,c), el in np.ndenumerate(grid):
        visible[r,c] = (all(val<el for val in grid[r, :c]) or # left
                        all(val<el for val in grid[r, c+1:]) or # right
                        all(val<el for val in grid[:r, c]) or # top
                        all(val<el for val in grid[r+1:, c])) # bottom
        
    return visible.flatten().tolist().count(True)

def sol2():
    grid = advent.read_input_as_grid(YEAR, DAY).astype(int)
    scores = np.zeros_like(grid)
    rows, cols = grid.shape

    for (r,c), el in np.ndenumerate(grid):
        if r == 0 or r == rows-1 or c == 0 or c == cols-1 :
            continue
        
        left = right = top = bottom = 0

        for val in grid[r, :c][::-1]: # left
            left += 1
            if val >= el:
                break
        
        for val in grid[r, c+1:]: # right
            right += 1
            if val >= el:
                break
        
        for val in grid[:r, c][::-1]: # top
            top += 1
            if val >= el:
                break

        for val in grid[r+1:, c]: # bottom
            bottom += 1
            if val >= el:
                break

        scores[r,c] = left * right * top * bottom
        
    return max(scores.flat)


print(sol1()) # 1705
print(sol2()) # 371200