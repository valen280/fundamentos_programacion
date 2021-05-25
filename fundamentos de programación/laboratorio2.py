# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 19:59:13 2021

@author: Valentina Hurtado Prada
"""
def valor_menor ():
    valor1 = int (input ("Ingrese valor 1 :"))
    valor2 = int (input ("Ingrese valor 2 :"))
    valor3 = int (input ("Ingrese valor 3 :"))
    if (valor1 < valor2) and (valor1<valor3):
        print(valor1)
    else:
        if (valor2<valor3):
            print(valor2)
        else:
            print(valor3)
            
valor_menor()
valor_menor()
        

