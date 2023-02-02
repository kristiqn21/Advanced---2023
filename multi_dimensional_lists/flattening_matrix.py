# matrix = [[int(el) for el in input().split(', ')] for _ in range(int(input()))]
# result = [num for row in matrix for row in num]

number_rows = int(input())
matrix = []

for row in range(number_rows):
    row_data = list(map(int, input().split(', ')))
    matrix.append(row_data)

result = [num for row in matrix for num in row]
print(result)