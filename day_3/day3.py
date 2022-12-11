f = open("input.txt")
m = 0

for l in f :
    compartment1, compartment2 = l[:len(l)//2], l[len(l)//2:-1]
    for a in compartment1 :
        if a in compartment2 :
            m += (ord(a) - ord('a') + 1) if a.islower() else (ord(a) - ord('A') + 27)
            break
print(m)
