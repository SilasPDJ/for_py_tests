"""
  AO PREENCHER ESSE CABEÇALHO COM O MEU NOME E O MEU NÚMERO USP, 
  DECLARO QUE SOU O ÚNICO AUTOR E RESPONSÁVEL POR ESSE PROGRAMA. 
  TODAS AS PARTES ORIGINAIS DESSE EXERCÍCIO PROGRAMA (EP) FORAM 
  DESENVOLVIDAS E IMPLEMENTADAS POR MIM SEGUINDO AS INSTRUÇÕES
  DESSE EP E QUE PORTANTO NÃO CONSTITUEM DESONESTIDADE ACADÊMICA
  OU PLÁGIO.  
  DECLARO TAMBÉM QUE SOU RESPONSÁVEL POR TODAS AS CÓPIAS
  DESSE PROGRAMA E QUE EU NÃO DISTRIBUI OU FACILITEI A
  SUA DISTRIBUIÇÃO. ESTOU CIENTE QUE OS CASOS DE PLÁGIO E
  DESONESTIDADE ACADÊMICA SERÃO TRATADOS SEGUNDO OS CRITÉRIOS
  DIVULGADOS NA PÁGINA DA DISCIPLINA.
  ENTENDO QUE EPS SEM ASSINATURA NÃO SERÃO CORRIGIDOS E,
  AINDA ASSIM, PODERÃO SER PUNIDOS POR DESONESTIDADE ACADÊMICA.

  Nome :
  NUSP :
  Prof.:

  Referências: Com exceção das rotinas fornecidas no enunciado
  e em sala de aula, caso você tenha utilizado alguma referência,
  liste-as abaixo para que o seu programa não seja considerado
  plágio ou irregular.
"""

import random

MAX_TENTATIVAS = 6
NUM_LETRAS = 5


##### FUNÇÕES PRONTAS #####

def inicializa_teclado():
    '''
    Devolve a lista com as teclas na ordem.
    As letras que aparecem nos chutes e que não estão no teclado são substtuídas por ' '.
    '''

    teclado = [['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
               ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
               ['z', 'x', 'c', 'v', 'b', 'n', 'm']]
    return teclado


def imprime_teclado(teclado):
    ''' Exibe o teclado com as letras possiveis. '''
    print('-----------------------------------------')
    for linha in teclado:
        for letra in linha:
            print(letra, end=' ')
        print()
    print('-----------------------------------------')


##### FUNÇÕES OBRIGATÓRIAS #####


def cria_lista_palavras(nome_arquivo):
    ''' recebe uma string com o nome do arquivo e devolve uma lista
        contendo as palavras do arquivo'''
    arquivo = open(nome_arquivo, 'r')
    palavras = arquivo.read()
    lista = palavras.split('\n')
    lista = lista[:-1]
    return lista


def checa_tentativa(palavra, chute):
    feedback = [0] * len(palavra)
    palavra_restante = list(palavra)
    chute_restante = list(chute)
    if len(chute) > len(palavra):
        return feedback

    # Primeiro, marcar os acertos diretos (1)
    for i in range(len(chute)):
        if chute[i].lower() == palavra[i].lower():
            feedback[i] = 1
            # Remove a letra para evitar contagens duplas
            palavra_restante[i] = None
            chute_restante[i] = None

    # Depois, marcar os acertos indiretos (2)
    for i in range(len(chute)):
        # Apenas verifica as letras não acertadas diretamente
        if chute_restante[i] is not None:
            if chute_restante[i] in palavra_restante:
                feedback[i] = 2
                # Remove a letra da palavra_restante para evitar contagens duplas
                palavra_restante[palavra_restante.index(
                    chute_restante[i])] = None

    return feedback


def imprime_resultado(lista):
    ''' Recebe a lista de tentativas e imprime as tentativas,
      usando * para verde , + para amarelo e _ para letras que não aparecem na 
      palavra sorteada. A lista de tentativas tem formato 
      [[chute1, feedback1], [chute2, feedback2], …, [chuten,feedbackn]. 
      Esta funcao nao devolve valor. '''
    # fazer
    for tentativas in lista:
        chute, sinais = tentativas
        print(chute)
        resultado = ''
        for sinal in sinais:
            if sinal == 0:
                resultado += '_ '
            elif sinal == 1:
                resultado += '* '
            elif sinal == 2:
                resultado += '+ '
        print(resultado)
    pass  # remover isso


def atualiza_teclado(chute, feedback, teclado=None):
    ''' Modifica teclado para que as letras marcadas como inexistentes
         no chute sejam substituidas por espacos. Esta funcao nao devolve valor.'''
    if not teclado: return
    for e, letra in enumerate(chute):
        if feedback[e] == 0:
            for i in range(len(teclado)):
                if letra.lower() in teclado[i]:
                    index_letra = teclado[i].index(letra)
                    teclado[i][index_letra] = ' '

##### FUNÇÕES EXTRAS (caso existam) #####


def main():
    ' Implementa mecanismo principal do jogo. '
    # pede opção de lingua
    lingua = ''
    while lingua != 'P' and lingua != 'I':
        lingua = input(
            "Qual o idioma (I para inglês ou P para português)? ").upper()

    # carrega lista de palavras do arquivo correspondente
    if lingua == 'P':
        lista_palavras: list = cria_lista_palavras('palavras.txt')
    elif lingua == 'I':
        lista_palavras: list = cria_lista_palavras('words.txt')

    # sorteia uma palavra da lista"
    palavra = lista_palavras[random.randint(0, len(lista_palavras)-1)]

    num_tentativas = 0
    lista_tentativas = []
    ganhou = False
    teclado = inicializa_teclado()
    while num_tentativas < MAX_TENTATIVAS and not ganhou:
        imprime_teclado(teclado)

        # validação para não digitar mais de 5 letras
        chute_length = 999
        while chute_length > 5:
            chute = input('Tente adivinhar qual a palavra: ')
            chute_length = len(chute)

        lista_feedback = checa_tentativa(palavra, chute)

        atualiza_teclado(
            chute, lista_feedback, teclado)

        lista_tentativas.append([chute, lista_feedback.copy()])
        # contador de tentativas

        num_tentativas += 1
        imprime_resultado(lista_tentativas)
        if set(lista_feedback) == {1}:
            ganhou = True
            break

    print('-----------------------------------------')
    if ganhou:
        print("PARABÉNS! Com", num_tentativas, " você conseguiu ganhar!")
    else:
        print("Que pena... A palavra era", palavra, ".")


##### NÃO ALTERE O TRECHO ABAIXO #####
if __name__ == "__main__":
    main()
