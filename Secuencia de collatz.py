ultdigito = int(input("Ingrese el ultimo numero de su codigo"))

sumaultdig = ultdigito +3
n = 0

for i in range(1,ultdigito+1):
    i = int(input("Ingrese un numero"))
    n = n+i
z = n/ultdigito    
while ultdigito != 1:
    if ultdigito % 2 == 0:
        ultdigito //= 2
        print(ultdigito)
    else:
        ultdigito = (ultdigito*3) +1
    print,
    