#while <condicion_verdadera>:
#Cuerpo del ciclo
#condiciones son: expresiones boleanas (or, and) y operaciones de comparacion
#ciclos controlados por un contador entero

#i=0
#k=0

#while i<10:
#    print ("ciclo")
#    #importante modificar el valor del contador 
#    i+=1


#ciclos controlados por el valor de una variable
#import random 
#a=0
#while a !=5:
#    a=random.randint(1,10)
#    print(a)
#    print("se acabo")

#ciclos controlados por un evento 

#a=0
#while 1==1:
#    a=int(input("ingrese un numero: "))
#    if a==10:
#        break
#for: se utiliza para recorrer un iterable 
#lista,tupla,diccionario...
#Lista:conjunto de variables organizadas en espacios consecutivos de memoria, 
#a las que se les asigna un unico nombre. se diferencian por la posicion que ocupan respecto
#al primer elemento de la lista 
#no hay problema en listas vacias 

#miLista=[1,True,"Textos",5151]
#miLista2=[]

#en python todos son objetos 
#print(miLista)
#miLista.append(45)
#print(miLista)
#miLista.insert(0,"Hola")
#print(miLista)
#miLista.pop(2)
#print(miLista)
#print(len(miLista))
#tupla: lista inmutable.

miLista=[5,45,89,6,7]

#for:ciclo para recorrer iterables. El cuerpo 
#se repite tanta veces como elemento tenga el iterable.
#en cada ciclo se guarda el valor del elemento 

#estructura del for en python:
# for<variable_donde_guarda_el_elemento in iterable:

#for x in miLista:
#    print (x)
#    if x>50:
#        print("grande")
#si solo utilizo el iterable para definir la cantidad
#de repeticiones, entonces no es necesaria la variable 

#for _ in miLista:
#    print("ciclo")
    
#si no tengo un iterable, puedo usar la funcion range() 
#para generar una secuencia de numeros

#for x in range(-10,10):
#    print(x)    

# *****************TALLER**************************
#crear un programa que pida un numero al usuario y:
#1. imprima los numeros impares entre -numero y numero
#2. imprima los numeros primos entre 0 y numero*100
#el numero que ingrese el programa debe garantizar que el usuario ingrese un numero >0

#entrega antes de las 4 en el repositorio remoto 2


def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def imprimir_impares(num):
    print("Números impares entre -{} y {}:".format(num, num))
    for i in range(-num, num + 1):
        if i % 2 != 0:
            print(i, end=" ")

def imprimir_primos(num):
    print("\nNúmeros primos entre 0 y {}:".format(num * 100))
    for i in range(num * 100 + 1):
        if es_primo(i):
            print(i, end=" ")

def main():
    numero = 0
    while numero <= 0:
        try:
            numero = int(input("Ingrese un número mayor que 0: "))
            if numero <= 0:
                print("El número debe ser mayor que 0. Inténtelo de nuevo.")
        except ValueError:
            print("Debe ingresar un número entero válido.")

    imprimir_impares(numero)
    imprimir_primos(numero)

if __name__ == "__main__":
    main()