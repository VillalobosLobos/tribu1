import random

def hayMutacion():
	r=random.uniform(0,1)
	return True if r<0.3 else False

def cambioEstado(estado):
	return '0' if estado=='1' else '1'

def mutacion(hijo):
	nuevo=''
	for i in str(hijo):
		if hayMutacion():
			nuevo=nuevo+cambioEstado(i)
		else:
			nuevo=nuevo+i
	return nuevo

def inicioMutacion(hijos):
	salida=[]
	for i in hijos:
		salida.append([mutacion(i[0]),mutacion(i[1])])
	return salida
			


