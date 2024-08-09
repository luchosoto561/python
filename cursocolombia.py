import numpy as np
import matplotlib.pyplot as plt
# como los datos normalmente los representamos como matrices es de ahi de donde viene la necesidad de utilizar numpy

lista1 = [1,5,6,7,34,56]
m = np.array(lista1) #necesitamos arreglos porque cuando trabajamos con datos, necesitamos velocidad y bajo uso de recursos, por lo que quedate con que los arreglos son como las listas pero que no estan en una dimension sino que estan en mas de una (cosas multidimensionales) -> solo se crean arreglos con datos homogeneos
m2 = np.array(lista1,dtype = "float16") 
#m3 = np.array([12,3,5,7,5],[3,56,23,6,8]) #arreglo de dos dimensiones

#metodos para crear arreglos: Arange,Linspace y Logspace, Zeros y Ones 

#m3.shape(4,6)# decis que tenga 4 filas y 6 columnas

print(m[:3]) #te imprime los primeros 3 elementos del arreglo
print(m[3:]) #te imprime de la posicion 3 hasta el final

m4 = np.arange(20) #arreglo de 20 elementos

#-------------------------------------------------------------------

a = np.array([1,2,3,4])
b = a[2:4]
b[0] = 0
print("b = ", b )# imprime cero porque cuando modifico un arreglo creado atraves de otro arreglo se modifica el arreglo original

c = a.copy() # te copia el arreglo pero si lo modificas no pasa nada 

#-----------------------------------------------------------------
a1 = np.array([1,2,3,4,5,6,7])
mascara = [True, True, False, True, False, False, True]
mascara2 = a1>3
print(a1)
print(a1[mascara])# te imprime los valores de a1 que en la misma posicion de mascara esta el valor True
print(a1[mascara2])# te imprime True en los elementos que a1 es mayor que tres

a1[a1 > 3] = 0
print(a1)#imprime todo igual que a1 pero en los lugares donde el valor es mayor que tres te lo devuelve en cero

#----------------------------------------------------------------

np.random.seed(0)# el cero es la semilla generadora de numeros aleatorios si le pongo tres me da un vector que tiene 3 elementos aleatorios, si pongo 3,3 te genera una matriz de 3x3 con numeros aleatorios

np.random.seed(12)
campana_gauss = np.random.rand(10000)
plt.hist(campana_gauss, bins = 1000)
plt.show()