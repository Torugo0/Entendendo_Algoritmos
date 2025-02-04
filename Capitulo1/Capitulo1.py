# Algoritmo = é um conjunto de instruções que realizam uma tarefa

#PESQUISA BINÁRIA 
    # Lista ordenada

# Pesquisa simples é feito em ordem (ou pesquisa estúpida)

# No código abaixo eu passo o item para a função e ele tenta adivinhar. Sendo assim, o "chute" é dele.
def pesquisa_binaria(lista, item): # Página 27
    baixo = 0
    alto = len(lista) - 1
    
    while baixo <= alto:
        meio = int((baixo + alto) / 2) # Posição [i], não o valor.
        chute = lista[meio] # armazena o valor
        
        if chute == item:
            return meio
        
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
    return None
    
    
minha_lista = [1, 3, 5, 7, 9]

print(pesquisa_binaria(minha_lista, 3))
print(pesquisa_binaria(minha_lista, -1))

# Tempo de execução

#Tempo linear = Se uma lista tem 100 itens, vai ser necessário 100 tentativas para achar algo (supondo que esteja no fim), 4 bilhões itens, 4 bilhões de tentativas. E assim por diante. (0(n))

# Tempo logarítmico = se uma tabela tem 100 itens, ela precisa de no máximo 7 tentativas. 4 bilhões, 32 tentativas (0(log N))

# A notação Big O conta o número de operações, uma lista simples de 100 elementos faz 100 operações de verificação por exemplo. 
# Pesquisa simples = O(n) // Pesquisa binária = O(log N)
# Pesquisa simples nunca terá tempo de execução mais lento do que O(n)

#A rapidez de um algoritmo não é medida em segundos, mas pelo crescimento do número de operações  

# EXERCICIO 1.6 - VOLTAR DEPOIS PARA ENTENDER

# O problema do caixeiro-viajante se resume a um tempo fatorial(O(n!)), ele consome muitas operações, mas para casos envolvendo números pequenos "pode" ser uma opção. 
    # - Mas a partir do momento que lidamos com mais de 100 cidades é impossivel calcular a resposta em função do tempo.
    # - (100! = 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000 )
    
# RECAPITULAÇÃO DO CAPITULO.
    
    # - A pesquisa binária é muito mais rapida do que uma pesquisa simples
    # - O(Log n)(pesquisa binária) é mais rápido do que O(n)(pesquisa simples), e o O(log n) fica ainda mais rápido conforme os elementos da lista aumentam.
    # - A rapidez de um algoritmo não é medida em segundos, e sim por meio do seu crescimento.
    # - O tempo de execução dos algoritmos é expresso na notação big O.