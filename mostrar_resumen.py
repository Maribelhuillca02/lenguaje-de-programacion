def mostrar_resumen(tram, n): 

 

    c1 = 0 

    c2 = 0 

    c3 = 0 

    c4 = 0 

 

    for tipo in tram: 

 

        if tipo == 1: 

            c1 += 1 

        elif tipo == 2: 

            c2 += 1 

        elif tipo == 3: 

            c3 += 1 

        elif tipo == 4: 

            c4 += 1 

 

    print("\n--- RESUMEN DE ATENCIONES ---") 

    print("Total de expedientes:", n) 

    print("Constancia de matricula:", c1) 

    print("Constancia de vacante:", c2) 

    print("Certificado de estudios:", c3) 

    print("Ficha unica de matricula (FUM):", c4)