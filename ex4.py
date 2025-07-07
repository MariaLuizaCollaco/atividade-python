print('\nBem-vindo a livraria de Maria Luiza Martins\n')#imprimindo a saudação do programa

lista_livro = []#Criando uma lista vazia
id_global = 0#Criando a id global se setando ela pra 0

def cadastrar_livro(id):#Definindo função para cadastrar livros
    print('\nPrencha os campos>>\n')
    print(f'ID do livro: {id}\n') #Exibe a ID do livro a ser cadastrado
    nomeLivro = input('Por favor entre como nome do livro: ')#Usuário entra com os dados (nome, autor e editora)
    nomeAutor = input('Por favor entre como nome do autor: ')#                      ||                   
    nomeEditora = input('Por favor entre como nome da editora: ')#                  ||

    livro = {#Dicionário para armazenar os dados fornecidos pelo usuário
        'id': id,#chave e valor
        'nome': nomeLivro,#chave e valor
        'autor': nomeAutor,#chave e valor
        'editora': nomeEditora#chave e valor
    }

    lista_livro.append(livro)#Adicionado as informaçãoes do dicionário sempre para o final da lista (lista_livro)
    print("\nLivro cadastrado com sucesso!")

def consultar_livro():#Definindo uma função para consultar os livros de 3 diferentes maneiras a escolha do usuário
    while True:#Inicia o loop
        print('\nEscolha uma opção:')
        print('1 - Consultar todos')
        print('2 - Consultar por ID')
        print('3 - Consultar por autor')
        print('4 - Retornar ao menu\n')

        opcao = input('Digite o número da opção desejada: ')#Leitura da opção escolhida pelo usuário

        #Verificação condicional do opção escolhida pela usuário
        if opcao == '1':
            print('\n### MOSTRANDO TODOS OS LIVROS! ###')
            for livro in lista_livro:#Percorre todos os itens da lista (lista_livros) sem critério exibindo todos
                print(f"ID: {livro['id']}, Nome: {livro['nome']}, Autor: {livro['autor']}, Editora: {livro['editora']}")#Exibe todas as informações
        elif opcao == '2':
            print('\n### PESQUISANDO POR ID! ###')
            pesquisa = int(input('\nDigite o ID: '))#Leitura do ID desejado pelo usuário
            encontrado = False#Definindo uma váriavel do tipo boleana para falsa
            for livro in lista_livro:#Percorre todos os itens da lista (lista_livros)
                if livro['id'] == pesquisa:#Verifica e exibe somente os itens que corresponde ao valor pesquisado (ID)
                    print(f"ID: {livro['id']}, Nome: {livro['nome']}, Autor: {livro['autor']}, Editora: {livro['editora']}")
                    encontrado = True
                    break
            if not encontrado:
                print('\n### ID incorreto ou inexistente! ###')#Erro se ID digitado não for encontrado
        elif opcao == '3':
            print('\n### PESQUISANDO POR AUTOR! ###')
            pesquisa = input('\nDigite o nome do autor: ')#Leitura do ID desejado pelo usuário
            encontrado = False#Definindo uma váriavel do tipo boleana para falsa
            for livro in lista_livro:#Percorre todos os itens da lista (lista_livros)
                if livro['autor'] == pesquisa:#Verifica e exibe somente os itens que corresponde ao valor pesquisado (Autor)
                    print(f"ID: {livro['id']}, Nome: {livro['nome']}, Autor: {livro['autor']}, Editora: {livro['editora']}")
                    encontrado = True
            if not encontrado:
                print('\n### Autor não encontrado ou inexistente! ###')#Erro se autor digitado não for encontrado
        elif opcao == '4':
            print('\nRetornando ao menu...')#Opção para retornar ao menu principal
            break
        else:
            print('\nOpção selecionada é inválida')#Opção selecionada não configurada

def remover_livros():#Definindo função para fazer exclusão de livros a escolha do usuário
    while True:#Inicia o loop
        try:#Uso do try para verificar erro no tipo de valor inserido pelo usuário. Solicitado = int(valor inteiro) Possível errro se: Entrada = char
            id_remover = int(input('\nDigite o ID do livro que deseja remover: '))#usuário seleciona pelo ID o livro que deseja excluir
            for livro in lista_livro:#Percorre todos os itens da lista (lista_livros)
                if livro['id'] == id_remover:#Verifica e exibe somente o item que corresponde a ID inserida
                    lista_livro.remove(livro)#Remove o item
                    print('\n### Livro removido com sucesso! ###')
                    return#Retorna a lista agora modificada
            print ('### ID incorreto ou inexistente! ###')
        except ValueError:#Erro para o caso de o id_remover receber um valor diferente de int
            print('### Digite um número válido! ###')

while True:#inicia o loop
    print('\nEscolha uma opção:')
    print('1 - Cadastrar livro')
    print('2 - Consultar livro')
    print('3 - Remover livro')
    print('4 - Encerrar programa\n')

    opcao_menu = input('Digite a escolha desejada: ')#Escolhe a opção desejada no menu principal

    if opcao_menu == '1':
        id_global += 1#Faz a atribuição da ID para os livros sem repetir
        cadastrar_livro(id_global)#chama as funções e executa seus blocos de comandos
    elif opcao_menu == '2':
        consultar_livro()#chama as funções e executa seus blocos de comandos
    elif opcao_menu == '3':
        remover_livros()#chama as funções e executa seus blocos de comandos
    elif opcao_menu == '4':
        print('\nEncerrando o programa! Até logo...')
        break
    else:
        print('### Opção selecionada inválida! ###\n')