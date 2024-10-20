from modelos import Livro, Usuario, Emprestimo
from exceptions import *


class Biblioteca:
    def __init__(self):
        self.livros = [] # armazena todos os livros cadastrados na biblioteca.
        self.usuarios = [] # armazena os usuários cadastrados.
        self.emprestimos = [] # armazena as informações sobre os empréstimos feitos.

# permite inserir informações sobre o livro, como título, autor,
#  ano de publicação e número de cópias disponíveis.
    def cadastrar_livro(self, titulo, autor, ano_publicacao, copias):
        novo_livro = Livro(titulo, autor, ano_publicacao, copias)
        self.livros.append(novo_livro)

# cadastra informações do usuário como nome, número de identificação e contato.
    def cadastrar_usuario(self, nome, identificacao, contato):
        novo_usuario = Usuario(nome, identificacao, contato)
        self.usuarios.append(novo_usuario)

# Retorna o objeto do livro se ele for encontrado, caso contrário, lança um erro
    def buscar_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                return livro
        raise LivroNaoEncontradoError("Livro não encontrado.")

# Retorna o objeto do usuário se ele for encontrado, caso contrário, lança um erro
    def buscar_usuario(self, identificacao):
        for usuario in self.usuarios:
            if usuario.identificacao == identificacao:
                return usuario
        raise UsuarioNaoEncontradoError("Usuário não encontrado.")

# Realiza o empréstimo de um livro, Verifica se o livro tem cópias disponíveis antes de
#  confirmar o empréstimo (Se não, gera erro) e 
# Se o empréstimo for bem-sucedido, diminui o número de cópias disponíveis 
# e registra o empréstimo.
    def emprestar_livro(self, titulo_livro, identificacao_usuario):
        livro = self.buscar_livro(titulo_livro)
        usuario = self.buscar_usuario(identificacao_usuario)

        try:
            livro.emprestar()
            novo_emprestimo = Emprestimo(usuario, livro)
            self.emprestimos.append(novo_emprestimo)
            print(f"Empréstimo do livro '{livro.titulo}' realizado com sucesso para {usuario.nome}.")
        except LivroIndisponivelError:
            print(f"Livro '{titulo_livro}' indisponível para empréstimo.")

    def devolver_livro(self, titulo_livro, identificacao_usuario):
        for emprestimo in self.emprestimos:
            if emprestimo.livro.titulo == titulo_livro and emprestimo.usuario.identificacao == identificacao_usuario and emprestimo.ativo:
                emprestimo.finalizar_emprestimo()
                emprestimo.livro.devolver()
                print(f"Livro '{titulo_livro}' devolvido com sucesso por {emprestimo.usuario.nome}.")
                return
        print(f"Empréstimo ativo não encontrado para o livro '{titulo_livro}' e o usuário '{identificacao_usuario}'.")
