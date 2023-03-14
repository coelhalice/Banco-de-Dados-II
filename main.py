from database import Database
from helper.writeAJson import writeAJson

db = Database(database="pokedex", collection="pokemons")
pokemon = db.collection.find_one({"name": "Bulbasaur"})

writeAJson(pokemon, "pokemon")

Pokedex.acha_pokemon("Kakuna")

Pokedex.semMultipliers()

Pokedex.pokemon_com_2_fraquezas()