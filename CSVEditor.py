import pandas as pd
import numpy as np
from datetime import datetime, timedelta

MainData = pd.read_csv('data\output_dataframe.csv') 
Carbon = pd.read_csv('data\carbon_intensity_example_out.csv') 

# display  
print("Original 'output_dataframe.csv' CSV MainData: \n") 
print(MainData) 
  
# drop function which is used in removing or deleting rows or columns from the CSV files 
MainData.drop('Period from', inplace=True, axis=1) 
MainData.drop('Period to', inplace=True, axis=1) 
MainData.drop('Price_moving_avg', inplace=True, axis=1) 
  
# display  
print("\nCSV MainData after deleting the columns :\n") 
print(MainData)

# Define the start and end date
start_date = datetime(2024, 6, 2)
end_date = datetime(2024, 7, 2)

# Generate a list of datetime objects at 30 minute intervals
num_intervals = int((end_date - start_date).total_seconds() / 1800) + 1  # 1800 seconds = 30 minutes
timestamps = [start_date + timedelta(minutes=30*x) for x in range(num_intervals)]

# Convert datetime objects to Unix timestamps
unix_timestamps = [int(t.timestamp()) for t in timestamps]

MainData.insert(0, 'unix_timestamp', unix_timestamps[:len(MainData)])  # Ensure it matches the length of the existing DataFrame

# Adding Carbon Intensity

CarbonIntensity = Carbon['CarbonIntensity']
MainData['Carbon Intensity'] = CarbonIntensity

MainData.to_csv('data\GrafanaData.csv', index=False)

# Calculating Emissions Savings

CarbonThreshold = 100
carbon_filtered_rows = MainData[MainData['Carbon Intensity'] < CarbonThreshold].head(48)

Carbon_filtered_sum = carbon_filtered_rows['Carbon Intensity'].sum()

Carbon_First_48 = MainData['Carbon Intensity'].head(48).sum()                       

print("Sum of Emissions for first 48 rows with Intensity < threshold:", Carbon_filtered_sum)
print("Sum of Emissions for first 48 rows without threshold:", Carbon_First_48)