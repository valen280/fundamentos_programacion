# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 22:17:52 2021

@author: Valentina Hurtado Prada
"""
# Declaracion de librerías


# Declaración de variables y/o constantes



# Entrada - Captura de datos 
var_ent_estatura = int(input("Digite su estatura en centimetros : "))
var_ent_peso = int(input("Digite su peso en kilos : "))



# Proceso - Realizando Cálculos
var_ent_masa_corporal = var_ent_peso /((var_ent_estatura **2 )/10000)


# Salida - Imprimiendo los resultados
print("Su masa corporal es : ", var_ent_masa_corporal)