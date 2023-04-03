class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Enter a command: ")
            if command == "quit":
                print("Goodbye!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command. Try again.")

class LivroCLI(SimpleCLI):
    def __init__(self, livroModel):
        super().__init__()
        self.livroModel = livroModel
        self.add_command("create", self.create_livro)
        self.add_command("read", self.read_livro)
        self.add_command("update", self.update_livro)
        self.add_command("delete", self.delete_livro)

    def create_livro(self):
        titulo = input("Titulo: ")
        autor = input("Autor: ")
        ano = input("Ano: ")
        preco = input("Preco: ")
        self.livroModel.create_livro(titulo, autor, ano, preco)

    def read_livro(self):
        id = input("Enter the id: ")
        livro = self.livro_model.read_livro_by_id(id)
        if livro:
            print(f"Titulo: {livro['titulo']}")
            print(f"Autor: {livro['autor']}")
            print(f"Ano: {livro['ano']}")
            print(f"Preco: {livro['preco']}")
    
    def update_livro(self):
        id = input("Enter the new id: ")
        titulo = input("New Titulo: ")
        autor = input("New Autor: ")
        ano = input("New Ano: ")
        preco = input("New Preco: ")
        self.livroModel.update_livro(titulo, autor, ano, preco)

    def delete_livro(self):
        id = input("Enter the id: ")
        self.livro_model.delete_livro(id)

    def run(self):
        print("Welcome to the Livro CLI!")
        print("Available commands: create, read, update, delete, quit")
        super().run()