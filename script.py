

codigoArrays = []
descricaoArrays = []
quantidadeArrays = []


estoqueAbaixodopermitido = 100

indice = 1
senhaVerificada = 'lucas'
senha = ''
totalSenha = 3
resultadoTotal = 0
salverSenha = False


def valorMenoIgualZero():
    if qt < 0:
        print("Não é permitdo cadastrar valores iguais ou menos que Zero")
def somaQuantidade():
    global qt
    soma = 0
    for qt in quantidadeArrays:
        soma += qt
    print(f'Quantidade de itens em estoque: {soma}')


def totalProdutos():
    global qt
    for qt in codigoArrays:
        codigoArrays.count(q)
    print("Total de produtos cadastrados é : ", q)


def minPermitido():
    countEstoque = 0
    for i in quantidadeArrays:
        if (i < estoqueAbaixodopermitido):
            countEstoque = countEstoque + 1

    print("Produtos com estoque abaixo do mínimo permitido (100 Unidades)", countEstoque)


def mensagemChance():
    print('SENHA INCORRETA , VOCE TEM MAIS ', limiteSenha, 'CHANCES')


def mensagemAcessoBloqueado():
    print('SEU ACESSO FOI BLOQUEADO! PROCURE O ADMINISTRADOR')


def mostraRelatorioCompleto():
    global lista_codigoOrdenada, lista_ordenadaDescricao, lista_ordenadaQuantidade, i, j, q
    lista_codigoOrdenada = sorted(codigoArrays)
    lista_ordenadaDescricao = sorted(descricaoArrays)
    lista_ordenadaQuantidade = sorted(quantidadeArrays)
    i = 0
    j = 0
    q = 0
    while (i < len(lista_codigoOrdenada)):
        while (j < len(lista_ordenadaDescricao)):
            while (q < len(lista_ordenadaQuantidade)):
                print(" ", codigoArrays[q], "     ", descricaoArrays[q], "         ", quantidadeArrays[q])
                print("\n")
                q = q + 1
            j = j + 1
        i = i + 1

def mostraRelatorioVenda():
    global lista_codigoOrdenada, lista_ordenadaDescricao, lista_ordenadaQuantidade, i, j, q
    lista_codigoOrdenada = sorted(codigoArrays)
    lista_ordenadaDescricao = sorted(descricaoArrays)
    lista_ordenadaQuantidade = sorted(quantidadeArrays)
    i = 0
    j = 0
    q = 0
    while (i < len(lista_codigoOrdenada)):
        while (j < len(lista_ordenadaDescricao)):
            while (q < len(lista_ordenadaQuantidade)):
                print(" ", codigoArrays[q], "     ", descricaoArrays[q], "         ", quantidadeArrays[q])
                print("\n")
                q = q + 1
            j = j + 1
        i = i + 1

def cabecalhoRelatorioVenda():
    print("\nDESCRIÇÃO QUANTIDADE EM ESTOQUE: ")

while True:
    print("\n")
    print("|———-  Menu de opções ——-—|  ")
    print("1 - Cadastrar Produto ")
    print("2 - Alterar Produto ")
    print("3 - Excluir Produto ")
    print("4 - Listar Produtos ")
    print("5 - Comprar produto")
    print("6 - Vender produto")
    print("7 - Sair")

    opcao = int(input("\nDigite a opcao desejada\n>>"))

    if opcao == 1:
        # Indice comeca no. 1
        while indice > 0:

            codigo = int(input('Digite um codigo: '))
            if codigo not in codigoArrays:
                codigoArrays.insert(indice, codigo)
            else:
                print("\n CODIGO DUPLICADO NO SISTEMA !!!")
                break
            if codigo <= 0:
                print("QUANTIDADE NAO PODE SER <= 0 - TENTE NOVAMENTE")
                break

            descricao = str(input('Descricao do produto: '))
            descricaoArrays.insert(indice, descricao)

            quantidade = int(input('Quantidade do produto: '))
            if quantidade <= 0:
                print("QUANTIDADE NAO PODE SER <= 0 - TENTE NOVAMENTE")
            else:
                quantidadeArrays.insert(indice, quantidade)

            print('Produto Cadastrado')

            r = str(input('Deseja Continuar ? [S/N]')).upper().strip()[0]
            if ("S" in r):
                indice = indice + 1
                # Indice passa valer 2
            else:
                break

    elif opcao == 2:
        print('================ Alteracao do Produto ================')
        countSenha = 0
        if (countSenha <= 2):
            while (countSenha <= 2):
                if (salverSenha == False):
                    senha = input('Digite a senha de acesso : ')
                if (senha == senhaVerificada or salverSenha == True):
                    codigoAlterado = int(input('Digite o codigo do produto a ser alterado : '))
                    if codigoAlterado not in codigoArrays:
                        print("\n PRODUTO NÃO CADASTRADO.")
                        break
                        if quantidade <= 0:
                            print("QUANTIDADE NAO PODE SER <= 0 - TENTE NOVAMENTE")
                            break
                    if (codigoAlterado in codigoArrays):

                        salverSenha = True

                        lista_codigoOrdenada = sorted(codigoArrays)
                        lista_ordenadaDescricao = sorted(descricaoArrays)
                        lista_ordenadaQuantidade = sorted(quantidadeArrays)

                        codigoAlterado = codigoAlterado - 1

                        descricao = str(input('Descricao do produto: '))
                        descricaoArrays[codigoAlterado] = descricao

                        quantidade = int(input('Quantidade do produto: '))
                        quantidadeArrays[codigoAlterado] = quantidade

                        if quantidade <= 0:
                            print("QUANTIDADE NAO PODE SER <= 0 - TENTE NOVAMENTE")
                            break

                        print('Produto alterado')
                        break
                    else:
                        print('Produto nao Cadastrado')

                else:
                    countSenha = countSenha + 1
                    limiteSenha = totalSenha = totalSenha - 1
                    mensagemChance()
            else:
                mensagemAcessoBloqueado()

    elif opcao == 3:
        countSenha = 0
        if (countSenha <= 2):
            while (countSenha <= 2):
                if (salverSenha == False):
                    senha = input('Digite a senha de acesso : ')
                if (senha == senhaVerificada or salverSenha == True):
                    codigoAlterado = int(input("Digite o codigo do produto a ser excluido : "))
                    if (codigoAlterado in codigoArrays):

                        salverSenha = True
                        codigoAlterado = codigoAlterado - 1

                        lista_codigoOrdenada = sorted(codigoArrays)
                        lista_ordenadaDescricao = sorted(descricaoArrays)
                        lista_ordenadaQuantidade = sorted(quantidadeArrays)

                        i = 0
                        j = 0
                        q = 0

                        while (i < len(lista_codigoOrdenada)):
                            while (j < len(lista_ordenadaDescricao)):
                                while (q < len(lista_ordenadaQuantidade)):
                                    print(descricaoArrays[q], quantidadeArrays[q], end='' '\n')
                                    q = q + 1
                                j = j + 1
                            i = i + 1

                        excluirProd = str(input('DESEJA EXCLUIR O PRODUTO ? - [S/N]')).upper()

                        if ('S' in excluirProd):
                            del (codigoArrays[codigoAlterado])
                            del (descricaoArrays[codigoAlterado])
                            del (quantidadeArrays[codigoAlterado])
                            print('Produto excluido com Sucesso!!!')

                        else:
                            print('PRODUTO NÃO EXCLUÍDO')
                            continue
                    else:
                        print('Produto nao encontrado')
                        break
                else:
                    countSenha = countSenha + 1
                    limiteSenha = totalSenha = totalSenha - 1
                    print('SENHA INCORRETA , VOCE TEM MAIS ', limiteSenha)
            else:
                print('SEU ACESSO FOI BLOQUEADO! PROCURE O ADMINISTRADOR')
                quit()

    elif opcao == 4:
        print("\nCÓDIGO DESCRIÇÃO QUANTIDADE EM ESTOQUE: ")
        print("-----------------------------------------")

        lista_codigoOrdenada = sorted(codigoArrays)
        lista_ordenadaDescricao = sorted(descricaoArrays)
        lista_ordenadaQuantidade = sorted(quantidadeArrays)

        i = 0
        j = 0
        q = 0

        while (i < len(lista_codigoOrdenada)):
            while (j < len(lista_ordenadaDescricao)):
                while (q < len(lista_ordenadaQuantidade)):
                    print(" ", codigoArrays[q], "     ", descricaoArrays[q], "         ", quantidadeArrays[q])
                    print("\n")
                    q = q + 1
                j = j + 1
            i = i + 1

        totalProdutos()
        somaQuantidade()
        minPermitido()
        print("\n")

    elif opcao == 5:
        print('================ COMPRA PRODUTO ================')
        codigoAlterado = int(input('Digite o codigo do produto que deseja Comprar: '))
        if codigoAlterado not in codigoArrays:
            print("\n PRODUTO NÃO CADASTRADO.")
            continue
        cabecalhoRelatorioVenda()
        print("-----------------------------------------")

        lista_codigoOrdenada = sorted(codigoArrays)
        lista_ordenadaDescricao = sorted(descricaoArrays)
        lista_ordenadaQuantidade = sorted(quantidadeArrays)

        i = 0
        j = 0
        q = 0

        while (i < len(lista_codigoOrdenada)):
            while (j < len(lista_ordenadaDescricao)):
                while (q < len(lista_ordenadaQuantidade)):
                    print(descricaoArrays[q], "      ", quantidadeArrays[q])
                    q = q + 1
                j = j + 1
            i = i + 1

            qt = int(input('Digite a quantidade que deseja comprar:  '))
            if qt <= 0:
                print(("***ERRO*** "))
                print("QUANTIDADE DE PRODUTO NAO PODE SER MENOR OU IGUAL ZERO")
                break
            codigoAlterado = codigoAlterado - 1
            ultimaQuantidade = quantidadeArrays[codigoAlterado] + qt
            quantidadeArrays[codigoAlterado] = ultimaQuantidade

            print("Quantidade Atualizada de itens do Produto: ", ultimaQuantidade)
            break

    elif opcao == 6:
        print('================ COMPRA VENDER ================')
        codigoAlterado = int(input('Digite o codigo do produto que deseja Vender: '))
        if codigoAlterado not in codigoArrays:
            print("\n PRODUTO NÃO CADASTRADO.")
            continue
        cabecalhoRelatorioVenda()
        print("-----------------------------------------")

        lista_codigoOrdenada = sorted(codigoArrays)
        lista_ordenadaDescricao = sorted(descricaoArrays)
        lista_ordenadaQuantidade = sorted(quantidadeArrays)

        i = 0
        j = 0
        q = 0

        while (i < len(lista_codigoOrdenada)):
            while (j < len(lista_ordenadaDescricao)):
                while (q < len(lista_ordenadaQuantidade)):
                    print(descricaoArrays[q], "      ", quantidadeArrays[q])
                    q = q + 1
                j = j + 1
            i = i + 1

            qt = int(input('Digite a quantidade que deseja Vender:  '))
            if qt <= 0:
                print(("***ERRO*** "))
                print("QUANTIDADE DE PRODUTO NAO PODE SER MENOR OU IGUAL ZERO")
                break
            codigoAlterado = codigoAlterado - 1
            ultimaQuantidade = quantidadeArrays[codigoAlterado] - qt
            quantidadeArrays[codigoAlterado] = ultimaQuantidade

            print("Quantidade Atualizada de itens do Produto: ", ultimaQuantidade)
            break

    elif opcao == 7:
        print("Programa Finalizado!")
        quit()
        break
    else:
        print("Opção inválida")