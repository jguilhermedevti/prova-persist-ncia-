import pandas as pd
import random

nomes = ['Pikachu', 'Charmander', 'Moltres', 'Articuno', 'Zapdos']
total_de_oponentes = len(nomes) - 1

forcas_geradas = [random.randint(50, 150) for _ in range(len(nomes))]
pokemons = pd.Series(forcas_geradas, index=nomes)

print("Força dos Pokémons")
print(pokemons)

try:
    with open("resultado_pokemons.txt", "w", encoding="utf-8") as arquivo:
        
        for pokemon_atual, forca_atual in pokemons.items():
            
            # pokemons fracos da linha
            oponentes_vencidos = [
                oponente 
                for oponente, forca_oponente in pokemons.items() 
                if pokemon_atual != oponente and forca_atual > forca_oponente
            ]
            
            # resultado com base nos vencidos
            if not oponentes_vencidos:
                resultado = "nenhum"
            elif len(oponentes_vencidos) == total_de_oponentes:
                resultado = "todos"
            else:
                resultado = ", ".join(oponentes_vencidos)
                
            linha_final = f"O Pokémon {pokemon_atual}, ganha de: {resultado}\n"
            arquivo.write(linha_final)
            
    print("\nArquivo 'resultado_pokemons.txt' criado com sucesso!")

except Exception as e:
    print(f"Ocorreu um erro ao escrever o arquivo: {e}")
