print("solution (part 1)")

f = open("./data.txt", "r")
data = f.read()
lines = [row for row in data.split('\n')]
closings = {"(": ")", "[": "]", "{": "}", "<": ">"}

error_weight = {")": 3, "]": 57, "}": 1197, ">": 25137}

errored = []
for line in lines: 
    accumulator = []
    for e in line:
        if e in ["(", "[", "{", "<"]:
            accumulator.append(e)
        elif closings[accumulator.pop()] != e:
            errored.append(e)
            break

print(sum([error_weight[error] for error in errored]))

print("solution (part 2)")

score_weight = {")": 1, "]": 2, "}": 3, ">": 4}

incompletes = []
for line in lines: 
    accumulator = []
    for e in line:
        if e in ["(", "[", "{", "<"]:
            accumulator.append(e)
        elif closings[accumulator.pop()] != e:
            accumulator = []
            break
    
    if len(accumulator):
        incompletes.append([closings[e] for e in accumulator][::-1])

scores = []
for incomplete in incompletes:
    local_score = 0
    for e in incomplete:
        local_score = local_score * 5 + score_weight[e]
    scores.append(local_score)

print(sorted(scores))
print(sorted(scores)[len(scores)//2])
