import os
import csv


#Procedimiento modificar csv
def createRtt(fich, numerocampo, valor,linea):
    #modifica la linea del fichero poniendo un valor en el campo especificado
    try:
        print('Abro fichero: ',os.path.abspath(fich))
        fichdestino=fich+'nuevo'
        print('Abro fichero: ',fichdestino)
        entrada = csv.reader(open(fich,'r'),delimiter=',', quotechar="'")
        salida = csv.writer(open(fichdestino,'w'))

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
    except Exception as inst:
        print(type(inst))    # the exception instance
        print(inst.args)     # arguments stored in .args
        print(inst)          # __str__ allows args to be printed directly,
                             # but may be overridden in exception subclasses


#ficheroModif='D:/Trabajo/Formacion/Phyton/GitRepository/RTTs/TrafRTTE_TCC_TFP_CS_VOICE_A_SUR1M_20170614153704_20170614153709_0_Test.dat'
ficheroModif='D:/Trabajo/Formacion/Phyton/GitRepository/RTTs/prueba.dat'
createRtt(ficheroModif, 5,"valor",1)
