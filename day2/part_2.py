with open("input.txt", "r") as file:
    data = file.read()
input_array = data.split(",")
# delete this line below
# input_array = [input_array[4]]
# print(input_array)
agr = 0
fake = 0
sku_temp = 0
for interval in input_array:
    print(interval)
    interval_split = interval.split("-")

    for sku in range(int(interval_split[0]), int(interval_split[1]) + 1):
        sku_m = len(str(sku)) / 2
        print(f"evaluating {sku}")

        for part_length in range(1, int(sku_m) + 1):
            if sku_temp == sku:
                continue
            part_count = len(str(sku)) / part_length
            if part_count != int(part_count):
                continue
            print(
                f"we are braking it by part length {part_length}  to {part_count} parts"
            )
            fake = 1
            for part in range(part_length, len(str(sku)), part_length):
                print(
                    f"evaluating if {str(sku)[part - part_length : part]} is same as {str(sku)[part : part + part_length]}"
                )
                if (
                    str(sku)[part - part_length : part]
                    == str(sku)[part : part + part_length]
                ):
                    pass
                else:
                    fake = 0
            if fake == 1:
                agr += sku
                sku_temp = sku
                print(f"----->{sku} has been added")
print(agr)
