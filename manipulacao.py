def cadastrarjogador():
    nome = input("Digite seu nome:")
    pontuacao = input("digite sua pontuacao:")

    arquivo = open("jogadores.txt","a")
    arquivo.write(nome + "-" + pontuacao + "\n")
    arquivo.close()

    print("jogador salvo ")

def verRanking():
    arquivo = open("jogadores.txt", "r")
    linhas = arquivo.readlines()
    arquivo.close()

    print("=== RANKING ===")

    for linha in linhas:
        print(linha)

while True:
    print("1 - cadastrar jogador")
    print("2 - ver ranking")
    print("3 - sair")

    opcao = input("escolha uma opcao:")

    if opcao == "1":
        cadastrarjogador()
    elif opcao == "2":
        verRanking()
    elif opcao == "3":
        print("saindo do sistema.......")
        break
    else:
        print("opcao invalida!")