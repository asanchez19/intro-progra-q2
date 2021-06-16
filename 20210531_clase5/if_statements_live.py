# edad = int(input("Digite su edad: "))

# Estructura: 
# Palabra reservada if + condición + dos puntos(:)
# if edad < 18:
#     print('Menor de edad')
# else:
#     print('Mayor de edad')


if edad < 18:
    print('Menor de edad')
elif edad >= 18 and edad < 35:
    print('Adulto Joven')
elif edad >= 35 and edad < 65:
    print('Adulto')
else:
    print('Adulto mayor')

amigo = input('Digite el nombre de su amigo: ')

if amigo == 'Carlos':
    print('Hola Carlos')
    edad = int(input("Cuantos años tienes? "))
    if edad > 18:
        print('Bienvenido a la fiesta')
    else:
        print('Lo siento Carlos, es una fiesta para adultos.')
else:
    print('Usted no es mi amigo! :(')
