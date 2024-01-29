# texto_variado = "palabra 1234 +-* #$%& "
# print (type (texto_variado))

# # Podemos utilizar comillas triples para que el texto se muestre como la cadena que hemos escrito
# print  (""" 
# Funcionamiento de \
#  programa (opciones)
#    -1 para acceder a opciones
    #  -2 para salir
#""")

# Subscriting e indexado

# texto = "Python"


# print (texto [0])
# print (texto [5])
# print (texto [-1])
# print (texto [-6])

# print (texto [6]) # Error, no podemos acceder a una posición que no existe
# print (texto [-7]) # Error, no podemos acceder a una posición que no existe

# letra = (texto[0])
# print(letra)

# # texto[0] = "p" # Error, no podemos modificar una cadena

# letra = "p"
# print (letra)

# texto_compuesto = letra + texto[1] #concatenación
# print (texto_compuesto)

#############################################

# Slicing o substraining
#texto = "Python"

# print (texto[0:3])
# print (texto [0:-3])
# print (texto [2:])
# print (texto [:3])

#print (texto [-3::-1])

#print (texto[::-1])
# print (texto [1:50])
# print (texto [2:2])


#####################
#Cadenas y formatos

# texto = "Hola mundo! Buenastardes"
# print (texto.lower()) #Hace las letras minusculas
# print (texto.upper()) #Hace las letras mayusculas
# print (texto.capitalize()) #Hace la primer letra de la oriacion mayuscula
# print (texto.title()) #Hace que las primeras letras de cada palabra sean mayusculas
# print (texto.swapcase()) #Intercambia mayusculas y minusculas
# texto = texto.upper()
# print (texto)

print ('{} + {} = {}'. format(2, 3, 2+3))
print ('{} + {} = {}'. format("Hola", "mundo", "Hola mundo"))
print ('{:.3f} + {:.4f} = {}'. format(2, 3, 2+3))
print ('{1} + {0} = {2}'.format(2, 3, 2+3))
print ('{2} + {0} + {1}'.format("Hola", "mundo", "Hola mundo"))
print ('{:d} = {:b} = {:o} = {:x}'.format(15, 15, 15, 15))