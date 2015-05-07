from arbolB import *

a = ABB()

print("Creando arbol")

a.meter(a.ABB, 5,5)
a.meter(a.ABB, 3,3)
a.meter(a.ABB, 2,2)
a.meter(a.ABB, 4,4)
a.meter(a.ABB, 7,7)
a.meter(a.ABB, 6,6)
a.meter(a.ABB, 10,10)

print("Arbol creado")

print("preOrden")
a.preOrden(a.ABB)
print("inOrden")
a.inOrden(a.ABB)
print("postOrden")
a.postOrden(a.ABB)

print("Sacando nodos")
print(a.sacar(a.ABB, 4))
print(a.sacar(a.ABB, 6))
print(a.sacar(a.ABB, 3))
print(a.sacar(a.ABB, 7))

print("Arbol con nodos afuera")
a.preOrden(a.ABB)

print("sacando la raiz")
print(a.sacar(a.ABB, 5))

print("Imprimiendo arbol")
a.preOrden(a.ABB)

