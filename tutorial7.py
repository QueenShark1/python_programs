#1.
def addition(x, y):
    return x+y

print(addition(5,3))
        
         #OR

z = (addition(5,3))

print(z)

         #OR

z = (addition("hey", " there"))

print(z)


game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],]


def game_board(player, row, column):
    print("   0  1  2")
    for count, row in enumerate(game):
            print(count, row)

game_board(player=1, row=2, column=0)
#game[0][1] = 1
#game_board()


#2.
def game_board(player=0, row=0, column=0):
    print("   0  1  2")
    game[row][column] = player
    for count, row in enumerate(game):
            print(count, row)

game_board()
game_board(player=1, row=2, column=1)
#game[0][1] = 1
#game_board()
                         #OR

#3.
def game_board(player=0, row=0, column=0,):
    print("   0  1  2")
    if player != 0:
        game[row][column] = player
    for count, row in enumerate(game):
            print(count, row)

game_board()
game_board(player=1, row=2, column=1)
#game[0][1] = 1
#game_board()

#4.
game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],]

def game_board(player=0, row=0, column=0, just_display=False):
    print("   0  1  2")
    if not just_display:
        game[row][column] = player
    for count, row in enumerate(game):
        print(count, row)

game_board(just_display=True)
game_board(player=1, row=2, column=1)
#game[0][1] = 1
#game_board()


#function parameters and typing- python3 programming tutorial p.7