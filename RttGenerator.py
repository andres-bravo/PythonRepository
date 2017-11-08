#! python 3

import sys
import time
import csv
import os
import shutil



#Procedimiento rtt_generator
#Crea un nuevo fichero (destination_file) a partir de fichero (master_file) modificando los campos con indices en matriz matrix_field_index y
#les pone los valores de matrix_field_values
def rtt_generator(master_file, destination_file,matrix_field_index, matrix_field_values):
    try:
        print('Abro fichero: ',os.path.abspath(master_file))
        fichdestino=destination_file
        print('Abro fichero: ',fichdestino)
        entry_file = csv.reader(open(master_file,'r'),delimiter=',', quotechar="'")
        #al abrir el fichero le ponemos parámetro newline='' para que no meta líneas en blaco al insertar líneas
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
        #Generamos fichero de Control
        (nombreFicheroDestinoCtr, extension) = os.path.splitext(fichdestino)
        nombreFicheroDestinoCtr = nombreFicheroDestinoCtr +'.ctr'
        print('Abro fichero de control Destino', nombreFicheroDestinoCtr)
        output_ctr_file = open(nombreFicheroDestinoCtr,'w',newline='')
        #Guardo nombre fichero destino sin directorio par insertarlo en el la linea [INFILE] del Ctr para que pueda ser importado el dat y el ctr
        (dirFicheroDestinoDat,filenameFicheroDestinoDat) = os.path.split(destination_file)
        
        (nombreFicheroOrigenCtr, extension) = os.path.splitext(master_file)
        nombreFicheroOrigenCtr = nombreFicheroOrigenCtr+'.ctr'
        print('Abro fichero de control origen:', nombreFicheroOrigenCtr)
        input_ctr_file = open(nombreFicheroOrigenCtr,'r')
        for reg in input_ctr_file:
            print(reg)
            if (('INFILE' in reg)):
                reg = 'INFILE \'' + filenameFicheroDestinoDat +'\''+'\n'
            print (reg)
            output_ctr_file.write(reg)
        

    except Exception as inst:
        print(type(inst))    # the exception instance
        print(inst.args)     # arguments stored in .args
        print(inst)          # __str__ allows args to be printed directly,
                             # but may be overridden in exception subclasses
