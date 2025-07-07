#Atividade 1:
print('\n### Bem-vindo a loja da Maria Luiza Collaço Martins! ###\n')
valProduto = float(input('Entre com o valor do produto: ')) # variável que pega o valor unitário
qtdProduto = int(input('Entre com a quantidade do produto: ')) # variável que pega a quantidade de produtos

valTotal = valProduto * qtdProduto # calculando o valor total da compra

# Testa a primeira condição
if valTotal > 0 and valTotal < 2500: # Verifica se o valor total dos produtos é menor que 2500
    print('Valor inválido para desconto')
    print(f'O valor SEM desconto: R${valTotal}\n')

# Testa a segunda condição
elif valTotal >= 2500 and valTotal < 6000: # Verifica se o valor total dos produtos esta entre 2500 e 5999
    desconto = (valTotal *  4) / 100 # Calcula o desconto de 4%
    valDesconto = valTotal - desconto # Calcula o valor total com o desconto
    print(f'O valor SEM desconto: R${valTotal:.2f}')
    print(f'O valor COM desconto: R${valDesconto:.2f}\n')

# Testa a terceira condição
elif valTotal >= 6000 and valTotal < 10000: # Verifica se o valor total dos produtos esta entre 6000 e 9999
    desconto = (valTotal *  7) / 100 # Calcula o desconto de 7%
    valDesconto = valTotal - desconto # Calcula o valor total com o desconto
    print(f'O valor SEM desconto: R${valTotal:.2f}')
    print(f'O valor COM desconto: R${valDesconto:.2f}\n')

# Testa a quarta condição
elif valTotal >= 10000:
    desconto = (valTotal * 11) / 100 #Calcula o desconto de 11%
    valDesconto = valTotal - desconto # Calcula o valor total com o desconto
    print(f'O valor SEM desconto: R${valTotal:.2f}')
    print(f'O valor COM desconto: R${valDesconto:.2f}\n')

# Testa um valor inválido
else:
    print("\n### ERRO! ###")