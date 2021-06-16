# saludo = 'Hola!'


# Podemos accesar a una letra del string(palabra) directamente por su indice.
# print(saludo)
# print(saludo[4]) 

# print(saludo[:5]) # Puedo definir el inicio y el final de mi sub string.j

# print(saludo[1:]) # Todos menos el primero

# print(saludo[:4]) # Todos menos el ultimo


amigos = ['Sebastian', 'Ricardo', 'Kevin', 'Christian', 'Ericka']

print(amigos[1:-3])

# print(amigos[:2])
# print(amigos[3:])

# print(amigos[-4:])
# Error lógico - ambas variables apuntan a la misma pocisión de memoria.
# mejores_amigos = amigos

# mejores_amigos.append('Jorge')

# print(mejores_amigos)
# print(amigos)

#Loteria del lunes pasado
loteria = [99, 5, 29]

#Solución: Crear una copia del objeto que quiero respaldar.

loteria_vieja = loteria[:]

#Loteria de hoy
loteria.append(10)

print(loteria)
print(loteria_vieja)
