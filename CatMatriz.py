# encoding: utf-8

# Parte 1: Importe o conteúdo do arquivo conf01.py e crie uma matriz a
# partir dele. Na sua matriz, use:

# 0: casa vazia
# 1: casa bloqueada
# 2: casa de saída
# 3: casa onde o gato está.

# Parte 2: Simule a movimentação do gato indo na direção da saída. Em
# sua simulação, você deverá colocar o número 4 para indicar que uma
# determinada casa já foi visitada pelo gato.


import importlib
import sys

filename = sys.argv[1]
mod = importlib.import_module(filename)
cat = mod.cat

cat     = [5, 5]
blocks  = [ (1,1), (1,5), (2,5), (4,5), (5,1), (5, 4), (6, 5), (8, 2) ]
exits   = [ (0,0), (6, 10), (9, 10), (10, 1) ]
minimum = 5

def gerar_matriz (n_linhas, n_colunas):
    return [["*"]*n_colunas for _ in range(n_linhas)]

matrix = gerar_matriz(11,11)


for i in mod.blocks:  # Ele irá ler onde existe os bloqueios 
    matrix[i[0]][i[1]] = 1     # Após isso, ele irá atribuir o numero 1 na posição da matriz em que
                                # houver o bloqueio

for i in mod.exits:  # Ele irá ler onde existe as saídas
    matrix[i[0]][i[1]] = 2



for i in range(11):    # ele vai quebrar uma linha a cada 11 elementos
    print(matrix[i])
    

          
        
