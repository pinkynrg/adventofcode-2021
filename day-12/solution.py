print("solution (part 1)")

f = open("./data.txt", "r")
data = f.read()
connections = [row for row in data.split('\n')]

graph = {}
for connection in connections:
    [a1, b1] = connection.split('-')
    [a2, b2] = reversed(connection.split('-'))
    if a1 not in graph:
        graph[a1] = []
    if a2 not in graph:
        graph[a2] = []
    graph[a1] += [b1]
    graph[a2] += [b2]

def is_large(name):
    return True if name == name.upper() else False

def find_paths(graph, start, path = []):
    path = [*path, start]
    good_directions = [] if start == 'end' else [e for e in filter(lambda x: is_large(x) or x not in path, graph[start])]
    if len(good_directions) == 0:
        return path
    elif len(good_directions) == 1:
        return find_paths(graph, good_directions[0], path)
    else:
        fork = []
        for direction in good_directions:
            result = find_paths(graph, direction, path)
            if isinstance(result[0], list):
                fork += result
            else:
                fork += [result]
        return fork
    
ending_path = list(filter(lambda x: x[-1] == 'end', find_paths(graph, 'start')))
print(len(ending_path))

print("solution (part 2)")

def find_paths_with_jolly(graph, start, jolly, jolly_visited=0, path = []):
    path = [*path, start]
    good_directions = [] if start == 'end' else [e for e in filter(lambda x: is_large(x) or x not in path or (jolly == x and jolly_visited < 2), graph[start])]
    if len(good_directions) == 0:
        return path
    elif len(good_directions) == 1:
        direction = good_directions[0]
        local_jolly_visited = jolly_visited + 1 if jolly == direction else jolly_visited
        return find_paths_with_jolly(graph, direction, jolly, local_jolly_visited, path)
    else:
        fork = []
        for direction in good_directions:
            local_jolly_visited = jolly_visited + 1 if jolly == direction else jolly_visited
            result = find_paths_with_jolly(graph, direction, jolly, local_jolly_visited, path)
            if isinstance(result[0], list):
                fork += result
            else:
                fork += [result]
        return fork

small_caves = [e for e in graph.keys() if e != 'start' and e != 'end' and not is_large(e)]
solutions = []
for small_cave in small_caves:
    paths = list(filter(lambda x: x[-1] == 'end', find_paths_with_jolly(graph, 'start', small_cave)))
    for path in paths:
        solution = ','.join(path)
        if solution not in solutions:
            solutions.append(solution)

print(len(solutions))