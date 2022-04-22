miLista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
numero = 0
lfinal =[]
contador = 0
arreglo  = int(len(miLista))

#miLista.sort()
for i in range(arreglo) :
    for j in range(arreglo):
           if miLista[i] == miLista[j]:
                contador += 1
                if  miLista[i] not in lfinal:
                    lfinal.append(miLista[i])
                    contador = 0
           elif miLista[i] not in lfinal and contador >= 1:
                lfinal.append(miLista[i])
                contador = 0 
                    


print(lfinal)    







