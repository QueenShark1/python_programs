#1.
game = [[2, 0, 1],
        [2, 0, 0],
        [2, 2, 0],]

for row in game:
    print(row[0])
    


#2.
game = [[2, 0, 1],
        [1, 0, 1],
        [2, 2, 1],]

check = []

for row in game:
    #print(row[0])
    check.append(row[0])

if check.count(row[0]) == len(row) and row[0] != 0:
    print("winner!")



#3.
game = [[2, 0, 1],
        [1, 0, 0],
        [2, 2, 1],]

columns = [0, 1, 2]

for col in columns:
    check = []


for row in game:
    #print(row[col])
    check.append(row[0])

if check.count(row[0]) == len(row) and row[0] != 0:
    print("winner!")



#4.
game = [[2, 0, 1],
        [1, 0, 1],
        [2, 2, 1],]

for col in range(len(game)):
    check = []

    for row in game:
        check.append(row[col])

    if check.count(check[0]) == len(check) and check[0] != 0:
        print("winner!")

'''
def win(current_game):
    for row in game:
        print(row)
        if row.count(row[0]) == len(row) and row[0] != 0:
            print("winner")

win(game)
'''

#Vertical Winners-python3 programming tutorial p.11