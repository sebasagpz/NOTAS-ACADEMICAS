print(f"----REGISTRO Y ANÁLISIS NOTAS ACADEMICAS---")

print("INGRESO DE MATERIAS")
materias = ("MATEMATICAS", "LENGUAJE", "BIOLOGIA")
print(f"MATERIAS DISPONIBLES {materias}")

print(f"SELECCIONA UNA MATERIA")
materia1 = input("Usuario, selecciona el nombre de la primera materia: ").upper()

print("INGRESAR ESTUDIANTE")
nombre1 = input("Usuario, selecciona el nombre del estudiante que quieres agregar: ")

print("INGRESAR NOTAS")
nota1 = float(input("Ingresa la nota 1 del parcial: "))
nota2 = float(input("Ingresa la nota 2 del parcial: "))
nota3 = float(input("Ingresa la nota 3 del parcial: "))

list1 = [nota1, nota2, nota3]
dic1 = {
    nombre1 : list1,
}

print(f"MENÚ DE OPCIONES\n Usa las claves para desplazarte por el menu\n ADD: AGREGAR NUEVO ESTUDIANTE\n MODIFY: MODIFICAR NOTAS DE UN ESTUDIANTE\n DEL: REMOVER UN ESTUDIANTE\n TMP: NOTAS FINALES")
pre = input("INGRESA LO QUE QUIERES HACER: ").upper()


if pre == "ADD":
    print("AGREGAR NUEVO ESTUDIANTE")
    materia2 = input("Usuario, agrega el nombre de la segunda materia: ")
    nombre2 = input("Usuario, selecciona el nombre del estudiante que quieres agregar: ")
    print("INGRESAR NOTAS")
    nota11 = float(input("Ingresa la nota 1 del parcial: "))
    nota12 = float(input("Ingresa la nota 2 del parcial: "))
    nota13 = float(input("Ingresa la nota 3 del parcial: "))
    list2 = [nota11, nota12, nota13]
    dic2 = {
        nombre2 : list2
    }

    
nombre2 = ""
aprobo1 = ""
aprobo2 = ""
desaprobo1 = ""
desaprobo2 = ""

if pre == "MODIFY":
    print("MODIFICA LAS NOTAS DE UN ESTUDIANTE EXISTENTE")
    prenombre = input("Ingresa el nombre del estudiante al que quieres modificar: ")
    if prenombre == nombre1:
        notap1 = int(input(f"INGRESA LA NOTA QUE QUIERES MODIFICAR (1, 2, 3). "))
        if notap1 == 1:
            modify1 = float(input(f"INGRESA LA NOTA A MODIFICAR"))
            list1[0] = modify1
            print(f"La nota modificada fue a {list1[0]}")
        elif notap1 == 2:
            modify2 = float(input(f"INGRESA LA NOTA A MODIFICAR"))
            list1[1] = modify2
            print(f"La nota modificada fue a {list1[1]}")
        elif notap1 == 3:
            modify3 = float(input(f"INGRESA LA NOTA A MODIFICAR"))
            list1[2] = modify3
            print(f"La nota modificada fue a {list1[2]}")
        else:
            print(f"No se acepta esta opción")
    elif prenombre == nombre2:
        notap2 = int(input(f"INGRESA LA NOTA QUE QUIERES MODIFICAR (1, 2, 3): "))
        if notap2 == 1:
            modify11 = float(input(f"INGRESA LA NOTA A MODIFICAR"))
            list1[0] = modify11
            print(f"La nota modificada fue a {list2[0]}")
        elif notap2 == 2:
            modify12 = float(input(f"INGRESA LA NOTA A MODIFICAR"))
            list1[1] = modify12
            print(f"La nota modificada fue a {list2[1]}")
        elif notap2 == 3:
            modify13 = float(input(f"INGRESA LA NOTA A MODIFICAR"))
            list1[2] = modify13
            print(f"La nota modificada fue a {list2[2]}")
        else:
            print(f"No se acepta esta opción")
    else:
      print("Este estudiante no existe / MODIFY")
            
if pre == "DEL":
    print("REMUEVE UN ESTUDIANTE DE LA BASE DE DATOS")
    delnombre = input("Ingresa el nombre del estudiante que quieres eliminar: ")
    if delnombre == nombre1:
        dic1.clear()
        print("Se borró el estudiante.")
    elif delnombre == nombre2:
        dic2.clear()
        print("Se borró el estudiante.")
    else:
     print("Ese nombre no está permitido/no existe / DEL")


if pre == "TMP":
    nombretmp1 = input("Ingresa el nombre del estudiante al que quieres saber sus notas finales: ")
    if nombretmp1 == nombre1:
        print("TERMINA EL PROCESO\n REGISTRO")
        print(f"NOTAS FINALES DEL ESTUDIANTE {nombre1}\MATERIA: {materia1}\nNOTA 1: {list1[0]}\n NOTA 2: {list1[1]}, NOTA 3: {list1[2]}")
        suma1 = list1[0] + list1[1] + list1[2]
        division1 = suma1 / 3

        print(f"PROMEDIO FINAL DEL ESTUDIANTE {nombre1}: {division1}")
        if division1 > 3:
            aprobo1 = division1
            print("El estudiante aprobó")
        else:
            desaprobo1 = division1
            print("El estudiante desaprobó")
         
    elif nombretmp1 == nombre2:
        print("TERMINA EL PROCESO\n REGISTRO")
        print(f"NOTAS FINALES DEL ESTUDIANTE {nombre2}\nMATERIA: {materia2}\nNOTA 1: {list2[0]}\n NOTA 2: {list2[1]}, NOTA 3: {list2[2]}")
        suma2 = list2[0] + list2[1] + list2[2]
        division2 = suma2 / 3
        print(f"PROMEDIO FINAL DEL ESTUDIANTE {nombre2}: {division2}")
        if division2 > 3:
            aprobo2 = division2
            print("El estudiante aprobó")
        else:
            desaprobo2 = division2
            print("El estudiante desaprobó")

print("RESUMEN GENERAL")
totalestudiantes = [nombre1, nombre2]
print(f"ESTUDIANTES EN TOTAL: {len(totalestudiantes)}")
totalaprobados = [aprobo1, aprobo2]
print(f"APROBARON: {len(totalaprobados)}")
totaldesaprobados = [desaprobo2, desaprobo1]
print(f"DESAPROBARON: {len(totaldesaprobados)}")


