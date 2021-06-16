mi_primer_diccionario = {
    'saludo': 'Hola Mundo!'
}

print(mi_primer_diccionario['saludo'])

usuario = {
    'username': 'asanchez',
    'password': '123',
}

user = input('Digite su nombre de usuario: ')
password = input('Digite su contraseña: ')

if usuario['username'] == user and usuario['password'] == password:
    print('Bienvenido al sistema!')
else:
    print('Credenciales incorrectas!')

usuario['rol'] = 'admin'

print(usuario)


usuarios = [
    {
        'username': 'asanchez',
        'password': '123',
    },
    {
        'username': 'mmoreira',
        'password': '123',
    },
    {
        'username': 'dpidado',
        'password': '123',
    },
]

print(usuarios)

print(usuarios[1]['username'])
