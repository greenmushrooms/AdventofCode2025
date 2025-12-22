import numpy as np

with open("input.txt") as file:
    data = file.read()

data_list = data.splitlines()

matrix = []
for string_line in data_list:
    list_line = []
    for char in string_line:
        list_line.append(char)
    matrix.append(list_line)

tree_array = np.array(matrix)

print(tree_array[0])
previous_line = (tree_array[0] == 'S').astype(int)
print(previous_line)
splits = 0
for line in tree_array[1:]:

    line = (line == '^')

    hits = previous_line * line
    # splits += sum((np.append(hits[1:],False) + np.append(False,hits[:-1])))
    splits = sum(previous_line)
    # print(splits)
    previous_line = (np.append(hits[1:],False) + np.append(False,hits[:-1])) + (previous_line ^ hits)
    print(previous_line)

print(splits)
