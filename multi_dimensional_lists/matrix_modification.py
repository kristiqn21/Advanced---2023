size = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(size)]

command = input().split()

while command[0] != 'END':
    command_type, row, col, num = command[0], int(command[1]), int(command[2]), int(command[3])

    if not (0 <= row <= size and 0 <= col <= size):
        print("Invalid coordinates")
    elif command_type == 'Add':
        matrix[row][col] += num
    elif command_type == 'Subtract':
        matrix[row][col] -= num

    command = input().split()

[print(*row) for row in matrix]