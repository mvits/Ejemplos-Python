# While

contador = 0
bandera = True

while bandera:#contador < 10:
	#print(contador)
	contador+=1

	if contador == 5:
		continue
	if contador == 6:
		bandera = False #break
else:
	#print("Il while finisce!!!")


#For
 lista = [1,2,3,4,5,6,7,8,9,10]

 for valor in lista:
 	#print(valor)
 	pass

 lista_dos = range(0,10)

 lista_dos = range(0,20,2)

 for valor in lista_dos:
 	#print(valor)
 	pass


 indice = 0 
 for valor in lista:
 	#print(valor, "tiene el indice", indice)
 	indice +=1
 	pass

 
 for indice,valor in enumerate(lista):
 	#print(valor, "tiene el indice", indice)
 	pass

 for valor in range(0, len(lista)):
 	#print(valor)
 	pass

 for valor in "Il mio corso":
 	pass

 diccionario = {"a": 10, "b": 20, "c": 500}
 
 for llave,valor in diccionario.items():
 	print("la llave es : ", llave, "tiene el valor de : ", valor)





 	