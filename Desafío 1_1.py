ventas = int(input("Ingresa tu salario:"))
sueldo = ventas*1.1
print(f'salario total: {sueldo:.2f}')


catalogo_frutas = { 'naranja' : 8, 'sandia': 11, 'limon': 4 }
fruta = str(input('Ingresa nombre fruta: '))
catalogo_frutas.get(fruta, 'no esta')

import random 
dado1 = random.randint(1,6)
dado2 = random.randint(1,6) 
print (f'valor dado 1  : {dado1} \n  valor dado 2: {dado2} \n suma dados {dado1+dado2}       ')


calorias = int(input("ingresa tu límite de calorías"))
chocolate_cal = int(input('cuantas calorías tiene una porción de chocolate:'))
total = calorias/chocolate_cal
print(f'puedes comer {total} porciones de chocolate')