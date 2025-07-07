print('### Bem vindo(a) a loja de Maria Luiza Collaço Martins ###')
print('----------------------------------------------------------')
print('-------------------------Cardápio-------------------------')
print('----------------------------------------------------------')
print('-------|  Tamanho  |  Cupuaçu (CP)  |  Açaí (AC)  |-------')
print('-------|     P     |    R$  9.00    |  R$ 11.00   |-------')
print('-------|     M     |    R$ 14.00    |  R$ 16.00   |-------')
print('-------|     G     |    R$ 18.00    |  R$ 20.00   |-------')
print('----------------------------------------------------------')
print('----------------------------------------------------------')
print('----------------------------------------------------------')

total = 0 #Definindo variavel de soma total da compra pra 0

#Iniciando loop para realização do pedido e testes condicionais
while True:
    #Adição de .upper() pra evitar erro no programa se o usuario entrar com o sabor em minusculo
    sabor = input('Qual seria o SABOR desejado? (CP ou AC): ').upper() 

    #Verificação do sabor
    if sabor == 'CP' or sabor == 'AC':
        pass #Pass passa pra próxima parte do código
    else:
        print('### SABOR desejado inválido! ###')
        continue #Continue faz com que o loop reinicie (Erro na escolha do sabor
    
    #if sabor != 'CP' and sabor != 'AC':
    #    print('### SABOR desejado inválido! ###')
    #    print('Tente novamente!')
    #    continue

    #Adição de .upper() pra evitar erro no programa se o usuario entrar com o sabor em minusculo
    tamanho = input('Qual seria o TAMANHO desejado? (P/M/G): ').upper()

    #Verificação do tamanho
    if tamanho == 'P' or tamanho == 'M' or tamanho == 'G':
        pass
    else:
        print('### TAMANHO desejado inválido! ###')
        continue
    #if tamanho != 'P' and tamanho != 'M' and tamanho != 'G':
    #    print('### TAMANHO desejado inválido! ###')
    #    print('Tente novamente!')
    #    continue
    
    if sabor == 'CP':
        if tamanho == 'P':
            preco = 9.00
        elif tamanho == 'M':
            preco = 14.00
        else:
            preco = 18.00
    elif sabor == 'AC':
        if tamanho == 'P':
            preco = 11.00
        elif tamanho == 'M':
            preco = 16.00
        else:
            preco = 20.00

    
    total += preco
    print(f'Produto adicionado, subtotal do pedido: R${total:.2f}')

    pedidoExtra = input('Deseja pedir mais alguma coisa? (S/N): ').upper()

    if pedidoExtra == 'S':
        continue
    else:
        break

print(f'Valor total do pedido: R${total:.2f}')

#print(f'Você pediu um {sabor} tamanho {tamanho}, total ficou: {total}')
#print(f'Seu pedido foi: {sabor} tamanho: {tamanho}')
