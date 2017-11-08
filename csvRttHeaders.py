#! python 3

import sys
import time
import csv
import os
#from os import listdir, walk, path
#from os.path import isfile, join, splitext




print('csvRttHeaders.py')
#Gb
#ficheroheaders = "D:/Trabajo/Formacion/Phyton/GitRepository/RTTs/TrafRTTE_TCC_TFP_PS_Gb_SEAER1_20170503115029_20170503115031_0_Test.ctr"
#Gn
ficheroheaders = "D:/Trabajo/Formacion/Phyton/GitRepository/RTTs/TrafRTTE_TCC_TFP_PS_Gn_CMON1_20170503123121_20170503123131_0_Test.ctr"
#Sgsn
ficheroheaders = "D:/Trabajo/Formacion/Phyton/GitRepository/RTTs/TrafRTTE_TCC_SGSN2G_RTT_B_GUISG1_20170503120828_20170503120838_0_Test01.ctr"

with open(ficheroheaders) as csvarchivo:
    entrada = csv.reader(csvarchivo, delimiter=',', quotechar="'")
    indice = 0
    for reg in entrada:
        #print("linea", indice)
        #print(reg)
        #if (('MSISDN' in reg[0]) or ('Imei' in reg[0] or 'Imsi' in reg[0]) or 
        #    ('Direction' in reg[0]) or ('Calling' in reg[0])):
        #Solo numero lineas que tengan Sgsn cambiar para cada adaptación
        #Gb
        #CadenaBusqueda = "TFP_Gb"
        #Gn
        #CadenaBusqueda = "TFP_Gn"
        #Sgsn
        CadenaBusqueda = "Sgsn_"
        if ((CadenaBusqueda in reg[0])):
            print("campo", indice)
            print(reg[0])
            indice += 1

"""
directorio = "D:/Trabajo/Formacion/Phyton/GitRepository/RTTs"
for fich in os.listdir(directorio):
    if os.path.isfile(os.path.join(directorio,fich)):
        (nombreFichero, extension) = os.path.splitext(fich)
        if (extension == ".head"):
            print(os.path.join(directorio,fich))
            #Manejo de csv
            with open(os.path.join(directorio,fich)) as csvarchivo:
                entrada = csv.reader(csvarchivo, delimiter=',', quotechar="'")
                indice = 1
                for reg in entrada:
                    #print("linea", indice)
                    #print(reg)
                    if (('MSISDN' in reg[0]) or ('IMEI' in reg[0] or 'IMSI' in reg[0]) or ('Direction' in reg[0]) or ('Calling' in reg[0])):
                        print("campo", indice)
                        print(reg[0])
                    indice += 1
"""