# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 19:00:48 2021

@author: valentina hurtado Prada
"""
var_e_nom = "***"
var_e_basic = 0.0
var_e_for = 0.0
var_e_pas = 0.0
var_p_s_conEst = 0
var_p_s_med = 0.0
var_e_nota = 0.0

var_e_nom = input("Digite nombre del estudiante :")
while (var_e_nom != "***"):
    var_e_basic = float(input("Definitiva de basic :"))
    var_e_for = float(input("Definitiva de fortran :"))
    var_e_pas = float(input("Definitiva de pascal :"))
    
    var_p_s_med = (var_e_basic + var_e_for + var_e_pas) / 3
    print("La media es : ",var_p_s_med)
    
    var_e_nom = input("Digite su nombre :")
    var_p_s_conEst = var_p_s_conEst + 1
   

print ("Adios..") 
print ("Numero de estudiantes : ", var_p_s_conEst)