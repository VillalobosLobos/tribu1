def tablaSeleccion(fenotipo,valor,fitnes,probabilidad,acumulado):
	fila=len(fenotipo)

	titulo='Selección Tribú 1'
	print(f'\n{titulo.center(61)}\n')
	print(f' No. | Fenotipo | Valor | Fitnes | Probabilidad | Acumulado |')
	for i in range(1,fila+1):
		print(f'{str(i).center(5)}|{str(fenotipo[i-1]).center(10)}|{str(valor[i-1]).center(7)}|{str(fitnes[i-1]).center(8)}|{str(probabilidad[i-1]).center(14)}|{str(acumulado[i-1]).center(11)}|')

def tituloPadres():
	titulo='Padres generados por \'r\''
	print(f'\n{titulo.center(61)}')



