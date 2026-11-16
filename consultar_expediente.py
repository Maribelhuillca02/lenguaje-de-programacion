def consultar_expediente(cod, dni_a, nom_a, 

                         dni_e, nom_e, tram, fec, n): 

 

    print("\n--- CONSULTA DE EXPEDIENTE ---") 

 

    try: 

        codigo = int(input("Ingrese el codigo que desea consultar: ")) 

    except ValueError: 

        print("Codigo invalido.") 

        return 

 

    for i in range(n): 

 

        if cod[i] == codigo: 

            print("\nEXPEDIENTE ENCONTRADO") 

            print("--------------------------------") 

            print("Codigo: EXP-", cod[i], sep="") 

            print("DNI apoderado:", dni_a[i]) 

            print("Apoderado:", nom_a[i]) 

            print("DNI estudiante:", dni_e[i]) 

            print("Estudiante:", nom_e[i]) 

            print("Tramite:", nombre_tramite(tram[i])) 

            print("Fecha de recepcion:", fec[i]) 

            return 

 

    print("No se encontro el expediente solicitado.")