#! python 3

import sys
import time
import csv
import os
#from os import listdir, walk, path
#from os.path import isfile, join, splitext




print('csvManager')
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

