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
        self.mistakes = []
        self.HashmapFunciones = {}  # diccionarios
        self.HashmapVariables = {}  # diccionarios
        self.codigo = ""
        self.errorstring = ""

    def hashing_function(self, identificador):
        aux = 0
        for i in identificador:
            aux += ord(i)
        return aux % 20

    def insertar_to_dictionary(self, p):
        key = self.hashing_function(p.nombre)
        self.HashmapFunciones[key] = p

    def insertar_to_dictionary_var(self, p):
        key = self.hashing_function(p.nombre)
        self.HashmapVariables[key] = p

    def leer_archivo(self, arch):
        self.__leerarchivo(arch)

    def imprimirFuncion(self):
        print(self.codigo)

    def __leerarchivo(self, arch):
        print(" \u001b[32mArchivo Recuperado\u001b[37m")
        archivo = open(arch, "r", encoding="utf-8")
        valor = archivo.readlines()
        archivo.seek(0)
        self.codigo = archivo.read()
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
        for i in range(len(dato)):
            if dato[i] != " " and dato[i] != "," and dato[i] != ")":
                leer += dato[i]
            elif dato[i] == ' ' and dato[i - 1] == ",":
                a = 0
            elif dato[i] == "," or dato[i] == ")":
                palabra = Palabras_Reservadas.Palabras_Reservadas()
                palabra.setIden("parametro")
                palabra.setNombre(leer)
                palabra.setTipo(declaraciones[0])
                self.variables.put(palabra)
                declaraciones.pop()
                leer = ""
                self.insertar_to_dictionary_var(palabra)
            else:
                declaraciones.append(leer)
                leer = ""

    def __leer_String(self, linea):
        stack = queue.LifoQueue()
        declaracion = ""
        declaraciones = []
        n = len(linea)
        i = 0
        while i < n:
            if linea[i] != " " and linea[i] != "(" and linea[i] != "=" and linea[i] != ";" and linea[i] != "}":
                declaracion += linea[i]
            elif linea[i] == "}":
                self.funcion.get()
            elif linea[i] == '(' and declaracion != "if" and declaracion != "while" and declaracion != "for":
                declaracion = ""
                stack.put("(")
                i += 1
                while not stack.empty():
                    if linea[i] == ")":
                        stack.get()
                    declaracion += linea[i]
                    i += 1
                i -= 1
                if declaracion != ")":
                    self.__parametro(declaracion)
                declaracion = ""
            elif linea[i] == "=" and len(declaraciones) == 2:
                reservada = Palabras_Reservadas.Palabras_Reservadas()
                if self.funcion.empty():
                    reservada.setIden("variable")
                    reservada.setNombre(declaraciones[1])
                    reservada.setTipo(declaraciones[0])
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
                if self.VariableExists(reservada.getNombre()):
                    auxiliar = "Se encontro error en la linea " + str(
                        self.lineaA) + reservada.getNombre() + "ha sido declarada previamente"
                    self.mistakes.append(auxiliar)
                else:
                    self.variables.put(reservada)
                    self.insertar_to_dictionary_var(reservada)
            elif linea[i] == "=" and len(declaracion) != 2:
                guardastring = declaraciones.pop(0)
                declaracion = ""
                stack.put("(")
                i += 1
                while not stack.empty():
                    declaracion += linea[i]
                    i += 1
                    if linea[i] == ";":
                        stack.get()
                if not self.VariableExists(guardastring):
                    error = "Se encontró error en la línea " + str(
                        self.lineaA) + ": " + guardastring + " no se encuentra declarado"
                    self.mistakes.append(error)
                else:
                    self.HashmapVariables.get(self.hashing_function(guardastring)).setValor(declaracion)

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
                declaracion = ""
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
                declaracion = ""
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
                reservada.setValor(declaracion)
                self.funcion.put(reservada)
                self.FunImprimir.put(reservada)
                declaracion = ""
                self.insertar_to_dictionary(reservada)
            elif declaracion == "return":
                if not self.funcion.empty():
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
                            self.errorstring = "Se encontró error en la línea " + str(
                                self.lineaA) + " void no tiene valor de retorno"
                            self.mistakes.append(self.errorstring)
                        elif reservadaP.getTipo() != reservada.getTipo() and reservada.getTipo() != self.funcion.queue[
                            -1].getTipo():
                            self.errorstring = "Se encontró error en la línea " + str(
                                self.lineaA) + " valor de retorno no coincide con la declaración de " + reservadaP.getNombre()
                            self.mistakes.append(self.errorstring)
                        elif reservada.getTipo() != self.funcion.queue[-1].getTipo():
                            self.errorstring = "Se encontró error en la línea " + str(
                                self.lineaA) + " valor de retorno no coincide con la declaración de " + \
                                               self.funcion.queue[-1].getNombre()
                            self.mistakes.append(self.errorstring)
                else:
                    self.errorstring = "Se encontró error en la línea " + str(
                        self.lineaA) + ": 'return' fuera de la función correspondiente"
                    self.mistakes.append(self.errorstring)
            elif declaracion == "int":
                bandera = True
                declaracion = ""
                stack.put("(")
                j = i
                j += 1
                while not stack.empty():
                    if linea[j] != '=' and linea[j] != ' ' and linea[j] != '(':
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
                    palabra.setNombre(declaracion)
                    palabra.setLugarP("main")
                    palabra.setTipo("int")
                    self.funcion.put(palabra)
                    self.FunImprimir.put(palabra)
                    declaracion = ""
                    self.insertar_to_dictionary(palabra)
                else:
                    declaraciones.append("int")
                    declaracion = ""
            elif declaracion == "float":
                bandera = True
                declaracion = ""
                stack.put("(")
                j = i
                j += 1
                while not stack.empty():
                    if linea[j] != '=' and linea[j] != ' ' and linea[j] != '(':
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
                    palabra.setNombre(declaracion)
                    palabra.lugarP("main")
                    palabra.setTipo("float")
                    self.funcion.put(palabra)
                    self.FunImprimir.put(palabra)
                    declaracion = ""
                    self.insertar_to_dictionary(palabra)
            elif declaracion == "string":
                bandera = True
                declaracion = ""
                stack.put("(")
                j = i
                j += 1
                while not stack.empty():
                    if linea[j] != '=' and linea[j] != ' ' and linea[j] != '(':
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
                    palabra.setNombre(declaracion)
                    palabra.setLugarP("main")
                    palabra.setTipo("string")
                    self.funcion.put(palabra)
                    self.FunImprimir.put(palabra)
                    declaracion = ""
                    self.insertar_to_dictionary(palabra)
                else:
                    declaraciones.append("string")
                    declaracion = ""
            else:
                declaraciones.append(declaracion)
                declaracion = ""
            i += 1

    def __VariableExists(self, nombre):
        a = self.hashing_function(nombre)
        if a in self.HashmapVariables.keys():
            return True
        else:
            return False

    def VariableExists(self, nombre):
        return self.__VariableExists(nombre)

    def __Imprime_Errores(self):
        if len(self.mistakes) == 0:
            print("\u001b[34mCodigo compilado correctamente\u001b[37m")
        else:
            for i in self.mistakes:
                print("\u001b[31m")
                print(i)
            print("\u001b[37m")

    def ImprimeErrores(self):
        return self.__Imprime_Errores()
