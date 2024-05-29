def calcular_lucratividade(lucro, preco_venda):
    return (lucro / preco_venda) * 100

def calcular_rentabilidade(lucro, investimento):
    return (lucro / investimento) * 100

# Dados do problema
lucro = 40000  # em R$
preco_venda = 300000  # em R$
investimento = 250000  # em R$

# Calculando a lucratividade
lucratividade = calcular_lucratividade(lucro, preco_venda)

# Calculando a rentabilidade
rentabilidade = calcular_rentabilidade(lucro, investimento)

# Exibindo os resultados
print("Lucro previsto: R$", lucro)
print("Lucratividade prevista: {:.1f}%".format(lucratividade))
print("Rentabilidade prevista: {:.1f}%".format(rentabilidade))
