# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 18:47:38 2021

@author: Valentiba Hurtado Prada
"""

#progeama que calcula la nota de un estudiante
#entradas
#pedir el nombre del estudiante y sus 3 notas de parciales


canEst= int(input("Cantidad de estudiantes : "))

#inicializar la variable qie controla el ciclo 

conRep=0

while(conRep < canEst):
    #instrucciones a repetir
    nomEst= input("Nombre estudiante : ")
    notUnoEst= float(input("Parcial uno : "))
    notDosEst= float(input("Parcial dos : ")) 
    notTresEst= float(input("Parcial tres : ")) 
    
    #calculos
    notDefEst = (notUnoEst + notDosEst + notTresEst)/3
    
    #imprimir salidas
    print(f"la nota definitiva es : {notDefEst :.1f} " )
    
    # Invrmentar la varible que controla el ciclo 
    conRep = conRep + 1 


