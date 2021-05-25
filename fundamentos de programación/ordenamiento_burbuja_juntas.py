# -*- coding: utf-8 -*-
"""
Created on Sun May 23 08:34:07 2021

@author: Luz Dary Prada
"""

#  FUNCIÓN DESARROLLADA POR EL PROGRAMADOR
#  ORDENAMIENTO BURBUJA DESCENDENTE
print("FUNCIÓN DESARROLLADA POR EL PROGRAMADOR")
def ordenamientoBurbuja(unaLista,tipo):
    if(tipo=="ascendente"):
        for numPasada in range(len(unaLista)-1,0,-1) :#ciclo que recorre la lista
            for i in range(numPasada): #ciclo interno que recorre,contadores
                if unaLista[i]>unaLista[i+1]: #comparacion con el actual|con siguiente
                    temp = unaLista[i]
                    unaLista[i] = unaLista[i+1]
                    unaLista[i+1] = temp

    if(tipo=="descendente"):
        for numPasada in range(len(unaLista)-1,0,-1) :#ciclo que recorre la lista
            for i in range(numPasada): #ciclo interno que recorre,contadores
                if unaLista[i]<unaLista[i+1]: #comparacion con el actual|con siguiente
                    temp = unaLista[i]
                    unaLista[i] = unaLista[i+1]
                    unaLista[i+1] = temp

unaLista = [2,14,93,17,23,31,15,55,4 ]#creando la lista
print("lista original :",unaLista)
tipo="descendente"
ordenamientoBurbuja(unaLista,tipo)
print("Lista Ordenada burbuja descendiente : ", unaLista)