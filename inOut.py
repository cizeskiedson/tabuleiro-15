# @author -> Edson Cizeski ra107514
# Inicio da implementacao do A*
# Programa le uma entrada e retorna uma saida



def leEntrada(tabuleiro):
    #comeca a ler os dados passados por input
    string = input('Digite os valores do jogo: \n') #le uma string com os numeros  
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

def escreveSaida(tabuleiro):
    print('========= Tabuleiro final ==========')
    for linha in tabuleiro:
        for num in linha:
            print(f'{num:>4}', end=" ")
        print()
    print('====================================')

def main():
    tabuleiro = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]  #representa as 4 linhas do tabuleiro (16 casas)
    leEntrada(tabuleiro)
    print(tabuleiro)
    escreveSaida(tabuleiro)


main()