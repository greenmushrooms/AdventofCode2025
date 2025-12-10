with open("input.txt", "r") as file:
    data = file.read()
battery_list = data.splitlines()
print(battery_list)
bank_length = len(battery_list[0])
agr = 0
for battery_bank in battery_list:
    b1 = 0
    b2 = 0
    bcount = 1
    for battery in battery_bank:
        bcount += 1
        if int(battery) > b1 and bcount <= bank_length:
            b1 = int(battery)
            b2 = 0
        elif int(battery) > b2:
            b2 = int(battery)
    agr += int(f"{b1}{b2}")
    print(f"{b1}{b2}")
print(agr)
