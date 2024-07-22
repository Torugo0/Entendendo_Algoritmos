# Array = significa que todas as suas tarefas estão armazenadas uma ao lado da outra na memoria (Sabemos os endereços do array)

# Lista encadeada = Seus itens podem estar em qualquer lugar da memoria (Pelos elementos não estarem proximos um dos outros não sabemos a posição especifica)
    # -> Listas encadeadas tem leitura lenta(O(n)), inserção rapida (O(1)).
    
# Sequencial -> Necessario ler todos os elementos para chegar a um determinado (ler nove elementos se quiser o decimo)
# Aleatório -> Acessa o item de forma aleatoria, onde o item estiver

# O codigo de ordenação por seleção, é bom mas não muito rapido. // O QuickSort é um algoritmo de seleção mais rapido, com tempo de execução O(n log n)

def buscaMenor(arr):
    menor = arr[0]
    menor_indice = 0
    for i in range (1, len(arr)): # Começa do 1 pois o menor já esta definido por 0
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
    return menor_indice

def ordenacaoporSelecao(arr):
    novoArr = []
    for i in range (len(arr)):
        menor = buscaMenor(arr)
        novoArr.append(arr.pop(menor)) # POP exclui/pega pelo indice
    return novoArr

print (ordenacaoporSelecao([5,3,6,2,10]))

# Anotações para entendimento do POP // O pop remove pelo indice e retorna o elemento removido
array = [1,2,3,4,5]
exem = array.pop(1)
newarr = []
newarr.append(exem)
print(newarr)