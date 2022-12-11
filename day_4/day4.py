f = open("input.txt")
m = 0

for l in f :
    a, b, c, d = map(int, l.replace(',','-').split('-')) #map : applique a tous les params de la liste
    if all(x in range(a, b+1) for x in range(c, d+1)) or all(x in range(c, d+1) for x in range(a, b+1)) :
        m += 1
print(m)