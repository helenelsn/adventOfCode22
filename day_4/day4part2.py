f = open("input.txt")
m = 0

for l in f :
    a, b, c, d = map(int, l.replace(',','-').split('-'))
    for i in range(a, b+1) :
        if i in range(c, d+1) :
            m += 1
            break
print(m)