#! python 3

import sys
import time
import csv
import os
import shutil

#Array de indices de campos a modificar
#Gb, 1 ReportReason, 4 SmCause, 6 Imsi, 7 Msisdn
#matrix_field_index = [1,4,6,7]
#matrix_field_values = [3,2,'214070000000103','34600000103']
#Gn, 2 Gtp_Cause, 3 Imsi, 5 MsIsdn
matrix_field_index = [2,3,5]
matrix_field_values = [5,'214070000000104','34600000104']

#Procedimiento modificar csv
def rtt_generator(master_file, matrix_field_index, matrix_field_values):
    #Crea un nuevo fichero modificando los campos con indices en matriz matrix_field_index y
    #les pone los valores de matrix_field_values.
    try:
        print('Abro fichero: ',os.path.abspath(master_file))
        fichdestino=master_file+'nuevo'
        print('Abro fichero: ',fichdestino)
        entry_file = csv.reader(open(master_file,'r'),delimiter=',', quotechar="'")
        output_file = csv.writer(open(fichdestino,'w',newline=''))

        for reg in entry_file:
            print(reg)
            #print(reg[matrix_field_index[0]], matrix_field_values[0])
            j = 0
            for i in matrix_field_index:
                reg[i] = matrix_field_values[j]
                j+=1
            print(reg)
            output_file.writerow(reg)

        """    
        #entrada = csv.reader(filedescriptor, delimiter=',', quotechar="'")
        templinea = 1
        for reg in entrada:
            #print("linea", indice)
            print(reg)
            if (templinea==linea):
                print("Escribo esta linea")
                indicecampo=0
                for campoinreg in reg:
                    print(indicecampo,campoinreg)
                    if (indicecampo==numerocampo):
                        print('Modifico este campo:', indicecampo)
                        reg[indicecampo]=valor
                        print("Valor linea modificada\n",reg)
                    indicecampo+=1
            templinea+=1
            salida.writerow(reg)
            #if (('MSISDN' in reg[0]) or ('IMEI' in reg[0] or 'IMSI' in reg[0]) or ('Direction' in reg[0]) or ('Calling' in reg[0])):
            #    print("campo", indice)
        print("Final funcion")
        """
    except Exception as inst:
        print(type(inst))    # the exception instance
        print(inst.args)     # arguments stored in .args
        print(inst)          # __str__ allows args to be printed directly,
                             # but may be overridden in exception subclasses

#Fichero a modificar
#Gb
#CsvFileModif = "D:/Trabajo/Formacion/Phyton/GitRepository/RTTs/TrafRTTE_TCC_TFP_PS_Gb_SEAER1_20170503115029_20170503115031_0_Test.dat"
#Gn
CsvFileModif = "D:/Trabajo/Formacion/Phyton/GitRepository/RTTs/TrafRTTE_TCC_TFP_PS_Gn_CMON1_20170503123121_20170503123131_0_Test.dat"
rtt_generator(CsvFileModif,matrix_field_index,matrix_field_values)
print("Renombrando Fichero:" + shutil.move(CsvFileModif+'nuevo', CsvFileModif))
