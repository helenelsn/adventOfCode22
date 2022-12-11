f = open("input.txt")
Monkeys = []
current = []
count = 0

for i, l in enumerate(f) :
    l = l[:-1]
    if i % 7 == 0 :
        continue
    elif i % 7 == 1 :
        current.append([int(i)for i in (l[l.find(":")+1:].replace(",", " ").split())])
    elif i % 7 == 2 :
        current.append(l[l.find("old")+3:].split())
    elif i % 7 == 3 :
        current.append(int((l.split())[-1]))
    elif i % 7 == 4 :
        current.append(int((l.split())[-1]))
    elif i % 7 == 5 :
        current.append(int((l.split())[-1]))
    else :
        current.append(count)
        Monkeys.append(current)
        current = []

Monkeys.append(current)
print(Monkeys)
print("=================================")

worry = 0
for j in range(1) :
    for l in Monkeys :
        for i in l[0] :
            if l[1][1] == "old" :
                l[1][1] = i
            if l[1][0] == '+' :
                worry = i + int(l[1][1])
            else :  
                worry = i * int(l[1][1])
            worry//=3
            #print(l[0])
            print(i)
            print("=================================")
            #print(l[-2]-1)
            #l[0].pop(0)
            Monkeys[l[-3]-1][0].append(worry) if worry % l[2] == 0 else Monkeys[l[-2]-1][0].append(worry)
            l[-1] += 1
