def es_decimal(cadena):
    return cadena.isdigit()

def es_binario(cadena):
    return all(c in "01" for c in cadena)

def es_octal(cadena):
    return all(c in "01234567" for c in cadena)

def es_hexadecimal(cadena):
    try:
        int(cadena, 16)
        return True
    except ValueError:
        return False

def mostrar_resultados(valor_decimal):
    print("\nResultados:")
    print(f"Decimal     : {valor_decimal}")
    print(f"Binario     : {bin(valor_decimal)[2:]}")
    print(f"Octal       : {oct(valor_decimal)[2:]}")
    print(f"Hexadecimal : {hex(valor_decimal)[2:].upper()}")

def main():
    while True:
        print("\n--- Conversor de Bases ---")
        print("1. Ingresar número decimal")
        print("2. Ingresar número binario")
        print("3. Ingresar número octal")
        print("4. Ingresar número hexadecimal")
        print("5. Salir")

        opcion = input("Selecciona una opción (1-5): ")

        if opcion == "1":
            valor = input("Ingresa un número decimal: ")
            if es_decimal(valor):
                mostrar_resultados(int(valor))
            else:
                print("Entrada no válida. Asegúrate de ingresar un número decimal correcto.")

        elif opcion == "2":
            valor = input("Ingresa un número binario: ")
            if es_binario(valor):
                mostrar_resultados(int(valor, 2))
            else:
                print("Entrada no válida. Asegúrate de ingresar un número binario correcto (solo 0 y 1).")

        elif opcion == "3":
            valor = input("Ingresa un número octal: ")
            if es_octal(valor):
                mostrar_resultados(int(valor, 8))
            else:
                print("Entrada no válida. Usa solo dígitos del 0 al 7.")

        elif opcion == "4":
            valor = input("Ingresa un número hexadecimal (sin 0x): ")
            if es_hexadecimal(valor):
                mostrar_resultados(int(valor, 16))
            else:
                print("Entrada no válida. Usa solo dígitos del 0-9 y letras A-F.")

        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
