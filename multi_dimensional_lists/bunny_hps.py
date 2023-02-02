size = int(input())

matrix = []
bunny_pos = []
best_path = []

best_direction = None
collected_eggs = 0


directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row in range(size):
    matrix.append(input().split())

    if 'B' in matrix[row]:
        bunny_pos = [row, matrix[row].index('B')]


for direction, positions in directions.items():
    row, col = [
        bunny_pos[0] + positions[0],
        bunny_pos[1] + positions[1]
    ]

    path = []
    col_eggs = 0

    while 0 <= row < size and 0 <= col < size:
        if matrix[row][col] == 'X':
            break


        col_eggs += int(matrix[row][col])
        path.append([row, col])

        row += positions[0]
        col += positions[1]

    if col_eggs >= collected_eggs:
        collected_eggs = col_eggs
        best_direction = direction
        best_path = path

print(best_direction)
print(*best_path, sep="\n")
print(collected_eggs)
