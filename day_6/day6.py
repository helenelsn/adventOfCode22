#trouver la premiere sequence de 4 caracteres consecutifs différents 

f = open("input.txt")
print(f)
lines = f.readline()
str = []

def analyse_str(str) :
    count = 1
    for i in range(3) :
        if str[i] not in str[i+1:] :
            count += 1
            if count == 4 :
                return 1
    return 0

for i in range(len(lines)-3) :
    if analyse_str(lines[i:i+4]) :
        print(i+4) 
        break