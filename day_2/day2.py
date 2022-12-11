# A et X = rock
# B et Y = paper
# C et Z = scissors

f = open("input.txt")
m = 0

for l in f :
    player1, player2 = l[:-1].split()
    m += "0XYZ".find(player2)
    if ((player1 == 'A' and player2 == 'Y') or (player1 == 'B' and player2 == 'Z') or (player1 == 'C' and player2 == 'X')) :
        m += 6
    elif ("0ABC".find(player1) == "0XYZ".find(player2)) :
        m += 3
print(m)
