from ClaseManejadorRegistros import ManejadorRegistros

if __name__ == '__main__':
    archivo = "registros.csv"
    ListaRegistros = ManejadorRegistros()
    ListaRegistros.carga(archivo)

    ban = True
    while ban:
        print("Menu")
        print("1 - Día y hora de menor y mayor temperatura, humedad y presion")
        print("2 - Temperatura promedio mensual por cada hora")
        print("3 - Listado por dia")
        print("0 - Salir")
        print("")
        op = input("Ingrese una opcion: ")
        print("")

        if op == "0":
            ban = False

        elif op == "1":
            mayorTemperatura = ListaRegistros.MayorTemperatura()
            print(f"Mayor temperatura: {mayorTemperatura}")
            ListaRegistros.mostrarMayorTemperatura(mayorTemperatura)
            print("")

            menorTemperatura = ListaRegistros.MenorTemperatura()
            print(f"Menor temperatura: {menorTemperatura}")
            ListaRegistros.mostrarMenorTemperatura(menorTemperatura)
            print("")

            mayorHumedad = ListaRegistros.MayorHumedad()
            print(f"Mayor humedad: {mayorHumedad}")
            ListaRegistros.mostrarMayorHumedad(mayorHumedad)
            print("")

            menorHumedad = ListaRegistros.MenorHumedad()
            print(f"Menor humedad: {menorHumedad}")
            ListaRegistros.mostrarMenorHumedad(menorHumedad)
            print("")

            mayorPresion = ListaRegistros.MayorPresion()
            print(f"Mayor presion: {mayorPresion}")
            ListaRegistros.mostrarMayorPresion(mayorPresion)
            print("")

            menorPresion = ListaRegistros.MenorPresion()
            print(f"Menor presion: {menorPresion}")
            ListaRegistros.mostrarMenorPresion(menorPresion)
            print("")

        elif op == "2":
            ListaRegistros.temperaturaPromedio()

            

        elif op == "3":
            dia = ListaRegistros.getDia(input("Ingrese un dia: "))
            print("")
            ListaRegistros.mostrar(dia)

        else:
            print("Opcion no valida")
        
        print("")