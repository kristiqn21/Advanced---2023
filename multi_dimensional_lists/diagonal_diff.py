n = int(input())
matrix = [[int(el) for el in input().split(' ')] for _ in range(n)]

first = 0
second = 0

for i in range(n):
    first += matrix[i][i]
    second += matrix[n - 1 - i][i]

print(abs(first - second))