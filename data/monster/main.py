import os
import shutil

# Lista dos nomes dos 151 Pokémon da primeira geração
nomes_pokemon = [
    "Dratini", "Dragonair", "Dragonite"
]


def mover_pokemons(pasta_origem, pasta_destino):
    # Iterar sobre os arquivos na pasta de origem
    for nome_arquivo in os.listdir(pasta_origem):
        # Verificar se o nome do arquivo contém "Shiny" e um Pokémon da primeira geração
        for nome_pokemon in nomes_pokemon:
            if "shiny" in nome_arquivo.lower() and nome_pokemon.lower() in nome_arquivo.lower():
                # Construir o caminho completo do arquivo na pasta de origem
                caminho_origem = os.path.join(pasta_origem, nome_arquivo)

                # Construir o caminho completo do arquivo na pasta de destino
                caminho_destino = os.path.join(pasta_destino, nome_arquivo)

                # Mover o arquivo para a pasta de destino
                shutil.move(caminho_origem, caminho_destino)
                print(f"Arquivo {nome_arquivo} movido para {pasta_destino}")
                break  # Se um Pokémon for encontrado, não é necessário verificar os outros

# Exemplo de uso
pasta_origem = 'C:/ttk-tfs-pokemon/data/monster/shiny/gen1'  # Substitua pelo caminho da sua pasta de origem
pasta_destino = 'C:/ttk-tfs-pokemon/data/monster/shiny/gen1/Dragao'  # Substitua pelo caminho da sua pasta de destino

# Criar as pastas se não existirem
if not os.path.exists(pasta_origem):
    os.makedirs(pasta_origem)

if not os.path.exists(pasta_destino):
    os.makedirs(pasta_destino)

# Simular a presença de arquivos na pasta de origem
arquivos_simulados = [
    "Shiny Bulbasaur.txt", "Ivysaur.txt", "Charmander123.txt",
    "Pidgeotto.txt", "Golbat.txt", "Shiny Pikachu.txt"
]

for nome_arquivo in arquivos_simulados:
    caminho_arquivo_origem = os.path.join(pasta_origem, nome_arquivo)
    with open(caminho_arquivo_origem, 'w') as arquivo:
        arquivo.write(f"Conteúdo do arquivo {nome_arquivo}")

# Exemplo de chamada da função mover_pokemons
mover_pokemons(pasta_origem, pasta_destino)
