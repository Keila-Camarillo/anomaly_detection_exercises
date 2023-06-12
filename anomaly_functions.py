import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_histograms_and_boxplots(df, cols):
    """
    Plot histograms and boxplots for each column in a DataFrame.
    
    Parameters:
        df (pandas.DataFrame): The DataFrame containing the data.
        cols (list): A list of column names to plot.
    
    Returns:
        None
    """
    for col in cols:
        plt.hist(df[col])
        plt.title(col.replace('_', ' ').capitalize())
        plt.show()
        
        sns.boxplot(data=df, x=col)
        plt.show()
        
        print('------------')

# ------------------------------------------------------------------------------------------------------
# These functions stay together
def filter_numeric_columns(data):
    """
    Filter out columns that are not of type int or float from a DataFrame.

    Parameters:
        data (pandas.DataFrame): The DataFrame containing the data.

    Returns:
        pandas.DataFrame: The DataFrame with only numeric columns.
    """
    # Filter columns that are int or float
    numeric_columns = data.select_dtypes(include=[np.number])
    
    return numeric_columns

    return numeric_columns
def identify_lower_outliers(data, csv_file, multiplier=1.5):
    """
    Use the IQR Range Rule and the upper and lower bounds to identify the lower outliers of each column of a CSV file.

    Parameters:
        data (pandas.DataFrame): The DataFrame containing the data.
        csv_file (str): The path to the CSV file.
        multiplier (float): The multiplier to determine the outlier bounds. Default is 1.5.

    Returns:
        None
    """
    # Load the CSV file
    data = pd.read_csv(csv_file)
    data = filter_numeric_columns(data)

    # Calculate the lower and upper bounds for each column
    lower_bounds = data.quantile(0.25) - (multiplier * (data.quantile(0.75) - data.quantile(0.25)))

    # Identify lower outliers
    outliers = {}
    for column in data.columns:
        column_outliers = data[data[column] < lower_bounds[column]]
        outliers[column] = column_outliers

    # Print outlier summary and suggest which outliers to keep
    for column, column_outliers in outliers.items():
        print(f"Column: {column}")
        print(f"Lower bound: {lower_bounds[column]}")
        print("Outliers:")
        print(column_outliers)
        print()

        if column_outliers.empty:
            print("No outliers found in this column.")
        else:
            print("Suggested outliers to keep:")
            # Provide your logic here to decide which outliers to keep based on whether they make sense or not
            # You can modify this part of the code to reflect your decision-making process

        print("=" * 50)
        
def identify_upper_outliers(data, csv_file, multiplier=1.5):
    # Load the CSV file
    data = pd.read_csv(csv_file)
    data = filter_numeric_columns(data)

    # Calculate the lower and upper bounds for each column
    upper_bounds = data.quantile(0.75) + (multiplier * (data.quantile(0.75) - data.quantile(0.25)))

    # Identify upper outliers
    outliers = {}
    for column in data.columns:
        column_outliers = data[data[column] > upper_bounds[column]]
        outliers[column] = column_outliers

    # Print outlier summary and suggest which outliers to keep
    for column, column_outliers in outliers.items():
        print(f"Column: {column}")
        print(f"Upper bound: {upper_bounds[column]}")
        print("Outliers:")
        print(column_outliers)
        print()

        if column_outliers.empty:
            print("No outliers found in this column.")
        else:
            print("Suggested outliers to keep:")


        print("=" * 50)

# ------------------------------------------------------------------------------------------------------