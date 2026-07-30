import pandas as pd
dados_vendas = {'Produto': ['notebook', 'mouse', 'teclado', 'monitor'],
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

