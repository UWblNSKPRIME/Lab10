import pandas as pd
import matplotlib.pyplot as plt

FILE_PATH = 'API_SE.PRM.UNER_DS2_en_csv_v2_122858.csv' 
START_YEAR = 2000

def load_and_prepare_data(file_path):
    try:
        df = pd.read_csv(file_path, skiprows=4)
        
        all_columns = df.columns
        year_columns = [col for col in all_columns if col.isdigit() and int(col) >= START_YEAR]
        
        return df, year_columns
    except FileNotFoundError:
        print(f"Помилка: Файл не знайдено за шляхом {FILE_PATH}")
        return None, None
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        return None, None

def plot_bar_chart_for_country(df, year_columns):
    country_name_input = input("Введіть назву країни (напр. 'Ukraine' або 'United States'): ")

    country_data = df[df['Country Name'].str.contains(country_name_input, case=False, na=False)]

    if country_data.empty:
        print(f"Країну '{country_name_input}' не знайдено. Спробуйте ще раз.")
        return
    
    if len(country_data) > 1:
        print(f"Знайдено декілька збігів, обрано: {country_data.iloc[0]['Country Name']}")
    
    country_row = country_data.iloc[0]
    country_name_found = country_row['Country Name']
    indicator_name = country_row['Indicator Name']

    values = pd.to_numeric(country_row[year_columns], errors='coerce')
    values = values.dropna()
    
    if values.empty:
        print(f"Для країни '{country_name_found}' відсутні дані за цей період.")
        return

    plt.figure(figsize=(12, 7))
    plt.bar(values.index, values.values, color='skyblue')
    
    plt.title(f"{indicator_name}\nдля {country_name_found}")
    plt.xlabel('Рік')
    plt.ylabel('Значення показника')
    
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    plt.tight_layout()
    plt.show() 

if __name__ == "__main__":
    data_df, years = load_and_prepare_data(FILE_PATH)
    if data_df is not None:
        plot_bar_chart_for_country(data_df, years)