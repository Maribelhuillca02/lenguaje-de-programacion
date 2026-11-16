def listar_expedientes(cod, dni_a, nom_a, 

                       dni_e, nom_e, tram, fec, n): 

 

    print("\n--- EXPEDIENTES REGISTRADOS ---") 

 

    if n == 0: 

        print("No hay expedientes registrados.") 

        return 

 

    for i in range(n): 

 

        print("\n--------------------------------") 

        print("Codigo: EXP-", cod[i], sep="") 

        print("DNI apoderado:", dni_a[i]) 

        print("Apoderado:", nom_a[i]) 

        print("DNI estudiante:", dni_e[i]) 

        print("Estudiante:", nom_e[i]) 

        print("Tramite:", nombre_tramite(tram[i])) 

        print("Fecha de recepcion:", fec[i]) 