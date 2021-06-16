# divisas  = (5, 10)
# usd, eur = divisas

# print(divisas)

# print(usd)
# print(eur)


# amigos = [('Sabas', 'Gomez'), ('Juan', 'Jara')]

for name, last_name in amigos:
    print(last_name, name)

amigos = ['Juan', 'Sebas']

for index, amigo in enumerate(amigos):
    print(f'{index + 1} - {amigo}')


autos = []

autos.append({
    'marca': marca,
    'modelo': modelo,
    'estilo': estilo
})
