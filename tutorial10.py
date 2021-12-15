#1.
game = [[1, 1, 1],
        [0, 2, 0],
        [2, 2, 0],]

def win(current_game):
    for row in game:
        print(row)
        col1 = row[0]
        col2 = row[1]
        col3 = row[2]

        if col1 == col2 == col3:
             print("winner!!!")

win(game)             



#2.
game = [[1, 1, 1],
        [0, 2, 0],
        [2, 2, 0],]

def win(current_game):
    for row in game:
        print(row)
        all_match = True
        for iteam in row:
            print(iteam, row[0])
            if iteam != row[0]:
                all_match = False 
        if all_match:
            print("winner")

win(game)             



#3.
game = [[1, 0, 1],
        [0, 0, 0],
        [2, 2, 0],]

def win(current_game):
    for row in game:
        print(row)
        if row.count(row[0]) == len(row):
            print("winner")

win(game)



#4.
game = [[1, 0, 1],
        [0, 0, 0],
        [2, 2, 0],]

def win(current_game):
    for row in game:
        print(row)
        if row.count(row[0]) == len(row) and row[0] != 0:
            print("winner")

win(game)


#Calculating Horizontal Winner- python3 programming tutorial p.10