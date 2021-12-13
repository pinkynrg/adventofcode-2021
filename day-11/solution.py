from time import sleep
import os


def print_matrix(lightmap, sleep_ms = 0):
    BOLD = '\033[1m'
    GRAY = '\033[2m'
    END = '\033[0m'
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in lightmap:
        for e in row:
            if e["energy"] == 0:
                print("{}{}{}".format(BOLD, e["energy"], END), end="")
            else:
                print("{}{}{}".format(GRAY, e["energy"], END), end="")
        print("")
    print("")
    sleep(sleep_ms/1000)

def safe_get(matrix, x, y, attr = None):
    if x >= len(matrix[0]) or x < 0:
        return None
    if y >= len(matrix) or y < 0:
        return None
    return matrix[y][x] if attr is None else matrix[y][x].get(attr)

def get_neightbors(x, y, amap):
    coordinates = [[x+0,y-1], [x+1,y-1], [x+1,y+0], [x+1,y+1], [x+0,y+1], [x-1,y+1], [x-1,y+0], [x-1,y-1]]
    results = []
    for coord in coordinates:
        results.append({"value": safe_get(amap, coord[0], coord[1]), "x": coord[0], "y": coord[1]})
    return results

def step(amap):
    return list(map(
        lambda row: list(map(lambda e: {**e, "energy": e["energy"]+1}, row)), 
        amap
    ))

def transfer(x, y, amap, flash_count):
    if amap[y][x]["energy"] > 9 and not amap[y][x]["flashed"]:
        amap[y][x]["flashed"] = True
        flash_count += 1
        neightbors = get_neightbors(x, y, amap)
        for n in neightbors:
            if n['value'] is not None:
                amap[n["y"]][n["x"]]["energy"] += 1
                [amap, flash_count] = transfer(n["x"],n["y"], amap, flash_count)
    return [amap, flash_count]

def flash(amap):
    return list(map(
        lambda row: list(map(lambda e: {"flashed": False, "energy": 0} if e["energy"] > 9 else e, row)), 
        amap
    ))

print("solution (part 1)")

f = open("./data.txt", "r")
data = f.read()
lightmap = [[{"energy": int(e), "flashed": False} for e in row] for row in data.split('\n')]                

flash_counts = 0
steps = 100
for _ in range(steps):
    lightmap = step(lightmap)
    for y, row in enumerate(lightmap):
        for x, e in enumerate(row):
            [lightmap, flash_counts] = transfer(x, y, lightmap, flash_counts)
    lightmap = flash(lightmap)
    print_matrix(lightmap)
print(flash_counts)

print("solution (part 2)")

lightmap = [[{"energy": int(e), "flashed": False} for e in row] for row in data.split('\n')]                

def all_flashing(amap):
    return all([all([e["energy"] == 0 for e in row]) for row in amap])

steps = 0
while not all_flashing(lightmap):
    lightmap = step(lightmap)
    for y, row in enumerate(lightmap):
        for x, e in enumerate(row):
            [lightmap, flash_counts] = transfer(x, y, lightmap, flash_counts)
    lightmap = flash(lightmap)
    steps += 1
    print_matrix(lightmap)

print(steps)
