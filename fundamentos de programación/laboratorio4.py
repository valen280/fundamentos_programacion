# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 21:06:47 2021

@author: Luz Dary Prada
"""

def enteros_organizados ():
    entero1 = int(input("Ingrese entero 1 :"))
    entero2 = int(input("Ingrese entero 2 :"))
    entero3 = int(input("Ingrese entero 3 :"))
    
    if (entero1 < entero2) and (entero1 < entero3):
        print(entero1)
    else:
        if (entero2 < entero3 ):
            print (entero2)
        else:
            print(entero3)