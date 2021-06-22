amigos = [
    {
        'nombre': 'Pablo',
        'profesion': 'Ingeniero'
    },
    {
        'nombre': 'Maria',
        'profesion': 'Diseñadora'
    },
    {
        'nombre': 'Esteban',
        'profesion': 'Doctor'
    },       
]

# def buscar(nombre):
#     for amigo in amigos:
#         if amigo['nombre'] == nombre:
#             return amigo
#     return None

# amigo = buscar('Pablo')

# print(amigos)

# amigo['profesion'] = 'dentista'

# print(amigos)

#Buscar elementos en una lista de diccionarios. 
def buscar(nombre):
    for (index, amigo) in enumerate(amigos):
        if amigo['nombre'] == nombre:
            return index
    return None
    
index = buscar('Maria')

print(index)

index = buscar(input('Digite el nombre de la persona que quiere actualizar: '))

nombre = input('Digite su nombre: ')
profesion = input('Digite su profesion')

# Actualizar elementos por su indice. 

amigos[index]['nombre'] = nombre
amigos[index]['profesion'] = profesion

print(amigos)

index = buscar(input('Digite el nombre de la persona que quiere eliminar: '))

amigos.pop()

print(amigos)


#DRY -  DON'T REPEAT YOUR SELF!!
