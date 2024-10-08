import math
# if, elif , else
# Creamos variables
a = 1
b = 2
if a>b:
    print("A es mayor que B") 
elif a<b:
    print("B es mayor que A")

# Asignando valores para tricotomia
a = input("Elige el valor de a: ")
b = input("Elige el valor de b: ")

if a>b: print("A es mayor que B") 
elif a<b:   print("B es mayor que A")
else:   print("B es igual a A")

# Usando conjunción y disunción "y" "o"

a = 1
b = 5
c = 3

if c>a and c>b:
    print("Es mayor que" ,a,b)
elif c>a or c>b:
    print(c, "es mayor que",b, "o" ,a)
    if c>a:
        print(c,"es mayor que",a)
    else:
        print(c, "es mayor que b",b)
else:
    print(c,"es mayor que",b,",",a)

# par y que tenga raiz cuadrada

a = int((input("Elige el valor de a: ")))
if a//2 == a/2:
    print(a, "es par")
else:
    print(a, "No es par")

if math.sqrt(a) //2:
    print(a,"Tiene raiz y es:",(math.sqrt(a)))
    if math.sqrt(a) == round(math.sqrt(a)):
        print("Entonces",a ,"tiene Raíz exacta")
    else:
        print("Entonces",a,"no tiene Raíz exacta")
    
