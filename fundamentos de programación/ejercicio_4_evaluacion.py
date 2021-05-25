# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 21:52:09 2021

@author: valentina hurtado Prada
"""
# punto 4-82202111481-82202113939-8220213926
import numpy as np # se importa libreria
def INIARR(L): # arreglo
  N=L 
  x= np.zeros((N)) # inciar funcion en ceros
  return x 
sumarango=0 # hasta donde va la funcion
a=input("hasta donde ira :") # saber hasta que numero va
a=int(a)
b=int(input("que valor quiere que se le imprima de la serie :")) #el valor que se va imprimir
c=int(input("limite inferior de la serie que quiere :")) # punto c, valor limite inferior
d=int(input("limite superior de la serie que quiere :")) # valor limite superior
z=int(d-c+1) # saber de cuantos son los arreglos mas pequeños
L=INIARR(a) # arreglo para a
L[0]=1 # se colocan los 2 primeros numeros (primer numero)
L[1]=1# segundo numero
k=0
while (k<a-2): # se realiza un bucle
 L[k+2]=L[k+1]+L[k] # para que se vayan sumando los numeros
 k=k+1

M=INIARR(z) # arreflo mas pequeño
M=L[c-1:d] # limite hasta otro
s=0
while (s<z): # bucle
  sumarango = sumarango + M[s] # acumulador
  s=s+1
print("serie que quiso imprimir", L) # imprimir
print("valor que se le imprimio de la serie", L[b-1]) #imprimir
print("rango que escogio",M,"suma de este rango",sumarango) #imprimir