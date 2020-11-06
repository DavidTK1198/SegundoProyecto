
import queue
import array
import hashlib
import Palabras_Reservadas

class TablaSimbolos:
    def __init__(self):
         self.funcion = queue.LifoQueue()
         self.FunImprimir = queue.LifoQueue()
         self.variables = queue.LifoQueue()
         self.codigoFuente = []
         self.PalabrasReservadas = []
         self.init_Palabras_Reservada()
         self.operators = []
         self.init_Operators()
         self.mistakes = []
         self.HashmapFunciones = {} #diccionarios
         self.HashmapVariables = {} #diccionarios

    def init_Operators(self):
        self.operators.append(' ')
        self.operators.append('(')
        self.operators.append(')')
        self.operators.append('{')
        self.operators.append('}')
        self.operators.append('[')
        self.operators.append(']')
        self.operators.append(';')
        self.operators.append('=')
        self.operators.append('+')
        self.operators.append('-')
        self.operators.append('/')
        self.operators.append('*')
        self.operators.append(':')
        self.operators.append(',')
        self.operators.append('.')
        self.operators.append('!')
        self.operators.append('<')
        self.operators.append('>')
        self.operators.append('\'')
        self.operators.append('"')

    def init_Palabras_Reservada(self):
        self.PalabrasReservadas.append("void");
        self.PalabrasReservadas.append("if");
        self.PalabrasReservadas.append("while");
        self.PalabrasReservadas.append("for");
        self.PalabrasReservadas.append("int");
        self.PalabrasReservadas.append("float");
        self.PalabrasReservadas.append("char");
        self.PalabrasReservadas.append("string");
        self.PalabrasReservadas.append("bool");

    def hashing_function(self, identificador):
        aux = 0
        for i in identificador:
            aux+= ord(i)
        return aux % 20

    def insertar_to_dictionary(self, p):
        key = self.hashing_function(p.nombre)
        self.HashmapFunciones[key] = p
        print(self.HashmapFunciones)



