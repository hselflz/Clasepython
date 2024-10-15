# Definir funciones
#def funcion1(*NC): #Solo se le pueden meter valores str
    #NC (Nombre Completo)  el asterisco es para que tome los parametros como lista
    #print("Hola me llamo",NC[0],NC[1], NC[2])

#funcion1("Ricardo", "Polanco","Cortés") #Asi se llama a una función, se pueden meter varios parametros
# Los parametros se pueden dividir por las comas, si quito en la función el nombre y dejo apellido, solo sale el apellido o segundo parametro

# Fijar parametros

def fun1(nombre, apellido): #se "puede" cambiar el orden
    print("Hola me llamo", nombre , apellido)
fun1(apellido="Cortés", nombre="Ricardo",) #Si metemos parametros sustituirá a los definidos

def fun2(nombre="Fulano", apellido="Mengano", edad=37):  

    nombre1 = input("Introduce tu nombre: ")
    if len(nombre1) <= 5:
        if nombre1 == "":
            print("Mi nombre es: ", nombre)
        else: 
            print("Mi nombre es :" , nombre1)
    else:
        print("nombre no valido")

    apellido1 = input("Introduce tu apellido: ")
    
    if apellido1 == "":
        print("Mi apellido es: ", apellido)
    else: 
        print("Mi apellido es :" , apellido1)

    edad1 = int((input("Escribe tu edad: ")))
    if type(edad1) == int:
        if edad1 == "":
            print("Tengo", edad,"años.")
        else: 
            print("Tengo", edad1,"años.")
    else:
        print("Edad no valida")
fun2()
