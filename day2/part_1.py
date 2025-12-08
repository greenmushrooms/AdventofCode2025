with open("input.txt", "r") as file:
    data = file.read()
input_array = data.split(",")
agr = 0
for interval in input_array:
    print(interval)
    interval_split = interval.split("-")
    for sku in range(int(interval_split[0]), int(interval_split[1]) + 1):
        sku_m = len(str(sku)) / 2
        if sku_m == int(sku_m) and str(sku)[: int(sku_m)] == str(sku)[int(sku_m) :]:
            agr += sku
            print(f"{sku} has been added")
print(agr)
