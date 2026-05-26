from modelos import Libro, Miembro


class LibroNoEncontradoError(Exception):
    pass

class MiembroNoEncontradoError(Exception):
    pass

class LibroNoDisponibleError(Exception):
    pass

class LibroNoPrestadoError(Exception):
    pass

class ISBNDuplicadoError(Exception):
    pass

class DNIDuplicadoError(Exception):
    pass


class Biblioteca:
    def __init__(self):
        self.libros = []
        self.miembros = []

    def _buscar_libro(self, isbn):
        for l in self.libros:
            if l.isbn == isbn:
                return l
        return None

    def _buscar_miembro(self, dni):
        for m in self.miembros:
            if m.dni == dni:
                return m
        return None

    def agregar_libro(self, titulo, autor, isbn):
        if self._buscar_libro(isbn):
            raise ISBNDuplicadoError(f"Ya existe un libro con ISBN '{isbn}'.")
        self.libros.append(Libro(titulo, autor, isbn))
        print(f"Libro '{titulo}' agregado correctamente.")

    def agregar_miembro(self, nombre, dni):
        if self._buscar_miembro(dni):
            raise DNIDuplicadoError(f"Ya existe un miembro con DNI '{dni}'.")
        self.miembros.append(Miembro(nombre, dni))
        print(f"Miembro '{nombre}' agregado correctamente.")

    def prestar_libro(self, isbn, dni):
        libro = self._buscar_libro(isbn)
        if not libro:
            raise LibroNoEncontradoError(f"No se encontró el libro con ISBN '{isbn}'.")
        miembro = self._buscar_miembro(dni)
        if not miembro:
            raise MiembroNoEncontradoError(f"No se encontró el miembro con DNI '{dni}'.")
        if not libro.esta_disponible():
            raise LibroNoDisponibleError(f"El libro '{libro.titulo}' no está disponible.")
        libro.prestar(dni)
        miembro.tomar_libro(libro)
        print(f"Libro '{libro.titulo}' prestado a {miembro.nombre}.")

    def devolver_libro(self, isbn, dni):
        libro = self._buscar_libro(isbn)
        if not libro:
            raise LibroNoEncontradoError(f"No se encontró el libro con ISBN '{isbn}'.")
        miembro = self._buscar_miembro(dni)
        if not miembro:
            raise MiembroNoEncontradoError(f"No se encontró el miembro con DNI '{dni}'.")
        if libro.esta_disponible():
            raise LibroNoPrestadoError(f"El libro '{libro.titulo}' no está actualmente prestado.")
        libro.devolver()
        miembro.devolver_libro(libro)
        print(f"Libro '{libro.titulo}' devuelto por {miembro.nombre}.")

    def mostrar_libros(self):
        if not self.libros:
            print("No hay libros registrados.")
            return
        print("--- Libros registrados ---")
        for l in self.libros:
            print(l)

    def mostrar_miembros(self):
        if not self.miembros:
            print("No hay miembros registrados.")
            return
        print("--- Miembros registrados ---")
        for m in self.miembros:
            print(m)
