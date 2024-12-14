# Import needed libraries
import pandas as pd

# Read the flights.csv file and replace empty cells with the mode value that appears most frequently in Column Year.
flights = pd.read_csv('flights.csv')
flights['year'].fillna(flights['year'].mode()[0], inplace=True)
print(flights.to_string())
