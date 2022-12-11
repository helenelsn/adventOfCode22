# X = lose
# Y = draw
# Z = win

f = open("input.txt")
m = 0

for l in f :
    player1, player2 = l[:-1].split()
    if (player2 == 'X') :
        m += (player1 == 'A') * 3 + (player1 == 'B') + (player1 == 'C') * 2
    elif (player2 == 'Y') :
        m += "0ABC".find(player1) + 3
    else :
        m += 6 + (player1 == 'A') * 2 + (player1 == 'B') * 3 + (player1 == 'C')
print(m)
    