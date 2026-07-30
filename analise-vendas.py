import pandas as pd
dados_vendas = {'data': ['2026-01-01', '2026-01-02', '2026-01-03', '2026-01-04'],
                'Produto': ['notebook', 'mouse', 'teclado', 'monitor'],
                'Vendas': [100, 150, 200, 250],
                'quantidade': [10, 15, 20, 25],
                'preco_unitario': [4000.00, 45.00, 200.00, 3000.00],
                'vendedores': ['João', 'Maria', 'Pedro', 'Ana']}

# Criar um DataFrame a partir do dicionário de dados
df = pd.DataFrame(dados_vendas)

# Calcular o total de vendas por produto
df['total_vendas'] = df['quantidade'] * df['preco_unitario']

#metricas de vendas
faturamento_geral = df['total_vendas'].sum() #.sum() calcula a soma de todos os valores da coluna 'total_vendas'
total_itens = df['quantidade'].sum()
ticket_medio = df['total_vendas'].mean() #.mean() calcula a média de todos os valores da coluna 'total_vendas'
produto_mais_vendido = df.groupby('Produto')['quantidade'].sum().idxmax() #idxmax() retorna o índice (neste caso, o nome do produto) do valor máximo na série resultante do groupby

# Agrupamentos 
fatur_por_produto = df.groupby('Produto')['total_vendas'].sum().sort_values(ascending=False) #.sort_values(ascending=False) ordena os valores em ordem decrescente
fatur_por_vendedor = df.groupby('vendedores')['total_vendas'].sum().sort_values(ascending=False)

# Relatório de vendas
print("=" * 40) # print("=" * 40) cria uma linha de separação com 40 caracteres "="
print("Relatório de Vendas")
print("=" * 40)
print(f"Faturamento Geral: R$ {faturamento_geral:.2f}")
print(f"Total de Itens Vendidos: {total_itens}")
print(f"Ticket Médio: R$ {ticket_medio:.2f}")
print(f"Produto Mais Vendido: {produto_mais_vendido}")
print("=" * 40)

print("\n--- Faturamento por Produto ---")
for produto, valor in fatur_por_produto.items():
    print(f"{produto:<12}: R$ {valor:,.2f}")

print("\n--- Faturamento por Vendedor ---")
for vendedor, valor in fatur_por_vendedor.items():
    print(f"{vendedor:<12}: R$ {valor:,.2f}")