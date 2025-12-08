import random
INF = 10**9

def shortest_path(i, j, k):
    if k == 0:
        return matrix[i][j]
    # рекурсивна формула Флойда:
    # d_k(i,j) = min(d_{k-1}(i,j), d_{k-1}(i,k) + d_{k-1}(k,j))
    return min(
        shortest_path(i, j, k-1),
        shortest_path(i, k, k-1) + shortest_path(k, j, k-1)
    )

def print_matrix():
    dist = [[INF] * v for _ in range(v)]
    for i in range(v):
        for j in range(v):
            if i == j:
                dist[i][j] = 0
            elif matrix[i][j] == 1:
                dist[i][j] = 1
            else:
                dist[i][j] = INF

    for k in range(v):
        for i in range(v):
            for j in range(v):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    print("Матриця найкоротших шляхів: ")

    for row in dist:
        for i, r in enumerate(row):
            if r == INF or r == 0:
                row[i] = "/"

        print(*row)

with open('math.txt', 'r') as file:
    line = file.readline()
    line_without_spaces = line.replace(' ', '').strip()
    v = len(line_without_spaces)

    matrix = [[0 for _ in range(v)] for _ in range(v)]

    matrix[0] = [int(ch) for ch in line_without_spaces]

    for i in range(1, v):
        new_line = file.readline()
        if not new_line:
            raise ValueError

        new_line_without_spaces = new_line.replace(' ', '').strip()
        new_line_without_spaces = new_line_without_spaces[:v]

        lst = [int(ch) for ch in new_line_without_spaces]
        if len(lst) < v:
            raise ValueError

        matrix[i] = lst

print_matrix()
