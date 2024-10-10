for i in range(5):
    print(i ,"Hola")

Dias = ["Lunes","Martes","Miercoles","Jueves","Viernes"]
for Dia in Dias:
    if Dia == "Miercoles":
        continue
print("El valor de día es ", Dia)


n = int(input("Escribe un número natural: "))
print("Tu número es",n)

if n == 0:
    fact = 1
    print("El factorial de ",n, "es", fact)
else:
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    print("El factorial de" ,n,"\nEs: ",fact)

#El bucle while

i = 0
suma = 0
while i < 50:
    i += 1
    suma = suma+i 
print("La suma de los primeros 50 numeros es =" , suma)

contador = 0
sum = 0
while contador < 50:
    contador += 1
    contador = contador+contador
print(contador)