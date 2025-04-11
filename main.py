'''
GRUPO:
- Mateus de Sousa Arruda;
- Renan Demétrio Santos Vital;
- Samuel de Sousa Costa Pedrosa;
- Luiz Felipe Guimarães Azevedo Silva.
'''

from operacoesbd import *
from metodos import *
conn = criarConexao('127.0.0.1', 'root', '12345678', 'ouvidoriabd') 


print( "Bem vindo a ouvidoria da universidade!")
while True:

    print( "\n 1) Listagem das Manifestações \n 2) Listagem de Manifestações por Tipo \n 3) Criar uma nova Manifestação \n 4) Exibir quantidade de manifestações \n 5) Pesquisar uma manifestação por código \n 6) Excluir uma Manifestação pelo Código \n 7) Sair do Sistema.\n")
    opcao = (input("Selecione uma das opções:\n"))
    try:
        opcao = int(opcao)
    except ValueError:
        print("Codigo informado é inválido.")
        continue

    #Listagem das Manifestações
    if opcao == 1:
        lista = listarManifestacoes(conn)
        if len(lista) == 0 :
            print("Não há nenhuma manifestação cadastrada no sistema.")
        else:
            print("Essas são todas as manifestações cadastradas até o momento:\n")
            for i in range(len(lista)):
                print(f"[{lista[i][0]}] ({lista[i][4]}) {lista[i][2]} → {lista[i][3]}: {lista[i][1]}")      

    #Listagem de Manifestações por Tipo
    elif opcao == 2:
        tipo = int(input("Escolha o tipo de manifestação que você deseja filtrar, 1 para reclamação, 2 para sugestão e 3 para elogio: "))
        tipoFiltrado = filtrarTipo(tipo)

        if tipoFiltrado == None:
            print("Opção inválida! Por favor, escolha 1, 2 ou 3.")
            continue
        
        listaFiltrada = listarManifestacoesPorTipo(conn, tipoFiltrado)
        if len(listaFiltrada) == 0:
            print("Não temos nenhuma manifestação desse tipo cadastrada no sistema")
        else:
            print(f"\nLista de manifestações do tipo '{tipoFiltrado}':\n")
            for item in listaFiltrada:
                print(f"[{item[0]}] {item[2]} → {item[3]}: {item[1]}")

    #Criar uma nova Manifestação
    elif opcao == 3:
        descricao = input("Digite a manifestação: ")
        autor = input("Digite o seu nome: ")
        ouvidor = input("Digite o nome do ouvidor: ")
        tipo = int(input("Escolha o tipo de manifestação, 1 para reclamação, 2 para sugestão e 3 para elogio: "))
        tipoFiltrado = filtrarTipo(tipo)

        if tipoFiltrado == None:
            print("Opção inválida! Por favor, escolha 1, 2 ou 3.")
            continue


        resultadoCadastro = criarNovaManifestacao(conn,descricao, autor, ouvidor, tipoFiltrado)

        if resultadoCadastro == None:
            print("Erro ao cadastar nova manifestação, tente novamente.")
        else:
            print("Manifestação cadastrada com sucesso e o seu código é", resultadoCadastro)

    #Exibir quantidade de manifestações
    elif opcao == 4:
        quantidadeManifestacoes = exibirQuantidadeManifestacoes(conn)
        if quantidadeManifestacoes == 0:
            print("Não há manifestações cadastrada.")
        
        else:
            print("Até o momento, o sistema possui exatas",quantidadeManifestacoes , "manifestações")

    #Pesquisar uma manifestação por código
    elif opcao == 5:
        codigo = int(input("Digite o código da manifestação:"))
        resultado = pesquisarManifestacaoPorCodigo(conn, codigo)
        if len(resultado) == 0:
            print("Não há manifestações cadastrada com este código.")

        else:
            print("A manifestação cadastrada com este código é:")
            print(f"[{resultado[0][0]}] ({resultado[0][4]}) {resultado[0][2]} → {resultado[0][3]}: {resultado[0][1]}")
        
    #Excluir uma Manifestação pelo Código    
    elif opcao == 6:
        codigo = int(input("Digite o código da manifestação que voce deseja excluir: "))
        resultadoExclusao = excluirManifestacao(conn, codigo)
        if resultadoExclusao == 0:
            print("Nenhuma manifestação cadastrada no sistema com este código.")

        else:
            print("Manifestação excluida com sucesso!")

    elif opcao == 7:
        print("Obrigado por ultilizar o nosso sistema de ouvidoria! Até breve.")
        break
    else:
        print("Codigo informado é inválido.")


encerrarConexao(conn)
        
        