# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 19:37:12 2021

@author: Valentina Hurtado Prada
"""
tabla = 0
multiplicador = 1
resultado = 0
sumaResultados = 0
conRepCiclo = 1 

tabla = int(input(" Tabla : "))
multiplicador = int(input( "multiplicador : "))

    
for conRepCiclo in range ( multiplicador + 1):

    resultado = tabla * conRepCiclo
    sumaResultados = sumaResultados + resultado
    
    print(tabla, " * ", conRepCiclo , " = ",resultado)
    conRepCiclo = conRepCiclo + 1
print (" En que vuelta va : ", conRepCiclo)
print("La suma de los resultados es : ", sumaResultados)  
