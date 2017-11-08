#! python 3

import sys
import time

filename='D:/Trabajo/Formacion/Phyton/GitRepository/ficheroejemplo.txt'
#Escribir en fichero desde cero
text='Texto a incluir en fichero\n'
filedescriptor=open(filename,'w')
filedescriptor.write(text)

filedescriptor.close()

#Append en fichero
text='\ntexto a añadir al final'
filedescriptor=open(filename,'a')
filedescriptor.write(text)
filedescriptor.close()

#Read from file
print('\n\nLectura fichero entero')
filedescriptor=open(filename,'r')
text=filedescriptor.read()
print(text)

print('\n\nLectura por lineas')
filedescriptor=open(filename,'r')
text=filedescriptor.readlines()
print(text)

