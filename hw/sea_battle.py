field1 = [
    [0, 1, 0, 1, 1],
    [1, 0, 0, 0, 0],
    [1, 0, 1, 1, 0],
    [1, 0, 0, 0, 1],
    [0, 1, 0, 0, 1]
]

field2 = [
    [1, 1, 1, 0, 0],
    [0, 0, 1, 1, 0],
    [1, 0, 0, 0, 1],
    [1, 0, 1, 0, 0],
    [0, 0, 0, 1, 1]
]

def get_square(square):
    column = square[0]
    row = square[-1]
    return column + row

print(get_square('b4'))