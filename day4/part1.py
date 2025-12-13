import numpy as np
import numpy.ma as ma

with open("input_sample.txt", "r") as file:
    data = file.read()
formated_data = data.replace(".", "0").replace("@", "1")
formated_list = formated_data.splitlines()

formated_matrix = []
for row in formated_list:
    formated_matrix.append(list(row))

matrix = np.array(formated_matrix).astype(int)


# print(matrix)
# print(f"line break")
counts = np.zeros_like(matrix, dtype=int)

counts[:-1, :] += matrix[1:, :]  # u
# print(counts)
counts[:-1, :-1] += matrix[1:, 1:]  # ul
# print(counts)
counts[:, :-1] += matrix[:, 1:]  # l
# print(counts)
counts[1:, :-1] += matrix[:-1, 1:]  # ld
# print(counts)

counts[1:, :] += matrix[:-1, :]  # d
# print(counts)

counts[1:, 1:] += matrix[:-1, :-1]  # dr
# print(counts)

counts[:, 1:] += matrix[:, :-1]  # r
# print(counts)

counts[:-1, 1:] += matrix[1:, :-1]  # ur
# print(counts)


matrix = matrix == 1

counts = counts < 4
print(counts)

countsx = counts * matrix
# print(counts)
aggr = 0
for r in countsx:
    for c in r:
        if c:
            aggr += 1

print(aggr)
