import pandas as pd 
from sklearn.model_selection import train_test_split
from skleran.ensemble import RandomForecastClassifier
from sklearn.metrica import classification_report

ddef main (){
    print ("MODELO PREDITIVO: RISCO DE POBREZA ENERGÉTICA\n")
    
    nome_arquivo = 'dataset_pobreza_energetica(2).csv'

    try:
        df = pd.read_cvs(nome_arquivo)
        print (f"[OK] Dados carregados com sucesso! Total de domicílios analisados: {len(df)}")
        print (f"[ERRO] Não encontei o arquvio '{nome_arquivo}'.")
        return

        y = df ['risco_pobreza_energetica']

        features = ['renda_per_capita_rs', 'num_moradores', 'num_comodos', 'acesso_rede_oficial', 'percentual_gasto_energia', 'inscrito_cadunico']

        X = df [festure]

        X = pd.concat([X, pd.get_dummies(df['regiao_administrativa'], prefix='regiao')], axis=1)


        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

    
        print("[...] Treinando o modelo de Machine Learning...")
        modelo = RandomForestClassifier(n_estimators=100, random_state=42)
        modelo.fit(X_train, y_train)

        previsoes = modelo.predict(X_test)
    
        print("\n--- Relatório de Desempenho da IA ---")
        print(classification_report(y_test, previsoes))
    
        df['predicao_ia'] = modelo.predict(X)
    
        caminho_saida = 'data/resultados_finais_ia.csv'
        df.to_csv(caminho_saida, index=False)
        print(f"\n[OK] Mapeamento concluído! Previsões salvas em: {caminho_saida}")
        print("O projeto está pronto para ser conectado ao Power BI.")

    if __name__ == "__main__":
        main()
    }