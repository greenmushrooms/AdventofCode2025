import numpy as np
import numpy.ma as ma

with open("input.txt", "r") as file:
    data = file.read()
formated_data = data.replace(".", "0").replace("@", "1")
formated_list = formated_data.splitlines()

formated_matrix = []

aggr = 0
count = 0
for row in formated_list:
    formated_matrix.append(list(row))

matrix = np.array(formated_matrix).astype(int)

last = 1
while count < 121 and last != aggr:
    last = aggr
    count += 1
    counts = np.zeros_like(matrix, dtype=int)

    counts[:-1, :] += matrix[1:, :]  # u
    counts[:-1, :-1] += matrix[1:, 1:]  # ul
    counts[:, :-1] += matrix[:, 1:]  # l
    counts[1:, :-1] += matrix[:-1, 1:]  # ld
    counts[1:, :] += matrix[:-1, :]  # d
    counts[1:, 1:] += matrix[:-1, :-1]  # dr
    counts[:, 1:] += matrix[:, :-1]  # r
    counts[:-1, 1:] += matrix[1:, :-1]  # ur

    matrix = matrix == 1

    counts = counts < 4

    countsx = counts * matrix

    # print(matrix)
    # print("-------------")

    for r in countsx:
        for c in r:
            if c:
                aggr += 1

    matrix[countsx] = 0
    print(aggr)
