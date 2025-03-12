print("------------------------------")
print("-BUSCAR UN NUMERO EN CUNJUNTO-")
print("------------------------------")

#Definicon de la funcion
def buscarDatoEnlista(datoABuscar, lista):
    r = False
    for i in lista:
        if i == datoABuscar:
            r = True
    return r 

#Entrada
dato = int(input("Numero a buscar: ")) #se recibe el dato del usuario

#Procesamiento
lista = [1,2,3,4,5] #Se almacena una lista de datos
if buscarDatoEnlista(dato, lista):
    print("lo encontre")
else:
    print("no lo encontre")

#salida
print("\nEso era...")