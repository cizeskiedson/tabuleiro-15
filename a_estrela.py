#Autor: Edson Matheus A. Cizeski
#RA 107514
#Implementatacao do algoritmo A*

##imports

import heapq
import copy

## classe que define um no da arvore

class verticeArvore:
    def __init__(self, tabuleiro, custoG, custoH, ptrPai, filhos):
        self.tabuleiro = tabuleiro
        self.g = custoG
        self.h_linha = custoH
        self.pai = ptrPai
        self.filhos = filhos

    def calculaF(self):
        return self.g + self.h_linha

## retorna config final esperada
def config_final():
    return [[1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15], [4, 8, 12, 0]]

## le a matriz entrada

def limpaEntrada(string):
    if(string[0] == ' '):
        string = string[1:]
    return string

def leEntrada(tabuleiro):
    #comeca a ler os dados passados por input
    string = input() #le uma string com os numeros  
    string = limpaEntrada(string)
    valorLido = string.split(' ') #divide os numeros pelo separador ' ' 
    listaValor = [0] * 16 # inicializa uma lista com os valores de 16 posicoes
    for k in range(0, len(valorLido)):
        if valorLido[k]:
            listaValor[k] = int(valorLido[k]) #pega cada numero e salva na lista
 
    inc = 0 #variavel de incremento

    #comeca a colocar os valores em ordem nas posicoes do tabuleiro
    for i in range(0, 4):
        for j in range(0, 4):
            tabuleiro[i][j] = listaValor[inc] #tabuleiro recebe na posicao (i, j) o valor da lista em ordem
            inc+=1


## funcao que retorna os sucessores de um no

def achaNo(valor, no_pai):
    for i in range(0, 4):
        for j in range(0, 4):
            if no_pai.tabuleiro[i][j] == valor:
                return (i, j)
    return (-1, -1)

def geraSucessor(no_pai):
    #print("sucessores\n")
    # pego o no_pai
    # procuro os sucessores a partir do elemento 0
    valor = 0
    i, j = achaNo(valor, no_pai)
    if i == -1 or j == -1:
        print('erro ao encontrar elemento na matriz \n')
        exit(1)
    else:
    # vejo quem sao seus filhos

    # começo a gerar seus sucessores
        if(i > 0): #tem sucessor em cima
            no_cima = copy.deepcopy(no_pai.tabuleiro) #copia tabuleiro pra o novo no
            #troca as posicoes dos dois elementos
            aux = no_cima[i][j]
            no_cima[i][j] = no_cima[i-1][j]
            no_cima[i-1][j] = aux
            #cria verticeArvore filho com profundidade g + 1 
            filho = verticeArvore(no_cima, no_pai.g + 1, heuristica1(no_cima), [], [])
            #adiciona filho na lista do pai
            no_pai.filhos.append(filho)
        if(i < 3): # tem sucessor em baixo
            no_baixo = copy.deepcopy(no_pai.tabuleiro) #copia tabuleiro pra o novo no
            #troca as posicoes dos dois elementos
            aux = no_baixo[i][j]
            no_baixo[i][j] = no_baixo[i+1][j]
            no_baixo[i+1][j] = aux
            #cria verticeArvore filho com profundidade g + 1 
            filho = verticeArvore(no_baixo, no_pai.g + 1, heuristica1(no_baixo), [], [])
            #adiciona filho na lista do pai
            no_pai.filhos.append(filho)
        if(j > 0): #tem sucessor na esquerda
            no_esquerda = copy.deepcopy(no_pai.tabuleiro) #copia tabuleiro pra o novo no
            #troca as posicoes dos dois elementos
            aux = no_esquerda[i][j]
            no_esquerda[i][j] = no_esquerda[i][j-1]
            no_esquerda[i][j-1] = aux
            #cria verticeArvore filho com profundidade g + 1 
            filho = verticeArvore(no_esquerda, no_pai.g + 1, heuristica1(no_esquerda), [], [])
            #adiciona filho na lista do pai
            no_pai.filhos.append(filho)
        if(j < 3): #tem sucessor na direita
            no_direita = copy.deepcopy(no_pai.tabuleiro) #copia tabuleiro pra o novo no
            #troca as posicoes dos dois elementos
            aux = no_direita[i][j]
            no_direita[i][j] = no_direita[i][j+1]
            no_direita[i][j+1] = aux
            #cria verticeArvore filho com profundidade g + 1 
            filho = verticeArvore(no_direita, no_pai.g + 1, heuristica1(no_direita), [], [])
            #adiciona filho na lista do pai
            no_pai.filhos.append(filho)


# algoritmo A*
A = {} 
F = {}
heap_f = []

def a_estrela(tabuleiro):
    indiceDicionario = str(tabuleiro)
    global A 
    global F
    v = verticeArvore(tabuleiro, 0, heuristica1(tabuleiro), [], [])
    A[indiceDicionario] = v

    global heap_f
    heapq.heappush(heap_f, (A[indiceDicionario].calculaF(), indiceDicionario))
    while (A != {}) and (not checa_igual(v.tabuleiro)):
        posicao_minimo = calcula_min(heap_f, A)
        v = A.get(posicao_minimo) #encontra no dicionario o elemento desejado
        indiceDicionario = str(v.tabuleiro) #indice dicionario recebe a string da matriz (chave do dic)
        A.pop(indiceDicionario) #remove estado aberto
        F[indiceDicionario] = v #adiciona estado fechado
        
        if v.filhos:
            m = v.filhos
        else:
            geraSucessor(v)
            m = v.filhos
        #comeca g(m)
        #pesquisa entre todos os sucessores
        for i in range(0, len(m)):
            m_linha = m[i]
            posicao_m_linha = str(m[i].tabuleiro)
            if posicao_m_linha in A and m_linha.g < A[posicao_m_linha].g: #caso 1
                A.pop(posicao_m_linha)
            if (posicao_m_linha not in (A and F)):
                adicionaEmA(m_linha, posicao_m_linha, v, A)
                heapq.heappush(heap_f, (A[posicao_m_linha].calculaF(), posicao_m_linha))
        indiceDicionario = ""

    return v.g ##resposta eh a profundidade do ultimo vertice

def adicionaEmA(m_linha, posicao, pai, A):
    A[posicao] = m_linha
    A[posicao].pai = pai
    A[posicao].h_linha = m_linha.h_linha


def checa_igual(tabuleiro):
    if heuristica1(tabuleiro) == 0: return True
    else: return False

def calcula_min(f, A):
    for i in range(0, len(A)):
        minimo = heapq.heappop(f)
        if(minimo[1] in A):
            return minimo[1]


# heuristicas

#1
def heuristica1(tabuleiro):    
    final = config_final()
    conta_fora_ordem = 0
    for i in range(0, 4):
        for j in range(0, 4):
            if tabuleiro[i][j] == 0:
                continue
            if tabuleiro[i][j] != final[i][j]:
                conta_fora_ordem += 1
    return conta_fora_ordem


#2
def prox(i, j): #funcao q retorna a posicao do prox elemento do tabuleiro
    if j == 3:
        j = 0
        return (i+1, j)
    else:
        return (i, j+1)

def heuristica2(tabuleiro):
    conta_fora_ordem = 0
    for i in range(0,4):
        for j in range(0,4):
            if tabuleiro[i][j] == 0: # nao analisa caso vazio
                continue
            if not (i == 3 and j == 3): # nao analise se chegar no final do tabuleiro
                x, y = prox(i, j) # calcula as posicoes do proximo elemento
                if tabuleiro[i][j] == tabuleiro[x][y] - 1: # ve se eh igual
                    continue
                else:
                    conta_fora_ordem += 1 # se nao for, soma
    return conta_fora_ordem

#3
dict_posicoes = {'1': [0,0], 
                 '2': [1,0], 
                 '3': [2,0], 
                 '4': [3,0], 
                 '5': [0,1], 
                 '6': [1,1], 
                 '7': [2,1], 
                 '8': [3,1],
                 '9': [0,2],
                 '10':[1,2],
                 '11':[2,2],
                 '12':[2,3],
                 '13':[0,3],
                 '14':[1,3],
                 '15':[2,3],
                 '0': [3,3]}

def distancia_manhattan(i_atual, j_atual, i_final, j_final):
    print('i_atual ' + str(i_atual) + ' j_atual ' + str(j_atual))
    print('i_final ' + str(i_final) + ' j_final ' + str(j_final))
    soma = 0
    soma = abs(i_atual - i_final)
    soma = soma + abs(j_atual - j_final)
    return soma

def heuristica3(tabuleiro):
    soma = 0
    for i in range(0, 4):
        for j in range(0,4):
            chave = str(tabuleiro[i][j]) #define a chave como o valor da posicao (i,j)
            x, y = dict_posicoes.get(chave) #pesquisa pela posicao correta desse valor
            if (x == i) and (y == j): #caso valor ja esteja na pos correta
                continue
            else: #somar distancia manhattan
                soma = soma + distancia_manhattan(i, j, x, y)
                print('soma ' + str(soma))
    return soma



##Main

def main():
    tabuleiro = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]] #inicializa matriz tabuleiro
    leEntrada(tabuleiro)
    res = heuristica3(tabuleiro)
    print(res)

main()