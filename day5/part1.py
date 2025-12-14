with open("input.txt") as file:
    data = file.read()
# print(data)
data_split = data.split("\n\n")

fresh_list = data_split[0].splitlines()

stuff = data_split[1].splitlines()
aggr = 0
for item in stuff:
    fresh = False
    for condition in fresh_list:
        con = condition.split("-")
        if int(item) >= int(con[0]) and int(item) <= int(con[1]):
            print(f"item {item} is fresh, its on this condition: {condition}")
            fresh = True
            aggr += 1
            break
print(aggr)
