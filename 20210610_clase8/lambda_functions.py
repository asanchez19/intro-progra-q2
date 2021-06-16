# def dividir(x,y):
#     return x/y
    
# print(dividir(6,2))

dividir = lambda x,y: x/y

print(dividir(6,2))

print(((lambda x,y: x/y) (6,2)))


def saludar(nombre):
    print(f'Hola {nombre}')
        
saludar('Gabriel')

hola = saludar

hola('Pedro')



promedio = lambda seq: sum(seq) / len(seq)
total = lambda seq: sum(seq)
top = lambda seq: max(seq)


lista =  [1, 2, 3, 10]

print(promedio(lista))
print(total(lista))
print(top(lista))

operaciones= {
    'promedio': promedio,
    'total': total,
    'top': top
}


estudiantes = [
    {
        'nombre': 'Maria',
        'notas': [100, 50, 75, 80]
    },
    {
        'nombre': 'Jorge',
        'notas': [66, 80, 50, 80]
    },
    {
        'nombre': 'Lorena',
        'notas': [100, 90, 80, 95]
    }
]


for estudiante in estudiantes:
    nombre = estudiante['nombre']
    notas = estudiante['notas']
    
    operacion = input('Digite una operacion (promedio/total/top)')
    
    funcion_operacion = operaciones[operacion] 
    print(f"Se le está aplicando la operacion {operacion} al estudiante {nombre} y el resultado es: {funcion_operacion(notas)}")
