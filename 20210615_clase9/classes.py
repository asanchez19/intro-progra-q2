mi_estudiante = {
    'nombre': 'Luis',
    'edad': 25,
    'notas': [100, 85, 90, 50, 100],
    'porcentaje': 92, # Digamos que acá podemos calcular el porcentaje dinamicamente.
}


def porcentaje_estudiante(notas):
    return sum(notas)/len(notas)


# print(porcentaje_estudiante(mi_estudiante['notas']))


class Estudiante:
    def __init__(self, nuevo_nombre, nuevo_apellido, nuevas_notas, nueva_edad = 'No aplica'):
        self.nombre = nuevo_nombre
        self.edad = nueva_edad
        self.notas = nuevas_notas
        self.apellido = nuevo_apellido
    
    def promedio(self, puntos_extra = 0):
        return (sum(self.notas) + puntos_extra)/len(self.notas)
        
    def suma(self):
        return sum(self.notas)
        
    def obtener_nombre_completo(self):
        return f'{self.nombre} {self.apellido}'
        
    def calcula_nota_final(self):
        raise NotImplementedError('Este sistema aún no tiene la capacidad de calcular la nota final')



estudiante_uno = Estudiante('Luis', 'Chaves', [100, 85, 90, 50, 100], 28)

print(estudiante_uno.__class__)

print(estudiante_uno.obtener_nombre_completo())
print(estudiante_uno.edad)
print(estudiante_uno.promedio())
print(estudiante_uno.suma())

try:
    estudiante_dos = Estudiante('Juan', 'Jara', [80, 90, 88, 100])
    print(estudiante_dos.obtener_nombre_completo())
    print(estudiante_dos.edad)
    print(estudiante_dos.promedio())
    print(estudiante_dos.suma())
    estudiante_dos.calcula_nota_final()
    print(5 + 'hola')
    
except NotImplementedError:
    input('Hola clase')
    print('Gracias por utilizar nuestro sistema, sin embargo aún no tenemos disponible esta funcionalidad, intenta más tarde. :)')
except ZeroDivisionError:
    print('No se puede dividir entre 0')
    
# except ConnectionError:
    # connect()
except:
    print('Ocurrio un error inesperado! Comuniquese con TI')
finally:
    print('No importa lo que ocurra, esta línea siempre se ejecuta.')
