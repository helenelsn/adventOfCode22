f = open("input.txt")
m = 0
L = []

for l in f :
    l = l[:-1] #.split()
    if l != "" :
        m += int(l)
    else :
        L.append(m)
        m = 0
L.append(m)
m = 0
for i in range(3) :
    #print(max(L))
    m += max(L)
    L.remove(max(L))
print(m)

#L.sort()
# print(sum(L[-3 : ]))