#trouver la premiere sequence de 4 caracteres consecutifs différents 

f = open("day_6/input2.txt")
lines = f.readlines()
count = 0
str = []

def analyse_str(str) :
    for i, c in enumerate(str) :
        print()
        if c not in str[i:] :
            return 1
    return 0

for c in lines :
    #j = i + 4
    print(c)
    if analyse_str(lines[i:i+4]) :
        
        break 
