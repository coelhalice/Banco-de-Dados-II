from database import Database
from helper.writeAJson import writeAJson

db = Database(database="pokedex", collection="pokemons")

class Pokedex:
    def __init__(self, db_name, collection_name):
        self.db = Database(db_name, collection_name)

    def acha_pokemon(name):
        pokemon1 = db.collection.find({"name": name})
        writeAJson(pokemon1,"pokemon_achado")

    def semMultipliers():
        pokemon2 = db.collection.find({"weaknesses": {"$size": 1}})
        writeAJson(pokemon2,"NÃO tem o campo multipliers ou ele é None/null")

    def pokemon_com_2_fraquezas():
        pokemon3 = db.collection.find({"weaknesses": {"$size": 2}})
        writeAJson(pokemon3,"pokemons_2_fraquezas")

    def pokemon_fogo_ou_fraco_fogo():
        pokemon4 = db.collection.find({"$or": [{"type":"Fire"},{"weaknesses": "Fire"}]})
        writeAJson(pokemon4,"pokemons de fogo ou fraco contra fogo")
    
    def pokemon_agua_e_grama():
        pokemon5 = db.collection.find({"$and": [{"type":"Water"},{"type":"Grass"}]})
        writeAJson(pokemon5,"pokemons de agua e grama")
    
    