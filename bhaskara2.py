import math
a = float(input("Por favor, informe o valor de a: "))
b = float(input("Por favor, informe o valor de b: "))
c = float(input("Por favor, informe o valor de c: "))

discriminante = (b ** 2) - (4 * a * c)


if (discriminante == 0):
    raiz1 = (-b + math.sqrt(discriminante))/(2*a)
    print("a raiz desta equação é ", raiz1)
else:
    if discriminante < 0:
        print ("esta equação não possui raízes reais")
    else:
        raiz1 = ((- b) + math.sqrt(discriminante))/(2*a)
        raiz2 = ((- b) - math.sqrt(discriminante))/(2*a)
        
        if raiz1 < raiz2:
            print ("as raízes da equação são", raiz1, "e", raiz2)
        else:
            print ("as raízes da equação são", raiz2, "e", raiz1)
            
        


