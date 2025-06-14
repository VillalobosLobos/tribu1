def tablaSeleccion(fenotipo,valor,fitnes,probabilidad,acumulado):
	fila=len(fenotipo)

	titulo='Selección Tribú 1'
	print(f'\n{titulo.center(61)}\n')
	print(f' No. | Fenotipo | Valor | Fitnes | Probabilidad | Acumulado |')
	for i in range(1,fila+1):
		print(f'{str(i).center(5)}|{str(fenotipo[i-1]).center(10)}|{str(valor[i-1]).center(7)}|{str(fitnes[i-1]).center(8)}|{str(probabilidad[i-1]).center(14)}|{str(acumulado[i-1]).center(11)}|')

def ciclo(padres,hijos,mutacion):
	titulo=' No. | Padres | Aptos para cruza | Hijos | Mutación |'
	print(f'\n\n{titulo.center(len(titulo))}')

	for i in range(0,len(padres)):
		print(f'  1  |{padres[i][0].center(8)}|{hijos[i][2].center(18)}|{hijos[i][0].center(7)}|{mutacion[i][0].center(10)}|')
		print(f'  2  |{padres[i][1].center(8)}|{" ".center(18)}|{hijos[i][1].center(7)}|{mutacion[i][1].center(10)}|')
		print(f'{"-"*len(titulo)}')




