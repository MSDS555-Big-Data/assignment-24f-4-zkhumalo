# Import needed libraries
import pandas as pd

# Read the flights.csv file and remove the rows that contain empty cells
flights = pd.read_csv('flights.csv')
flights.dropna(inplace=True)
print(flights.to_string())
