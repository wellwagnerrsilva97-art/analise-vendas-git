import pandas as pd
import os

# ==========================================
# 1. DEFINE O CAMINHO DO ARQUIVO
# ==========================================
# Exemplo CSV:  caminho_arquivo = "vendas.csv"
# Exemplo Excel: caminho_arquivo = "vendas.xlsx"
caminho_arquivo = "vendas.xlsx"

# ==========================================
# 2. CARREGA OS DADOS
# ==========================================
try:
    if caminho_arquivo.endswith('.csv'):
        # Se o CSV usar ponto e vírgula como separador (comum no Excel em português), adicione sep=';'
        df = pd.read_csv(caminho_arquivo, encoding='utf-8')
    elif caminho_arquivo.endswith(('.xlsx', '.xls')):
        df = pd.read_excel(caminho_arquivo)
    else:
        raise ValueError("Formato de arquivo não suportado!")
        
    print(f"Arquivo '{caminho_arquivo}' carregado com sucesso!\n")

except FileNotFoundError:
    print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado no diretório atual.")
    exit()

# ==========================================
# 3. TRATAMENTO E ANÁLISE DOS DADOS
# ==========================================

# Garantir que o nome das colunas corresponda ao seu arquivo real:
# Ex: 'Quantidade', 'Preco_Unitario', 'Produto', 'Vendedor'

# Se o seu arquivo não tiver uma coluna de Faturamento Total pronta, crie uma:
if 'Faturamento_Total' not in df.columns:
    df['Faturamento_Total'] = df['Quantidade'] * df['Preco_Unitario']

# Métricas Principais
faturamento_geral = df['Faturamento_Total'].sum()
total_itens = df['Quantidade'].sum()
ticket_medio = df['Faturamento_Total'].mean()

# Agrupamentos
fatur_por_produto = df.groupby('Produto')['Faturamento_Total'].sum().sort_values(ascending=False)
fatur_por_vendedor = df.groupby('Vendedor')['Faturamento_Total'].sum().sort_values(ascending=False)

# ==========================================
# 4. EXIBIÇÃO DO RELATÓRIO
# ==========================================
print("=" * 45)
print("            RELATÓRIO DE VENDAS")
print("=" * 45)
print(f"Faturamento Total   : R$ {faturamento_geral:,.2f}")
print(f"Total de Itens      : {total_itens:,}")
print(f"Ticket Médio / Venda: R$ {ticket_medio:,.2f}")
print("-" * 45)

print("\n--- Faturamento por Produto ---")
print(fatur_por_produto.map('R$ {:,.2f}'.format).to_string())

print("\n--- Faturamento por Vendedor ---")
print(fatur_por_vendedor.map('R$ {:,.2f}'.format).to_string())