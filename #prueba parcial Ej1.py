#prueba parcial Ej1
mayor=0
menor=0

while True:
    try:
        pacientes=int(input("Ingrese la cantidad de pacientes a registrar: "))
    except ValueError:
        print("ingrese un numero valido")
        continue
    
    for i in range(pacientes):
        try:
            nombre=input("Ingrese el nombre del paciente: ")
        except ValueError:
            print("ingrese un numero valido")
            continue
        
        try:
            edad=int(input(f"Ingrese la edad de {nombre}: "))
        except ValueError:
            print("ingrese un numero valido")
            continue
            
        if edad <= 60:
            print("60 años o menos.")
            menor+=1
            continue
        elif edad > 60:
            print("Mayor de 60 años.")
            mayor+=1
            continue
        else:
            print("ingrese un numero valido")
    else:
        print(f"Se registraron {mayor} pacientes mayores de 60 años.")
        print(f"Se registraron {menor} pacientes de 60 años o menos.")
        break