def read_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        lines = [x.strip() for x in lines]
    return lines


def read_file2(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        lines = [x.strip('\n') for x in lines]
    return lines