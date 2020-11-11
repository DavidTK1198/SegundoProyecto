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
    palabrita = Palabras_Reservadas.Palabras_Reservadas()
    simbolito.insertar_to_dictionary(palabrita)
    print(simbolito.VariableExists("David"))


    #simbolito.insertar_to_dictionary(palabrita)
    #valor = simbolito.HashmapFunciones.get(10)
    #simbolito.leer_archivo()


    pilarda = queue.LifoQueue()
    pilarda.put(2)
    pilarda.put(4)
    print(pilarda.queue[-1])
    print(pilarda.queue[-1])
    print(pilarda.queue[-1])
    print(pilarda.queue[-1])
    print(pilarda.queue[-1]) #AK77 PAH


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
