class PlanAhorro:
    ccuotas = 60
    ccpagas = 10
    @classmethod
    def cambiar(cls,c):
        cls.ccpagas=c
    @classmethod
    def getccpagas(cls):
        return cls.ccpagas
    def __init__(self, cod, modelo, version, valor):
         self.__cod = cod
         self.__modelo = modelo
         self.__version = version
         self.__valor = valor
    def getCod(self):
         return self.__cod
    def getModelo(self):
         return self.__modelo
    def getVersion(self):
         return self.__version
    def getValor(self):
        return self.__valor
    def actvalor(self,new):
      self.__valor=new
      print("El nuevo valor es: {}".format(self.__valor))   
    def valorcuota(self):
         vc = (float(self.__valor)/PlanAhorro.ccuotas)+float(self.__valor)*0.10
         print("Valor de cuota: {}".format(vc))
         return vc
    def montototal(self):
        mt= PlanAhorro.ccpagas*self.valorcuota()
        return mt
        
        
     