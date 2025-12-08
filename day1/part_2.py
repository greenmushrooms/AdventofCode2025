import csv

with open("input.csv", newline="") as f:
    reader = csv.reader(f)
    data = list(reader)

output_list = []

agr = 50
cnt = 0
for x in data:
    print(f"turning {x}")
    distance = int(x[0][1:])
    if distance == 0:
        print("pass")
        continue

    if x[0][:1] == "L":
        if distance >= agr:
            if agr != 0:
                cnt += 1
                distance -= agr
            cnt += int(distance / 100)
            agr = 0
        agr -= distance
    else:
        if distance >= 100 - agr:
            if agr != 0:
                cnt += 1
                distance -= 100 - agr

            print(f"distiance is {distance} agr is {agr} adding {int(distance / 100)}")
            cnt += int(distance / 100)
            agr = 0
        agr += distance
    print(f"possition at {agr}||{agr % 100}")
    agr = agr % 100
    print(f"current count {cnt}")
print(cnt)
