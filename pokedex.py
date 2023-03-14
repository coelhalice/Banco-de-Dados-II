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
        pokemons = db.collection.find({"weaknesses": {"$size": 1}})
    writeAJson(pokemon2,"NÃO tem o campo multipliers ou ele é None/null")

    def pokemon_com_2_fraquezas():
        pokemon2 = db.collection.find({"weaknesses": {"$size": 2}})
        writeAJson(pokemon2,"pokemons_2_fraquezas")
    
    def segEvAte_33
        pokemons = db.collection.find({"next_evolution.1.num": {"$lte": "032"})
     writeAJson(pokemon2,"pokemons_2_fraquezas")
                                       
    