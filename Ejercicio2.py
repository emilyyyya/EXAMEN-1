def obtener_tasa_interes():
    while True:
        try:
            tasa_interes = float(input("Ingrese la tasa de interés anual (entre 1% y 10%): "))
            if tasa_interes < 1 or tasa_interes > 10:
                raise ValueError("La tasa de interés debe estar entre 1% y 10%.")
            return tasa_interes
        except ValueError as e:
            print(f"Error: {e}")

def obtener_anios():
    while True:
        try:
            anios = int(input("Ingrese el número de años: "))
            if anios <= 0:
                raise ValueError("El número de años debe ser mayor que cero.")
            return anios
        except ValueError as e:
            print(f"Error: {e}")

def calcular_capital_final(capital_inicial, tasa_interes, anios):
    tasa_interes_decimal = tasa_interes / 100
    capital_final = capital_inicial * (1 + tasa_interes_decimal) ** anios
    return capital_final

def main():
    capital_inicial = 1000

    while True:
        print("\n--- Menú ---")
        print("1. Calcular capital final")
        print("2. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            tasa_interes = obtener_tasa_interes()
            anios = obtener_anios()
            capital_final = calcular_capital_final(capital_inicial, tasa_interes, anios)
            print("El capital final es:", capital_final)
        elif opcion == "2":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()

