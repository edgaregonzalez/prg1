import random
'''
Desarrollar cada una de las siguientes funciones y escribir un programa que permita
verificar su funcionamiento imprimiendo la lista luego de invocar a cada función:
a) Cargar un vector con números al azar de cuatro dígitos. La cantidad de elementos
también será un número al azar de dos dígitos.
b) Calcular y devolver la sumatoria de todos los elementos de la lista anterior.
c) Eliminar todas las repeticiones de un valor en la lista anterior. El valor a eliminar
se recibe como parámetro.
d) Determinar si el contenido de una lista cualquiera es capicúa, sin usar listas
auxiliares.
'''
lista = []

def CargarVector():
    for i in range(random.randint(10,99)):
        lista.append(random.randint(1000,9999))
    return lista

def sumarLista(vector):
    return sum(vector)


def eliminarValor( n, vector):
    for i in vector:
        if(i == n):
            vector.remove(i)
    return vector


print(CargarVector())
print(sumarLista(lista))
valor = int(input('Ingrese un valor a eliminar: '))
print(eliminarValor(valor, lista))
print(sumarLista(lista))