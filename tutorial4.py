#1.
game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],]

print(" 0  1  2")
for row in game:
    print(row)


#2.
game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],]

print("   0  1  2")
count = 0
for row in game:
    print(count, row)
    count += 1

           #OR
#3.
game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],]

print("   0  1  2")
for count, row in enumerate(game):
    print(count, row)
    

#4.
game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],]

print("   0  1  2")
for count, row in enumerate(game):
    #print(count, row) adfl;gfdv;hdnp
    ''' multi line
    comment'''
    for iteam in row:
        print(iteam)


#5.
game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],]

print("   a  b  c")
for count, row in enumerate(game):
    print(count, row)

#built-in functions python3 programming tutorial p.4