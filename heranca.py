

# Classe base
class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def autenticar(self):
        return f"Usuário {self.nome} autenticado!"

# Classe derivada - funcionário
class Funcionario(Usuario):
    def __init__(self, nome, email, cargo):
        super().__init__(nome, email)
        self.cargo = cargo
