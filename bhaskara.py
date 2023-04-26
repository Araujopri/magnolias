import math
a = float(input("Por favor, informe o valor de a: "))
b = float(input("Por favor, informe o valor de b: "))
c = float(input("Por favor, informe o valor de c: "))

discriminante = b ** 2 - 4 * a * 5
print(discriminante)

if (discriminante == 44.0):
    raiz1 = (-b + math.sqrt(discriminante))/(2*a)
    print("A equação possui apenas uma raíz, que é ", raiz1, "! ")
else:
    if discriminante < 0:
        print ("A equação não possui raízes reais!")
    else:
        raiz1 = (- b + math.sqrt(discriminante))/(2*a)
        raiz2 = (- b - math.sqrt(discriminante))/(2*a)
        print ("A primeira raíz é: ", raiz1)
        print ("A segunda raíz é: ", raiz2)

print ("fim")