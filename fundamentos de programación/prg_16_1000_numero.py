# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 18:36:24 2021

@author: Valentina Hurtado Prada
"""
import random
can_num = 0
con_Rep = 0
numero = 0
acumulador_Suma = 0
promedio_num_aleatorios = 0.0

acumulador_positivos = 0.0
acumulador_negativos = 0.0
promedio_positivos=0.0
promedio_negativos=0.0
contador_positivos=0.0
contador_negativos = 0.0



can_num = int(input("Cantidad de números :"))

while (con_Rep < can_num):
    numero = random.randint (-1000,1000)
    acumulador_Suma = acumulador_Suma + numero
    
    if (numero>0):
        print("numero positivo : ",numero)
        acumulador_positivos = acumulador_positivos + numero
        contador_positivos = contador_positivos + 1
    else:
        print("numero negativo : ",numero)
        acumulador_negativos = contador_negativos
        contador_negativos = contador_negativos + 1
        
    con_Rep = con_Rep + 1
promedio_positivos = acumulador_positivos/contador_positivos
promedio_negativos = acumulador_negativos/contador_negativos  
promedio_num_aleatorios = acumulador_Suma / con_Rep


print( "suma de numeros aleatorios",acumulador_Suma)
print("promedio de numeros aleatorios", promedio_num_aleatorios)
    
print("suma de numeros positivos :" , acumulador_positivos)
print("promedio de numeros ",promedio_positivos)

print("suma de numeros negativos :" , acumulador_negativos)
print("promodio de numeros negativos :" , promedio_negativos)

    