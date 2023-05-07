import csv
from ClasePlanAhorro import PlanAhorro
class Manejador:
    __lista = []
    def __init__(self):
        __lista=[]
    def abrirarchivo(self):
        archivo = open("planes.csv")
        reader= csv.reader(archivo, delimiter=";")
        for fila in reader:
            cod = fila[0]
            modelo = fila [1]
            version = fila[2]
            valor = fila[3]
            inst = PlanAhorro(cod,modelo,version,valor)
            self.__lista.append(inst)
        archivo.close
    def actvalor(self):
        for i in range(len(self.__lista)):
            print("Codigo Plan: {}\tModelo:{}\tVersion del Vehiculo:{}".format(self.__lista[i].getCod(),self.__lista[i].getModelo(),self.__lista[i].getVersion()))
            value = float(input("Ingrese nuevo valor del vehiculo. "))
            self.__lista[i].actvalor(value)
    def darValor(self):
        i=0
        val=float(input("Ingrese el valor de cuota deseado. "))
        while (i<len(self.__lista)):
            if (self.__lista[i].valorcuota()<val):
                print("---Planes con valor de cuota inferior al ingresado---\nCodigo Plan: {}\tModelo:{}\tVersion del Vehiculo:{}".format(self.__lista[i].getCod(),self.__lista[i].getModelo(),self.__lista[i].getVersion()))
            i+=1
    def mostrarmonto(self):
        p=str(input("Ingrese el modelo de auto del que desea obtener el monto a pagar para licitar el vehiculo. "))
        i=0
        while (i<len(self.__lista) and p!=self.__lista[i].getModelo()):
            i+=1
        if i<len(self.__lista):
            print("El monto que hay que pagar pagar para licitar al vehiculo es de: {}" .format(self.__lista[i].montototal()))
        else:
            print("El modelo de auto ingresado es invalido.")
    def cambiarcuotas(self):
        c=int(input("Ingrese la nueva cantidad de cuotas que debe tener pagas para licitar. "))
        PlanAhorro.cambiar(c)
        print("Cantidad nueva de cuotas para licitar: {}".format(PlanAhorro.getccpagas()))

