from pokedex import Pokedex
from database import Database
from helper.writeAJson import writeAJson

db = Database(database="pokedex", collection="pokemons")
db.resetDatabase()

Pokedex.acha_pokemon("Kakuna")

Pokedex.semMultipliers()

Pokedex.pokemon_com_2_fraquezas()

Pokedex.pokemon_fogo_ou_fraco_fogo()

Pokedex.pokemon_agua_e_grama()