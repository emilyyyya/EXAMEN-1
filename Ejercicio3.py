def palabras_repetidas(lista1, lista2):
    try:
        # Convertir ambas listas a conjuntos para eliminar duplicados
        set_lista1 = set(lista1)
        set_lista2 = set(lista2)

        # Encontrar palabras repetidas, ignorando mayúsculas y minúsculas
        palabras_repetidas = set_lista1.intersection(set_lista2)

        # Convertir las palabras repetidas a una lista y ordenarlas alfabéticamente
        lista_repetidas = sorted(list(palabras_repetidas))

        return lista_repetidas
    except Exception as e:
        print(f"Error: {e}")
        return []

def main():
    while True:
        print("\n--- Menú ---")
        print("1. Encontrar palabras repetidas")
        print("2. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            lista1 = input("Ingrese la primera lista de palabras separadas por espacios: ").split()
            lista2 = input("Ingrese la segunda lista de palabras separadas por espacios: ").split()
            lista_repetidas = palabras_repetidas(lista1, lista2)
            print("Palabras repetidas encontradas:", lista_repetidas)
        elif opcion == "2":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
