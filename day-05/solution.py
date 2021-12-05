print("solution (part 1)")
f = open("./data.txt", "r")
data = f.read()
list_from_data = data.split('\n')

lines = []
for e in list_from_data:
    line = [[int(n) for n in point_string.split(',')] for point_string in e.split(' -> ')]
    lines.append(line)

board = [[0 for _ in range(0,1000)] for _ in range(0,1000)]

v_lines = filter(lambda line: line[0][0] == line[1][0], lines)
h_lines = filter(lambda line: line[0][1] == line[1][1], lines)

for line in v_lines:
    x = line[0][0]
    [y1,y2] = [line[0][1], line[1][1]+1] if line[0][1] < line[1][1] else [line[1][1], line[0][1]+1]
    for y in range(y1, y2):
        board[y][x] += 1

for line in h_lines:
    y = line[0][1]
    [x1,x2] = [line[0][0], line[1][0]+1] if line[0][0] < line[1][0]+1 else [line[1][0], line[0][0]+1]
    for x in range(x1,x2):
        board[y][x] += 1

intersections_count = 0

for line in board:
    for point in line:
        if point > 1:
            intersections_count += 1

print(intersections_count)

print("solution (part 2)")

def find_line_point(line):
    [x1,y1] = line[0]
    [x2,y2] = line[1]
    steps_count = abs(y2-y1) if x2-x1 == 0 else abs(x2-x1)
    x_step = (1 if x1 < x2 else -1) * (0 if x1 == x2 else 1)
    y_step = (1 if y1 < y2 else -1) * (0 if y1 == y2 else 1)
    points = []
    for step in range(0, steps_count+1):
        points.append([x1 + step * x_step, y1 + step * y_step])
    return points

board = [[0 for _ in range(0,1000)] for _ in range(0,1000)]

for line in lines:
    for point in find_line_point(line):
        board[point[0]][point[1]] += 1

intersections_count = 0

for line in board:
    for point in line:
        if point > 1:
            intersections_count += 1

print(intersections_count)