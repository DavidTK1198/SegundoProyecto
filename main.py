'''
UNIVERSIDAD NACIONAL DE COSTA RICA
ESTRUCTURAS DE DATOS - EIF-207
PROYECTO # 2
ESTUDIANTES: DAVID BARRIENTOS, DANIEL MADRIGAL, JOEL ZAMORA
PROFESOR: JOSE CALVO SUÁREZ
'''

import Simbolos
import Palabras_Reservadas
import queue

# Press the green button in the gutter to run the script.
def incrementar(x):
    x = x+1
if __name__ == '__main__':
    simbolito = Simbolos.TablaSimbolos()
    simbolito.leer_archivo("funcion1.txt")
    simbolito.imprimirFuncion()
    simbolito.ImprimeErrores()
    print("-------------------")
    simbolito2 = Simbolos.TablaSimbolos()
    simbolito2.leer_archivo("funcion2.txt")
    simbolito2.imprimirFuncion()
    simbolito2.ImprimeErrores()



    #simbolito.insertar_to_dictionary(palabrita)
    #valor = simbolito.HashmapFunciones.get(10)
    #simbolito.leer_archivo()





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
