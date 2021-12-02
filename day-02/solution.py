print("solution (part 1)")

f = open("./data.txt", "r")
data = f.read()
list_from_data = data.split('\n')

y = 0
x = 0

for e in list_from_data: 
    [action, str_value] = e.split(' ')
    value = int(str_value)
    if action == 'forward':
        x += value
    if action == 'up':
        y -= value
    if action == 'down':
        y += value

result = x * y
print(result)

print("solution (part 2)")

f = open("./data.txt", "r")
data = f.read()
list_from_data = data.split('\n')

y = 0
x = 0
aim = 0

for e in list_from_data: 
    [action, str_value] = e.split(' ')
    value = int(str_value)
    if action == 'forward':
        x += value
        y += aim * value
    if action == 'up':
        aim -= value
    if action == 'down':
        aim += value

result = x * y
print(result)