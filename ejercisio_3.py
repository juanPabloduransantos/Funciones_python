# construir una funcion que reciba como parametro una lista de datos numericos y retorne la suma de dichos datos.
def sumar_lista(numeros):
    return sum(numeros)


lista_numeros = [1, 2, 3, 4, 5]
resultado = sumar_lista(lista_numeros)
print("La suma de los números es:", resultado)