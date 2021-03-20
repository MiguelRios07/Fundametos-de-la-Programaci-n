# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 10:54:34 2021

@author: Kmilo
"""

print("SISTEMA DE NOTAS DE CURSO DE PROGRAMACION")

#Entrada

NumeroEstudiantes=int(input("digite la cantidad de estudiantes del grupo: "))

#Declara la variable que controla el ciclo
contadorRepeticiones = 0
cantidadEstudiantesAprobaron=0
cantidadEstudiantesReprobaron=0
sumaDefinitivaEstudiantes=0.0
sumaDefinitivaEstudiantesAprobaron=0.0
sumaDefinitivaEstudiantesReprobaron=0.0
promedioDefinitivaEstudiantes=0.0

#Proceso
#iniciar el ciclo

while contadorRepeticiones < NumeroEstudiantes:
    # lectura de las notas de cada estudiante
    nobreEstudiante =(input("digite el nombre del estudiante"))
    notaUnoEstudiante = float(input(" Digite la nota del primer parcial del estudiante :"))
    notaDosEstudiante = float(input(" Digite la nota del segundo parcial del estudiante :"))
    notaTresEstudiante = float(input(" Digite la nota del tercer parcial del estudiante :"))
    #calcular la definitiva de cada estudiante
    notaDefinitiva = (notaUnoEstudiante+notaDosEstudiante+notaTresEstudiante)/3
    #sumar las definitivas de los estudiantes para calcular promedio
    sumaDefinitivaEstudiantes= sumaDefinitivaEstudiantes+notaDefinitiva
    print("1. la definitiva es:", notaDefinitiva)
    
    if(notaDefinitiva>=3.0):
        cantidadEstudiantesAprobaron=cantidadEstudiantesAprobaron+1
        # sumar las notas de los estudiantes que aprobaron
    else:
        cantidadEstudiantesReprobaron=cantidadEstudiantesReprobaron+1
        # sumar las notas de los estudiantes que reprobaron
        sumaDefinitivaEstudiantesReprobaron=sumaDefinitivaEstudiantesReprobaron+notaDefinitiva
        
    
    #incrementar la variable que controla el ciclo
    contadorRepeticiones = contadorRepeticiones+1
    
    #fin del ciclo
#calcular el promedio del grupo
promedioDefinitivaEstudianes=sumaDefinitivaEstudiantes/NumeroEstudiantes

promedioDefinitivaEstudiantesAprobaron=sumaDefinitivaEstudiantesAprobaron/NumeroEstudiantesAprobaron
promedioDefinitivaEstudiantesReprobaron=sumaDefinitivaEstudiantesReprobaron/NumeroEstudiantesReprobaron

    
print("OTROS CALCULOS")
print("2. Cantidad de estudiantes que aprobaron :" , cantidadEstudiantesAprobaron)
print("3. Cantidad de estudiantes que reprobaron :" , cantidadEstudiantesReprobaron)
print(f"4. promedio del grupo:" {"promedioDefinitivaEstudiantes:2f)