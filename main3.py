import pandas as pd
import matplotlib.pyplot as plt

# Завантаження даних 
file_path = 'API_SE.PRM.UNER_DS2_en_csv_v2_122858.csv'

try:
    df = pd.read_csv(file_path, skiprows=4)

    if '2021' in df.columns:
        df_2021 = df[['Country Name', '2021']].copy()
        
        df_2021['2021'] = pd.to_numeric(df_2021['2021'], errors='coerce')

        df_2021 = df_2021.dropna(subset=['2021'])
        df_2021 = df_2021[df_2021['2021'] > 0]

        df_2021_sorted = df_2021.sort_values(by='2021', ascending=False)
        df_top5 = df_2021_sorted.head(5)

        if not df_top5.empty:
            
            labels = df_top5['Country Name']
            sizes = df_top5['2021']

            plt.figure(figsize=(12, 8))
            
            patches, texts, autotexts = plt.pie(sizes, 
                                                autopct='%1.1f%%', 
                                                startangle=90, 
                                                pctdistance=0.85)

            for autotext in autotexts:
                autotext.set_color('white')
                autotext.set_weight('bold')

            plt.legend(patches, labels, loc="center left", bbox_to_anchor=(1.0, 0.5), fontsize=10)

            plt.title('Частка 5 країн за показником (2021 рік)\n(Топ-5 за абсолютним показником)')
            
            plt.axis('equal') 
            plt.tight_layout()
            
            plt.show() 

        else:
            print("Помилка: Не знайдено 5 країн з даними за 2021 рік.")
            
except FileNotFoundError:
    print(f"Помилка: Файл не знайдено.")
except Exception as e:
    print(f"Виникла непередбачувана помилка: {e}")