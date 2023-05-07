from ClasePlanAhorro import PlanAhorro
from controlador import Manejador
from MenuOpciones import Menu
if __name__ == "__main__":
    c= Manejador()
    c.abrirarchivo()
    m = Menu()
    m.opciones(c)