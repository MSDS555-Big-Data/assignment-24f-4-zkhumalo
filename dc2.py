# Import needed libraries
import pandas as pd

# Read the flights.csv file and remove the duplicate cells
flights = pd.read_csv('flights.csv')
flights.drop_duplicates(inplace=True)
print(flights.to_string())
