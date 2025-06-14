import random

def padre(fenotipos,acumulado):
	r=round(random.uniform(0,1),4)
	salida=0
	for i in acumulado:
		if i>r:
			salida=i
			break
	return acumulado.index(salida)

def formarParejas(noTotal,fenotipos,acumulado):
	numParejas=int(noTotal/2)
	for i in range(0,numParejas):
		print(f'\nPadre 1 ---> {fenotipos[padre(fenotipos,acumulado)]}')
		print(f'Padre 2 ---> {fenotipos[padre(fenotipos,acumulado)]}')
	return 0


		
