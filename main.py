from biblioteca import Biblioteca
from utils import exibir_menu, ler_dados_livro, ler_dados_usuario

biblioteca = Biblioteca()

def executar():
    while True:
        opcao = exibir_menu()

        if opcao == '1':
            titulo, autor, ano, copias = ler_dados_livro()
            biblioteca.cadastrar_livro(titulo, autor, int(ano), copias)

        elif opcao == '2':
            nome, identificacao, contato = ler_dados_usuario()
            biblioteca.cadastrar_usuario(nome, identificacao, contato)

        elif opcao == '3':
            titulo_livro = input("Título do livro para empréstimo: ")
            identificacao_usuario = input("Identificação do usuário: ")
            biblioteca.emprestar_livro(titulo_livro, identificacao_usuario)

        elif opcao == '4':
            titulo_livro = input("Título do livro a devolver: ")
            identificacao_usuario = input("Identificação do usuário: ")
            biblioteca.devolver_livro(titulo_livro, identificacao_usuario)

        elif opcao == '5':
            print("\n--- Livros Cadastrados ---")
            for livro in biblioteca.livros:
                print(f"Título: {livro.titulo}, Autor: {livro.autor}, Ano: {livro.ano_publicacao}, Cópias Disponíveis: {livro.copias_disponiveis}")

        elif opcao == '6':
            print("Saindo...")
            break

        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    executar()
