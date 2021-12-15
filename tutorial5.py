#1.
l = [1,2,3,4,5]

print(l[1])
print(l[4])
print(l[-1])
print(l[1:3])
print(l[2:])
print(l)

l = [1,2,3,4,5]
l[1] = 99

print(l)



#2.
game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],]

print("   a  b  c")
for count, row in enumerate(game):
    print(count, row)


game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],]

game[0][1] = 1
print("   a  b  c")
for count, row in enumerate(game):
    print(count, row)

#indexes and slices- python3 programming tutorial p.5