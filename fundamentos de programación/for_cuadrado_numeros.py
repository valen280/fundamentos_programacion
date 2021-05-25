# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 18:44:41 2021

@author: Luz Dary Prada
"""
acu_suma = 0
cuadrado_num = 0
# num = 1
con_rep_while = 1

can_numero = int(input("cantidad de numeros :"))
while con_rep_while < can_numero +1 :
#for num in range (1,can_numero+1,3) :
    cuadrado_num = con_rep_while *con_rep_while
    acu_suma = acu_suma+cuadrado_num
    print("el cuadrado de :",con_rep_while,"es :",cuadrado_num)
    print("la suma acumulada es :",acu_suma)
    con_rep_while = con_rep_while + 1    
print("la suma de los cuadrados es :",acu_suma)