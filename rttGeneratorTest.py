#! python 3

import sys
import time
import csv
import os
import shutil
#De un modulo puedo importar lo que yo quiera
from RttGenerator import *
from csvRttHeadersv1 import *

#Array de indices de campos a modificar
#Gb, 1 ReportReason, 4 SmCause, 6 Imsi, 7 Msisdn
#matrix_field_index = [1,4,6,7]
#matrix_field_values = [3,2,'214070000000103','34600000103']
#Gn, 2 Gtp_Cause, 3 Imsi, 5 MsIsdn
#matrix_field_index = [2,3,5]
#matrix_field_values = [5,'214070000000104','34600000104']
#Voice, 6 A_IMSI, 7 B_IMSI, 9 B_MSISDN, 10 A_Direction_Number, 11 B_Direction_Number, 13 A_MSISDN, 82 A_RANAP_Cause, 83 B_RANAP_Cause, 40 A_BSSMAP_Cause, 
#       41 B_BSSMAP_Cause, 18 A_ISUP_Cause_Code, 19 B_ISUP_Cause_Code, 15 A_CC_Cause, 16 B_CC_Cause 
#Voice 2G Errors
#matrix_field_index = [6,7,9,10,11,13,40,41]
#matrix_field_values =['214070000000201','214070000000202','34600000202','34600000201','34600000202','34600000201',20,20]
#Voice 3G Errors
#matrix_field_index = [6,7,9,10,11,13,82,83]
#matrix_field_values =['214070000000203','214070000000204','34600000204','34600000203','34600000204','34600000203',20,20]
#Voice Call Control Errors
#matrix_field_index = [6,7,9,10,11,13,15,16]
#matrix_field_values =['214070000000203','214070000000204','34600000204','34600000203','34600000204','34600000203',20,20]
#Voice Signalling Errors
matrix_field_index = [6,7,9,10,11,13,18,19]
matrix_field_values =['214070000000205','214070000000206','34600000206','34600000205','34600000206','34600000205',20,20]
#Fichero a modificar
#Gb
#CsvFileModif = "D:/Trabajo/Formacion/Phyton/GitRepository/RTTs/TrafRTTE_TCC_TFP_PS_Gb_SEAER1_20170503115029_20170503115031_0_Test.dat"
#Gn
#CsvFileModif = "D:/Trabajo/Formacion/Phyton/GitRepository/RTTs/TrafRTTE_TCC_TFP_PS_Gn_CMON1_20170503123121_20170503123131_0_Test.dat"
#Voice 2G Error
#CsvFileModif = "D:\Trabajo\Proyectos\Development\PythonRepository\RTTs\TrafRTTE_TCC_TFP_CS_VOICE_A_SUR1M_20170614153704_20170614153709_0_Test.dat"
#CsvFileDestination = "D:\Trabajo\Proyectos\Development\PythonRepository\RTTs\TrafRTTE_TCC_TFP_CS_VOICE_A_SUR1M_20170614153704_20170614153709_0_Voice3GError.dat"
#Voice Call Control Error
#CsvFileModif = "D:\Trabajo\Proyectos\Development\PythonRepository\RTTs\TrafRTTE_TCC_TFP_CS_VOICE_A_SUR1M_20170614153704_20170614153709_0_Test.dat"
#CsvFileDestination = "D:\Trabajo\Proyectos\Development\PythonRepository\RTTs\TrafRTTE_TCC_TFP_CS_VOICE_A_SUR1M_20170614153704_20170614153709_0_VoiceCallControlError.dat"
#Voice Signalling Error
#CsvFileModif = "D:\Trabajo\Proyectos\Development\PythonRepository\RTTs\TrafRTTE_TCC_TFP_CS_VOICE_A_SUR1M_20170614153704_20170614153709_0_Test.dat"
#CsvFileDestination = "D:\Trabajo\Proyectos\Development\PythonRepository\RTTs\TrafRTTE_TCC_TFP_CS_VOICE_A_SUR1M_20170614153704_20170614153709_0_VoiceSignallingError.dat"
#Voice Radiio Resource Error 
CsvFileModif = "D:\Trabajo\Proyectos\Development\PythonRepository\RTTs\TrafRTTE_TCC_TFP_CS_VOICE_A_SUR1M_20170614153704_20170614153709_0_Test.dat"
CsvFileDestination = "D:\Trabajo\Proyectos\Development\PythonRepository\RTTs\TrafRTTE_TCC_TFP_CS_VOICE_A_SUR1M_20170614153704_20170614153709_0_VoiceRadioResourceError.dat"
ficheroHeaders="D:\Trabajo\Proyectos\Development\PythonRepository\RTTs\TrafRTTE_TCC_TFP_CS_VOICE_A_SUR1M_20170614153704_20170614153709_0_Test.ctr"
matrix_field_names=["A_IMSI","A_MSISDN","A_Direction_Number","B_IMSI","B_MSISDN","B_Direction_Number","A_RR_Cause","B_RR_Cause"]
matrix_field_index=csvHeadersIndexes(ficheroHeaders, matrix_field_names,"TFP_MC")
matrix_field_values=['214070000000207','34600000207','34600000207', '214070000000208','34600000208','34600000208',20,20]
rtt_generator(CsvFileModif,CsvFileDestination,matrix_field_index,matrix_field_values)
#Sobreescribo el fichero maestro con el nuevo
#print("Renombrando Fichero:" + shutil.move(CsvFileModif+'nuevo', CsvFileModif))