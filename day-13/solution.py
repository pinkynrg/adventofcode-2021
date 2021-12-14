print("solution (part 1)")

f = open("./data.txt", "r")
data = f.read()
[coordinates_data, fold_data] = data.split('\n\n')

coordinates = { "list": [], "object": {}}
for row in coordinates_data.split('\n'):
    [x, y] = row.split(',')
    if x not in coordinates['object']:
        coordinates['object'][x] = {}
    if y not in coordinates['object'][x]:
        coordinates['object'][x][y] = True
    coordinates['list'] += [{"x": int(x), "y": int(y)}]   

fold_rows = fold_data.split('\n') if fold_data else []
folds = []
for row in fold_rows:
    cleaned = row.replace('fold along ', '').split('=')
    folds += [{"type": cleaned[0], "value": int(cleaned[1])}]

def print_paper(paper):
    print("")
    for row in paper:
        print("".join(row))
    print("")

def create_paper(coordinates):
    width = max(map(lambda point: point["x"], coordinates['list']))
    height = max(map(lambda point: point["y"], coordinates['list']))
    paper = []
    for y in range(height+1):
        paper.append([])
        for x in range(width+1):
            paper[y].append("▓" if str(x) in coordinates['object'] and str(y) in coordinates['object'][str(x)] else "-")
    return paper

def fold_vertical(paper, fold):
    new_paper = []
    for y in paper:
        y[fold] = "|"
        [left, right] = ''.join(y).split("|")
        new_width = max(len(left), len(right))
        mirrored_right = right[::-1]
        new_row = []
        for x in range(0, new_width):
            left_point = left[x] if x < len(left) else "-"
            right_point = mirrored_right[x] if x < len(mirrored_right) else "-"
            point = "▓" if left_point == "▓" or right_point == "▓" else "-"
            new_row.append(point)
        new_paper.append(new_row)
    return new_paper

def fold_horizontal(paper, fold):
    new_paper = []
    top = paper[:fold]
    bottom = paper[fold+1:]
    width = len(paper[0]) if len(paper) > 0 else 0
    new_height = max(len(top), len(bottom))
    mirrored_bottom = bottom[::-1]
    for y in range(0, new_height):
        top_row = top[-(y+1)] if len(top)-y > 0  else ["-"] * width
        bottom_row = mirrored_bottom[-(y+1)] if len(mirrored_bottom)-y > 0  else ["-"] * width
        row = []
        for x in range(0, width):
            point = "▓" if top_row[x] == "▓" or bottom_row[x] == "▓" else "-"
            row.append(point)
        new_paper.append(row)
    return new_paper[::-1]

paper = create_paper(coordinates)
partial_folds = folds[:1]
for fold in partial_folds:
    if fold["type"] == "y":
        paper = fold_horizontal(paper, fold["value"])
    if fold["type"] == "x":
        paper = fold_vertical(paper, fold["value"])

hole_count = 0
for row in paper:
    for point in row:
        hole_count += 1 if point == "▓" else 0

print(hole_count)

print("solution (part 2)")

paper = create_paper(coordinates)

for fold in folds:
    if fold["type"] == "y":
        paper = fold_horizontal(paper, fold["value"])
    elif fold["type"] == "x":
        paper = fold_vertical(paper, fold["value"])

print_paper(paper)

    