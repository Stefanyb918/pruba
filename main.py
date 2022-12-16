
import math
import os
import random
import re
import sys


#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#
arr=[0,2,-3,3,2]


def plusMinus(arr):

    catidad_total =str(len(arr))

    print(f'la catidad total es :{catidad_total} elementos ')
    if int(catidad_total) == 1:
        print('Hay un elementos ')
    elif int(catidad_total) ==2:
        print('Hay Dos elementos  ')
    elif int(catidad_total) == 3:
        print('Hay Tres elementos  ')
    elif int(catidad_total) == 4:
        print('Hay Cuatro elementos  ')

    zero = []
    negatico = []
    positivo = []

    for i in arr:

        if float(i) == 0:
            zero.append(i)
        elif float(i) < 0:
            negatico.append(i)
        else:
            positivo.append(i)



    if len(zero) ==0:
        print("zero")
    elif len(zero)== 1:
        print("Un zero")
    elif len(zero)==2:
        print("Tres zero")


    if len(negatico) ==0:
        print("zero negatico")
    elif len(negatico)== 1:
        print("Un negatico")
    elif len(negatico)==2:
        print("Dos negatico")
    elif len(negatico) == 3:
        print("Tres negatico")

    if len(positivo) ==0:
        print("zero positivo")
    elif len(negatico)== 1:
        print("Un positivo")
    elif len(negatico)==2:
        print("Dos positivo")
    elif len(negatico) == 3:
        print("Tres positivo")









    for i in arr:
        pass


if __name__ == '__main__':
    plusMinus(arr)
    print("hola")
