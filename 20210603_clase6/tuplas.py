# Listas
amigos = ['Sebas', 'Kevin', 'Pablo']

print(amigos)

amigos.append('Ericka')

print(amigos, type(amigos))

# Tuplas

tupla = ('Sebas', 'Kevin', 'Maria')

print(tupla, type(tupla)) 

print(tupla[0])

lista_tuplas = [tupla, ('Alejandro', 'Javier')]

print(lista_tuplas[0][2])

# Las tuplas no se pueden modificar.
# tupla.append('Pedrito')

tupla = tupla + ('Pedrito',)

print(tupla)
