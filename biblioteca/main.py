from biblioteca import (
    Biblioteca,
    LibroNoEncontradoError,
    MiembroNoEncontradoError,
    LibroNoDisponibleError,
    LibroNoPrestadoError,
    ISBNDuplicadoError,
    DNIDuplicadoError
)


def mostrar_menu():
    print("\n=== Sistema de Gestión de Biblioteca ===")
    print("1. Agregar libro")
    print("2. Agregar miembro")
    print("3. Mostrar libros")
    print("4. Mostrar miembros")
    print("5. Prestar libro")
    print("6. Devolver libro")
    print("0. Volver")


def main():
    biblioteca = Biblioteca()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            isbn = input("ISBN: ")
            try:
                biblioteca.agregar_libro(titulo, autor, isbn)
            except ISBNDuplicadoError as e:
                print(f"Error: {e}")

        elif opcion == "2":
            nombre = input("Nombre: ")
            dni = input("DNI: ")
            try:
                biblioteca.agregar_miembro(nombre, dni)
            except DNIDuplicadoError as e:
                print(f"Error: {e}")

        elif opcion == "3":
            biblioteca.mostrar_libros()

        elif opcion == "4":
            biblioteca.mostrar_miembros()

        elif opcion == "5":
            isbn = input("ISBN del libro: ")
            dni = input("DNI del miembro: ")
            try:
                biblioteca.prestar_libro(isbn, dni)
            except (LibroNoEncontradoError, MiembroNoEncontradoError, LibroNoDisponibleError) as e:
                print(f"Error: {e}")

        elif opcion == "6":
            isbn = input("ISBN del libro: ")
            dni = input("DNI del miembro: ")
            try:
                biblioteca.devolver_libro(isbn, dni)
            except (LibroNoEncontradoError, MiembroNoEncontradoError, LibroNoPrestadoError) as e:
                print(f"Error: {e}")

        elif opcion == "0":
            break

        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()
