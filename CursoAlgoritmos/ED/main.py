#E.D

###
# Arrays & Listas
#
# Arrary: [1, 2, 3, 4, 5]
#Conjunto de datos en un lugar especifico - datos almacenados siempre son del mismo tipo y son finitos.
# Lista: []
# Guarda un conjunto de datos, epro es dinamina, osea es infinita. Se puede ir guardando cualqueir tipo de valor.
#
# DIFERENCIAS, cuando aplicar una u otra
#
# Cuando no se sabe la cantidad de datos que se va almacenar se utiliza una lista
# Pero si se conoce el numero fijo o tamano exacto, se utiliza un array.
#
# Who is more fast?
#
# Array: Memoria directa -> es muhco mas eficiente, ya que guarda el valor directo en memoria. #
#
# Lista: Memoria referencia -> No guarda el valor directo en memoria, sino en una referencia de moemoria,
# este es un valor o codigo unico que indica a la maquina en que lugar se encuentra.
# #
#Lenguaje compilado, funciona bajo nivel ->
#Lenguaje interpretado, funciona en alto nivel -> pasa el codigo al bajo y ejecuta en memoria
# ###


def binary_search(x, target):
    x.sort()  # Ordenamos la lista
    low = 0
    high = len(x) - 1

    while low <= high:
        mid = (low + high) // 2
        if x[mid] == target:
            return mid  # Retornamos la posición del elemento
        elif x[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Si no se encuentra el elemento

# Ejemplo de uso:
x = [10, 30, 50, 40, 20]
target = 40
resultado = binary_search(x, target)

print("Elemento encontrado en la posición:", resultado)

# Algoritmo de complejidad de: O(n log n)



