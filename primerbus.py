
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
    proble={'A':['B','C','D','E','F'],'B':['A','C'],'C':['A','B','D','G','H'],'D':['A','C','E','I'],'E':['A','D','F','J','K'],'F':['A','E'],'G':['C','H'],'H':['G','C','I','L'],'I':['D','J','N','M','L','H'],'J':['K','E','Ñ','I'],'K':['J','E'],'L':['M','I','H','O'],'M':['I','N','O','L'],'N':['I','M','Ñ','O'],'Ñ':['J','N'],'O':['L','M','N']}
    hs={'A':10,'B':11,'C':10.5,'D':10.25,'E':8,'F':12,'G':9,'H':7.5,'I':10,'J':12.25,'K':12,'L':9,'M':7,'N':10,'Ñ':11,'O':8.5} 
    soln=ascCol('A',10,proble,hs)
    print('SOLUCION ENCONTRADA:'+soln)
if __name__=='__main__': 
    main()
   