import pickle  # Importa el módulo pickle, que permite guardar y cargar objetos de Python en archivos binarios.

# Definición de la clase Alumnos
class Alumnos:
    def __init__(self, alumno_id, nombre, email):  # Constructor que inicializa un alumno
        self.id = alumno_id  # Asigna el ID del alumno
        self.nombre = nombre  # Asigna el nombre del alumno
        self.email = email  # Asigna el email del alumno

# Definición de la clase Cursos
class Cursos:
    def __init__(self, codigo, nombre, creditos):  # Constructor que inicializa un curso
        self.codigo = codigo  # Código único del curso
        self.nombre = nombre  # Nombre del curso
        self.creditos = creditos  # Número de créditos del curso

# Definición de la clase Matricula
class Matricula:
    def __init__(self, alumno_id, codigo_curso):  # Constructor que vincula un alumno con un curso
        self.IdAlumno = alumno_id  # ID del alumno matriculado
        self.CodigoCurso = codigo_curso  # Código del curso en el que se matricula
        self.Grado = []  # Lista vacía para almacenar las notas del alumno en ese curso

# Listas principales para guardar los datos en memoria
LAlumnos = []  # Lista de todos los alumnos
LCursos = []  # Lista de todos los cursos
Incripcion = []  # Lista de todas las matrículas (relaciones alumno-curso)

# Función para buscar un alumno por su ID
def buscar_alumno(alumno_id):
    for s in LAlumnos:  # Recorre la lista de alumnos
        if s.id == alumno_id:  # Si encuentra coincidencia por ID
            return s  # Devuelve el objeto alumno
    return None  # Si no lo encuentra, devuelve None

# Función para buscar un curso por su código
def buscar_curso(codigo):
    for c in LCursos:  # Recorre la lista de cursos
        if c.codigo == codigo:  # Si encuentra coincidencia por código
            return c  # Devuelve el objeto curso
    return None  # Si no lo encuentra, devuelve None

# Función para buscar una matrícula por alumno y curso
def buscar_matricula(alumno_id, codigo):
    for e in Incripcion:  # Recorre todas las matrículas
        if e.IdAlumno == alumno_id and e.CodigoCurso == codigo:  # Si coincide alumno y curso
            return e  # Devuelve la matrícula
    return None  # Si no encuentra, devuelve None

# Función para agregar un estudiante
def agregar_estudiante():
    Ids = input("ID estudiante: ")  # Pide el ID del alumno
    Nombre = input("Nombre: ")  # Pide el nombre del alumno
    email = input("Email: ")  # Pide el correo electrónico del alumno
    LAlumnos.append(Alumnos(Ids, Nombre, email))  # Crea un objeto Alumno y lo agrega a la lista
    print("Estudiante agregado")  # Confirma la acción

# Función para listar estudiantes
def listar_estudiantes():
    if not LAlumnos:  # Si la lista está vacía
        print("(sin estudiantes)")  # Muestra mensaje
        return  # Sale de la función
    for s in LAlumnos:  # Recorre los alumnos
        print(s.id, s.nombre, s.email)  # Muestra ID, nombre y email de cada alumno

# Función para agregar un curso
def agregar_curso():
    Codigo = input("Código curso: ")  # Pide el código del curso
    Nombre = input("Nombre: ")  # Pide el nombre del curso
    Creditos = int(input("Créditos: "))  # Pide los créditos y convierte a entero
    LCursos.append(Cursos(Codigo, Nombre, Creditos))  # Crea el curso y lo agrega a la lista
    print("Curso agregado")  # Confirma la acción

# Función para listar cursos
def listar_cursos():
    if not LCursos:  # Si no hay cursos
        print("(sin cursos)")  # Muestra mensaje
        return
    for c in LCursos:  # Recorre la lista de cursos
        print(c.codigo, c.nombre, c.creditos)  # Muestra código, nombre y créditos

# Función para matricular un estudiante en un curso
def matricular_estudiante():
    ids = input("ID estudiante: ")  # Pide el ID del estudiante
    codigo = input("Código curso: ")  # Pide el código del curso
    if not buscar_alumno(ids):  # Verifica si el alumno existe
        print("El estudiante no existe (primero agréguelo).")
        return
    if not buscar_curso(codigo):  # Verifica si el curso existe
        print("El curso no existe (primero agréguelo).")
        return
    if buscar_matricula(ids, codigo):  # Verifica si ya está matriculado
        print("Ya está matriculado en ese curso.")
        return
    Incripcion.append(Matricula(ids, codigo))  # Crea una matrícula y la guarda
    print("Matrícula creada")  # Confirma la acción

# Función para listar todas las matrículas
def listar_matriculas():
    if not Incripcion:  # Si no hay matrículas
        print("(sin matrículas)")
        return
    for e in Incripcion:  # Recorre todas las matrículas
        print(e.IdAlumno, "->", e.CodigoCurso, "Notas:", e.Grado)  # Muestra alumno, curso y notas

# Función para agregar una nota a una matrícula
def agregar_nota():
    ids = input("ID estudiante: ")  # Pide el ID del alumno
    codigo = input("Código curso: ")  # Pide el código del curso
    nota = float(input("Nota: "))  # Pide la nota y la convierte a float
    m = buscar_matricula(ids, codigo)  # Busca la matrícula correspondiente
    if m:  # Si existe
        m.Grado.append(nota)  # Agrega la nota a la lista de notas
        print("Nota registrada")  # Confirma
    else:
        print("Matrícula no encontrada")  # Si no existe, muestra error

# Función para calcular el promedio de una lista de notas
def promedio(grades):
    return round(sum(grades)/len(grades), 2) if grades else 0  # Calcula promedio, evita división entre cero

# Función para generar reporte por estudiante
def reporte_estudiante():
    sid = input("ID estudiante: ")  # Pide el ID del estudiante
    encontrado = False  # Variable bandera
    for e in Incripcion:  # Recorre matrículas
        if e.IdAlumno == sid:  # Si el ID coincide
            encontrado = True
            print(sid, "->", e.CodigoCurso, e.Grado, "Prom:", promedio(e.Grado))  # Muestra notas y promedio
    if not encontrado:  # Si no se encontró
        print("Sin datos para ese estudiante")

# Función para generar reporte por curso
def reporte_curso():
    code = input("Código curso: ")  # Pide el código del curso
    encontrado = False
    for e in Incripcion:  # Recorre matrículas
        if e.CodigoCurso == code:  # Si coincide el código
            encontrado = True
            print(e.IdAlumno, e.Grado, "Prom:", promedio(e.Grado))  # Muestra alumno y notas
    if not encontrado:
        print("Sin datos para ese curso")

# Función para guardar los datos en un archivo binario
def guardar_archivo():
    with open("Datos.pkl", "wb") as f:  # Abre el archivo en modo escritura binaria
        pickle.dump((LAlumnos, LCursos, Incripcion), f)  # Guarda las listas en el archivo

# Función para cargar los datos desde un archivo binario
def cargar_archivo():
    global LAlumnos, LCursos, Incripcion  # Indica que modificará las listas globales
    try:
        with open("Datos.pkl", "rb") as f:  # Abre el archivo en modo lectura binaria
            LAlumnos, LCursos, Incripcion = pickle.load(f)  # Carga los datos guardados
    except FileNotFoundError:  # Si el archivo no existe
        pass  # No hace nada (deja las listas vacías)

# Función principal con menú interactivo
def menu_principal():
    while True:  # Bucle infinito hasta que el usuario decida salir
        print("\n--- GESTOR DE NOTAS ---")  # Encabezado del menú
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
        op = input("Elige opción: ")  # Pide la opción al usuario
        if op == "1": listar_estudiantes()  # Muestra lista de estudiantes
        elif op == "2": listar_cursos()  # Muestra lista de cursos
        elif op == "3": listar_matriculas()  # Muestra matrículas
        elif op == "4": agregar_estudiante()  # Permite agregar estudiante
        elif op == "5": agregar_curso()  # Permite agregar curso
        elif op == "6": matricular_estudiante()  # Permite matricular estudiante
        elif op == "7": agregar_nota()  # Permite añadir nota
        elif op == "8": reporte_curso()  # Genera reporte por curso
        elif op == "9": reporte_estudiante()  # Genera reporte por estudiante
        elif op == "0":  # Si elige salir
            print("Saliendo...")  # Mensaje de salida
            guardar_archivo()  # Guarda datos antes de salir
            break  # Rompe el bucle (termina el programa)
        else:
            print("Opción inválida")  # Mensaje de error si elige una opción incorrecta

# Punto de entrada del programa
if __name__ == "__main__":
    cargar_archivo()  # Carga los datos almacenados (si existen)
    menu_principal()  # Llama al menú principal
