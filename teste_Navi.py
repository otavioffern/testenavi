#1

import numpy as ny

n = ny.zeros([5000000])

j = 0

for j in range (1,5000001):
    if (j%2 == 0 and j%37 == 0 and j%49 == 0):
        n[j]=1
    
y = ny.sum(n)
print('Há ', y, 'valores')

###########################################################
#2

import math as m
import statistics as s

x = ny.zeros([10])

i = 0

for i in range(0,9):
    if i%2 == 0:
        x[i]=(3**i)+7*(m.factorial(i))
    else:
        x[i] = 2**i + 4*(m.log(i))
        
print('O máximo está na posição', x.argmax())

k = round(s.mean(x),2)
print('A média é ', k)

###########################################################
#3

import numpy as ny

nomes = ny.chararray([5], itemsize = 20, unicode=True)
notas = ny.zeros([5])

j = 0
l = 0
dici = {}

for j in range(0,5):
        nomes[(j)] = input('Nome do Aluno {} : '.format(j+1))
        notas[(j)] = int(input('Nota do Aluno {} : '.format(j+1)))
        dici[nomes[(j)]]=notas[(j)]

maior_nota = max(dici, key = dici.get)
print('{} tirou a maior nota que foi {}'.format(maior_nota, dici[maior_nota]))