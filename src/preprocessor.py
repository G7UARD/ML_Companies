import re

class TextPreprocessor:
    def __init__(self):
        pass

    def clean_text(self, text):
        if not isinstance(text, str):
            return ""
        # Приводим к нижнему регистру и удаляем лишние знаки
        text = text.lower()
        text = re.sub(r'[^a-z0-9\s]', '', text)
        return text.strip()

    def process_dataframe(self, df, column_name):
        print(f"Нормализация текста в колонке: {column_name}")
        df[f'cleaned_{column_name}'] = df[column_name].apply(self.clean_text)
        return df