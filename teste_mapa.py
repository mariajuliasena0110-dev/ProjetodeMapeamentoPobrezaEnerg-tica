import geopandas as gpd

caminho_shp = 'mapa_df/limite_do_distrito_federal.shp'
mapa_df = gpd.read_file(caminho_shp)

print("--- Colunas do Mapa do DF ---")
print(mapa_df.columns)
print("\n--- Primeiras linhas ---")
print(mapa_df.head(3))
