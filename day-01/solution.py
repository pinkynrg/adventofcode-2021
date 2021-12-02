print("solution (part 1)")

f = open("./data.txt", "r")
data = f.read()
list_from_data = data.split('\n')
casted_list = [int(e) for e in list_from_data]

# part 1

increase = 0
decrease = 0

for index, _ in enumerate(casted_list):
    if index + 1 < len(casted_list):
        if casted_list[index] < casted_list[index + 1]: 
            increase += 1
        else:
            decrease += 1

print(increase)
print(decrease)

print("solution (part 2)")

increase = 0
decrease = 0

for index, _ in enumerate(casted_list):
    if index + 3 < len(casted_list):
        sliding_sum_a = casted_list[index] + casted_list[index+1] + casted_list[index+2]
        sliding_sum_b = casted_list[index+1] + casted_list[index+2] + casted_list[index+3]
        if sliding_sum_a < sliding_sum_b: 
            increase += 1
        else:
            decrease += 1

print(increase)
print(decrease)