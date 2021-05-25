# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 23:38:03 2021

@author: valentina Hurtado Prada
"""

#punto 3
N=int(input("cuantos empleados tiene su empresa :"))
k=0
horasextras=0 # variables empresa en total
pagohorasextras=0
totalhoras=0
pagohoras=0

horasextras1=0 #variables seccion 1
pagohorasextras1=0
totalhoras1=0
pagohoras1=0
k1=0

horasextras2=0 #variables seccion 2
pagohorasextras2=0
totalhoras2=0
pagohoras2=0
k2=0

horasextrasF=0 # variable seccion femenina
pagohorasextrasF=0
totalhorasF=0
pagohorasF=0
kF=0

while (k<N): 
  k=int(k+1) #contadoe
  print("introduzca su nombre :")
  nombreempleado=input()#nombramiento
  pagohoraemp=int(input("cuanto se le paga por hora :")) # variable pago hora
  horastrabajadas=int(input("cuantas horas trabajo :")) # variable horas trabajadas
  print("introduzca su genero F o M mayuscula por favor :") # a que genero pertenece
  genero=input()
  sector=int(input("a cual seccion pertenece 1 o 2 o 3 :"))# variable sectores
  salud=0.125#descuento por salud
  ICBF=0.04#descuento por ICBF
  totalhoras=totalhoras+horastrabajadas # cuantas horas trabajo
  if (horastrabajadas>35): #condicion
    salario=35*pagohoraemp+(horastrabajadas-35)*1.5*pagohoraemp# salario
    pagohorasextras=pagohorasextras+(horastrabajadas-35)*pagohoraemp*(1.5) #horas extras
    horasextras=horasextras+(horastrabajadas-35)#horas extras
  else:
    salario=horastrabajadas*pagohoraemp # si no pasa lo anterior
  pagohoras=pagohoras+salario
  if (salario>2000000-1 and salario<3000001): #filtro 1
    retencion=0.05 # retencion por el filtro 1
  if (salario>3000000 and salario<4000001):#filtro 2
    retencion=0.07# retencion por el filtro 2
  if (salario>4000000 and salario<5000001):#filtro 3
    retencion=0.09# retencion por el filtro 3
  if (salario>5000000):#filtro4
    retencion=0.11# retencion por el filtro 4
  #sectores
  if (sector==1): #condicion sector 1
    if (horastrabajadas>35):# salario si las horas son mayores a 35
      pagohorasextras1=pagohorasextras1+(horastrabajadas-35)*pagohoraemp*(1.5)
      horasextras1=horasextras1+(horastrabajadas-35)
    pagohoras1=pagohoras1+salario
    totalhoras1=totalhoras1+horastrabajadas
    k1=k1+1
  if (sector==2): #condicion sector 2
    if (horastrabajadas>35):# salario si las horas son mayores a 35
      pagohorasextras2=pagohorasextras2+(horastrabajadas-35)*pagohoraemp*(1.5)
      horasextras2=horasextras2+(horastrabajadas-35)
    pagohoras2=pagohoras2+salario
    totalhoras2=totalhoras2+horastrabajadas
    k2=k2+1
  if (genero=="F"):#condicion sector f
    if (horastrabajadas>35):# salario si las horas son mayores a 35
      pagohorasextrasF=pagohorasextrasF+(horastrabajadas-35)*pagohoraemp*(1.5)
      horasextrasF=horasextrasF+(horastrabajadas-35)
    pagohorasF=pagohorasF+salario
    totalhorasF=totalhorasF+horastrabajadas
    kF=kF+1
  #imprimir informe personal
  print("empleado",nombreempleado,"codigos(82202111481-82202113939-8220213926)","su salario sin descontar seria:",salario,"descuento por salud:",salario*salud, "descuento por ICBF:",salario*ICBF,"descuento por retencion:",salario*retencion)
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
# en el sector 3 se realiza la resta porque lo que sobra es el informe del sector 3
#informe genero
print("informe femenino")
print("total empleados:",kF,"total horas:",totalhorasF,"total extras:",horasextrasF,"pago horas:",pagohorasF, "pago extras:",pagohorasextrasF)

print("informe masculino")
print("total empleados:",k-kF,"total horas:",totalhoras-totalhorasF,"total extras:",horasextras-horasextrasF,"pago horas:",pagohoras-pagohorasF, "pago extras:",pagohorasextras-pagohorasextrasF)
# en el sector masculino se realiza la resta porque lo que sobra es el informe del sector masculino