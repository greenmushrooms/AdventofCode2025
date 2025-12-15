import numpy as np

with open("input.txt") as file:
    data = file.read()

data_list = data.splitlines()

matrix = []
for line in data_list:
    matrix.append(line.split())

# print(matrix[:-1])
num_array = np.array(matrix[:-1]).astype(int)
print("here")
# print(num_array)

print(num_array[:, 0])
i = 0
aggr = 0
for opperation in matrix[-1]:
    print(f"first item in sub list is {num_array[0][i]}")
    sub_aggr = num_array[0][i]
    for num in num_array[:, i]:
        if opperation == "*":
            print(f"multiply by {num}")
            sub_aggr *= num
        else:
            print(f"add {num}")
            sub_aggr += num
        print(f"we have {sub_aggr}")
    print(sub_aggr)
    aggr += sub_aggr
    i += 1

matrix = np.array(clean_list)
matrix = matrix[:,1:].astype(int)

print(matrix)