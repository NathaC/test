demo_list = [1, 'hello', 1.34, True, [1,2,3]]

colors=['red', 'green', 'blue']

#  contructor: es una especie de funcion que permite definir una lista 

numbers_list= list((1,2,3,4)) #haciendo una dupla para hacer una lista

print(numbers_list)


#Quiero crear una lista del 1 al 10

r= list(range(1,10))  #el llega hasta un numero antes del 2do paremetro que en este caso es 10, llega hasta 9
print(r)


#metodos para ejecutar de tipo de dato de lista, todo lo quepuedo hacer con una lista

print(dir(colors))


#Para saber si un elemento esta o existe en una lista

print("green" in colors)   #solo me da dos estados True o False

print("pink" in colors)  #Aqui me sale False ñorque pink no esta 




#podemos reasignarlos
#Alterar los datos de una lista

print(colors)
colors[1]="yellow"         # aqui a colors cambiame el indice 1 por yellow 

print(colors)


#append . con este puedo agrgar un nuevo elemento 


colors.append("violet")
print(colors)


#Como pasar pasar o agregar dos elementos , pues haciendo una duppla (())

colors.append(("black","yellow"))
print(colors)  #aqui lo interrpreta como un solo elemento junto 


#extend : tanpoco recibe multiples valores , recibe uno solo,pero le podemos una dupla o una lista y el los va a agregar como un solo elemento a cada uno de estos
colors.extend(("black","yellow"))
print(colors)






#Agregar elementos desde una posicion , ejemplo agregar un elemento 
colors.insert( 1 ,"gray")
print(colors)


#Insertar un elemento mas pero que este al ultimo 

colors.insert(len(colors), "green")
print(colors)

#-----------------------------
#Insertar un elemento mas pero que este al ultimo 


# colors.insert(-1, "green")
#print(colors)


#-------------------------------



#Quitar el ultimo elemento

colors.pop()
print(colors)

#Al pnerlo dos veces , me quita dos elementos 



#--------------------------

#pop : quiero quitar el elemento en el indice de 2 ()acordar que en una lista empieza por 0, sino coloco el indice me elimina el ultimo elemento de la lista 

colors.pop(2)
print(colors)

#------- Quitar dupla 

colors.remove(('black','yellow'))
print(colors)



#Remover: remover un elemento 


colors.remove("gray")
print(colors)

#----------------------

#Limpiar todo los elementos de la lista
#colors.clear
#print(colors)





#Ordenar alfabeticamente de forma inversa


colors.sort(reverse=True)
print(colors)


#Ordenar elementos alfabeticamente 

colors.sort()
print(colors)

#Quieron obtener el indice de un elemento de la lista (Acordar que una lista empieza por 0)

print(colors.index("black"))

print(colors.index("blue"))