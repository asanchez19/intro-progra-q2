class Estudiante:
    def __init__(self, nombre, colegio):
        self.nombre = nombre
        self.colegio = colegio
        self.notas = []
        
    def promedio(self):
        return sum(self.notas) / len(self.notas)
        
estudiante_pablo = Estudiante('Pablo', 'Colegio de los Angeles')

print(estudiante_pablo.nombre)
estudiante_pablo.notas.append(100)
estudiante_pablo.notas.append(50)
print(estudiante_pablo.promedio())


# class EstudianteTrabajador:
#     def __init__(self, nombre, colegio, salario):
#         self.nombre = nombre
#         self.colegio = colegio
#         self.notas = []  
#         self.salario = salario 
    
#     def promedio(self):
#         return sum(self.notas) / len(self.notas)


# estudiante_bryan = EstudianteTrabajador('Bryan', 'Liceo de Costa Rica', 20000)

# print(estudiante_bryan.nombre)
# estudiante_bryan.notas.append(85)
# estudiante_bryan.notas.append(80)
# print(estudiante_bryan.promedio())

class EstudianteTrabajador(Estudiante):
    def __init__(self, nombre, colegio):
        super().__init__(nombre, colegio)  
        self.salarios = []    
    
    def calcula_aguinaldo(self):
        return sum(self.salarios) / 12
 
estudiante_bryan = EstudianteTrabajador('Bryan', 'Liceo de Costa Rica')
#         
print(estudiante_bryan.nombre)

estudiante_bryan.notas.append(85)
estudiante_bryan.notas.append(80)
print(estudiante_bryan.promedio())

estudiante_bryan.salarios.append(200000)
estudiante_bryan.salarios.append(300000)
estudiante_bryan.salarios.append(350000)
estudiante_bryan.salarios.append(300000)

print(estudiante_bryan.calcula_aguinaldo())
