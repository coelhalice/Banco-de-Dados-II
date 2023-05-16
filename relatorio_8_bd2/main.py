from database import Database
from game_database import GameDatabase

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://3.222.117.135:7687", "neo4j", "ohm-roots-promotions")
db.drop_all()

game_db = GameDatabase(db)

# Criando alguns jogadores
game_db.create_player("Estela")
game_db.create_player("Fernando")
game_db.create_player("Sofia")

# Criando algumas partidas e suas relações
game_db.create_match("Estela, Guilherme", "Estela")
game_db.create_match("Estela, Sofia", "Sofia")
game_db.create_match("Sofia, Guilherme", "Sofia")

# Atualizando o nome de um jogador
game_db.update_player("Fernando", "Guilherme")

game_db.insert_player_match("Estela", "Estela, Guilherme")
game_db.insert_player_match("Estela", "Estela, Sofia")
game_db.insert_player_match("Sofia", "Estela, Sofia")
game_db.insert_player_match("Sofia", "Sofia, Guilherme")
game_db.insert_player_match("Guilherme", "Estela, Guilherme")
game_db.insert_player_match("Guilherme", "Sofia, Guilherme")

# Deletando um jogador de uma partida
#game_db.delete_player("Sofia")
#game_db.delete_match("Sofia", "Sofia, Guilherme")

# Imprimindo todas as informações do banco de dados
print("Jogadores:")
print(game_db.get_players())
print("Partidas:")
print(game_db.get_matches())

# Fechando a conexão com o banco de dados
db.close()