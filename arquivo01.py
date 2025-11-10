import pandas as pd
import random

nomes = ['Pikachu', 'Charizard', 'Bulbasaur', 'Squirtle', 'Mewtwo']
total_de_oponentes = len(nomes) - 1

forcas_geradas = [random.randint(50, 150) for _ in range(len(nomes))]
pokemons = pd.Series(forcas_geradas, index=nomes)

print("--- Força dos Pokémons Gerada ---")
print(pokemons)
print("-----------------------------------")


