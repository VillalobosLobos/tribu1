import random

def padre(fenotipos,acumulado):
	r=round(random.uniform(0,1),4)
	salida=0
	for i in acumulado:
		if i>=r:
			salida=i
			break
	return acumulado.index(salida)

def formarParejas(noTotal,fen,acumulado):
	parejas=[]
	numParejas=int(noTotal/2)
	fenotipos=fen
	for i in range(0,numParejas):
		p1=fenotipos[padre(fenotipos,acumulado)]
		p2=fenotipos[padre(fenotipos,acumulado)]
		parejas.append([p1,p2])
	return parejas

def siHayCruza():
	r=random.uniform(0,1)
	#Como consideramos 0.7 de probabilidad para la cruza
	return True if r<0.7 else False


def puntoCruza(fenotipo):
	return random.randint(1,len(fenotipo)-1)

def cruza(fen1,fen2):
	corte=puntoCruza(fen1)
	nuevoFen1=fen1[:corte]+fen2[corte:]
	nuevoFen2=fen2[:corte]+fen1[corte:]
	return [nuevoFen1,nuevoFen2,"si, pto.Corte: "+str(corte)]

def inicioCruza(parejas):
	hijos=[]
	for i in parejas:
		if siHayCruza():
			hijos.append(cruza(i[0],i[1]))
		else:
			hijos.append([i[0],i[1],"No apto"])
	return hijos














