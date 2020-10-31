
## Esta funcion regresa a los hijos de un estado
def getHijos(edo,proble): 
    return proble[edo]
## Esto regresa al mejor estado en la lista
def siguiente(lista ,hs): 
    hmejor =1000
    mejor= ''
    for edo in lista:   
        if hs[edo]<hmejor: 
            hmejor=hs[edo] 
            mejor=edo
    return mejor,hmejor
## Esto implementa la busqueda por ascenso de colina
def ascCol(edo,hedo,proble,hs): 
    hijos=getHijos(edo,proble)
    nuevo ,hnuevo=siguiente(hijos ,hs) 
    if hnuevo >hedo:
        soln=edo 
    else:
        soln=ascCol(nuevo ,hnuevo ,proble ,hs) 
    return soln

def main():
    proble={'A':['B','C','D'],'B':['A','C','E'],'C':['A','B','D','E'],'D':['A','C','F'],'E':['B','C','F'],'F':['D','E']}
    hs={'A':45,'B':40,'C':35,'D':37,'E':23,'F':15} 
    soln=ascCol('A',45,proble,hs)
    print('SOLUCION ENCONTRADA:'+soln)
if __name__=='__main__': 
    main()
   