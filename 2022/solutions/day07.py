from utils import advent

YEAR = '2022'
DAY = '07'

class File:
    def __init__(self, size, name):
        self.name = name
        self.size = int(size)

    def __str__(self):
        return self.name + ' ' + str(self.size)

class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.total_size = 0
        self.directories = []
        self.files = []

    def add_directory(self, dir):
        dir.parent = self
        self.directories.append(dir)
    
    def add_file(self, file):
        self.files.append(file)

    def calc_size(self):
        self.total_size = 0
        self.total_size += sum([file.size for file in self.files])
        self.total_size += sum([dir.calc_size() for dir in self.directories], 0)
        return self.total_size

def parse_command(command: str):
    global cwd
    parsed = command.split(' ')
    if parsed[1] == 'cd':
        dir_name = parsed[2]
        if dir_name == '/': cwd = root
        elif dir_name == '..': cwd = cwd.parent
        else: cwd = [dir for dir in cwd.directories if dir.name == dir_name][0]

def parse_line(input: str):
    global cwd
    parsed = input.split(' ')
    if parsed[0] == '$':
        parse_command(input)
    elif parsed[0] == 'dir':
        if parsed[1] not in [dir.name for dir in cwd.directories]:
            cwd.add_directory(Directory(parsed[1], cwd))
    else:
        if parsed[1] not in [file.name for file in cwd.files]:
            cwd.add_file(File(*parsed))

def build_tree(input):
    global cwd, root
    cwd = root = Directory('/', None)
    for line in input: parse_line(line)
    root.calc_size()
    return root

def sol1():
    input = advent.read_input_as_lines(YEAR, DAY)
    build_tree(input)

    def tot_weight_by_size(dir: Directory, max_size: int):
        weight = 0
        if dir.total_size <= max_size:
            weight += dir.total_size
        
        # recursively calc and add subdirs size
        for subdir in dir.directories:
            weight += tot_weight_by_size(subdir, max_size)
        
        return weight

    return tot_weight_by_size(root, 100000)

def sol2():
    input = advent.read_input_as_lines(YEAR, DAY)
    build_tree(input)
    space_to_free = root.total_size - (70000000 - 30000000)

    def find_min_size(dir: Directory, min_size: int, min_found: Directory):
        current_min = min_found
        if dir.total_size >= min_size and dir.total_size <= current_min.total_size:
            current_min = dir
        
        # recursively search min in subdirs
        for subdir in dir.directories:
            sub_min = find_min_size(subdir, min_size, current_min)
            if sub_min.total_size <= current_min.total_size:
                current_min = sub_min
        
        return current_min

    return find_min_size(root, space_to_free, root).total_size


print(sol1()) # 1307902
print(sol2()) # 7068748

