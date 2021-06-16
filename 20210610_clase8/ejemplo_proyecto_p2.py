# inventario = {
#     'nombre_tienda': 'Tienda Simón',
#     'sede': 'Escazu',
#     'departamentos': [
#         {
#             'nombre': 'Damas',
#             'productos': [
#                 {
#                     'nombre': 'Blusa',
#                     'cantidad': 100,
#                     'precio': 5000
#                 },
#                 {
#                     'nombre': 'Pantalon negro',
#                     'cantidad': 50,
#                     'precio': 15000
#                 },
#             ]
#         },
#         {
#             'nombre': 'Caballeros',
#             'productos': []
#         },
#         {
#             'nombre': 'Niños',
#             'productos': []
#         },
#     ]
# }

inventario = {
    'nombre_tienda': 'Tienda Simón',
    'sede': 'Escazu',
    'departamentos': {
        'damas': {
            'nombre': 'Damas',
            'productos': [
                {
                    'nombre': 'Blusa Dama',
                    'cantidad': 100,
                    'precio': 5000
                },
                {
                    'nombre': 'Pantalon negro',
                    'cantidad': 50,
                    'precio': 15000
                },
            ]
        },
        'caballeros': {
            'nombre': 'Caballeros',
            'productos': [
                {
                    'nombre': 'Camisa',
                    'cantidad': 100,
                    'precio': 5000
                },
            ]
        },
        'ninos': {
            'nombre': 'Niños',
            'productos': [
                {
                    'nombre': 'Juguete de Lego',
                    'cantidad': 100,
                    'precio': 5000
                },
            ]
        },
    }
}

# def consultar_productos_dept_damas():
#     productos = inventario['departamentos'][0]['productos']
#     for (index, producto) in enumerate(productos):
#         print(f'[{index + 1}] **************')
#         print(f"Producto: {producto['nombre']}")
#         print(f"Precio: {producto['precio']}")
#         print(f"Cantidad: {producto['cantidad']}")
#         print('**************')


# Cuando seleccione la opción 1. Ejecuta una función como esta.
# consultar_productos_dept_damas()


def consultar_productos(departamento):
    productos = inventario['departamentos'][departamento]['productos']
    for (index, producto) in enumerate(productos):
        print(f'[{index + 1}] **************')
        print(f"Producto: {producto['nombre']}")
        print(f"Precio: {producto['precio']}")
        print(f"Cantidad: {producto['cantidad']}")
        print('**************')




print('*** Departamento de Damas ***')
consultar_productos('damas')


print('*** Departamento de Caballeros ***')
consultar_productos('caballeros')


print('*** Departamento de Niños ***')
consultar_productos('ninos')
