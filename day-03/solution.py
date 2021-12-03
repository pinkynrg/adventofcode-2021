print("solution (part 1)")
f = open("./data.txt", "r")
data = f.read()
list_from_data = data.split('\n')

binary_length = 12
solution = [0] * binary_length

for index in range(binary_length):
    for e in list_from_data:
        if e[index] == '1':
            solution[index] = int(solution[index]) + 1
        if e[index] == '0':
            solution[index] = int(solution[index]) - 1

gamma = ''.join(['0' if e < 0 else '1' for e in solution])
epsilon = ''.join(['1' if e < 0 else '0' for e in solution])

print(int(gamma, 2) * int(epsilon, 2))

print("solution (part 2)")

temp = list_from_data

for index in range(12):
    helper = 0
    for e in temp:
        if e[index] == '1':
            helper = int(helper) + 1
        if e[index] == '0':
            helper = int(helper) - 1
    if helper < 0:
        temp = [e for e in temp if e[index] == '0']
    else:
        temp = [e for e in temp if e[index] == '1']

    if len(temp) == 1:
        break

oxy = int(temp[0], 2)

temp = list_from_data

for index in range(12):
    helper = 0
    for e in temp:
        if e[index] == '1':
            helper = int(helper) + 1
        if e[index] == '0':
            helper = int(helper) - 1
    if helper < 0:
        temp = [e for e in temp if e[index] == '1']
    else:
        temp = [e for e in temp if e[index] == '0']

    if len(temp) == 1:
        break

co2 = int(temp[0], 2)
print(oxy*co2)