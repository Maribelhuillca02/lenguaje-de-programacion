def guardar_archivo(ruta, cod, dni_a, nom_a, 

                    dni_e, nom_e, tram, fec, n): 

 

    carpeta = os.path.dirname(ruta) 

 

    if carpeta: 

        os.makedirs(carpeta, exist_ok=True) 

 

    with open(ruta, "w", encoding="utf-8") as archivo: 

 

        for i in range(n): 

            linea = ( 

                f"{cod[i]}|{dni_a[i]}|{nom_a[i]}|" 

                f"{dni_e[i]}|{nom_e[i]}|{tram[i]}|{fec[i]}\n" 

            ) 

 

            archivo.write(linea) 

 

    print("Los expedientes se guardaron correctamente.") 

 