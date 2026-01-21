import pandas as pd
import os

class Dataloader:
    """Class for loading data from different forms of data (CSV, Excel and more)"""

    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def load_csv(self):
        if os.path.exists(self.file_path):
            self_data = pd.read_csv(self.file_path)
            print(f"You've succsesfully downloaded data from {self.file_path}")
            return self.data
        else:
            print("Error: File didn't found")
            return None
    
    def get_basic_stats(self):
        if self.data is not None:
            return self.data.describe()
        else:
            print("Data haven't downloaded")

    if __name__ == "__main__":
        loader = DataLoader("C:/Users/timur/Desktop/CDV inf/Coding/Projects/ML_Companies/data/100_largest_companies.csv")
        df = loader.load_csv()
        if df is not None:
            print(loader.get_basic_stats())