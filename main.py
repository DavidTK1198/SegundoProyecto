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
if __name__ == '__main__':
    simbolito = Simbolos.TablaSimbolos()
    palabrita = Palabras_Reservadas.Palabras_Reservadas("A","marihuana","D","DA","P")
    simbolito.insertar_to_dictionary(palabrita)
    valor = simbolito.HashmapFunciones.get(10)
    print(valor.nombre)

    print("yamete kudasai")
    print("ak7 mae ando con toda la gallada, fumando rolando si esa marihuana")
    print("Maruchan")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
