from data_cleaning import load_data, clean_data
from visualization import plot_histogram, plot_scatter
from statistical_analysis import calculate_summary_statistics, calculate_correlation


def main():
    file_path = '../data/dataset.csv'

    # i will load and clean derived data
    data = load_data(file_path)
    clean_data = clean_data(data)

    # generate the summary stat
    summary_stats = calculate_summary_statistics(clean_data)
    print("Summary Statistics:\n", summary_stats)

    # generate the correlation matrix
    correlation_matrix = calculate_correlation(clean_data)
    print("Correlation Matrix:\n", correlation_matrix)

    # clearly visualize data
    plot_histogram(clean_data, 'column_name')
    plot_scatter(clean_data, 'column1', 'column2')


if __name__ == "__main__":
    main()
