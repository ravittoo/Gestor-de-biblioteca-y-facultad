from facultad import (
    Facultad,
    EstudianteNoEncontradoError,
    CursoNoEncontradoError,
    CursoSinCupoError,
    EstudianteYaInscriptoError,
    EstudianteNoInscriptoError,
    MatriculaDuplicadaError,
    CodigoDuplicadoError
)


def mostrar_menu():
    print("\n=== Sistema de Gestión de Facultad ===")
    print("1. Registrar estudiante")
    print("2. Registrar curso")
    print("3. Mostrar estudiantes")
    print("4. Mostrar cursos")
    print("5. Inscribir estudiante en curso")
    print("6. Desinscribir estudiante de curso")
    print("0. Salir")


def main():
    facultad = Facultad()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            matricula = input("Matrícula: ")
            carrera = input("Carrera: ")
            try:
                facultad.registrar_estudiante(nombre, apellido, matricula, carrera)
            except MatriculaDuplicadaError as e:
                print(f"Error: {e}")

        elif opcion == "2":
            nombre = input("Nombre del curso: ")
            codigo = input("Código: ")
            profesor = input("Profesor: ")
            cupo = input("Cupo máximo: ")
            try:
                facultad.registrar_curso(nombre, codigo, profesor, int(cupo))
            except CodigoDuplicadoError as e:
                print(f"Error: {e}")
            except ValueError:
                print("Error: el cupo debe ser un número entero.")

        elif opcion == "3":
            facultad.mostrar_estudiantes()

        elif opcion == "4":
            facultad.mostrar_cursos()

        elif opcion == "5":
            matricula = input("Matrícula del estudiante: ")
            codigo = input("Código del curso: ")
            try:
                facultad.inscribir_estudiante(matricula, codigo)
            except (EstudianteNoEncontradoError, CursoNoEncontradoError,
                    EstudianteYaInscriptoError, CursoSinCupoError) as e:
                print(f"Error: {e}")

        elif opcion == "6":
            matricula = input("Matrícula del estudiante: ")
            codigo = input("Código del curso: ")
            try:
                facultad.desinscribir_estudiante(matricula, codigo)
            except (EstudianteNoEncontradoError, CursoNoEncontradoError,
                    EstudianteNoInscriptoError) as e:
                print(f"Error: {e}")

        elif opcion == "0":
            print("Saliendo...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()
