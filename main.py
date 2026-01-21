import os
import sys
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# 1. Настройка путей
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(BASE_DIR, 'src')
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)

# 2. Импорты
try:
    from data_loader import DataLoader
    from eda_manager import EDAManager
    from preprocessor import TextPreprocessor
    print("[OK] Модули загружены")
except ImportError as e:
    print(f"[!] Ошибка импорта: {e}")
    sys.exit(1)

def main():
    # Находим файл в папке data
    data_dir = os.path.join(BASE_DIR, 'data')
    files = [f for f in os.listdir(data_dir) if f.endswith('.csv')]
    
    if not files:
        print(f"[!] В папке {data_dir} нет CSV файлов!")
        return
    
    data_path = os.path.join(data_dir, files[0])
    print(f"[OK] Читаю файл: {data_path}")

    # Читаем файл напрямую через pandas для надежности
    try:
        df = pd.read_csv(data_path)
    except Exception as e:
        print(f"[!] Ошибка чтения файла через pandas: {e}")
        return

    if df is not None:
        print(f"\n--- Загружено строк: {len(df)} ---")
        
        # ПУНКТ 5: Нормализация (NLP)
        prep = TextPreprocessor()
        # Проверяем наличие колонки Name
        col = 'Name' if 'Name' in df.columns else df.columns[1]
        df = prep.process_dataframe(df, col)
        
        print("\n--- [NLP] Очищенный текст (Пункт 5) ---")
        print(df[[col, f'cleaned_{col}']].head())

        # ПУНКТ 6: Векторизация (NLP)
        vectorizer = TfidfVectorizer(max_features=5)
        tfidf_matrix = vectorizer.fit_transform(df[f'cleaned_{col}'])
        
        print("\n--- [NLP] Векторизация (Пункт 6) ---")
        print("Ключевые слова:", vectorizer.get_feature_names_out())
        print("Матрица (первые 3 строки):\n", tfidf_matrix.toarray()[:3])

        # ПУНКТ 4: Анализ
        print("\n--- [EDA] Статистика и График ---")
        eda = EDAManager(df)
        eda.show_basic_info()
        eda.plot_correlation_matrix()
        
    else:
        print("[!] Таблица пуста.")

if __name__ == "__main__":
    main()