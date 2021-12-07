import statistics
import math

print("solution (part 1)")

f = open("./data.txt", "r")
data = f.read()
list_from_data = data.split('\n')

positions = [int(e) for e in list_from_data[0].split(',')]

median = statistics.median(positions)

fuel = 0

for position in positions:
    fuel += abs(position-median)

print(fuel)

print("solution (part 2)")

minimum = min(positions)
maximum = max(positions)

solutions = []

for e in range(minimum, maximum+1):
    fuel = 0
    for position in positions:
        distance = abs(position-e)
        fuel += distance * (distance + 1) // 2 
    solutions.append(fuel)

print(min(solutions))