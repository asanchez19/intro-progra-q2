hay_platos_sucios = input("Hay platos sucios?(si/no)")

if  hay_platos_sucios.lower() == 'si':
    quiero_lavar_platos = input('Quiero lavarlos ahora mismo?(si/no) ')
    
    if quiero_lavar_platos.lower() == 'si':
        tengo_lo_necesario = input('Hay agua, jabón y esponja?')
        
        if tengo_lo_necesario.lower() == 'si':
            print('Lavar')
            print('Secar')
            print('Y guardar platos')
            print('FIN')
        else:
            print('FIN')
    else:
        print('FIN')
else:
    print('FIN')
