import numpy as np
with open('input.txt') as f:
    lines = []
    for line in f:
        stripped = line.rstrip('\n')
        lines.append(stripped)

max_len = max(len(line) for line in lines)
lines = [line.ljust(max_len) + '\n' for line in lines]

rotated_data = [] 
cols = zip(*lines)
for col in list(cols)[::-1]:
    rotated_data.append(''.join(col))


sub_list = []
operation_array = [] 
clean_list = [] 
for item in rotated_data:
    # print(f"evaluating {item}")
    if item[-1] == '+' or item[-1] == '*':
        sub_list.append(item[:-1])
        clean_list.append(sub_list)
        operation_array.append(item[-1])
        sub_list = []
        continue
    sub_list.append(item)

print(clean_list)

new_list = [] 
for line in clean_list:
    new_list.append(line[1:])
print(new_list)


aggr = 0
for pos, operation in enumerate(operation_array):

    clean_nums = [x for x in new_list[pos] if x.strip()] 
    
    if not clean_nums: continue # Skip if empty

    nums = [int(x) for x in clean_nums]  
    sub_aggr = nums[0]
    
    for num in nums[1:]:
        if operation == "*":
            sub_aggr *= num
        else:
            sub_aggr += num
    aggr += sub_aggr

print(aggr)

print(aggr)
# 11744694221048
# 11744694221048
# 11744693538946