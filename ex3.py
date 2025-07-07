def saudacao():#Definindo função para exibir texto de saudação
    print('\nBem-vindo a impressora Maria Luiza Collaço Martins\n')

def escolha_servico():#Definindo função para realizar a escolha do serviço desejado

    servicos = { #Declarando um dicionário com o tipo de serviço(chave) e preço(valor)
        'DIG': 1.10,
        'ICO': 1.00,
        'IPB': 0.40,
        'FOT': 0.20
    }

    while True:#Inicilizando looping
        print('Escolha o tipo de serviço desejado:')
        print('DIG - Digitalização')
        print('ICO - Impressão Colorida')
        print('IPB - Impressão Preto e Branco')
        print('FOT - Fotocópia')
        servico = input('\nDigite o código do serviço: ').upper()#Entrada de dados com a adição do .upper para evitar erro por maisculas ou minusculas
        if servico in servicos:#Verifica se o serviço desejado (variável servico) está presente no dicionário servicos
            return servico, servicos[servico]  # Retornando código e valor
        else:
            print('\nServiço selecionado é inválido\n')

def num_paginas():#Definindo a função que calcula a % do desconto baseado no numeros de páginas
    while True:#Inicializa o Loop
        try:#Uso do try para verificar erro no tipo de valor inserido pelo usuário. Solicitado = int(valor inteiro) Possível errro se: Entrada = char
            paginas = int(input("\nDigite o número de páginas: "))
            
            #Verificação do desconto de acordo com a quantidade de páginas
            if paginas >= 20000:
                print("\nErro: número de páginas muito grande! Tente novamente.") 
                continue
            elif paginas < 20:
                return paginas
            elif paginas >= 20 and paginas < 200:
                return paginas * 0.85
            elif paginas >= 200 and paginas < 2000:
                return paginas * 0.80
            elif paginas >= 2000 and paginas < 20000: 
                return paginas * 0.75
        except ValueError:
            print("Por favor, digite um número inteiro válido.")


def servico_extra():#Definindo função para exibir um possível serviço extra
    while True:#Inicialização do loop
        print('\nDeseja encadernar?')
        print('0 - Não quero')
        print('1 - Encadernação simples (R$ 15,00)')
        print('2 - Encadernação capa dura (R$ 40,00)')
        opcao = input('Selecione a opção que deseja: ')
        #verificação para saber se vai haver ou não algum serviço extra para ser somado no valor total
        if opcao == '0':
            return 0
        elif opcao == '1':
            return 15
        elif opcao == '2':
            return 40
        else:
            print('Opção inválida')

saudacao()#Impressão o texto de saudação através da função

#Atribuido funções a variáveis e imprimindo essas funções
servico, valor_por_pagina = escolha_servico()
pagina = num_paginas()
valor_servico_extra = servico_extra()

#Calculo total do serviço p/ pagiga + desconto(se houver) e + serviço extra(se houver)
total_valor_paginas = (valor_por_pagina * pagina) + valor_servico_extra

print(f'\nTotal do pedido: R$ {total_valor_paginas:.2f} (Serviço: {valor_por_pagina} * paginas: {pagina} + extra: {valor_servico_extra})')
