import seleccion as s
import mutacion as m
import cruza as c
import os

def tablaSeleccion(fenotipo,valor,fitnes,probabilidad,acumulado,titulo):
	fila=len(fenotipo)

	print(f'{titulo.center(61)}')
	print(f' No. | Fenotipo | Valor | Fitnes | Probabilidad | Acumulado |')
	for i in range(1,fila+1):
		print(f'{str(i).center(5)}|{str(fenotipo[i-1]).center(10)}|{str(valor[i-1]).center(7)}|{str(fitnes[i-1]).center(8)}|{str(probabilidad[i-1]).center(14)}|{str(acumulado[i-1]).center(11)}|')

def ciclo(padres,hijos,mutacion):
	titulo=' No. | Padres | Aptos para cruza | Hijos | Mutación |'
	print(f'\n{titulo.center(len(titulo))}')

	for i in range(0,len(padres)):
		print(f'  1  |{padres[i][0].center(8)}|{hijos[i][2].center(18)}|{hijos[i][0].center(7)}|{mutacion[i][0].center(10)}|')
		print(f'  2  |{padres[i][1].center(8)}|{" ".center(18)}|{hijos[i][1].center(7)}|{mutacion[i][1].center(10)}|')
		print(f'{"-"*len(titulo)}')

def mejor(valores):
	return max(valores)

def generaciones(fen,titulo,no,valAlto):
	os.system('clear')
	fenotipos=s.ordenarMutaciones(fen)
	valores=s.decodificar(fenotipos)
	fitnes=s.funcionFitnes(valores)
	totalA=s.totalAptitud(fitnes)
	prob=s.probabilidad(fitnes,totalA)
	acu=s.acumulado(prob)

	#Valores para mutar
	parejas=c.formarParejas(len(fenotipos),fenotipos,acu)
	hijos=c.inicioCruza(parejas)
	mutaciones=m.inicioMutacion(hijos)

	tablaSeleccion(fenotipos,valores,fitnes,prob,acu,titulo+no)
	ciclo(parejas,hijos,mutaciones)

	alto=mejor(fitnes)
	if alto>valAlto:
		valAlto=alto

	print(f'El valor más grande es: {valAlto}')

	try:
		print('¿Quieres ver otra generación? ',end='')
		sigue=int(input())

		if sigue==1:
			generaciones(mutaciones,"Generación ",str(int(no)+1),valAlto)
		else:
			print(f'\n\nAdios mi estimado :D')
	except ValueError:
		print(f'\n\nAdios mi estimado :D')




