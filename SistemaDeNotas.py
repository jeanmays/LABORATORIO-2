import pickle
class Alumnos:
    def __init__(self, alumno_id, nombre, email):
        self.id = alumno_id
        self.nombre = nombre
        self.email = email

class Cursos:
    def __init__(self, codigo, nombre, creditos):
        self.codigo = codigo
        self.nombre = nombre
        self.creditos = creditos

class Matricula:
    def __init__(self, alumno_id, codigo_curso):
        self.IdAlumno = alumno_id
        self.CodigoCurso = codigo_curso
        self.Grado = []

LAlumnos = []
LCursos = []
Incripcion = []

def buscar_alumno(alumno_id):
    for s in LAlumnos:
        if s.id == alumno_id:
            return s
    return None

def buscar_curso(codigo):
    for c in LCursos:
        if c.codigo == codigo:
            return c
    return None

def buscar_matricula(alumno_id, codigo):
    for e in Incripcion:
        if e.IdAlumno == alumno_id and e.CodigoCurso == codigo:
            return e
    return None

def agregar_estudiante():
    Ids = input("ID estudiante: ")
    Nombre = input("Nombre: ")
    email = input("Email: ")
    LAlumnos.append(Alumnos(Ids, Nombre, email))
    print("Estudiante agregado")

def listar_estudiantes():
    if not LAlumnos:
        print("(sin estudiantes)")
        return
    for s in LAlumnos:
        print(s.id, s.nombre, s.email)

def agregar_curso():
    Codigo = input("Código curso: ")
    Nombre = input("Nombre: ")
    Creditos = int(input("Créditos: "))
    LCursos.append(Cursos(Codigo, Nombre, Creditos))
    print("Curso agregado")

def listar_cursos():
    if not LCursos:
        print("(sin cursos)")
        return
    for c in LCursos:
        print(c.codigo, c.nombre, c.creditos)

def matricular_estudiante():
    ids = input("ID estudiante: ")
    codigo = input("Código curso: ")
    if not buscar_alumno(ids):
        print("El estudiante no existe (primero agréguelo).")
        return
    if not buscar_curso(codigo):
        print("El curso no existe (primero agréguelo).")
        return
    if buscar_matricula(ids, codigo):
        print("Ya está matriculado en ese curso.")
        return
    Incripcion.append(Matricula(ids, codigo))
    print("Matrícula creada")

def listar_matriculas():
    if not Incripcion:
        print("(sin matrículas)")
        return
    for e in Incripcion:
        print(e.IdAlumno, "->", e.CodigoCurso, "Notas:", e.Grado)

def agregar_nota():
    ids = input("ID estudiante: ")
    codigo = input("Código curso: ")
    nota = float(input("Nota: "))
    m = buscar_matricula(ids, codigo)
    if m:
        m.Grado.append(nota)
        print("Nota registrada")
    else:
        print("Matrícula no encontrada")

def promedio(grades):
    return round(sum(grades)/len(grades), 2) if grades else 0

def reporte_estudiante():
    sid = input("ID estudiante: ")
    encontrado = False
    for e in Incripcion:
        if e.IdAlumno == sid:
            encontrado = True
            print(sid, "->", e.CodigoCurso, e.Grado, "Prom:", promedio(e.Grado))
    if not encontrado:
        print("Sin datos para ese estudiante")

def reporte_curso():
    code = input("Código curso: ")
    encontrado = False
    for e in Incripcion:
        if e.CodigoCurso == code:
            encontrado = True
            print(e.IdAlumno, e.Grado, "Prom:", promedio(e.Grado))
    if not encontrado:
        print("Sin datos para ese curso")

def guardar_archivo():
    with open("Datos.pkl", "wb") as f:
        pickle.dump((LAlumnos, LCursos, Incripcion), f)

def cargar_archivo():
    global LAlumnos, LCursos, Incripcion
    try:
        with open("Datos.pkl", "rb") as f:
            LAlumnos, LCursos, Incripcion = pickle.load(f)
    except FileNotFoundError:
        pass

def menu_principal():
    while True:
        print("\n--- GESTOR DE NOTAS ---")
        print("1) Listar estudiantes")
        print("2) Listar cursos")
        print("3) Listar matrículas")
        print("4) Agregar estudiante")
        print("5) Agregar curso")
        print("6) Matricular estudiante")
        print("7) Agregar nota")
        print("8) Reporte por curso")
        print("9) Reporte por estudiante")
        print("0) Guardar y Salir")
        op = input("Elige opción: ")
        if op == "1": listar_estudiantes()
        elif op == "2": listar_cursos()
        elif op == "3": listar_matriculas()
        elif op == "4": agregar_estudiante()
        elif op == "5": agregar_curso()
        elif op == "6": matricular_estudiante()
        elif op == "7": agregar_nota()
        elif op == "8": reporte_curso()
        elif op == "9": reporte_estudiante()
        elif op == "0":
            print("Saliendo...")
            guardar_archivo()
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    cargar_archivo()
    menu_principal()
