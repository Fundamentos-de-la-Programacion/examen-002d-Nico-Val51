
# Funciones
def leer_opcion():
    while True:
        try:
            opc = int(input("Ingrese una opcion: "))
            if opc < 1 or opc > 6:
                raise ValueError
        except ValueError:
            print("Error: Ingrese una opcion valida")
        else:
            return opc

def cupos_tipos(tipo, planes, inscripciones):
    cupos = 0
    for cod in planes.keys():
        if tipo.lower() == planes[cod][1].lower():
            cupos += inscripciones[cod][1]
    if cupos > 0:
        print(f"\nHay un total de {cupos} cupos disponibles para los planes de tipo {tipo.lower()}")
    else:
        print(f"\nNo hay cupos para ese tipo de plan")

def busqueda_precios(min, max, planes, inscripciones):
    lista_p = []
    for cod in planes.keys():
        if (min < inscripciones[cod][0] < max) and inscripciones[cod][1] != 0:
            formato = planes[cod][0]+"--"+cod
            lista_p.append(formato)
        lista_p.sort()
    if len(lista_p) == 0:
        print("\nNo hay planes en ese rango de precios")
    else:
        print("\nLos siguientes planes estan en ese rango de precios:")
        for plan in lista_p:
            print(f"- {plan}")          

def buscar_codigo(codigo, planes):
    if codigo in planes.keys():
        return True
    else:
        return False

def actualizar_precio(codigo, nuevo_precio, inscripciones):
    check = buscar_codigo(codigo, inscripciones)
    if check == True:
        inscripciones[codigo][1] = nuevo_precio
        return True
    else:
        return False

def validar_codigo(codigo, planes):
    if codigo.isspace() == True or (codigo == ""):
        return False
    else:
        return True

def validar_nombre(nombre):
    if nombre.isspace() == True or nombre == "":
        return False
    else:
        return True

def validar_tipo(tipo):
    if tipo not in ("mensual", "trimestral", "anual"):
        return False
    else:
        return True

def validar_duracion(duracion):
    try:
        int(duracion)
        if int(duracion) <= 0:
            raise ValueError
    except ValueError:
        return False
    else:
        return True

def validar_piscina(piscina):
    if piscina == "s":
        return True
    else:
        return False

def validar_clases(clases):
    if clases == "s":
        return True
    else:
        return False

def validar_horario(horario):
    if horario.isspace() == True or horario == "":
        return False
    else:
        return True

def validar_precio(precio):
    try:
        int(precio)
        if int(precio) <= 0:
            raise ValueError
    except ValueError:
        return False
    else:
        return True

def validar_cupos(cupos):
    try:
        int(cupos)
        if int(cupos) < 0:
            raise ValueError
    except ValueError:
        return False
    else:
        return True

def agregar_plan(codigo, nombre, tipo, duracion, acceso_p, incluye_c, horario, precio, cupos, planes, inscripciones):
    if buscar_codigo(codigo, planes) == True:
        return False
    lista_p = [nombre, tipo, duracion, acceso_p, incluye_c, horario]
    lista_i = [precio, cupos]

    planes[codigo] = lista_p
    inscripciones[codigo] = lista_i
    return True

def eliminar_plan(codigo, planes, inscripciones):
    if buscar_codigo(codigo, planes) == False:
        return False
    planes.pop(codigo)
    inscripciones.pop(codigo)
    return True

# Main
planes = { 
    'F001': ['Plan Básico', 'mensual', 1, False, False, 'libre'], 
    'F002': ['Plan Full', 'mensual', 1, True, True, 'libre'], 
    'F003': ['Plan Estudiante', 'trimestral', 3, False, True, 
'tarde'], 
    'F004': ['Plan Senior', 'trimestral', 3, True, False, 'mañana'], 
    'F005': ['Plan Anual Pro', 'anual', 12, True, True, 'libre'], 
    'F006': ['Plan Nocturno', 'mensual', 1, False, True, 'noche']
}

inscripciones = { 
    'F001': [14990, 30], 
    'F002': [22990, 10], 
    'F003': [39990, 0], 
    'F004': [35990, 6], 
    'F005': [159990, 2], 
    'F006': [18990, 15]
}

while True:
    print("""========== MENÚ PRINCIPAL ========== 
1. Cupos por tipo de plan 
2. Búsqueda de planes por rango de precio 
3. Actualizar precio de plan 
4. Agregar plan 
5. Eliminar plan 
6. Salir 
=====================================""")
    opc = leer_opcion()

    if opc == 1:
        tipo = input("\nIngrese tipo de plan (Mensual/Trimestral/Anual): ")
        cupos_tipos(tipo, planes, inscripciones)

    elif opc == 2:
        while True:
            try:
                min = int(input("\nIngrese un precio minimo (Entero mayor a 0): "))
                max = int(input("Ingrese un precio maximo (Entero mayor a minimo): "))
                if min <= 0 or max <= 0 or max <= min:
                    raise ValueError
            except ValueError:
                print("Error: Ingrese un numero entero valido")
            else:
                break
        busqueda_precios(min, max, planes, inscripciones)

    elif opc == 3:
        while True:
            cod = input("\nIngrese el codigo del plan que desea actualizar: ")
            while True:
                try:
                    precio = int(input("Ingrese el nuevo precio (Entero mayor a 0): "))
                    if precio <= 0:
                        raise ValueError
                except ValueError:
                    print("Error: Precio ingresado no valido")
                else:
                    break
            actualizar = actualizar_precio(cod, precio, inscripciones)
            if actualizar == True:
                print("> Precio actualizado")
            else:
                print("> Codigo no existe")
            
            while True:
                try:
                    cont = input("Desea actualizar otro precio? (s/n) ").lower()
                    if cont not in ("s","n"):
                        raise ValueError
                except ValueError:
                    print("Ingrese un valor valido (s/n)")
                else:
                    break
            if cont == "n":
                break

    elif opc == 4:
        while True:
            cod = input("\nIngrese el codigo del nuevo plan: ")
            if validar_codigo(cod, planes) == False:
                print("El codigo no puede estar en blanco")
                continue
            
            nom = input("Ingrese el nombre del nuevo plan: ")
            if validar_nombre(nom) == False:
                print("El nombre no puede estar en blanco")
                continue
            
            tipo = input("Ingrese el tipo del nuevo plan (mensual/trimestral/anual): ")
            if validar_tipo(tipo) == False:
                print("El tipo debe ser 'mensual', 'trimestral' o 'anual'")
                continue
            

            dura = input("Ingrese la duracion (meses) del nuevo plan: ")
            if validar_duracion(dura) == False:
                print("La duración debe ser un numero entero mayor a 0")
                continue
            
            a_pisc = input("Incluye acceso a piscina? (s/n) ").lower()
            if a_pisc not in ("s", "n"):
                continue
            acceso_p = validar_piscina(a_pisc)
            
            clases = input("Incluye clases? (s/n) ").lower()
            if clases not in ("s", "n"):
                continue
            incluye_c = validar_clases(clases)

            hora = input("Ingrese el horario del nuevo plan: ")
            if validar_horario(hora) == False:
                print("El horario no puede estar en blanco")
                continue
            
            precio = input("Ingrese el precio del nuevo plan: ")
            if validar_precio(precio) == False:
                print("El precio debe ser un numero entero mayor a 0")
                continue
            
            cupo = input("Cuantos cupos disponibles tiene el nuevo plan: ")
            if validar_cupos(cupo) == False:
                print("La cantidad de cupos disponible debe ser un numero entero mayor a 0")
                continue
            
            check = agregar_plan(cod, nom, tipo, dura, acceso_p, incluye_c, hora, precio, cupo, planes, inscripciones)
            if check == True:
                print("> Plan agregado")
                break
            else:
                print("> Codigo ya existe")
                break

    elif opc == 5:
        cod = input("\nIngresa el codigo del plan a eliminar: ")
        check = eliminar_plan(cod, planes, inscripciones)
        if check == True:
            print("> Plan eliminado")
        else:
            print("> Codigo no existe")

    elif opc == 6:
        print("\n> Programa finalizado")
        break

    print("")