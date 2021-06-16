usuarios = [
    {
        'username': 'asanchez',
        'password': '123',
        'rol': 'admin'
    },
    {
        'username': 'mmoreira',
        'password': '123',
        'rol': 'invitado'
    },
    {
        'username': 'dpidado',
        'password': '123',
        'rol': 'invitado'
    },
]

def despedida():
    saludo()
    print('Nunca viene y ya se va!')

   
def saludo():
    print('Hola clase! Ya casi salimos! :)')


def get_nombre_completo(nombre, apellido):
    print(f'{nombre} {apellido}')

    
def es_admin(usuario):
    return usuario['rol'] == 'admin'


get_nombre_completo('Alejandro', 'Sanchez')

print(es_admin(usuarios[0]))

usuario_admin = None

for usuario in usuarios:
    if es_admin(usuario):
        usuario_admin = usuario
        break
    else:
        print('No es admin')

print(usuario_admin['username'], usuario_admin['rol'])
