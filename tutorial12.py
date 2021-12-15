#1.
game = [[1, 0, 2],
        [1, 1, 0],
        [2, 2, 1],]


if game[0][0] == game[1][1] == game[2][2]:
    print("winner")
if game[2][0] == game[1][1] == game[0][2]:
    print("winner")


#2.
game = [[1, 0, 2],
        [1, 1, 0],
        [2, 2, 1],]

diags = []
for ix in range(len(game)):
    diags.append(game[ix][ix])
print(diags)
    
    #if game[2][0] == game[1][1] == game[0][2]:
    #print("winner")


'''
for col in range(len(game)):
    check = []

    for row in game:
        check.append(row[col])

    if check.count(check[0]) == len(check) and check[0] != 0:
                print("winner!")
'''



'''
def win(current_game):
    for row in game:
        print(row)
        if row.count(row[0]) == len(row) and row[0] != 0:
            print("winner")

win(game)
'''


#3.
game = [[1, 0, 2],
        [1, 1, 0],
        [2, 2, 1],]

for i in reversed(range(len(game))):
    print(i)

'''
diags = []
for ix in range(len(game)):
    diags.append(game[ix][ix])
'''

#4.
game = [[1, 0, 2],
        [1, 1, 0],
        [2, 2, 1],]

cols = list(reversed(range(len(game))))
rows = range(len(game))

for idx in rows:
    print(idx, cols[idx])


#OR IN MORE SIMPLEST WAY

game = [[1, 0, 2],
        [1, 1, 0],
        [2, 2, 1],]

for col, row in enumerate(reversed(range(len(game)))):
    print(col, row)



#5.
game = [[1, 0, 2],
        [1, 2, 0],
        [2, 2, 1],]

diags = []
for col, row in enumerate(reversed(range(len(game)))):
    diags.append(game[row][col])

print(diags)

              #and

game = [[1, 0, 2],
        [1, 2, 0],
        [2, 2, 1],]

diags = []
for col, row in enumerate(reversed(range(len(game)))):
    diags.append(game[row][col])

diags = []
for ix in range(len(game)):
    diags.append(game[ix][ix])

#diagonal winning algo- python3 programming tutorial p.12