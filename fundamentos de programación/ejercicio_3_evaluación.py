# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 23:12:52 2021

@author: Luz Dary Prada
"""

#punto 3
N=int(input("cuantos empleados tiene su empresa"))
k=0
horasextras=0
pagohorasextras=0
totalhoras=0
pagohoras=0

horasextras1=0
pagohorasextras1=0
totalhoras1=0
pagohoras1=0
k1=0

horasextras2=0
pagohorasextras2=0
totalhoras2=0
pagohoras2=0
k2=0

horasextrasF=0
pagohorasextrasF=0
totalhorasF=0
pagohorasF=0
kF=0

while (k<N):
  k=int(k+1)
  print("introduzca su nombre")
  nombreempleado=input()
  pagohoraemp=int(input("cuanto se le paga por hora"))
  horastrabajadas=int(input("cuantas horas trabajo"))
  print("introduzca su genero F o M mayuscula por favor")
  genero=input()
  sector=int(input("a cual seccion pertenece 1 o 2 o 3"))
  salud=0.125
  ICBF=0.04
  totalhoras=totalhoras+horastrabajadas
  if (horastrabajadas>35):
    salario=35*pagohoraemp+(horastrabajadas-35)*1.5*pagohoraemp
    pagohorasextras=pagohorasextras+(horastrabajadas-35)pagohoraemp(1.5)
    horasextras=horasextras+(horastrabajadas-35)
  else:
    salario=horastrabajadas*pagohoraemp
  pagohoras=pagohoras+salario
  if (salario>2000000-1 and salario<3000001):
    retencion=0.05
  if (salario>3000000 and salario<4000001):
    retencion=0.07
  if (salario>4000000 and salario<5000001):
    retencion=0.09
  if (salario>5000000):
    retencion=0.11
  #sectores
  if (sector==1):
    if (horastrabajadas>35):
      pagohorasextras1=pagohorasextras1+(horastrabajadas-35)pagohoraemp(1.5)
      horasextras1=horasextras1+(horastrabajadas-35)
    pagohoras1=pagohoras1+salario
    totalhoras1=totalhoras1+horastrabajadas
    k1=k1+1
  if (sector==2):
    if (horastrabajadas>35):
      pagohorasextras2=pagohorasextras2+(horastrabajadas-35)pagohoraemp(1.5)
      horasextras2=horasextras2+(horastrabajadas-35)
    pagohoras2=pagohoras2+salario
    totalhoras2=totalhoras2+horastrabajadas
    k2=k2+1
  if (genero=="F"):
    if (horastrabajadas>35):
      pagohorasextrasF=pagohorasextrasF+(horastrabajadas-35)pagohoraemp(1.5)
      horasextrasF=horasextrasF+(horastrabajadas-35)
    pagohorasF=pagohorasF+salario
    totalhorasF=totalhorasF+horastrabajadas
    kF=kF+1
  #imprimir informe personal
  print("empleado",nombreempleado,"codigos","su salario sin descontar seria:",salario,"descuento por salud:",salario*salud, "descuento por ICBF:",salario*ICBF,"descuento por retencion:",salario*retencion)
  print("su salario recibido seria:",salario*(1-salud-retencion-ICBF),"despues de trabajar:",horastrabajadas)

#informe empresa 
print("total empleados:",k,"total horas:",totalhoras,"total extras:",horasextras,"pago horas:",pagohoras, "pago extras:",pagohorasextras)

#informe sectores

print("informe sector 1")
print("total empleados:",k1,"total horas:",totalhoras1,"total extras:",horasextras1,"pago horas:",pagohoras1, "pago extras:",pagohorasextras1)

print("informe sector 2")
print("total empleados:",k2,"total horas:",totalhoras2,"total extras:",horasextras2,"pago horas:",pagohoras2, "pago extras:",pagohorasextras2)
  
print("informe sector 3")
print("total empleados:",k-k1-k2,"total horas:",totalhoras-totalhoras1-totalhoras2,"total extras:",horasextras-horasextras1-horasextras2,"pago horas:",pagohoras-pagohoras1-pagohoras2, "pago extras:",pagohorasextras-pagohorasextras1-pagohorasextras2)

#informe genero
print("informe femenino")
print("total empleados:",kF,"total horas:",totalhorasF,"total extras:",horasextrasF,"pago horas:",pagohorasF, "pago extras:",pagohorasextrasF)

print("informe masculino")
print("total empleados:",k-kF,"total horas:",totalhoras-totalhorasF,"total extras:",horasextras-horasextrasF,"pago horas:",pagohoras-pagohorasF, "pago extras:",pagohorasextras-pagohorasextrasF)