import pandas as pd
import numpy as np
from datetime import datetime, timedelta

data = pd.read_csv('output_dataframe.csv') 
  
# display  
print("Original 'output_dataframe.csv' CSV Data: \n") 
print(data) 
  
# drop function which is used in removing or deleting rows or columns from the CSV files 
data.drop('Period from', inplace=True, axis=1) 
data.drop('Period to', inplace=True, axis=1) 
data.drop('Price_moving_avg', inplace=True, axis=1) 


  
# display  
print("\nCSV Data after deleting the columns :\n") 
print(data)

# Define the start and end date
start_date = datetime(2024, 6, 2)
end_date = datetime(2024, 7, 2)

# Generate a list of datetime objects at 30 minute intervals
num_intervals = int((end_date - start_date).total_seconds() / 1800) + 1  # 1800 seconds = 30 minutes
timestamps = [start_date + timedelta(minutes=30*x) for x in range(num_intervals)]

# Convert datetime objects to Unix timestamps
unix_timestamps = [int(t.timestamp()) for t in timestamps]

data.insert(0, 'unix_timestamp', unix_timestamps[:len(data)])  # Ensure it matches the length of the existing DataFrame

data.to_csv('GrafanaData.csv', index=False)



#2024-06-02
#2024-07-01