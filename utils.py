def exibir_menu():
    print("\n--- Sistema de Gerenciamento de Biblioteca ---")
    print("1. Cadastrar livro")
    print("2. Cadastrar usuário")
    print("3. Emprestar livro")
    print("4. Devolver livro")
    print("5. Consultar livros")
    print("6. Sair")
    return input("Escolha uma opção: ")

def ler_dados_livro():
    titulo = input("Título do livro: ")
    autor = input("Autor: ")
    ano = input("Ano de publicação: ")
    copias = int(input("Número de cópias disponíveis: "))
    return titulo, autor, ano, copias

def ler_dados_usuario():
    nome = input("Nome do usuário: ")
    identificacao = input("Identificação (CPF ou outro): ")
    contato = input("Contato: ")
    return nome, identificacao, contato
