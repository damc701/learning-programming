Algoritmo NOTASESTUDIANTES
	Definir notas, Como Real 
	Definir i, j Como Entero
	dimension notas[3,4]
	Para i <- 1 hasta 3 Con Paso  1 Hacer
		Escribir " estudiante ", i
		para j <- 1 Hasta 3 Con Paso 1 Hacer
			Escribir " ingrese la nota ", j, ": "
			Leer  notas[i,j]
		FinPara
	FinPara
	para i<- 1 Hasta 3 Con Paso 1 Hacer
		Escribir " notas del estudiante ", i, ": "
		Para j <- 1 Hasta 3 Con Paso 1 Hacer
			Escribir Sin Saltar notas[i,j], " "
		FinPara
	FinPara
FinAlgoritmo
