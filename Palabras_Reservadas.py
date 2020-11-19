'''
UNIVERSIDAD NACIONAL DE COSTA RICA
ESTRUCTURAS DE DATOS - EIF-207
PROYECTO # 2
ESTUDIANTES: DAVID BARRIENTOS, DANIEL MADRIGAL, JOEL ZAMORA
PROFESOR: JOSE CALVO SUÁREZ
'''
class Palabras_Reservadas:
    def __init__(self):
        self.tipo = ""
        self.nombre = ""
        self.identificacion = ""
        self.lugarP = ""
        self.valor = ""

    def setTipo(self, tipo):
        self.tipo = tipo

    def setNombre(self, nom):
        self.nombre = nom

    def setIden(self, ident):
        self.identificacion = ident

    def setLugarP(self, lugP):
        self.lugarP = lugP

    def setValor(self, valor):
        self.valor = valor

    def toString(self):
        print("Nombre" + self.nombre + '\n')
        print("Tipo" + self.tipo + '\n')
        print("Identificador" + self.identificacion + '\n')
        print("Lugar Procedencia" + self.lugarP + '\n')
        print("Valor" + self.valor + '\n')
        
    def getLugarP(self):
        return self.lugarP

    def getNombre(self):
        return self.nombre
    def getTipo(self):
        return self.tipo
    def getValor(self):
        return self.valor
    def getIdentificador(self):
        return self.identificacion




