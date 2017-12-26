# Diccionarios

d =  {
		'Clave1': [1,2,3],
		'Clave2': True,
		4: False
	 }



d[4] = "Hola"

print (d['Clave1'])

print (d['Clave2'])

print (d[4])


valor = d.get('Clave1',False) # Buscar a partir de claves

print (valor)

del d[4] # Eliminar a partir de claves

print(d)


llaves = d.keys() # Retorna las llaves

llaves  = list(d.keys()) # Lista de llaves

valores  = list(d.values()) # Lista de Valores


llaves  = tuple(d.keys()) # Tuplas de llaves

valores  = tuple(d.values()) # Tuplas de Valores

print (llaves)
print (valores)


d2 =  {
		've1': [1,2],
		've2': False,
	 }

d.update(d2) # Extender diccionario


print(d)



