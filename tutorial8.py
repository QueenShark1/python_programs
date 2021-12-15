#1.
game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],]

def game_board(player=0, row=0, column=0, just_display=False):
    print("   0  1  2")
    if not just_display:
        game[row][column] = player
    for count, row in enumerate(game):
        print(count, row)

game_board()


#2.
game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],]

def game_board(player=0, row=0, column=0, just_display=False):
    print("   0  1  2")
    if not just_display:
        game[row][column] = player
    for count, row in enumerate(game):
        print(count, row)

print(game)
game_board(player=1, row=1, column=1)
print(game)


#3.
game = "I want to play a game"
print(id(game))
def game_board(player=0, row=0, column=0, just_display=False):
    game = "A game"
    print(id(game))
    print(game)
print(game)
game_board()
print(game)
print(id(game))


#4
game = "I want to play a game"
print(id(game))
def game_board(player=0, row=0, column=0, just_display=False):
    game = "A game"
    print(id(game))
    print(game)
print(game)
game_board()
print(game)
print(id(game))


#5.
game = [1, 2, 3]
print(id(game))
def game_board(player=0, row=0, column=0, just_display=False):
    game[1] = 99
    
game_board()
print(game)
print(id(game))


#6.
x = 1
def test():
    x = 2
test()
print(x)


x = 1
def test():
    global x
    x = 2
test()
print(x)


#7.
game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],]

def game_board(game_map, player=0, row=0, column=0, just_display=False):
    print("   0  1  2")
    if not just_display:
        game_map[row][column] = player
    for count, row in enumerate(game_map):
        print(count, row)
    return game_map

game = game_board(game, just_display=True)
game = game_board(game, player=1, row=2, column=1)

#Mutability revisited- python3 programming tutorial p.8