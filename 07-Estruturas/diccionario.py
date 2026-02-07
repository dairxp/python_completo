"""
Que es un diccionario de python y cuando utlizarlo

{'clave':valor, 'clave2':valor2} 

"""

"""
personas= {'bruno':24, 'pedro':20, 'maria':19, 'nestor':35}
print(personas['maria'])
"""

###

personas= {'bruno':24, 'pedro':20, 'maria':19, 'nestor':35}
"""
for persona,edad in personas.items():
	#print(persona)
	print(f"Mi nombre es {persona} y mi edad es: {edad}")
"""

#agregar elemento

personas['tomas']=30
print(personas)

"eliminar elemento de diccioanrio"