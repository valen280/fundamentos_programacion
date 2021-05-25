# -*- coding: utf-8 -*-
"""
Created on Sat May 22 18:28:08 2021

@author: Valentina Hurtado Prada
"""

#practica_1 con vectores
#almacenar en un vector las 5 notas del parcial
#declarar el vector - lista

listaNotas =[]
sumaNotas = 0.0
#asignar valores a la lista con ciclo
for poslista in range(5):
    #leer desde teclado la nota
    notasEst = float(input("Digite nota:"))
    sumaNotas=sumaNotas+notasEst
    #almacenamos la escalar en el arreglo
    listaNotas.append(notasEst)
#imprimir lista
print(listaNotas)
print("La suma de las notas es :",sumaNotas)
