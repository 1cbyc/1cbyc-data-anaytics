import matplotlib.pyplot as plt
import seaborn as sns

def plot_histogram(df, column):
    plt.figure(figsize=(10, 6))
    sns.histplot(df[column], kde=True)
    plt.title(f'Histogram of {column}')
    plt.show()

def plot_scatter(df, column1, column2):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=df[column1], y=df[column2])
    plt.title(f'Scatter Plot of {column1} vs {column2}')
    plt.show()

# this is the visualization context for this