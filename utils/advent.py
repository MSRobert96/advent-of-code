import numpy as np

def read_input(year, day, example = False) -> str:
    with open(f"../{'examples' if example else 'inputs'}/{year}_{day}.txt", "r") as file:
        return file.read().strip()

def read_input_as_lines(year, day, example = False) -> str:
    return read_input(year, day, example).splitlines()

def read_input_as_grid(year, day, example = False):
    lines = read_input_as_lines(year, day, example)
    return np.array([[*line] for line in lines])
