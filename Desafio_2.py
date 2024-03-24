
#Suma números pares

num1 = int(input("Ingresa el primer número"))
num2 = int(input("Ingresa el segundo número"))
list =range(num1, num2+1)
pares =[]
suma = 0
for numero in list:
    if numero % 2 ==0:
        pares.append(numero)
        suma +=numero

print (pares, suma )

#Calculadora de áreas

import math
print( math.pi())

figura = int (input("Ingresa el número correspondiente a la figura: \n  1: Cuadrado \n 2: circulo \n 3:Triangulo"))

if figura == 1 :
        
        medidas = int(input("Ingresa la medida de una cara del cuadrado:"))
        area = medidas* medidas
        print(f"el área del cuadro es {area}")
elif figura ==2:
        medidas = int(input("Ingresa el radio del circulo:"))
        area = 2*medidas* medidas* math.pi()
        print(f"el área del circulo es {area}")     
elif figura ==3:
        medidas = int(input("Ingresa la base del triangulo:"))
        medidas2 = int(input("Ingresa la altura del triangulo:"))
        area = medidas*  medidas2 /2
        print(f"el área del circulo es {area}")     
else: 
    print("Figura no identificada")


avance = 0  
while avance < 10: 
    vel = int(input("Ingresa el avance del caracol por metros: "))
    avance += vel 
    print ("_"*avance + "🐌")
print("llegó a la meta")