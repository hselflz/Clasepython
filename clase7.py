#Funciones lamda

potencia = lambda b:b**2
print(potencia(5))

suma = lambda b,a : a+b
print(suma(2,3))

def funcion_1 (n):
    return lambda a:a*n

dobles = funcion_1(5)
print(dobles(2))
#Lo que hace es multiplicar a por n donde a es el parametro de "dobles"

triple = funcion_1(3)
print(triple(100))

def ordenada(a,b):
    return lambda x:a*x+b

recta = ordenada(2,-1)
print(recta(0))

recta = ordenada(2,-1)
for i in range(10):
    print("y= ", recta(i))

recta = ordenada (2,-1)
valores = []
for i in range(10):
    print(valores,i)
    valores.append(recta(i))
print(valores,i+1)

# Diccionarios 
dic = {} #Diccionario vacio
dic = {"Uno":5,
       "Dos":"Valor 2",
       "Tres":[1,2,3],
       "Cuatro":True,
       "Cuatro":25.3} #Cuando se tienen dos "Definiciones" imprime una de las 2
print(dic)
print(list(dic.keys()))

valores =list(dic.values()) 
print(valores[0])

valores =list(dic.values()) 
print(len(valores[1]),valores[1])

print(dic["Uno"])
print(dic["Dos"])
print(dic["Tres"])
print(dic["Cuatro"])

dic["Uno"] = "Hola que tal"
print(dic["Uno"])

dic["Cinco"] = {"L1":5, "L2":54}
print(dic)

#Ejercicio hacer un diccionario 

import pandas as pd

datos = {
    'Nombre':['Juan', 'Pedro', 'Jorge', 'Isaac', 'Nataly','Dana'],
    'Ocupacion': ['Estudia', 'Trabaja', 'Trabaja','Estudia', 'Estudia', 'Estudia'],
    "Estado civil": ["Soltero", 'Casado', 'Divorciado', 'Viudo', 'Soltero', 'Casado'],}
print(datos)

dataframe = pd.DataFrame(datos)
dataframe.to_csv('DatosDic.csv')







#Ejercicio 
import pandas as pd
basedata = {1,2,3}
datos = {
    "Nombre":['Juan', 'Maria', 'Pedro', 'Luisa'],
    'Edad': [25,28,22,30 ],
    'Ciudad': ['Madrid','Barcelona','Valencia','Sevilla']}

#Crear dataframe a partir del diccionario
dataframe = pd.DataFrame(datos)
dataframe.to_csv('DatosDic.csv')