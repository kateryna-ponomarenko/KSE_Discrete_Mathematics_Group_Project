import time
start = time.perf_counter()

INF = 10**9

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
            if r == INF:
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

end = time.perf_counter()
print("Time of work: ", end - start, "seconds" )

