from database import Database
from WriteAJson import writeAJson
from livroModel import LivroModel
from cli import livroCLI

db = Database(database="relatorio_05", collection="Livros")
livromodel = LivroModel(database=db)


livroCLI = livroCLI(livromodel)
livroCLI.run()