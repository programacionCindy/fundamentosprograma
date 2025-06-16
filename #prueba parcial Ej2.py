#prueba parcial Ej2
entradas=0
while True:
    print("===== Cine Estrella ======")
    print("Bienvenido al sistema de venta de entradas del Cine Estrella")
    print("")
    print("1.- Ver cuántas entradas quedan.")
    print("2.- Comprar una cantidad de entradas.")
    print("3.- Cargar entradas.")
    print("4.- Salir del sistema.")

    try:
        opcion=int(input("Selecciona una opción (1-4): "))
    except ValueError:
        print("ingrese un numero valido")
        continue

    if opcion==1:
        print(f"Entradas disponibles {entradas}")
    elif opcion==2:
        if entradas>0:
            comprar_entradas=int(input("¿Cuántas entradas desea comprar?: "))
            if comprar_entradas<= entradas:
                print(f"Compra exitosa. Quedan {entradas} entradas.")
                continue
            else:
                print("ingrese un numero valido")
                continue
        else:
            print("No hay suficientes entradas disponibles o número inválido.")
            continue

    elif opcion==3:
        carga_de_entradas=int(input("¿Cuántas entradas desea cargar?: "))
        entradas= entradas+carga_de_entradas
        print(f"Se han cargado {carga_de_entradas} entradas. Total disponible: {entradas}")
        continue
    elif opcion==4:
        print("Gracias por usar el sistema de ventas del Cine Estrella. ¡Hasta pronto!")
        break
    else:
        print("ingrese un numero valido")