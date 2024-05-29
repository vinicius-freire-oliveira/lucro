def calcular_preco_venda(custo):
    # Definindo a taxa de lucratividade e a taxa de impostos
    taxa_lucratividade = 0.12
    taxa_impostos = 0.08
    
    # Calculando o preço de venda
    preco_venda = custo / (1 - taxa_lucratividade - taxa_impostos)
    
    return preco_venda

# Dados do problema
custo = 100000 # em R$

# Calculando o preço de venda
preco_venda = calcular_preco_venda(custo)

# Exibindo o resultado
print("Preço de venda previsto: R$", preco_venda)
