#INSERTIONSORT
import matplotlib.pyplot as plt
import numpy as np
import random
import time

lista=[]
tamanhos=[1000,10000,30000,60000]
tempos=[]
def geraLista(tamanho):
  x=[]
  while(len(x)<tamanho):
    j=random.randrange(tamanho)
    if j not in x:
      x.append(j)
  return x

def geraListaPiorCaso(tamanho):
  x=[]
  for i in range(tamanho,0,-1):
    x.append(i)
  return x

def insertionsort(lista):
    now=time.time() 
    for i in range(1, len(lista)): 
        x=lista[i] 
   
        j=i-1
        while (j>=0 and x<lista[j]): 
                lista[j+1]=lista[j] 
                j-=1
        lista[j+1]=x
    then=time.time()
    return (then-now)


for i in tamanhos:
  lista=geraLista(i)
  #lista=geraListaPiorCaso(i)
  tempo=insertionsort(lista)
  tempos.append(tempo)
# Plot the data
plt.plot(tamanhos,tempos)
print(tempos)
# Show the plot
plt.show()
