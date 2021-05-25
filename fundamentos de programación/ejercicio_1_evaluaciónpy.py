# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 19:49:33 2021

@author: Valentina Hurtado Prada
"""

import math # importamos libreria para operaciones con raices

A = int(input("Lado del triangulo equilatero : ")) # se reconoce cuanto valen los lados
area = math.sqrt (3)/4 * A ** 2 # se saca el valor del area de un triangulo
perimetro = 3 * A #aplicando la formula dada hallamos el perimetro del triangulo siendo equilatero
print("El area del triángulo equilaterio es : ",area)#imprimir el resultado del area
print("El perimetro del triángulo equilatero es :",perimetro) # imprimir el resultado del perimetro