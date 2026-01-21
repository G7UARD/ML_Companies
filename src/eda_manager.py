import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class EDAManager:
    """Class for early analyze of data and visualization"""
    
    def __init__(self, dataframe):
        self.df = dataframe

    def show_basic_info(self):
        print("::Overall Info::")
        print(self.df.info())
        print("\n::Skipped Variables::")
        print(self.df.isnull().sum())

    def plot_correlation_matrix(self):
        plt.figure(figsize=(10, 8))
        numeric_df = self.df.select_dtypes(include=['float64', 'int64'])
        correlation_matrix = numeric_df.corr()
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
        plt.title("Matrix of Correlation")
        plt.show()

    def plot_distribution(self, column):
        plt.figure(figsize=(8, 6))
        sns.histplot(self.df[column], kde=True)
        plt.title(f"Distribution of columns {column}")
        plt.show()