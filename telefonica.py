class AgendaTelefonica:
    def __init__(self):
        self.contatos = {}
        
class AgendaTelefonica:
    def __init__(self):
        self.contatos = {}
    
    def adicionar_contato(self, nome, telefone):
        if nome in self.contatos:
            print(f"Contato '{nome}' já existe.")
        else:
            self.contatos[nome] = telefone
            print(f"Contato '{nome}' adicionado com sucesso.")

class AgendaTelefonica:
    def __init__(self):
        self.contatos = {}
    
    def adicionar_contato(self, nome, telefone):
        if nome in self.contatos:
            print(f"Contato '{nome}' já existe.")
        else:
            self.contatos[nome] = telefone
            print(f"Contato '{nome}' adicionado com sucesso.")
    
    def remover_contato(self, nome):
        if nome in self.contatos:
            del self.contatos[nome]
            print(f"Contato '{nome}' removido com sucesso.")
        else:
            print(f"Contato '{nome}' não encontrado.")

class AgendaTelefonica:
    def __init__(self):
        self.contatos = {}
    
    def adicionar_contato(self, nome, telefone):
        if nome in self.contatos:
            print(f"Contato '{nome}' já existe.")
        else:
            self.contatos[nome] = telefone
            print(f"Contato '{nome}' adicionado com sucesso.")
    
    def remover_contato(self, nome):
        if nome in self.contatos:
            del self.contatos[nome]
            print(f"Contato '{nome}' removido com sucesso.")
        else:
            print(f"Contato '{nome}' não encontrado.")
    
    def pesquisar_contato(self, nome):
        if nome in self.contatos:
            print(f"Nome: {nome}, Telefone: {self.contatos[nome]}")
        else:
            print(f"Contato '{nome}' não encontrado.")

class AgendaTelefonica:
    def __init__(self):
        self.contatos = {}
    
    def adicionar_contato(self, nome, telefone):
        if nome in self.contatos:
            print(f"Contato '{nome}' já existe.")
        else:
            self.contatos[nome] = telefone
            print(f"Contato '{nome}' adicionado com sucesso.")
    
    def remover_contato(self, nome):
        if nome in self.contatos:
            del self.contatos[nome]
            print(f"Contato '{nome}' removido com sucesso.")
        else:
            print(f"Contato '{nome}' não encontrado.")
    
    def pesquisar_contato(self, nome):
        if nome in self.contatos:
            print(f"Nome: {nome}, Telefone: {self.contatos[nome]}")
        else:
            print(f"Contato '{nome}' não encontrado.")
    
    def listar_contatos(self):
        if not self.contatos:
            print("A agenda está vazia.")
        else:
            for nome, telefone in self.contatos.items():
                print(f"Nome: {nome}, Telefone: {telefone}")

def menu():
    agenda = AgendaTelefonica()
    
    while True:
        print("\nAgenda Telefônica")
        print("1. Adicionar Contato")
        print("2. Remover Contato")
        print("3. Pesquisar Contato")
        print("4. Listar Contatos")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            nome = input("Digite o nome do contato: ")
            telefone = input("Digite o telefone do contato: ")
            agenda.adicionar_contato(nome, telefone)
        elif opcao == '2':
            nome = input("Digite o nome do contato a ser removido: ")
            agenda.remover_contato(nome)
        elif opcao == '3':
            nome = input("Digite o nome do contato a ser pesquisado: ")
            agenda.pesquisar_contato(nome)
        elif opcao == '4':
            agenda.listar_contatos()
        elif opcao == '5':
            print("Obrigado por usar a Agenda Telefônica. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
    