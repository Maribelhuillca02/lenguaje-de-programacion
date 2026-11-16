def validar_dni(dni): 

    return len(dni) == 8 and dni.isdigit() 

 

 

def validar_texto(texto): 

    return len(texto.strip()) > 0 and "|" not in texto 

 

 

def validar_tramite(opcion): 

    return opcion in (1, 2, 3, 4) 

 

 

def nombre_tramite(opcion): 

    tramites = { 

        1: "Constancia de matricula", 

        2: "Constancia de vacante", 

        3: "Certificado de estudios", 

        4: "Ficha unica de matricula (FUM)" 

    } 

 

    return tramites.get(opcion, "Desconocido") 

 

 

def generar_codigo(cod): 

    mayor = 0 

    for c in cod: 

        if c > mayor: 

            mayor = c 

    return mayor + 1 