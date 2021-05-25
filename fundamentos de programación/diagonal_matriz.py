# -*- coding: utf-8 -*-
"""
Created on Sun May 23 11:32:50 2021

@author: Valentina Hurtado Prada
"""
matrizNumeros=[[7,8,3],[1,9,2],[4,6,5]]
print(matrizNumeros)

sumEleMat=0
for f in range (3):
    for c in range(3):
        sumEleMat = sumEleMat + matrizNumeros[f][c]
print("la suma de los elementos es :",sumEleMat)

for f in range(3):
    for c in range(3):
        print(matrizNumeros[f][c])
        
#diagonal principal
sumDiaPri=0
for pos in range(3):
    sumaDiaPri=sumDiaPri+matrizNumeros[pos][pos]
print("diagonal principal",sumaDiaPri)

