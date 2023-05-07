from ClasePlanAhorro import PlanAhorro
from controlador import Manejador
class Menu:
    __opcion = 0
    def __init__(self) :
        self.__opcion = 0
    def opciones(self,lista):
        print("1: Actualizar el valor del vehiculo de cada plan.")
        print("2: Dado un valor, mostrar código del plan, modelo y versión del vehículo cuyo valor de la cuota sea inferior al valor dado.")
        print("3: Mostrar monto a pagar para licitar el vehículo")
        print("4: Modificar la cantidad de cuotas pagas para poder licitar")
        print("5: Salir.")
        while True:
            self.__opcion = int(input("Seleccione una opcion: "))
            if self.__opcion == 1:
                lista.actvalor()
            elif self.__opcion == 2:
                lista.darValor()
            elif self.__opcion == 3:
                lista.mostrarmonto()
            elif self.__opcion == 4:
                lista.cambiarcuotas()
            elif self.__opcion == 5:
                break
            else:
                print("La opcion ingresada es invalida, ingrese otra opcion.")
