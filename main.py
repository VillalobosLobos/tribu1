import seleccion as s
import mutacion as m
import general as g
import cruza as c
import os

#Variables
NOFENOTIPOS=10

val=s.valores(NOFENOTIPOS)
fen=s.fenotipos(val,NOFENOTIPOS)
fit=s.funcionFitnes(val)
tap=s.totalAptitud(fit)
pro=s.probabilidad(fit,tap)
acu=s.acumulado(pro)

os.system('clear')

parejas=c.formarParejas(NOFENOTIPOS,fen,acu)
hijos=c.inicioCruza(parejas)
mutaciones=m.inicioMutacion(hijos)

g.tablaSeleccion(fen,val,fit,pro,acu,"Generación 1")
g.ciclo(parejas,hijos,mutaciones)
valAlto=g.mejor(fit)

print(f'El valor más grande es: {valAlto}')

try:
	print('\n¿Quieres ver otra generación? ',end='')
	sigue=int(input())

	if sigue==1:
		g.generaciones(mutaciones,"Generación ","2",valAlto)
	else:
		print(f'\n\nAdios mi estimado :D')
except ValueError:
	print(f'\n\nAdios mi estimado :D')


