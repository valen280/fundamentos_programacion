# -*- coding: utf-8 -*-
"""
Created on Sat May 22 19:51:41 2021

@author: Valentina Hurtado Prada
"""
#metodos de ordenamiento
#crear lista
listaBase=[34,12,45,2,37,60,34,8]
#ordenar la lista con una función de python
listaBase.sort()
print("lista base ordenada ascendente:",listaBase)

listaBase.sort(reverse=True)
print("lista base ordenada descendente:",listaBase)

#====================================================================
#  ORDENAMIENTO BURBUJA ASCENDENTE
print("FUNCIÓN DESARROLLADA POR EL PROGRAMADOR")
def ordenamientoBurbujaAscendente(unaLista): #funcion del programador,parametro arreglo
    for numPasada in range(len(unaLista)-1,0,-1) :#ciclo que recorre la lista
        for i in range(numPasada): #ciclo interno que recorre,contadores
            if unaLista[i]>unaLista[i+1]: #comparacion con el actual|con siguiente
                temp = unaLista[i]
                unaLista[i] = unaLista[i+1]
                unaLista[i+1] = temp

unaLista = [54,26,93,17,77,31,44,55,20 ]#creando la lista
print("lista original :",unaLista)

ordenamientoBurbujaAscendente(unaLista)
print("Lista Ordenada burbuja : ", unaLista)
#===================================================================

#  FUNCIÓN DESARROLLADA POR EL PROGRAMADOR
#  ORDENAMIENTO BURBUJA DESCENDENTE
print("FUNCIÓN DESARROLLADA POR EL PROGRAMADOR")
def ordenamientoBurbujaDescendiente(unaLista): #funcion del programador,parametro arreglo
    for numPasada in range(len(unaLista)-1,0,-1) :#ciclo que recorre la lista
        for i in range(numPasada): #ciclo interno que recorre,contadores
            if unaLista[i]<unaLista[i+1]: #comparacion con el actual|con siguiente
                temp = unaLista[i]
                unaLista[i] = unaLista[i+1]
                unaLista[i+1] = temp

unaLista = [2,14,93,17,23,31,15,55,4 ]#creando la lista
print("lista original :",unaLista)

ordenamientoBurbujaDescendiente(unaLista)
print("Lista Ordenada burbuja descendiente : ", unaLista)
