# encoding: iso-8859-1
import sys

##################################################
## Crie uma função que lê um arquivo, linha por linha, e imprime o
## conteúdo.
##################################################
print('função que lê um arquivo, linha por linha, e imprime o conteúdo.\n')
def simple_print(arquivo) :
    f =  open(arquivo) 
    for line in f :
        line = line.rstrip()
        print(line)
    f.close()
# simple_print("docentes.txt") #se bloquear aqui ele não invoca o resto do método 
print('--------------------------------------------------------------------------------')
##################################################
## Crie uma função que lê um arquivo, linha por linha, e imprime um
## caracter por linha
##################################################

print('Função que lê um arquivo, linha por linha, e imprime um caracter por linha:\n')
def print_characters(arquivo) :
    f = open(arquivo)
    for line in f :
        line = line.rstrip()
        for el in line:
            print(el)
                 
    f.close()

# print_characters("docentes.txt")
print('--------------------------------------------------------------------------------')
##################################################
## Crie uma função que lê um arquivo, linha por linha, e imprime uma
## palavra por linha. 
##################################################
print('Função que lê um arquivo, linha por linha, e imprime uma palavra por linha:\n')
def print_words(arquivo) :
    f =  open(arquivo) 
    for line in f :
        line = line.split(" ")
        for line in line:
            print(line)         
    f.close()
print_words("docentes.txt")
##################################################
## Crie uma função que lê um arquivo, linha por linha, e retorna a
## vogal que mais se repete.
##################################################
def most_common_vowel(arquivo) :
    dicxd = {"a" : 0,"e" : 0,"i" : 0,"o" : 0,"u" : 0}
    f = open(arquivo)
    for line in f :
        line = line.rstrip()
        for el in line:
            el = el.lower()
            if el in dicxd:
                dicxd[el] += 1  #quando aparecer uma vogal ele irá incrementar nessa posição
    print('\n')
    print('A vogal que mais aparece é: \n')
    print max(dicxd, key=dicxd.get)
    f.close()
most_common_vowel("docentes.txt")
##################################################
## Crie uma função que lê um arquivo, linha por linha, e retorna o
## caracter que mais se repete.
##################################################
def most_common_character(arquivo) :
    pass


##################################################
## Crie uma função que lê um arquivo e devolve as cinco palavras mais
## comuns e a quantidade de ocorrência dessas palavras.
##################################################    
def print_most_common_words(arquivo) :
    pass

##################################################
## Crie uma função que lê um arquivo, linha por linha, e imprime na
## mesma linha os nomes de professores que iniciam com a mesma letra.
##################################################
def print_same_start(arquivo) :
    pass

##################################################
## Crie uma função que lê um arquivo, linha por linha, e imprime na
## mesma linha os nomes de professores que iniciam ou que terminam com
## a mesma letra.
##################################################
def print_same_start_or_same_end(arquivo) :
    pass

##################################################
## Crie uma função que lê um arquivo, linha por linha, e imprime na
## mesma linha os nomes de professores que iniciam com a mesma letra,
## ou cujos nomes completos tenham o mesmo resto quando divididos por
## 6. É provável que um mesmo professor esteja em várias listas.
##################################################
def print_same_start_or_same_mod_6(arquivo) :
    pass


