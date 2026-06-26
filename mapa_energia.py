import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# 1. Carrega os nossos dados numéricos
df = pd.read_csv('dataset_pobreza_energetica(2).csv')

# Agrupa os dados para ter o total de risco por região (preparando para o mapa)
risco_por_regiao = df.groupby('regiao_administrativa')['risco_pobreza_energetica'].sum().reset_index()

# 2. Carrega o arquivo cartográfico (SUBSTITUA PELO NOME DO SEU ARQUIVO)
# Pode ser um .shp, .geojson, .gpkg, etc.
caminho_do_mapa = 'seu_arquivo_de_mapa_aqui.shp' 
mapa = gpd.read_file(caminho_do_mapa)

# 3. Faz a fusão (Merge) da geometria do mapa com os nossos números
# ATENÇÃO: É preciso verificar qual é o nome da coluna dentro do arquivo do mapa que guarda o nome das regiões.
# Supondo que lá dentro a coluna se chame 'NM_REGIAO':
mapa_dados = mapa.merge(risco_por_regiao, 
                        left_on='NM_REGIAO', 
                        right_on='regiao_administrativa', 
                        how='left')

# 4. Plota o mapa cartográfico
fig, ax = plt.subplots(1, 1, figsize=(12, 10))

# Colore os polígonos usando o risco de pobreza (quanto maior, mais escuro)
mapa_dados.plot(column='risco_pobreza_energetica', 
                ax=ax, 
                legend=True,
                cmap='OrRd', # Uma paleta que vai do Laranja ao Vermelho Escuro
                edgecolor='black', # Borda preta separando as regiões
                missing_kwds={'color': 'lightgrey', 'label': 'Sem dados'}) # Regiões fora do nosso estudo ficam cinzas

plt.title('Mapa de Vulnerabilidade: Pobreza Energética', fontsize=14, fontweight='bold')
plt.axis('off') # Remove os eixos (latitude/longitude) para ficar mais limpo
plt.tight_layout()

# Salva o mapa
plt.savefig('mapa_vulnerabilidade.png', dpi=300)
plt.show()
