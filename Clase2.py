cadena1= "Hola,mundo"
cadena2 = "Python es genial"

print(cadena1)
print(cadena2)

nueva_cadena = cadena2.replace("genial" , "Increible")

print(nueva_cadena)

print(cadena1,"y",cadena2)

Char = "Char"
print(Char[2])

name = "Hola soy Fulano"

name = name.replace("Fulano", "Polanco")
print(name)

#split es para separar el string en una lista de variables
# Python es genial el output es = 'Python' 'es' 'genial'

separar = cadena2.split
print(separar)

print(name[3:10])
# n-1

mayus = cadena1.upper()
minus = cadena2.lower()

print(mayus, minus)

#se utiliza in para buscar dentro de una variable

satanic = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

#Como lorem != de Lorem entonces marca falso 
print("lorem" in satanic)

#Pero si lo buscamos en minuculas entonces da Verdadero
print("lorem" in satanic.lower())

#Longitud de varias cosas 

print(len(cadena1))

concatenar = (cadena1 + " " + cadena2)
print(concatenar)

print(cadena1, cadena2, sep=" ")

#Listas 

frutas = ['manzana' , 'pera' , ' naranja', 'kiwi']

print(frutas)

# frutas[1]=1

print(frutas)

#removiendo un elemento de la lista 

frutas.remove("kiwi")

print(frutas)

#append 

frutas.append('uva')

print(frutas)

lista = [1,2,3,4,5]

lista = (lista[0] + lista[1] +lista[2] + lista[3] + lista[4])

print(lista)