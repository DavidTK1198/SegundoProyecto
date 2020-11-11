'''
UNIVERSIDAD NACIONAL DE COSTA RICA
ESTRUCTURAS DE DATOS - EIF-207
PROYECTO # 2
ESTUDIANTES: DAVID BARRIENTOS, DANIEL MADRIGAL, JOEL ZAMORA
PROFESOR: JOSE CALVO SUÁREZ
'''

import Simbolos
import Palabras_Reservadas

# Press the green button in the gutter to run the script.
def incrementar(x):
    x = x+1
if __name__ == '__main__':
    simbolito = Simbolos.TablaSimbolos()
    palabrita = Palabras_Reservadas.Palabras_Reservadas("A","David","D","DA","P")
    simbolito.insertar_to_dictionary(palabrita)
    print(simbolito.VariableExists("David"))


    #simbolito.insertar_to_dictionary(palabrita)
    #valor = simbolito.HashmapFunciones.get(10)
    #simbolito.leer_archivo()
    x = 1
    incrementar(x)
    print(x)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
