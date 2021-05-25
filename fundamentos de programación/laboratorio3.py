# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 20:26:57 2021

@author: Valentina Hurtado Prada
"""
def cant_vocales (cadena):
    cant = 0
    for x in range (len(cadena)):
        if cadena[x]=="a" or cadena [x]=="e" or cadena [x]=="i" or cadena [x]=="o" or cadena [x]=="u":
            cant = cant + 1
    print("cantidad de vocales",cadena,"es",cant)

cant_vocales("valentina")
cant_vocales("esternocleidomastoideo")
cant_vocales("santiagoalejandro")