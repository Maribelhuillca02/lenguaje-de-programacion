def registrar_expediente(cod, dni_a, nom_a, 

                         dni_e, nom_e, tram, fec, n): 

 

    print("\n--- REGISTRO DE NUEVO EXPEDIENTE ---") 

 

    if n >= 100: 

        print("Se alcanzo el limite de 100 expedientes.") 

        return n 

 

    # Generación automática del código (max + 1) según las indicaciones 

    codigo = generar_codigo(cod) 

 

    while True: 

        dni_apoderado = input("DNI del apoderado: ").strip() 

 

        if validar_dni(dni_apoderado): 

            break 

 

        print("El DNI debe contener exactamente 8 digitos.") 

 

    while True: 

        nombre_apoderado = input("Nombre del apoderado: ").strip().upper() 

 

        if validar_texto(nombre_apoderado): 

            break 

 

        print("Ingrese un nombre valido.") 

 

    while True: 

        dni_estudiante = input("DNI del estudiante: ").strip() 

 

        if validar_dni(dni_estudiante): 

            break 

 

        print("El DNI debe contener exactamente 8 digitos.") 

 

    while True: 

        nombre_estudiante = input("Nombre del estudiante: ").strip().upper() 

 

        if validar_texto(nombre_estudiante): 

            break 

 

        print("Ingrese un nombre valido.") 

 

    print("\nTIPOS DE TRAMITE") 

    print("1. Constancia de matricula") 

    print("2. Constancia de vacante") 

    print("3. Certificado de estudios") 

    print("4. Ficha unica de matricula (FUM)") 

 

    while True: 

        try: 

            tipo = int(input("Seleccione el tipo de tramite: ")) 

 

            if validar_tramite(tipo): 

                break 

 

            print("Seleccione una opcion entre 1 y 4.") 

 

        except ValueError: 

            print("Ingrese un numero valido.") 

 

    fecha = input("Fecha de recepcion (DD/MM/AAAA): ").strip() 

 

    cod.append(codigo) 

    dni_a.append(dni_apoderado) 

    nom_a.append(nombre_apoderado) 

    dni_e.append(dni_estudiante) 

    nom_e.append(nombre_estudiante) 

    tram.append(tipo) 

    fec.append(fecha) 

 

    n += 1 

 

    print("\nExpediente registrado correctamente. Codigo asignado: EXP-" + str(codigo)) 

    return n