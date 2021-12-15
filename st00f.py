#1.
#iterable: a thing we can iterate over
#iterator: a special object with next() method.

x = [1, 2, 3, 4, 5]   #iterable.

for i in x:
    print(i)


#2.
#iterable: a thing we can iterate over
#iterator: a special object with next() method.

import itertools

x = [1, 2, 3, 4, 5]   #iterable.

n = itertools,itertools.cycle(x)   #iterator!

print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))


#3.
import itertools

x = [1, 2, 3, 4, 5]   #iterable.

n = itertools,itertools.cycle(x)   #iterator! ....also iterable.

for i in n:
    print(i)



#4.
import itertools

x = [1, 2, 3, 4, 5]   #iterable.

n = itertools,itertools.cycle(x)   #iterator!
 
y = iter(x)  #iterator .....also iterable.

for i in y:
    print(i)

      #OR

import itertools

x = [1, 2, 3, 4, 5]   #iterable.

n = itertools,itertools.cycle(x)   #iterator!
 
y = iter(x)  #iterator .....also iterable.


print(next(y))
print(next(y))
      
      #OR

import itertools

x = [1, 2, 3, 4, 5]   #iterable.

n = itertools,itertools.cycle(x)   #iterator!
 
y = iter(x)  #iterator .....also iterable.

next(y)

for i in y:
    print(i)







#5. (FINAL)

    import itertools

game = [[1, 0, 2],
        [2, 2, 2],
        [1, 2, 1],]

def win(current_game):
    #horizontal
    for row in game:
        print(row)
        if row.count(row[0]) == len(row) and row[0] != 0:
            print(f"player{row[0]} is the winner horizontally!")


    #diagonal
    diags = []
    for col, row in enumerate(reversed(range(len(game)))):
        diags.append(game[row][col])
    if diags.count(diags[0]) == len(diags) and diags[0] != 0:
        print(f"player{diags[0]} is the winner diagonally (/)!")

    diags = []
    for ix in range(len(game)):
        diags.append(game[ix][ix])
    if diags.count(diags[0]) == len(diags) and diags[0] != 0:
        print(f"player{diags[0]} is the winner diagonally (\\)!")


    #vertical
    for col in range(len(game)):
        check = []

        for row in game:
            check.append(row[col])

        if check.count(check[0]) == len(check) and check[0] != 0:
            print(f"player{check[0]} is the winner diagonally (|)!")


def game_board(game_map, player=0, row=0, column=0, just_display=False):
    try:
        print("   0  1  2")
        if not just_display:
            game_map[row][column] = player
        for count, row in enumerate(game_map):
            print(count, row)
        return game_map
    except IndexError as e:
        print("error: make sure you input row/column as 0 1 or 2?", e)
    except Exception as e:
        print("something went very wrong!", e)    


play = True
players = [1, 2]
while play:
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]

    game_won = False
    game = game_board(game, just_display=True)
    while not game_won:
        current_player = (player_choice)
        print(f"current_player: {current_player}")
        column_choice = int(input("what column do you want to pla?y? (0, 1, 2): "))
        row_choice = int(input("what row do you want to play? (0, 1, 2): "))
        game = game_board(game, current_player, row_choice, column_choice)    

#game = game_board(game, just_display=True)
#game = game_board(game_board, player=1, row=3, column=1)
