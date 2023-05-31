from database import Database
from teacher import TeacherCRUD, CLI

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://44.199.194.175:7687", "neo4j", "folder-occurrence-rack")
# db.drop_all()

# cria uma instância da classe TeacherCRUD, passando a instância da classe Database
teacher = TeacherCRUD(db)

# Criando um teacher
teacher.create('Chris Lima', '1956', '189.052.396-66')

# Utilizando a classe TeacherCRUD() pesquise o professor com o name de "Chris Lima" 
print(teacher.read('Chris Lima'))

# Utilizando a classe TeacherCRUD() altere o cpf do “Teacher” de name "Chris Lima" para "162.052.777-77"
teacher.update('Chris Lima', '162.052.777-77')

# Cria uma instância da classe CLI, passando a instância da classe TeacherCRUD
cli = CLI(teacher)
# Chama o método run da instância da classe CLI
cli.run()

# Fechando a conexão com o banco de dados
db.close()