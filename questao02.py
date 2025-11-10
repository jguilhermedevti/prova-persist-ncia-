import pandas as pd

informacoes_iniciais = {
    'Nome': ['Bia', 'Pedro', 'Gustavo', 'Felipe', 'Rosa'],
    'Idade': [23, 30, 25, 41, 28],
    'Cidade': ['São Paulo', 'Recife', 'Salvador', 'Manaus', 'Curitiba']
}
tabela_pessoas = pd.DataFrame(informacoes_iniciais)

print("Tabela Original")
print(tabela_pessoas)

print("\nDuas primeiras linhas")
print(tabela_pessoas.head(2))

print("\nApenas a coluna 'Nome'")
print(tabela_pessoas['Nome'])

print("\nPessoas com mais de 25 anos")
filtro_idade = tabela_pessoas['Idade'] > 25
print(tabela_pessoas[filtro_idade])

novos_estados = ['SP', 'PE', 'BA', 'AM', 'PR']
tabela_pessoas['Estado'] = novos_estados

nome_do_arquivo = 'pessoas.csv'

try:
    tabela_pessoas.to_csv(nome_do_arquivo, index=False, encoding='utf-8')
    print(f"\nTabela salva com sucesso em '{nome_do_arquivo}'")

    print(f"\nConteúdo do arquivo '{nome_do_arquivo}'")
    with open(nome_do_arquivo, 'r', encoding='utf-8') as arquivo_lido:
        print(arquivo_lido.read())

except Exception as erro:
    print(f"\n erro ao processar o arquivo: {erro}")

