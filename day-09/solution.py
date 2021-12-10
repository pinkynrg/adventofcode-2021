from math import prod
from time import sleep

print("solution (part 1)")

f = open("./data.txt", "r")
data = f.read()
heatmap = [[int(e) for e in row] for row in data.split('\n')]

def safe_get(matrix, x, y, attr = None):
    if x >= len(matrix[0]) or x < 0:
        return None
    if y >= len(matrix) or y < 0:
        return None
    return matrix[y][x] if attr is None else matrix[y][x].get(attr)

score = 0
for y, row in enumerate(heatmap):
    for x, char in enumerate(row):
        current = heatmap[y][x]
        neightbors = [
            safe_get(heatmap, x + 0, y - 1),
            safe_get(heatmap, x + 1, y - 1),
            safe_get(heatmap, x + 1, y + 0),
            safe_get(heatmap, x + 1, y + 1),
            safe_get(heatmap, x + 0, y + 1),
            safe_get(heatmap, x - 1, y + 1),
            safe_get(heatmap, x - 1, y + 0),
            safe_get(heatmap, x - 1, y + 0),
            safe_get(heatmap, x - 1, y - 1),
        ]
        if all([(neightbor is not None and neightbor > current) or neightbor is None for neightbor in neightbors]):
            score += (1 + current)

print(score)

print("solution (part 2)")

basins = []

def print_matrix(heatmap, sleep_time=0, name_filter=None):
    RED = '\033[95m'
    BOLD = '\033[1m'
    GRAY = '\033[2m'
    END = '\033[0m'
    for row in heatmap:
        for e in row:
            if e['basin'] and (name_filter is None or name_filter is not None and e['name'] in name_filter):
                if e['basin'] == 1:
                    print("{}{}{}".format(RED, e['value'], END), end="")
                else:
                    print("{}{}{}".format(BOLD, e['value'], END), end="")
            else:
                print("{}{}{}".format(GRAY, e['value'], END), end="")
        print("")
    print("")
    sleep(sleep_time/1000)

def get_neightbors(x, y, heatmap):
    return [
        {"value": safe_get(heatmap, x + 0, y - 1, "value"), "basin": safe_get(heatmap, x + 0, y - 1, "basin"), "x": x+0, "y": y-1},
        {"value": safe_get(heatmap, x + 1, y + 0, "value"), "basin": safe_get(heatmap, x + 1, y + 0, "basin"), "x": x+1, "y": y+0},
        {"value": safe_get(heatmap, x + 0, y + 1, "value"), "basin": safe_get(heatmap, x + 0, y + 1, "basin"), "x": x+0, "y": y+1},
        {"value": safe_get(heatmap, x - 1, y + 0, "value"), "basin": safe_get(heatmap, x - 1, y + 0, "basin"), "x": x-1, "y": y+0},
    ]

def analyze(x, y, heatmap):
    neightbors = get_neightbors(x, y, heatmap)
    name = 'basin-{}-{}'.format(x,y)
    size = 0
    if all([(neightbor['value'] is not None and neightbor['value'] > heatmap[y][x]['value']) or neightbor['value'] is None for neightbor in neightbors]):
        heatmap[y][x]['basin'] = 1
        heatmap[y][x]['name'] = name
        [heatmap, name, size] = mark_basins(x, y, heatmap, name)
    return [heatmap, name, size]


def mark_basins(x, y, heatmap, name, size = 1):
    neightbors = get_neightbors(x, y, heatmap)
    changed = []
    for neightbor in neightbors:
        if neightbor['value'] is not None and neightbor['basin'] is None and neightbor['value'] > heatmap[y][x]['value'] and neightbor['value'] < 9:
            heatmap[neightbor["y"]][neightbor["x"]]['name'] = name
            heatmap[neightbor["y"]][neightbor["x"]]['basin'] = size + 1
            changed.append(neightbor)
    for change in changed:
        [heatmap, name, size] = mark_basins(change["x"], change["y"], heatmap, name, size + 1)
    return [heatmap, name, size]

f = open("./data.txt", "r")
data = f.read()
heatmap = [[{"value": int(e), "name": None, "basin": None} for e in row] for row in data.split('\n')]

for y, _ in enumerate(heatmap):
    for x, _ in enumerate(row):
        [heatmap, name, size] = analyze(x, y, heatmap)
        if size > 0:
            basins.append({"name": name, "size": size})

sorted = sorted(basins, key=lambda x: x["size"], reverse=True)
print(len(sorted))
print(sorted[0:3])
print_matrix(heatmap, 0, [e['name'] for e in sorted[0:3]])
print(prod([e['size'] for e in sorted[0:3]]))


