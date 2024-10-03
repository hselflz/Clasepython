x = 10 
y = "Ivan"
print(x,y)

x = str(3) #cambia a str
y = int(3.0) #cambia de float a str
z = float(3) # cambia a flotante 

print(type(x), type(y), type(z))

#Las variables cambian según si es mayus o no 

a = 4
A = "Sally"
# a no sobreescribira A

print(a,A)

# Tipo de casos para nombrar variables

#Caso Camel, la primera letra de la palabra es mayuscula, excepto la primera
myVariableName = "Nombre"

#Caso Pascal, Todas las primeras letras es mayuscula
MyVariableName = "Nombre"

#Caso serpiente, todas las palabras son en minusculas y separadas por guines bajos
my_name_variable = "Nombre"

# Se pueden asginar valores a variables con comas 
x , y ,z = "Orange" , "Banana", "Cherry"
print(x), print(y), print(z)
print(x,y,z)

# Se pueden agregar un mismo valor para las variables.
x = y = z = "Hola"
# Y cambiar el valor de una sola sin cambiar el valor de las demás, aunque algunas veces puede no ser asi.
x=1
print(x,y,z)
#Desempaquetado
fruits = ["Apple", "Orange", "Cherry"]
x, y ,z = fruits
print(x,y,z)

#Se pueden cancatenar las variables, solo se puede usar concatenacion
print(x+y+z)

#Hacer un programa "Calculadora simple", suma, resta, multiplicacion, potencia, modulo, 

var_1 = 4
var_2 = 8


var_3 = var_2+var_1
print("La suma de 8 y 4 es: ", var_3)

var_3 = var_2-var_1
print("La resta de 8 y 4 es: ",var_3)

var_3= var_2 * var_1 
print("La multiplicación de 8 y 4 es: ", var_3)

var_3= var_2/var_1
print("La división de 8 y 4 es: ", var_3)

primer_valor = int(input("Escribe el primer valor: "))
segundo_valor = int(input("Escrube tu segundo valor: "))

print("La suma de", primer_valor, "más", segundo_valor, "es: ")
print(primer_valor+segundo_valor)

print("La resta de", primer_valor, "menos", segundo_valor, "es: ")
print(primer_valor-segundo_valor)

print("La multiplicación de", primer_valor, "por", segundo_valor, "es: ")
print(primer_valor*segundo_valor)

print("La división de", primer_valor, "entre", segundo_valor, "es: ")
print(primer_valor/segundo_valor)

#Comparativo, para comparar 2 valores se utilizan 2 iguales ==
print(1 == 1)
print(2 == 4)

#Ejercicio por decima extra.
print(int(0.1+0.1+0.1) == int(0.3))

#existen y,o como en teoria de conjuntos and,or

resultado = (4>8) or (3>2)
print(resultado)

resultado = (True==1) and (False==4%2) #como true es 1 y false 0 entonces, es verdadero
print(resultado)

#Existe abs para valor absoluto , round para redondear
print("el valor absoluto de -13 es: ",abs(-13))
print("El redondeo de 3.123, es: ",round(3.123))

#if´s se utilizan con sangria
resultado = input("Escribe 1 o 2: ")
if resultado == "1":
    print("Hola")
elif resultado == "2":
    print("Adios")

"""Se pueden hacer comentario 
de multilineas usando 2 comillas"""