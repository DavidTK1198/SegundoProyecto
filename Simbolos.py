import queue
import array
import hashlib
import Palabras_Reservadas
from io import open


class TablaSimbolos:
    def __init__(self):
        self.lineaA = 1
        self.funcion = queue.LifoQueue()
        self.FunImprimir = queue.LifoQueue()
        self.variables = queue.LifoQueue()
        self.codigoFuente = []
        self.PalabrasReservadas = []
        self.init_Palabras_Reservada()
        self.operators = []
        self.init_Operators()
        self.mistakes = []
        self.HashmapFunciones = {}  # diccionarios
        self.HashmapVariables = {}  # diccionarios

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
        self.PalabrasReservadas.append("void")
        self.PalabrasReservadas.append("if")
        self.PalabrasReservadas.append("while")
        self.PalabrasReservadas.append("for")
        self.PalabrasReservadas.append("int")
        self.PalabrasReservadas.append("float")
        self.PalabrasReservadas.append("char")
        self.PalabrasReservadas.append("string")
        self.PalabrasReservadas.append("bool")

    def hashing_function(self, identificador):
        aux = 0
        for i in identificador:
            aux += ord(i)
        return aux % 20

    def insertar_to_dictionary(self, p):
        key = self.hashing_function(p.nombre)
        self.HashmapFunciones[key] = p
        print(self.HashmapFunciones)

    def insertar_to_dictionary_var(self, p):
        key = self.hashing_function(p.nombre)
        self.HashmapVariables[key] = p
        print(self.HashmapVariables)

    def leer_archivo(self):
        self.__leerarchivo()

    def __leerarchivo(self):
        archivo = open("funcion1.txt", "r", encoding="utf-8")
        valor = archivo.readlines()
        archivo.close()
        for i in valor:
            n = i
            nuevo = n.strip()
            self.codigoFuente.append(nuevo)
            self.__leer_String(nuevo)
            self.lineaA += 1

    def __parametro(self, dato):
        declaraciones = []
        leer = ""
        for i in range(dato.len()):
            if dato[i] != " " and dato[i] != "," and dato[i] != ")":
                leer += dato[i]
            elif dato[i] == "," or dato[i] == ")":
                palabra = Palabras_Reservadas.Palabras_Reservadas()
                palabra.setIden("parametro")
                palabra.setNombre(leer)
                palabra.setTipo(declaraciones[0])
                # palabra.setPadre(funciones.top().getNombre())
                self.variables.put(palabra)
                declaraciones.pop()
                lectura = ""
                self.insertar_to_dictionary_var()
            else:
                declaraciones.append(leer)
                leer = ""

    def __leer_String(self, linea):
        stack = queue.LifoQueue()
        declaracion = ""
        declaraciones = []
        for i in range(len(linea)):
            print(linea[i])
            if linea[i] != " " and linea[i] != "(" and linea[i] != "=" and linea[i] != ";" and linea[i] != "}":
                declaracion += linea[i]
            elif linea[i] == "}":
                self.funcion.get()
            elif linea[i] == '(' and declaracion != "if" and declaracion != "while" and declaracion != "for":
                declaracion = ""
                stack.put("(")
                i = i + 1
                while not stack.empty():
                    if linea[i] == ")":
                        stack.get()
                    declaracion += linea[i]
                    i += 1
                i -= 1
                if declaracion != ")":
                    #self.__paramtros(declaracion)
                    declaracion = ""
            elif linea[i] == "=" and declaraciones.__len__() == 2:
                reservada = Palabras_Reservadas.Palabras_Reservadas()
                if self.funcion.empty():
                    reservada.setIden("variable")
                    reservada.setNombre(declaracion[1])
                    reservada.setTipo(declaracion[0])
                    reservada.setLugarP("main")
                    declaracion = ""
                    stack.put("(")
                    i += 2
                    while not stack.empty():
                        declaracion += linea[i]
                        i += 1
                        if linea[i] == ";":
                            stack.get()

                    i -= 1
                    reservada.setValor(declaracion)
                else:
                    reservada.setIden("variable")
                    reservada.setNombre(declaracion[1])
                    reservada.setTipo(declaracion[0])
                    reservada.setLugarP(self.funcion.get().getLugarP())
                    declaracion = ""
                    stack.put("(")
                    i += 1
                    while not stack.empty():
                        if linea[i] == ";":
                            stack.get()
                        declaracion += linea[i]
                        i += 1
                    i -= 1
                    reservada.setValor(declaracion)
                if self.VariableExists(reservada.getNombre()):
                    auxiliar = "Se encontro error en la linea " + self.lineaA + reservada.getNombre() + "ha sido declarada previamente"
                    self.mistakes.append(auxiliar)
                else:
                    self.variables.put(reservada)
                    self.insertar_to_dictionary_var(reservada)
            elif declaracion == "void":
                reservada = Palabras_Reservadas.Palabras_Reservadas()
                reservada.setIden("funcion")
                declaracion = ""
                stack.put("(")
                i += 1
                while not stack.empty():
                    if linea[i] == "(":
                        stack.get()
                    else:
                        declaracion += linea[i]
                        i += 1
                i -= 1
                reservada.setNombre(declaracion)
                reservada.setLugarP("main")
                reservada.setTipo("void")
                self.funcion.put(reservada)
                self.FunImprimir.put(reservada)
                reservada = ""
                self.insertar_to_dictionary(reservada)
            elif declaracion == "while":
                reservada = Palabras_Reservadas.Palabras_Reservadas()
                reservada.setIden("condicion")
                declaracion = ""
                i += 1
                stack.put("(")
                while not stack.empty():
                    if linea[i] == ")":
                        stack.get()
                    else:
                        declaracion += linea[i]
                        i += 1
                i -= 1
                reservada.setNombre("while")
                reservada.setLugarP(self.funcion.get().getNombre())
                reservada.setTipo("while")
                self.funcion.put(reservada)
                self.FunImprimir.put(reservada)
                reservada = ""
                self.insertar_to_dictionary(reservada)
            elif declaracion == "if":
                reservada = Palabras_Reservadas.Palabras_Reservadas()
                reservada.setIden("condicion")
                declaracion = ""
                i += 1
                stack.put("(")
                while not stack.empty():
                    if linea[i] == ")":
                        stack.get()
                    else:
                        declaracion += linea[i]
                        i += 1
                i -= 1
                reservada.setNombre("if")
                reservada.setLugarP(self.funcion.get().getNombre())
                reservada.setTipo("if")
                self.funcion.put(reservada)
                self.FunImprimir.put(reservada)
                reservada = ""
                self.insertar_to_dictionary(reservada)
            elif declaracion == "return":
                if self.funcion.not_empty():
                    declaracion = ""
                    i += 1
                    stack.put("(")
                    while not stack.empty():
                        declaracion += linea[i]
                        i += 1
                        if linea[i] == ";":
                            stack.get()
                    if self.VariableExists(declaracion):
                        reservada = self.HashmapVariables.get(self.hashing_function(declaracion))
                        reservadaP = self.HashmapFunciones.get(self.hashing_function(reservada.getLugarP()))
                        if reservadaP.getTipo() == "void":
                            errorString = "Se encontró error en la línea " + self.lineaA + " void no tiene valor de retorno"
                            self.mistakes.append(errorString)
                        elif reservadaP.getTipo() != reservada.getTipo() and reservada.getTipo() != self.funcion.queue[-1].getTipo():
                            errorString = "Se encontró error en la línea " + self.lineaA + " valor de retorno no coincide con la declaración de " + reservadaP.getNombre()
                            self.mistakes.append(errorString)
                        elif reservada.getTipo() != self.funcion.queue[-1].getTipo():
                            errorString = "Se encontró error en la línea " + self.lineaA + " valor de retorno no coincide con la declaración de " + self.funcion.queue[-1].getNombre()
                            self.mistakes.append(errorString)
                else:
                    errorString = "Se encontró error en la línea " + self.lineaA + " 'return' fuera de la función "
                    self.mistakes.append(errorString)
            elif declaracion == "int":
                bandera = True
                declaracion = ""
                stack.put("(")
                j = i
                j += 1
                while not stack.empty():
                    if linea[j] != '=' and linea[j] != ' ' and  linea[j] != '(':
                        declaracion += linea[j]
                    if linea[j] == '=':
                        stack.get()
                        bandera = False
                    if linea[j] == '(':
                        stack.get()
                        bandera = True
                    j += 1
                if bandera:
                    palabra = Palabras_Reservadas.Palabras_Reservadas()
                    palabra.setIden("funcion")
                    palabra.setNombre(statement)
                    palabra.lugarP("main")
                    palabra.setTipo("int")
                    self.funcion.put(palabra)
                    self.FunImprimir.put(palabra)
                    statement = ""
                    self.insertar_to_dictionary(palabra)
                else:
                    declaraciones.append("int")
                    declaracion = ""


    def __VariableExists(self, nombre):
        if self.hashing_function(nombre) in self.HashmapFunciones.keys():
            return False
        return True

    def VariableExists(self, nombre):
        return self.__VariableExists(nombre)
