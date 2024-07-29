import os
import sys
from data_cleaning import load_data, clean_data
from visualization import plot_histogram, plot_scatter
from statistical_analysis import calculate_summary_statistics, calculate_correlation


def main():
    # file_path = '../data/dataset.csv'
    # decided to use an absolute path for the dataset at this point
    file_path = os.path.join(os.path.dirname(__file__), '../data/dataset.csv')

    if not os.path.exists(file_path):
        print(f"file no dey here o: {file_path}")
        sys.exit(1)

    # i will load and clean derived data
    data = load_data(file_path)
    # changed mind and will run an if statement for it
    if data.empty:
        print("data no dey to process")
        sys.exit(1)

    # clean_data = clean_data(data)
    clean_data_df() = clean_data(data)

    # generate the summary stat
    # summary_stats = calculate_summary_statistics(clean_data)
    # changing the summary stat instruction
    summary_stats = calculate_summary_statistics(clean_data_df)
    print("Summary Statistics:\n", summary_stats)

    # generate the correlation matrix
    # correlation_matrix = calculate_correlation(clean_data)
    # correlation matrix need to be fixed:
    correlation_matrix = calculate_correlation(clean_data_df)
    print("Correlation Matrix:\n", correlation_matrix)

    # clearly visualize data
    # plot_histogram(clean_data, 'column_name')
    # plot_scatter(clean_data, 'column1', 'column2')
    plot_histogram(clean_data_df, 'column_name')
    plot_scatter(clean_data_df, 'column1', 'column2')


if __name__ == "__main__":
    main()
