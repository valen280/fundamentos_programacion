# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 19:30:34 2021

@author: Valentina Hurtado Prada
"""
can_ele = 0
suma = 0 
media = 0.0
num = 0

num = int(input("ingrese el numero: "))

while (num > 0):
    
    suma = suma + num
    num = int(input("ingrese el numero: "))
    can_ele = can_ele + 1
    
if can_ele != 0 :
    media = suma / can_ele
    print("la media es : " , media)
else:
    print("no hay numero para calcular la media ")
    


