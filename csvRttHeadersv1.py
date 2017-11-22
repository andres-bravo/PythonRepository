#! python 3

import sys
import time
import csv
import os

#Gb
#ficheroheaders = "D:/Trabajo/Formacion/Phyton/GitRepository/RTTs/TrafRTTE_TCC_TFP_PS_Gb_SEAER1_20170503115029_20170503115031_0_Test.ctr"
#Gn
#ficheroheaders = "D:/Trabajo/Formacion/Phyton/GitRepository/RTTs/TrafRTTE_TCC_TFP_PS_Gn_CMON1_20170503123121_20170503123131_0_Test.ctr"
#Sgsn
#ficheroheaders = "D:/Trabajo/Formacion/Phyton/GitRepository/RTTs/TrafRTTE_TCC_SGSN2G_RTT_B_GUISG1_20170503120828_20170503120838_0_Test01.ctr"
#Voice
#ficheroheaders = "D:\Trabajo\Proyectos\Development\PythonRepository\RTTs\TrafRTTE_TCC_TFP_CS_VOICE_A_SUR1M_20170614153704_20170614153709_0_Orig.ctr"


#Funcion que recibe un array de campos y un fichero de header fields (ctr)
#El parámetro adaptación sirve para coger sólo los campos del ctr y numerarlos ya que el ctr contiene muchas más líneas
#Devuelve un array de indices de campos (integers) con los indices de los campos recibidos por parámetro
def csvHeadersIndexes(ficheroheaders,matrix_field_names,adaptacion):
    try:
        with open(ficheroheaders) as csvarchivo:
            entrada = csv.reader(csvarchivo, delimiter=',', quotechar="'")
            print(ficheroheaders)
            matrix_field_indexes = []
            #Inicializo array matrix_field_indexes
            indice=0
            for field in matrix_field_names:
                matrix_field_indexes.append([field,0])
            print (matrix_field_indexes[0][0])
            for field in matrix_field_indexes:
                print(field[0])
            indicecamposctr=0
            for reg in entrada:
                if (adaptacion in reg[0]):
                    for field in matrix_field_indexes:
                        if (field[0] in reg[0]):
                            field[1]=indicecamposctr
                            #matrix_field_indexes[indice][1]=indicecamposctr
                            #indice=indice+1
                    indicecamposctr += 1
        #Devolvemos una lista de los indices de matrix_field_indexes
        matrix_only_indexes=[]
        for indice in matrix_field_indexes:
            matrix_only_indexes.append(indice[1])
        return matrix_only_indexes
                
    except Exception as inst:
        print(type(inst))    # the exception instance
        print(inst.args)     # arguments stored in .args
        print(inst)          # __str__ allows args to be printed directly,
                                 # but may be overridden in exception subclasses