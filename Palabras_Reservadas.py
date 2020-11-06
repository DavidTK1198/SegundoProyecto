'''
UNIVERSIDAD NACIONAL DE COSTA RICA
ESTRUCTURAS DE DATOS - EIF-207
PROYECTO # 2
ESTUDIANTES: DAVID BARRIENTOS, DANIEL MADRIGAL, JOEL ZAMORA
PROFESOR: JOSE CALVO SUÁREZ
'''
class Palabras_Reservadas:
    def __init__(self, tipo, nombre , identificacion, lugarP, valor):
        self.tipo = tipo
        self.nombre = nombre
        self.identificacion = identificacion
        self.lugarP = lugarP
        self.valor = valor

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




