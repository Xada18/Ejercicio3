from ClaseRegistro import Registro
import csv

class ManejadorRegistros:
    __registros = None
    __dias = 31

    def __init__(self):
        self.__registros = []

    def carga(self, file):
        archivo = open(file, "r")
        reader = csv.reader(archivo, delimiter=",")

        mes = next(reader)

        if mes[0] in ["Enero","Marzo","Mayo","Julio","Agosto","Octubre","Diciembre"]:
            dias = 31
        elif mes[0] in ["Abril","Junio","Septiembre","Noviembre"]:
            dias = 30
        elif mes[0] == "Febrero":
            dias = 28
        else:
            dias = 0

        if dias == 0:
            print("Archivo no valido")
        else:
            self.__registros = [[None for _ in range(24)]for _ in range(dias)]
            self.__dias = dias
            for datos in reader:
                dia = int(datos[0]) - 1
                hora = int(datos[1])
                temperatura = datos[2]
                humedad = datos[3]
                presion = datos[4]
                                    
                self.__registros[dia][hora] = Registro(temperatura, humedad, presion)



    def MayorTemperatura(self):
        i = 0
        j = 0
        mayor = self.__registros[i][j].getTemperatura()
        
        for i in range(self.__dias):
            for j in range(24):

                temperatura = self.__registros[i][j].getTemperatura()

                if temperatura > mayor:
                    mayor = temperatura

        return mayor
    
    def mostrarMayorTemperatura(self, mayor):
        i = 0
        j = 0
        print("Listado de dias y horas con la mayor temperatura del mes:")
        for i in range(self.__dias):
            for j in range(24):
                temperatura = self.__registros[i][j].getTemperatura()
                if temperatura == mayor:
                    print(f"Dia: {i}, Hora: {j}:00")

    def MayorHumedad(self):
        i = 0
        j = 0
        mayor = self.__registros[i][j].getHumedad()
        
        for i in range(self.__dias):
            for j in range(24):

                humedad = self.__registros[i][j].getHumedad()

                if humedad > mayor:
                    mayor = humedad

        return mayor
    
    def mostrarMayorHumedad(self, mayor):
        i = 0
        j = 0
        print("Listado de dias y horas con la mayor humedad del mes:")
        for i in range(self.__dias):
            for j in range(24):
                humedad = self.__registros[i][j].getHumedad()
                if humedad == mayor:
                    print(f"Dia: {i}, Hora: {j}:00")

    def MayorPresion(self):
        i = 0
        j = 0
        mayor = self.__registros[i][j].getPresion()
        
        for i in range(self.__dias):
            for j in range(24):

                presion = self.__registros[i][j].getPresion()

                if presion > mayor:
                    mayor = presion

        return mayor
    
    def mostrarMayorPresion(self, mayor):
        i = 0
        j = 0
        print("Listado de dias y horas con la mayor humedad del mes:")
        for i in range(self.__dias):
            for j in range(24):
                presion = self.__registros[i][j].getPresion()
                if presion == mayor:
                    print(f"Dia: {i}, Hora: {j}:00")




    def MenorTemperatura(self):
        i = 0
        j = 0
        menor = self.__registros[i][j].getTemperatura()
        
        for i in range(self.__dias):
            for j in range(24):

                temperatura = self.__registros[i][j].getTemperatura()

                if temperatura < menor:
                    menor = temperatura

        return menor
    
    def mostrarMenorTemperatura(self, menor):
        i = 0
        j = 0
        print("Listado de dias y horas con la menor temperatura del mes:")
        for i in range(self.__dias):
            for j in range(24):
                temperatura = self.__registros[i][j].getTemperatura()
                if temperatura == menor:
                    print(f"Dia: {i}, Hora: {j}:00")

    def MenorHumedad(self):
        i = 0
        j = 0
        menor = self.__registros[i][j].getHumedad()
        
        for i in range(self.__dias):
            for j in range(24):

                humedad = self.__registros[i][j].getHumedad()

                if humedad < menor:
                    menor = humedad

        return menor
    
    def mostrarMenorHumedad(self, menor):
        i = 0
        j = 0
        print("Listado de dias y horas con la menor humedad del mes:")
        for i in range(self.__dias):
            for j in range(24):
                humedad = self.__registros[i][j].getHumedad()
                if humedad == menor:
                    print(f"Dia: {i}, Hora: {j}:00")

    def MenorPresion(self):
        i = 0
        j = 0
        menor = self.__registros[i][j].getPresion()
        
        for i in range(self.__dias):
            for j in range(24):

                presion = self.__registros[i][j].getPresion()

                if presion < menor:
                    menor = presion

        return menor
    
    def mostrarMenorPresion(self, menor):
        i = 0
        j = 0
        print("Listado de dias y horas con la menor presion del mes:")
        for i in range(self.__dias):
            for j in range(24):
                presion = self.__registros[i][j].getPresion()
                if presion == menor:
                    print(f"Dia: {i}, Hora: {j}:00")

    def temperaturaPromedio(self):
        i = 0
        j = 0
        k = 0
        suma = [0] * 24
        for i in range(self.__dias):
            for j in range(24):
                temperatura = self.__registros[i][j].getTemperatura()
                suma[j] += temperatura
        
        for k in range(24):
            promedio = suma[k]/self.__dias
            print(f"Hora: {k}:00, Temperatura promedio: {promedio: .2f}")
            


    def getDia(self, dia):
        lista = self.__registros[int(dia) - 1]
        return lista

    def mostrar(self, dia):
        print(f'{"Hora":^20}{"Temperatura":^20}{"Humedad":^20}{"Presion":^20}')
        for i in range(24):
            print(f"{i:^20}{dia[i].getTemperatura():^20}{dia[i].getHumedad():^20}{dia[i].getPresion():^20}")
