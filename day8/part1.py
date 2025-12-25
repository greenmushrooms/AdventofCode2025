import numpy as np

with open("input_sample.txt") as file:
    data = file.read()


data_list = data.splitlines()
data_matrix = []
for line in data_list:
    line = line.split(",")
    data_matrix.append(line)

data_array = np.array(data_matrix).astype(int)
print(data_array)

data_array_size = len(data_array)


key_map = []
for i in range(data_array_size):
    for j in range(i+1,data_array_size):

        length = np.linalg.norm(data_array[i]-data_array[j])
        key_map.append([[i,j],length])

key_map.sort(key = lambda x: x[1])
print(key_map[:9])
key_map.sort(key = lambda x: x[0])
