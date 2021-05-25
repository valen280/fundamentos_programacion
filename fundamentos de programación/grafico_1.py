#ejercicio que almacena en listas-procesa en funciones -
#declarar las librerias a usar para la solucion
import matplotlib
import matplotlib.pyplot as plt 

#generar las listas con los datos inicializados
nombreProducto = ['Ron','Aguardiente','vino','cerveza','tequila']
exitenProdu=[75,50,100,150,40]

#funciones que resuelven el problema
def f_cal_tot_existencias():
    sumexis = 0
    for posLis in range(5):
        sumexis = sumexis + exitenProdu[posLis]
    print("total existencias:",sumexis)
def f_cal_tot_existencias_2():
    sumexis = 0
    for posLis in range(5):
        sumexis = sumexis + exitenProdu[posLis]
    return(sumexis)
#funcion que calcula el promedio de las existencias
def f_cal_tot_existencias_3():
    promexis = f_cal_tot_existencias_2()/len(exitenProdu)
    return(promexis)
    
#llamado a las funciones que realizan los cálculos
f_cal_tot_existencias
print("total existencia 2 :",f_cal_tot_existencias_2())
print("promedio de existencias : ",f_cal_tot_existencias_3())

#graficar la informacion
fig,ax = plt.subplots()
#definir el titulo del grafico
ax.set_title ('GRAFICO DE EXISTENCIAS DE PRODUCTOS')
ax.set_xlabel ('productos')
ax.set_ylabel ('existencias')

#crear el grafico 
plt.bar(nombreProducto,exitenProdu)

#publico el grafico
plt.show()