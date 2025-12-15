import numpy as np

lines = []
with open('input.txt') as f:
    for line in f:
        lines.append(line.rstrip('\n'))  # strip newline first

# Pad all lines to same length, then add newline back
max_len = max(len(line) for line in lines)
lines = [line.ljust(max_len) + '\n' for line in lines]

# Your rotation (unchanged)
rotated_data = [] 
cols = zip(*lines)
for col in list(cols)[::-1]:
    rotated_data.append(''.join(col))

# Your parsing (unchanged)
sub_list = []
operation_array = [] 
clean_list = [] 
for item in rotated_data.copy():
    if item[-1] == '+' or item[-1] == '*':
        sub_list.append(item[:-1])
        clean_list.append(sub_list)
        operation_array.append(item[-1])
        sub_list = []
        continue
    sub_list.append(item)

# Your calculation (fixed slice -> matrix[i])
matrix = np.array(clean_list)
matrix = matrix[:,1:].astype(int)

i = 0 
aggr = 0 
for operation in operation_array:
    sub_aggr = matrix[i][0]
    for num in matrix[i][1:]:  # fixed: was matrix[i, :] which double-counts first
        if operation == "*":
            sub_aggr *= num
        else:
            sub_aggr += num
    aggr += sub_aggr
    i += 1   
print(aggr)