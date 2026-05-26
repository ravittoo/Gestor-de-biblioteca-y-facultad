from modelos_facultad import Estudiante, Curso


class EstudianteNoEncontradoError(Exception):
    pass

class CursoNoEncontradoError(Exception):
    pass

class CursoSinCupoError(Exception):
    pass

class EstudianteYaInscriptoError(Exception):
    pass

class EstudianteNoInscriptoError(Exception):
    pass

class MatriculaDuplicadaError(Exception):
    pass

class CodigoDuplicadoError(Exception):
    pass


class Facultad:
    def __init__(self):
        self.estudiantes = []
        self.cursos = []

    def _buscar_estudiante(self, matricula):
        for e in self.estudiantes:
            if e.matricula == matricula:
                return e
        return None

    def _buscar_curso(self, codigo):
        for c in self.cursos:
            if c.codigo == codigo:
                return c
        return None

    def registrar_estudiante(self, nombre, apellido, matricula, carrera):
        if self._buscar_estudiante(matricula):
            raise MatriculaDuplicadaError(f"Ya existe un estudiante con matrícula '{matricula}'.")
        nuevo = Estudiante(nombre, apellido, matricula, carrera)
        self.estudiantes.append(nuevo)
        print(f"Estudiante '{nombre} {apellido}' registrado correctamente.")

    def registrar_curso(self, nombre, codigo, profesor, cupo_maximo):
        if self._buscar_curso(codigo):
            raise CodigoDuplicadoError(f"Ya existe un curso con código '{codigo}'.")
        nuevo = Curso(nombre, codigo, profesor, cupo_maximo)
        self.cursos.append(nuevo)
        print(f"Curso '{nombre}' registrado correctamente.")

    def inscribir_estudiante(self, matricula, codigo):
        estudiante = self._buscar_estudiante(matricula)
        if not estudiante:
            raise EstudianteNoEncontradoError(f"No se encontró el estudiante con matrícula '{matricula}'.")
        curso = self._buscar_curso(codigo)
        if not curso:
            raise CursoNoEncontradoError(f"No se encontró el curso con código '{codigo}'.")
        if estudiante in curso.estudiantes:
            raise EstudianteYaInscriptoError(f"El estudiante ya está inscripto en el curso '{curso.nombre}'.")
        if not curso.tiene_cupo():
            raise CursoSinCupoError(f"El curso '{curso.nombre}' no tiene cupo disponible.")
        curso.agregar_estudiante(estudiante)
        estudiante.inscribirse(curso)
        print(f"Estudiante inscripto en '{curso.nombre}' correctamente.")

    def desinscribir_estudiante(self, matricula, codigo):
        estudiante = self._buscar_estudiante(matricula)
        if not estudiante:
            raise EstudianteNoEncontradoError(f"No se encontró el estudiante con matrícula '{matricula}'.")
        curso = self._buscar_curso(codigo)
        if not curso:
            raise CursoNoEncontradoError(f"No se encontró el curso con código '{codigo}'.")
        if estudiante not in curso.estudiantes:
            raise EstudianteNoInscriptoError(f"El estudiante no está inscripto en el curso '{curso.nombre}'.")
        curso.quitar_estudiante(estudiante)
        estudiante.desinscribirse(curso)
        print(f"Estudiante desinscripto del curso '{curso.nombre}' correctamente.")

    def mostrar_estudiantes(self):
        if not self.estudiantes:
            print("No hay estudiantes registrados.")
            return
        print("--- Estudiantes registrados ---")
        for e in self.estudiantes:
            print(e)

    def mostrar_cursos(self):
        if not self.cursos:
            print("No hay cursos registrados.")
            return
        print("--- Cursos registrados ---")
        for c in self.cursos:
            print(c)
