with open("input.txt") as file:
    data = file.read()
# print(data)
data_split = data.split("\n\n")

fresh_list = data_split[0].splitlines()

stuff = data_split[1].splitlines()

condition_list = []
for range in fresh_list:
    new_range = []
    for item in range.split("-"):
        new_range.append(int(item))
    # print(new_range)
    condition_list.append(new_range)

condition_list.sort()
# print(condition_list)
i = 1
condition_previous = condition_list[0]
for condition in condition_list[1:]:
    # print(f"evaluating if {condition_previous[1]} is greater then {condition[0]}")
    if condition_previous[1] >= condition[0]:
        print(f"evaling if condition_list[")
        if condition_list[i - 1][1] < condition[1]:
            condition_list[i - 1][1] = condition[1]
        condition_list.pop(i)

    else:
        i += 1
        condition_previous = condition

print(condition_list)

aggr = 0
for condtion in condition_list:
    aggr += condtion[1] - condtion[0] + 1
print(aggr)
