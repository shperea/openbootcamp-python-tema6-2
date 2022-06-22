class Alumno:
    nombre = None
    nota = None

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

alumno = Alumno("Jose María", 7)
print("Nombre:", alumno.nombre, "\nNota:", alumno.nota)