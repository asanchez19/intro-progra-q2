amigo1 = 'Pablo'
amigo2 = 'Juan'
amigo3 = 'Esteban'
amigo4 = 'Maria'
contador_de_amigos = 4

print(amigo1, amigo2, amigo3, amigo4)

amigos = ['Pablo', 'Juan', 'Esteban', 'Maria']

frutas = ['Sandia', 'Jocote', 'Mango']

amigos.append(frutas) # Lista de listas.

print(amigos)

amigos.append('Luis')

print(amigos)

print(f'Yo tengo  {len(amigos)} amigos')

amigos.remove('Pablo')

print(f'Pablo ya no es mi amigo, ahora tengo {len(amigos)} amigos')

print(amigos)

print(amigos[0]) # Juan
print(amigos[3]) # Luis
# print(amigos[4]) # Luis
