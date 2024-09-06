biblioteca = []
emprestimos = {}


def adicionar_livro(titulo, autor, copias):
    novo_livro = {"titulo": titulo, "autor": autor, "copias": copias}
    biblioteca.append(novo_livro)
    print("Livro adicionado com sucesso!")




def emprestar_livro(titulo, usuario):
    for livro in biblioteca:
        if livro['titulo'] == titulo:
            if livro['copias'] > 0:
                livro['copias'] -= 1
                if usuario not in emprestimos:
                    emprestimos[usuario] = [titulo]
                else:
                    emprestimos[usuario].append(titulo)
                print(f"Livro '{titulo}' emprestado com sucesso.")
                return
            else:
                print(f"Não há cópias disponíveis do livro '{titulo}'.")
                return
    print(f"Livro '{titulo}' não encontrado.")


def devolver_livro(titulo, usuario):
    for livro in biblioteca:
        if livro['titulo'] == titulo:
            livro['copias'] += 1
            emprestimos[usuario].remove(titulo)
            if not emprestimos[usuario]:
                del emprestimos[usuario]
            print(f"Livro '{titulo}' devolvido com sucesso.")
            return
    print(f"Livro '{titulo}' não encontrado.")


def verificar_disponibilidade(titulo):
    for livro in biblioteca:
        if livro['titulo'] == titulo:
            print(f"O livro '{titulo}' tem {livro['copias']} cópias disponíveis.")
            return
    print(f"Livro '{titulo}' não encontrado.")


def listar_livros_emprestados(usuario):
    if usuario in emprestimos:
        print(f"Livros emprestados por {usuario}:")
        for livro in emprestimos[usuario]:
            print(f"- {livro}")
    else:
        print(f"O usuário {usuario} não possui livros emprestados.")


def menu():
    opcao = 0
    while opcao != 7:
        print("\n--- Gerenciador de Livros ---")
        print("1. Adicionar livro")
        print("2. Listar livros")
        print("3. Emprestar livro")
        print("4. Devolver livro")
        print("5. Verificar disponibilidade")
        print("6. Listar livros emprestados por usuário")
        print("7. Encerrar programa.")
        opcao = input("Escolha uma opção: ")


        if opcao == '1':
            titulo = input("Título: ")
            autor = input("Autor: ")
            copias = int(input("Número de cópias: "))
            adicionar_livro(titulo, autor, copias)
        elif opcao == '2':
            listar_livros()
        elif opcao == '3':
            titulo = input("Digite o nome do livro:  ")
            usuario = input("Digite seu nome:  ")
            emprestar_livro(titulo, usuario)
        elif opcao == '4':
            titulo = input("Digite o nome do livro:  ")
            usuario = input("Digite seu nome:  ")
            devolver_livro(titulo, usuario)
        elif opcao == '5':
            titulo = input("Digite o nome do livro:  ")
            verificar_disponibilidade(titulo)
        elif opcao == '6':
            usuario = input("Digite seu nome:  ")
            listar_livros_emprestados(usuario)
        elif opcao == '7':
            print("Encerrando")
        else:
            print("Opção inválida.")




menu()
