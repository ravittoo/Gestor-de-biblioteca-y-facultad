import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "biblioteca"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "facultad"))

from main import main as menu_biblioteca
from main_facultad import main as menu_facultad


def mostrar_menu():
    print("\n========================================")
    print("Gestores")
    print("========================================")
    print("1. Sistema de Gestión de Biblioteca")
    print("2. Sistema de Gestión de Facultad")
    print("0. Salir")
    print("----------------------------------------")


def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_biblioteca()

        elif opcion == "2":
            menu_facultad()

        elif opcion == "0":
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()
