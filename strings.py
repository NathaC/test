myString="Hello mundo"


#podemos operar sumar, dividir , etc

# dir   (todas la funciones  que hay)

print(dir(myString))


#  upper (convertir todo en MAYUSCULA)

print(myString.upper())

#Todo en minuscula 

print(myString.lower())

#swapcase   : cambia  si una letra  del texto esta en mayuscula , lo cambia a mayuscula,

print(myString.swapcase())


#capitalize: la primera letra en mayucula y lo demas lo mantiene igual

print(myString.capitalize())

#replace: remplazar le damos un texto que quiera remplazar con el oro , el hello lo va a reemplazar con bye

print(myString.replace('hello','bye'))

#lo que dice es bye world xd

#----------------------------------------------------


#metodos encadenados , un metodo detras de otro 
print(myString.replace('hello','bye').upper())

#------------------------------


#Cuantas veces esta la letra L en la variable  myString e imprimirlo 
print(myString.count('l'))

#cuantas veces esta el espacio vacio 
print(myString.count(' '))


#    ¿Mi texto empieza con la palabra hello? , me muestra false porque no comienza con hello en minuscula, sino en Hello con mayuscula al principio 

print(myString.startswith('hello'))

#-----------------


#Aqui da True  (como termina o empieza un caracter , te lo ofrece un string esto no lo podemos adivinar con un numero o lista)

print(myString.endswith('mundo'))


#split: Este me separa el texto cuando hay un espacion estre ellas

print(myString.split())




#****************
#Separame a partir de una coma 
print(myString.split(","))

#Resultatdo:  ['hello' , 'world']
#----------------------


#Separame a partir de la letra o

print(myString.split("o"))

#Resultatdo:  ['hell' , 'w', 'rld']
#-----------------------------


#*****************
# Me devuelve , cual es la posicion de la letra o 
#En caso de la o, es la posicion 4


#Empieza con el valor 0,es decir que H , es posicion 0

print(myString.find("o"))


#Me devuelve la longuitud 
#Acodar que  empieza por 0, es decir , que si una palabra tiene 12 letras , me dira que la longuitud es 11
#Acordar que me cuenta, el espacio en blanco

print(len(myString))


#Buscar el indice de una  letra-caracter  e

print(myString.index("e"))


#aqui me pregunta si es numerico 
print(myString.isnumeric())


#aqui me pregunta si es alfanumerico 
print(myString.isalpha())


#iMPRIME quien esta en la poscion 4
print(myString[6])


#iMPRIME quien esta en la poscion -1, me da la inversa , es decir, de que el ultimo (en este caso la ultima leta)se toma como -1, en este caso la letra o 


print(myString[-1])



#Concatenando : unir dos strig , con operador de concatenacion
#Dejar unespacion entre is para mejor visualizacion 

nombre="Naty"
print("My name is " + nombre)

#Concatenando de otra forma 
#esta variable  "name"  debe ser interpretado de una variable anterior, con letra clave f 
#Solo para version 3,6 de python asi arriba 



print(f"My name is " {name})




#Otra forma





