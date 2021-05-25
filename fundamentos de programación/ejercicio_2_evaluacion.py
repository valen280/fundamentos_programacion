# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 19:49:47 2021

@author: valentina hurtado Prada
"""

import math
area = 0 # variables
perimetro = 0 # variables
s = 0 #variables

lado1 = int(input("lado 1 :"))
lado2 = int(input("Lado 2: "))
lado3 = int(input("Lado 3: "))

s = (lado1 + lado2 + lado3)/2
area = (math.sqrt(s*(s-lado1)*(s-lado2)*(s-lado3)))
perimetro = lado1 + lado2 + lado3

print("El area del triángulo es :",area) 
print("El perimetro del triángulo es: ",perimetro) 