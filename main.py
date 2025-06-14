import seleccion as s
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
g.tablaSeleccion(fen,val,fit,pro,acu)

g.tituloPadres()
c.formarParejas(NOFENOTIPOS,fen,acu)



