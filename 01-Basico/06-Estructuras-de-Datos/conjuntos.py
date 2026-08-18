"""
conjuntos -> No puede tener elementos repetidos
	|		|
"""

conjunto_a_parti_list=set([1,2,3,4,5])
conjunto_a_parti_tupla=set((1,2,3,4,5,6,5,4	))

print(conjunto_a_parti_list)
print(conjunto_a_parti_tupla)

#
print("--------Conjuntos-------")
conjuntoA=set([1,2,3])
conjuntoB=set([3,4,5,6])

print(conjuntoA)
print(conjuntoB)

#Unir Conjuntos
conjuntoC =conjuntoA|conjuntoB

print(conjuntoC)

#interseccion de Conjuntos
interseccion =conjuntoA&conjuntoB
print(f"Los elemntos de la intesecioo son: {interseccion}")

#devovler lista sin repetidos

numeros=[1,2,1,2,3,2,3,1,2,3,4,5,4,3,2,1,2,3,4,5,6,7,8,9,1]
lista_sin_repetidos=set(numeros)

print(list(lista_sin_repetidos))