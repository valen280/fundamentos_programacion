# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 16:59:29 2021

@author: Valentina Hurtado Prada
"""
# Entrada 
monto_neto = int(input (" Ingrese el valor del monto neto : " ))

#Proceso 
iva = monto_neto * 19 / 100
total = monto_neto + iva
descuento = total * 5 / 100
total_des = total - descuento 

#Salida

print ("Su total con IVA es : ", total)
print ("Su total con el descuento :", total_des)

