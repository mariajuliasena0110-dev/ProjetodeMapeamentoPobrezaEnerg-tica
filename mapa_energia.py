import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt


df = pd.read_csv('dataset_pobreza_energetica(2).csv')


risco_por_regiao = df.groupby('regiao_administrativa')['risco_pobreza_energetica'].sum().reset_index()

caminho_do_mapa = 'seu_arquivo_de_mapa_aqui.shp' 
mapa = gpd.read_file(caminho_do_mapa)

mapa_dados = mapa.merge(risco_por_regiao, 
                        left_on='NM_REGIAO', 
                        right_on='regiao_administrativa', 
                        how='left')

fig, ax = plt.subplots(1, 1, figsize=(12, 10))

mapa_dados.plot(column='risco_pobreza_energetica', 
                ax=ax, 
                legend=True,
                cmap='OrRd', 
                edgecolor='black', 
                missing_kwds={'color': 'lightgrey', 'label': 'Sem dados'}) # 

plt.title('Mapa de Vulnerabilidade: Pobreza Energética', fontsize=14, fontweight='bold')
plt.axis('off') 
plt.tight_layout()


plt.savefig('mapa_vulnerabilidade.png', dpi=300)
plt.show()
