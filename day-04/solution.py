import functools

print("solution (part 1)")

f = open("./data.txt", "r")
data = f.read()
list_from_data = data.split('\n')

extractions = [int(e) for e in list_from_data[0].split(',')]

boards_section = filter(lambda x: x != '', list_from_data[2:])

boards = []
for index, e in enumerate(range(0, len(boards_section), 5)):
    board = []
    board_elements = boards_section[e:e + 5]
    for row in board_elements:
        row_elements = row.replace('  ',' ').strip().split(' ')
        row = [{"value": int(e), "extracted": False} for e in row_elements]
        board.append(row)
    boards.append(board)

winner_number = None
winner_board = None

for extracted in extractions:
    # updated boards for every extracted number
    for board in boards:
        for row in board:
            for element in row:
                if element['value'] == extracted:
                    element['extracted'] = True
    # check if there is a winning board
    for board in boards:
        for row in board:
            if all([e['extracted'] for e in row]):
                winner_number = extracted
                winner_board = board
                # print("winner row {} with number {}".format(row, winner_number))
                break
        for e in range(0,5):
            column = [row[e] for row in board]
            if all([e['extracted'] for e in column]):
                winner_number = extracted
                winner_board = board
                # print("winner column {} with number {}".format(column, winner_number))
                break
    # stop extracting
    if winner_number != None:
        break

# calculate score 
sum_not_extracted = 0
for row in winner_board:
    for e in row:
        if not e['extracted']:
            sum_not_extracted += e['value']

print(sum_not_extracted*winner_number)

print("solution (part 2)")

f = open("./data.txt", "r")
data = f.read()
list_from_data = data.split('\n')

extractions = [int(e) for e in list_from_data[0].split(',')]

boards_section = filter(lambda x: x != '', list_from_data[2:])

boards = []
for index, e in enumerate(range(0, len(boards_section), 5)):
    board = []
    board_elements = boards_section[e:e + 5]
    for row in board_elements:
        row_elements = row.replace('  ',' ').strip().split(' ')
        row = [{"value": int(e), "extracted": False} for e in row_elements]
        board.append(row)
    boards.append({"winning_number": None, "data": board})

winner_number = None
winner_boards = []

for extracted in extractions:
    # updated boards for every extracted number
    for board in boards:
        for row in board["data"]:
            for element in row:
                if element['value'] == extracted and not board["winning_number"]:
                    element['extracted'] = True
    # check if there is a winning board
    for board_index, board in enumerate(boards):
        for row in board["data"]:
            if all([e['extracted'] for e in row]):
                winner_number = extracted
                winner_board = board
                if not board["winning_number"]:
                    board["winning_number"] = winner_number
                    winner_boards.append(board_index)
                    # print("board {} won with {}".format(board_index, winner_number))

        for e in range(0,5):
            column = [row[e] for row in board["data"]]
            if all([e['extracted'] for e in column]):
                winner_number = extracted
                winner_board = board
                if not board["winning_number"]:
                    board["winning_number"] = winner_number
                    winner_boards.append(board_index)
                    # print("board {} won with {}".format(board_index, winner_number))

loser_board = boards[winner_boards[-1]]

# calculate score 
sum_not_extracted = 0
for row in loser_board["data"]:
    for e in row:
        if not e['extracted']:
            sum_not_extracted += e['value']

print(sum_not_extracted*loser_board['winning_number'])