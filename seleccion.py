from random import *

def ordenarMutaciones(parejas):
	fenotipos=[]
	for i in parejas:
		fenotipos.append(i[0])
		fenotipos.append(i[1])
	return fenotipos

def decodificar(fenotipos):
	valDecodificados=[]
	for i in fenotipos:
		valDecodificados.append(int(i,2))
	return valDecodificados

def fenotipos(valores,n):
	n=n+1
	longitud=len(bin(n)[2:])
	fenotipos=[]
	for i in valores:
		binario=bin(i)[2:]
		#Para agregar los ceros que faltan a la izquierda
		fenotipos.append(binario.zfill(longitud))
	return fenotipos

def valores(n):
	valores=[]
	n=n+1
	for i in range(1,n):
		valores.append(randint(0,n))
	return valores

def funcionFitnes(valores):
	fitnes=[]
	for i in valores:
		#Para la función fitnes x²
		evaluarFitnes=i*i
		fitnes.append(evaluarFitnes)
	return fitnes

def totalAptitud(fitnes):
	return sum(fitnes)

def probabilidad(fitnes,totalApt):
	prob=[]
	for i in fitnes:
		prob.append(round(i/totalApt,4))
	return prob

def acumulado(prob):
	acum=[]
	aux=0
	for i in prob:
		acum.append(round(aux+i,4))
		aux=aux+i
	return acum



