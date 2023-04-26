n = int(input("Digite o valor de n: "))

if n >= 0:

    fat = 1

    for i in range(1, n+1):

        fat*=i

print(fat)
