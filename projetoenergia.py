import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

print("[1/4] Carregando e preparando os dados da tabela...")
df = pd.read_csv('dataset_pobreza_energetica(2).csv')

# Agrupa o risco por região
risco_por_regiao = df.groupby('regiao_administrativa')['risco_pobreza_energetica'].sum().reset_index()

# Padroniza os nomes para MAIÚSCULAS para bater exatamente com o mapa do governo
risco_por_regiao['regiao_administrativa'] = risco_por_regiao['regiao_administrativa'].str.upper()

print("[2/4] Carregando o mapa do Distrito Federal...")
# Aponta para o novo arquivo que você baixou
caminho_shp = 'mapa_df/regioes_administrativas.shp' 
mapa = gpd.read_file(caminho_shp)

print("[3/4] Cruzando os dados de pobreza com a cartografia...")
# O merge liga o 'ra_nome' do mapa com a 'regiao_administrativa' da nossa tabela
mapa_dados = mapa.merge(risco_por_regiao, 
                        left_on='ra_nome', 
                        right_on='regiao_administrativa', 
                        how='left')

print("[4/4] Desenhando o mapa de vulnerabilidade...")
fig, ax = plt.subplots(1, 1, figsize=(14, 10))

# Plota o mapa. Regiões sem dados na tabela ficarão em cinza claro.
mapa_dados.plot(column='risco_pobreza_energetica', 
                ax=ax, 
                legend=True,
                cmap='OrRd', # Paleta Laranja-Vermelho
                edgecolor='black',
                linewidth=0.5,
                missing_kwds={'color': '#e0e0e0'})

plt.title('Risco de Pobreza Energética por Região Administrativa (DF)', fontsize=16, fontweight='bold')
plt.axis('off') # Esconde as linhas de latitude/longitude
plt.tight_layout()

# Salva a imagem em alta resolução
plt.savefig('mapa_vulnerabilidade_df.png', dpi=300, bbox_inches='tight')
print("\n🎉 Sucesso! O mapa foi gerado e salvo como 'mapa_vulnerabilidade_df.png'.")

# Mostra o mapa na tela
plt.show()
