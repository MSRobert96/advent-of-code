import numpy as np

def read_input(year, day) -> str:
    with open(f"../inputs/{year}_{day}.txt", "r") as file:
        return file.read().strip()

def read_input_as_lines(year, day) -> str:
    return read_input(year, day).splitlines()

def read_input_as_grid(year, day):
    lines = read_input_as_lines(year, day)
    return np.array([[*line] for line in lines])
