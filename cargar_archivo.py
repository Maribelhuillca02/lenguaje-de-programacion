 

def cargar_archivo(ruta): 

    cod = [] 

    dni_a = [] 

    nom_a = [] 

    dni_e = [] 

    nom_e = [] 

    tram = [] 

    fec = [] 

 

    try: 

        with open(ruta, "r", encoding="utf-8") as archivo: 

            for numero_linea, linea in enumerate(archivo, start=1): 

                partes = linea.strip().split("|") 

 

                if len(partes) != 7: 

                    print(f"Linea {numero_linea} invalida. Se omite.") 

                    continue 

 

                try: 

                    codigo = int(partes[0]) 

                    tipo_tramite = int(partes[5]) 

 

                    if tipo_tramite not in range(1, 5): 

                        continue 

 

                except ValueError: 

                    print(f"Datos invalidos en linea {numero_linea}.") 

                    continue 

 

                cod.append(codigo) 

                dni_a.append(partes[1]) 

                nom_a.append(partes[2]) 

                dni_e.append(partes[3]) 

                nom_e.append(partes[4]) 

                tram.append(tipo_tramite) 

                fec.append(partes[6]) 

 

    except FileNotFoundError: 

        print("No existe un archivo previo. Se iniciara sin expedientes.") 

 

    n = len(cod) 

 

    return cod, dni_a, nom_a, dni_e, nom_e, tram, fec, n