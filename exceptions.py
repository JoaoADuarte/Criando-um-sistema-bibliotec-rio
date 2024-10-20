# Acontece quando um usuário tenta pegar emprestado um livro, mas não há cópias disponíveis.
class LivroIndisponivelError(Exception):
    pass

# Acontece quando um usuário não é encontrado ao tentar buscar ou realizar operações.
class UsuarioNaoEncontradoError(Exception):
    pass

# quando um usuário não é encontrado ao tentar buscar ou realizar operações.
class LivroNaoEncontradoError(Exception):
    pass
