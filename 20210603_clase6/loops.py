amigos = ['Pedro', 'Daniel', 'Josue']

print(amigos)

# #Por convención el nombre de las listas es en prural.
# #Cuando vamos a recorrer esa lista en un ciclo for 
# # el nombre del cursor en singular.

for amigo in amigos:
    print(amigo)


# elementos = [1,2,3]


elementos = [5,6,7]

for _ in elementos:
    print('hola!!!')

# valor = 0
for _ in range(5):
    valor = valor + 2
    print(valor)
    
    
# # for index in range(5, 8):
# #     print(f'Rango con inicio y final {index}')
    
    
# for index in range(5, 16, 5):
#     # print('Rango con inicio y final ' + str(index))
#     print(f'Rango con inicio y final {index}')


# # for index in range(2, 202, 2):
# #     print(index)


# usuarios = [
#     {
#         'username': 'asanchez',
#         'password': '123',
#     },
#     {
#         'username': 'mmoreira',
#         'password': '123',
#     },
#     {
#         'username': 'dpidado',
#         'password': '123',
#     },
# ]

# for usuario in usuarios:
#     print(usuario)


# for usuario in usuarios:
#     print(usuario['username'])
#     print(usuario['password'])
#     print('---------')
# estoy_aprendiendo = True
while estoy_aprendiendo:
    print('Estoy aprendiendo')
    estoy_aprendiendo = input('Sigo aprendiendo?(s/n)') == 's'
    
print('Ya no estoy aprendiendo nada! :(')


print('Menu de departamentos: ')
print('1 - Damas')
print('2 - Caballeros')
print('3 - Niños')
print('4 - Salir')
opcion = int(input('Digite una opción del menu:'))
while opcion != 4:
    if opcion == 1:
        print('Departamento de damas')
    elif opcion == 2:
        print('Departamento de caballeros')
    elif opcion == 3:
        print('Departamento de niños')
    else:
        print('La opcion seleccionada no es valida!')
        
    opcion = int(input('Digite una opción del menu:'))

print('Saliendo del programa')
