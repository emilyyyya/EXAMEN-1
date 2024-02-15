def ordenar_personajes(lista_personajes):
    # Listas para almacenar personajes humanos y no humanos
    humanos = []
    no_humanos = []

    # Iterar sobre la lista de personajes
    for personaje in lista_personajes:
        if personaje["raza"] == "humano":
            humanos.append(personaje["nombre"])
        else:
            no_humanos.append(personaje["nombre"])

    # Ordenar las listas de personajes
    humanos.sort()
    no_humanos.sort()

    return humanos, no_humanos

# Ejemplo de uso
personajes = [
    {"nombre": "Mario", "raza": "humano"},
    {"nombre": "Luigi", "raza": "humano"},
    {"nombre": "Sonic", "raza": "erizo"},
    {"nombre": "Link", "raza": "humano"},
    {"nombre": "Donkey Kong", "raza": "gorila"},
    {"nombre": "Pikachu", "raza": "pokemon"},
]

humanos, no_humanos = ordenar_personajes(personajes)

print("Personajes humanos:")
for humano in humanos:
    print(humano)

print("\nPersonajes no humanos:")
for no_humano in no_humanos:
    print(no_humano)
