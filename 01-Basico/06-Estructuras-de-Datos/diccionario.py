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
print
#agregar elemento

personas['tomas']=30
print(personas)

# Eliminar elemento de diccioanrio

personas.pop('bruno')
print(f"Diccinario con eliminacion persona {personas}")

#Editar elemnto de diccioanrio
personas["maria"]=50
print(f"Diccinario Editado de persona {personas}")