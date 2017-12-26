l = [2,"tres",True,["uno",10]]

print (l)

l2 = l[1]

print (l2)

l3 = l[3][1]

print (l3)

l[2] = 123

print (l)

#Conteo 
l4 = l[0:3]

print (l4)


#Salto 
l5 = l[0:3:2]

print (l5)


#Salto y todos los elementos
l6 = l[1::2]

print (l6)



#Modificar Lista

l[0:2] = [4,3] 
print (l)

l[0:2] = [4] 

print (l)


# Acceder a la lista 

l7 = l[-1]

l7 = l[-3]

print (l7)