print("solution (part 1)")
f = open("./data.txt", "r")
data = f.read()
list_from_data = data.split(',')
initial_ages = [int(e) for e in list_from_data]

days = 80

ages = [e for e in initial_ages]

for e in range(0, days):
    new_born = filter(lambda age: age == 0, ages)
    ages = [6 if e == 0 else e-1 for e in ages]
    ages = ages + [8 for _ in new_born]

print(len(ages))

print("solution (part 2)")
f = open("./data.txt", "r")
data = f.read()
list_from_data = data.split(',')
initial_ages = [int(e) for e in list_from_data]

ages = [
    len(filter(lambda age: age == 0, initial_ages)), # 0
    len(filter(lambda age: age == 1, initial_ages)), # 1
    len(filter(lambda age: age == 2, initial_ages)), # 2
    len(filter(lambda age: age == 3, initial_ages)), # 3
    len(filter(lambda age: age == 4, initial_ages)), # 4
    len(filter(lambda age: age == 5, initial_ages)), # 5
    len(filter(lambda age: age == 6, initial_ages)), # 6
    int(0),                                          # 7
    int(0),                                          # 8
]

days = 256

for e in range(0, days):
    # new born added 
    cycled = ages[0]
    # age decrease
    ages[0] = ages[1]
    ages[1] = ages[2]
    ages[2] = ages[3]
    ages[3] = ages[4]
    ages[4] = ages[5]
    ages[5] = ages[6]
    ages[6] = ages[7] + cycled
    ages[7] = ages[8]
    ages[8] = cycled

print(ages[8]+ages[7]+ages[6]+ages[5]+ages[4]+ages[3]+ages[2]+ages[1]+ages[0])