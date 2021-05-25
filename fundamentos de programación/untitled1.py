# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 19:37:49 2021

@author: Valentina Hurtado Prada
"""
def numero_entero ():
    entero = int(input("Ingrese valor entero :"))
    entero = entero * entero
    print("el cuadrado del numero es:",entero)

def multiplicacion ():
    valor1 = int(input("ingrese primer valor :"))
    valor2 =int (input("ingrese segundo valor :"))
    mult = valor1 * valor2
    print("multiplicación de los dos valores: ", mult)
    
numero_entero ()
multiplicacion()