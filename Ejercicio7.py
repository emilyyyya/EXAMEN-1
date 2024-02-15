class Inventario:
    def __init__(self):
        self.items = []

    def agregar_item(self, nuevo_item):
        if nuevo_item in self.items:
            raise ValueError("El ítem ya está en el inventario.")
        else:
            self.items.append(nuevo_item)

def main():
    inventario = Inventario()

    while True:
        print("\n--- Menú ---")
        print("1. Agregar ítem al inventario")
        print("2. Mostrar inventario")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nuevo_item = input("Ingrese el nuevo ítem a añadir al inventario: ")
            try:
                inventario.agregar_item(nuevo_item)
                print(f"{nuevo_item} ha sido añadido al inventario.")
            except ValueError as e:
                print("Error:", e)
        elif opcion == "2":
            if inventario.items:
                print("Inventario:")
                for item in inventario.items:
                    print("-", item)
            else:
                print("El inventario está vacío.")
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
