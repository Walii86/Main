#print("Esta es una prueba git.")

datos_escuela = {
    "alumnos":[]
}

def mostrar_menu():
    print("Menú de Gestión Escolar")
    print("1- Agregar nuevo Alumno")
    print("2- Mostrar todos los Alumnos")
    print("3- Modificar Datos del Alumno")
    print("4- Expulsar Alumno")
    print("0- Salir del Programa")

def buscar_alumno_dni(dni):
    for alumno in datos_escuela["alumnos"]:
        if alumno["Dni"] == dni:
            return alumno
    return None

def agregar_alumno():
    nombre = input("Nombre del alumno: ")
    apellido = input("Apellido del Alumno: ")
    dni = input("Dni del alumno: ")
    fecha_nacimiento = input("Fecha de Nacimiento (DD/MM/AA): ")
    tutor = input("Nombre del Tutor: ")

    nuevo_alumno = {
        "Nombre": nombre,
        "Apellido": apellido,
        "Dni": dni,
        "Fecha de Nacimiento": fecha_nacimiento,
        "Tutor": tutor,
        "Notas": [],
        "Faltas": 0,
        "Amonestaciones": 0
    }

    datos_escuela["alumnos"].append(nuevo_alumno)
    print(f"Alumno '{nombre}' '{apellido}' agregado")

def mostrar_alumnos():

    print("LISTA DE ALUMNOS")
    if not datos_escuela["alumnos"]:
        print("No hay Alumnos registrados")
    else:
        contador = 1
        for alumno in datos_escuela["alumnos"]:

            print(f"{contador}- {alumno['Nombre']} {alumno['Apellido']} Dni: {alumno["Dni"]}")
            print(f"Fecha de Nacimiento: {alumno['Fecha de nacimiento']}")
            print(f"Tutor: {alumno['Tutor']}")
            print(f"Notas: {alumno['Notas']}")
            print(f"Faltas: {alumno['Faltas']}")
            print(f"Amonestaciones: {alumno['Amonestaciones']}")

            contador = contador + 1


def modificar_alumno():

    dni_a_modificar = input("Ingrese Dni a modificar: ")

    alumno = buscar_alumno_dni(dni_a_modificar)
    print(f"{alumno['Nombre']} {alumno['Apellido']}")
    print("Que datos quiere modificar?")
    print("a) Nombre y Apellido")
    print("b) Tutor")
    print("c) Agregar una Nota")
    print("d) Registrar una Falta")
    print("e) Registrar una Amonestación")

    opcion = input("Seleccione una opción: ")

    if opcion == 'a' or opcion == 'A':
        alumno['Nombre'] = input(f"Nuevo Nombre {alumno['Nombre']}: ")
        alumno['Apellido'] = input(f"Nuevo Apellido {alumno['Apellido']}: ")
    elif opcion == 'b' or opcion == 'B':
        alumno['Tutor'] = input(f"Nuevo Tutor {alumno['Tutor']}: ")
    elif opcion == 'c' or opcion == 'C':
        nota = input("Ingrese la nueva Nota: ")
        if es_numero(nota):
            nota = float(nota)
            alumno['Notas'].append(nota)
    elif opcion == 'd' or opcion == 'D':
        alumno['Faltas'] = alumno['Faltas'] + 1
        print("Se registra la Falta")
    elif opcion == 'e' or opcion == 'E':
        alumno['Amonestaciones'] = alumno['Amonestaciones'] + 1
        print("Se registra Amonestación")
    else:
        print("Opcion no válida")
        return
    print("Datos actualizados")

def expulsar_alumno():
    dni_expulsion = input("Ingrese Dni a Expulsar")

    alumno = buscar_alumno_dni(dni_expulsion)

    if not alumno:
        print("No se encontró alumno")
        return
    
    confirmacion = input(f"Está seguro de que quiere expulsar a {alumno['Nombre']} {alumno['Apellido']}: ? ")

    if confirmacion == 's' or confirmacion == 'S':
        datos_escuela["Alumnos"].remove(alumno)
        print("Alumno expulsado")

def main():

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregar_alumno()
        elif opcion == '2':
            mostrar_alumnos()
        elif opcion == '3':
            modificar_alumno()
        elif opcion == '4':
            expulsar_alumno()
        elif opcion == '0':
            print("Hasta Luego")
            break
        else:
            print("Intente de nuevo.")

if __name__ == "__main__":
    main()

