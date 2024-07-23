# Recursão é quando uma função chama a si mesma
# A recursão é usada para para tornar a resposta mais clara. Não há nenhum beneficio quanto ao desempenho ao utilizar recursão.

# CASO-BASE & CASO RECURSIVO
    # -> Caso-base é quando a função não chama a si mesma novamente, de forma que o programa não se torna um loop infinito.
    # -> Caso recursivo é quando uma função chama a si mesmo

# Quando escreve uma função recursiva é de extrema importância falara quando ela deve parar 

def regresiva(i):
    print(i)
    if i <= 1: # Caso-base
        return 
    else: # Recursão
        regresiva(i-1)
        
print(regresiva(10))

# A pilha de chamada (call stack)

def sauda(nome = "Vitor"):
    print(f"Hello, {nome}") # Função SAUDA
    sauda2(nome) # Sai da função sauda e entra na sauda2 adicionando sauda2 na pilha
    print("Preparando para dizer tchau") # Volta para a função sauda e retira a pilha/função sauda2
    tchau() # entra na pilha/função tchau adicionando ele na pilha
    # Retira a pilha tchau e volta a função inicial

def sauda2(nome):
    print(f"Como vai {nome} ?")

def tchau():
    print("OK, tchau !")

sauda() # Quando chamamos uma função a partir de outra, a chamada da função fica pausada em um estado parcialmente completo

# A pilha de chamada com recursão

def fat(x):
    if x == 1:
        return 1
    else: 
        return x * fat(x-1)
    
print(fat(3))