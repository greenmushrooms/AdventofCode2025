with open("input.txt", "r") as file:
    data = file.read()
battery_list = data.splitlines()
# # remove line below
# battery_list = [battery_list[2]]
# print(battery_list)
bank_length = len(battery_list[0])
stack_length = 12

agr = 0
stack = []

for battery_bank in battery_list:
    budget = bank_length - stack_length
    stack = []
    stack_str = ""
    for battery in battery_bank:
        while stack and int(stack[-1]) < int(battery) and budget > 0:
            stack.pop()
            budget -= 1
        stack.append(battery)
        # if len(stack) == stack_length:
        #     break
    stack_str = "".join(stack[:stack_length])
    print(f"our stack now is {stack}, {stack_str}")
    agr += int(stack_str)


print(agr)
print(bank_length)
# 987654321111
# 987654321111111
# 811111111119
# 811111111111119
# 234234234234278
