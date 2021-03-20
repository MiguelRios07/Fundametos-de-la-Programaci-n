# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 20:11:35 2021

@author: Kmilo
"""

# -*- coding: utf-8 -*-
#Decoración: Nombre del Algoritmo

print("-------------------------------------------------------") 
print("Ejercicio3: NÚMEROS PRIMOS ENTRE 1 Y 1000 : ")
print("-------------------------------------------------------") 
#Constantes
primero = 2
limite = 1000
#Inicializando
Cont = 0 
#Proceso 
for i in range(primero, limite):
   primo = True
   j = 2 
    
   while (i > j) and (primo == True):
     if i%j == 0 :
        #como no se considerá el Número(i) y el 1 
        #Si otro numero divide a i entonces ya tendría
        # tres divisores. por lo tanto, no es primo
        primo = False
        break #Por tal motivo se rompe el ciclo
     else:
       j = j + 1
      
   if primo == True :
     print(i, "es primo.") 
     Cont = Cont + 1
#Salida

print("\nSALIDA: ")
print("-------------------------------------------------------")
print("Entre", primero, "y" , limite, "hay", Cont, "nº primos")