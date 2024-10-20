class Livro: # Representa um livro no sistema
    def __init__(self, titulo, autor, ano_publicacao, copias_disponiveis):
        self.titulo = titulo
        self.autor = autor
        self.ano_ublicacao = ano_publicacao
        self.copias_disponiveis = copias_disponiveis

    def emprestar(self):
        if self.copias_disponiveis > 0:
            self.copias_disponiveis -= 1
        else:
            raise Exception("Livro indisponível para emprèstimo")
        
    def devolver(self):
        self.copias_disponiveis +=1
    

class Usuario: # representa um usuário da biblioteca.
    def __init__(self, nome, identificacao, contato):
        self.nome = nome
        self.identificacao = identificacao
        self.contato = contato


class Emprestimo: # Registra o empréstimo do livro
    def __init__(self, usuario, livro):
        self.usuario = usuario
        self.livro = livro
        self.ativo = True
    
    def finalizar_emprestimo(self):
        self.ativo = False




