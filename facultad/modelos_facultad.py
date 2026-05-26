class Estudiante:
    def __init__(self, nombre, apellido, matricula, carrera):
        self.nombre = nombre
        self.apellido = apellido
        self.matricula = matricula
        self.carrera = carrera
        self.cursos_inscriptos = []

    def inscribirse(self, curso):
        self.cursos_inscriptos.append(curso)

    def desinscribirse(self, curso):
        self.cursos_inscriptos.remove(curso)

    def __str__(self):
        if self.cursos_inscriptos:
            nombres = ", ".join(f"'{c.nombre}'" for c in self.cursos_inscriptos)
            return f"{self.nombre} {self.apellido} (Matrícula: {self.matricula}) - Carrera: {self.carrera} - Cursos: {nombres}"
        return f"{self.nombre} {self.apellido} (Matrícula: {self.matricula}) - Carrera: {self.carrera} - Sin cursos inscriptos"


class Curso:
    def __init__(self, nombre, codigo, profesor, cupo_maximo):
        self.nombre = nombre
        self.codigo = codigo
        self.profesor = profesor
        self.cupo_maximo = cupo_maximo
        self.estudiantes = []

    def tiene_cupo(self):
        return len(self.estudiantes) < self.cupo_maximo

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    def quitar_estudiante(self, estudiante):
        self.estudiantes.remove(estudiante)

    def __str__(self):
        inscriptos = len(self.estudiantes)
        return f"'{self.nombre}' - Cód: {self.codigo} | Prof: {self.profesor} | Cupo: {inscriptos}/{self.cupo_maximo}"
