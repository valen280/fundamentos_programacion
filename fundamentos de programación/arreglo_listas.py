# -*- coding: utf-8 -*-
"""
Created on Sat May 22 18:58:41 2021

@author: Valentina Hurtado Prada
"""
#variables escalares
print("Arreglo vectorial")
varVectorNum = [10,20,30,12,35,10]
print(varVectorNum)

#funciones de una lista
#adicional al final de la lista
varVectorNum.append(2000)
print(varVectorNum)

#adicionar datos por teclado a una lista

varVectorNumTec=[]
#adicionear datos por teclaso a la lista

for pos in range (3) :
    datoTeclado=int(input("digite valor:")) #escalar
    varVectorNumTec.append(datoTeclado)
print(varVectorNumTec)
varVectorNumTec.append(3000)
print(varVectorNumTec)
#borrar los elementos de la lista
#varVectorNumTec.clear()
#crear una lista con sus datos
varVectorNumDos=[2,4,6,8,10]
print(varVectorNumTec)
print(varVectorNumDos)
varVectorNumTec.extend(varVectorNumDos)
print(varVectorNumTec)
#conocer los elementos de la lista
tamVect=len(varVectorNumTec)
print("tamaño lista :",tamVect)
