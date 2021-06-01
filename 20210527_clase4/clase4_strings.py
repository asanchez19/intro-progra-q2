# Strings en Python.
nombre = 'Berny'
apellido = 'Berrocal'
edad = 40


print(nombre + apellido)

print(nombre + ' ' + apellido + ' edad: ' + str(edad))

# F Strings
print(f"{nombre} {apellido} edad: {edad} y me gusta Carl's Junior")


print(nombre+nombre)
print(nombre*5)

es_alejandro = nombre == 'alejandro'

print(f'Es alejandro?: {es_alejandro}')

nombre = 'alejandro'

es_alejandro = nombre == 'alejandro'

print(f'Es alejandro?: {es_alejandro}')


quiero_lavar_platos = input('Quiero lavar los platos?(si/no) ')

print(quiero_lavar_platos)

if quiero_lavar_platos == 'si':
    print('Estoy lavando platos')
else:
    print('No quiero lavar los platos')
    
# Para leer números por teclado debo convertirlos a int()   
edad =  int(input('Digite su edad: '))

print(edad + 5)
