import csv

with open("input.csv", newline="") as f:
    reader = csv.reader(f)
    data = list(reader)

output_list = []

agr = 50
cnt = 0
for x in data:
    print(x)
    if x[0][:1] == "L":
        agr -= int(x[0][1:])
        agr = agr % 100
    else:
        agr += int(x[0][1:])
        agr = agr % 100
    print(agr)
    if agr == 0:
        cnt += 1
print(cnt)
