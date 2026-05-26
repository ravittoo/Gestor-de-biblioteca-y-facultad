class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True
        self.prestado_a = None

    def esta_disponible(self):
        return self.disponible

    def prestar(self, dni_miembro):
        self.disponible = False
        self.prestado_a = dni_miembro

    def devolver(self):
        self.disponible = True
        self.prestado_a = None

    def __str__(self):
        estado = "Disponible" if self.disponible else f"Prestado a DNI: {self.prestado_a}"
        return f"'{self.titulo}' - {self.autor} (ISBN: {self.isbn}) [{estado}]"


class Miembro:
    def __init__(self, nombre, dni):
        self.nombre = nombre
        self.dni = dni
        self.libros_prestados = []

    def tomar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, libro):
        self.libros_prestados.remove(libro)

    def __str__(self):
        if self.libros_prestados:
            titulos = ", ".join(f"'{l.titulo}'" for l in self.libros_prestados)
            return f"{self.nombre} (DNI: {self.dni}) - Libros: {titulos}"
        return f"{self.nombre} (DNI: {self.dni}) - Sin libros prestados"
