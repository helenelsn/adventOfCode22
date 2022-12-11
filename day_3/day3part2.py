f = open("input.txt")
m = 0
L = []

for i, line in enumerate(f) :
    L.append(line[:-1])
    if i % 3 == 2 :
        for a in L[0] :
            if a in L[1] and a in L[2] :
                m += (ord(a) - ord('a') + 1) if a.islower() else (ord(a) - ord('A') + 27)
                break
        L.clear()
print(m)
    