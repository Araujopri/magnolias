import math
x1 = int(input("Informe a coordenada x1 do plano cartesiano: "))
y1 = int(input("Informe a coordenada y1 do plano cartesiano: "))
x2 = int(input("Informe a coordenada x2 do plano cartesiano: "))
y2 = int(input("Informe a coordenada y2 do plano cartesiano: "))
d2ps= math.sqrt(((x1-x2)**2)+((y1-y2)**2))
print (d2ps)
if d2ps >= 10:
    print ("longe")
else:
    print ("perto") 

