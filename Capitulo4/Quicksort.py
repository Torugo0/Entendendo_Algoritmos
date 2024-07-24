# Um algoritmo que resolve apenas um tipo de problema não é muito util

# A estrategia dividir para conquistar (DC) é usada após descubrir o caso-base mais simples possivel.
    # -> É uma maneira de pensar sobre o problema.
    
def soma(lista):
    total = 0
    for x in lista:
        total += x
    return total

print(soma([1,2,3,4]))

# Usando recursão

def soma_recursao(arr):
    if arr == []:
        return 0
    return arr[0] + soma_recursao(arr[1:])

arr = [2,4,6]
print(soma_recursao(arr)) # LEMBRE-SE QUE CADA CHAMADA DA FUNÇÃO GERA UMA PILHA COM UM NOVO CONTEXTO 

def cont_lista(lista):
    if lista == []:
        return 0
    return 1 + cont_lista(lista[1 : ])

print(cont_lista([1,2,3,4,5]))

# Maior valor numa lista 

def maxima(lista):
    if len(lista) == 2:
        return lista[0] if lista[0] > lista[1] else lista[1]
    sub_max = maxima(lista[1:])
    return lista[0] if lista[0] > sub_max else sub_max

print(maxima([2,4,6,10,11]))