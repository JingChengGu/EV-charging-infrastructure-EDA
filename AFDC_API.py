import requests
import pandas as pd

# Define the API endpoint and your API key
api_key = '7oh3YCkkA1Bpea6GzbgeBQ5RD2EygtrVdcRppXw8'
url = f'https://developer.nrel.gov/api/alt-fuel-stations/v1.json?&api_key={api_key}'

# Make the GET request to the API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Get the data in JSON format
    data = response.json()

    # Extract relevant data from the response
    fuel_stations = data['fuel_stations']

    # Convert the data into a pandas DataFrame
    df = pd.json_normalize(fuel_stations)

    # Save the DataFrame to a CSV file
    df.to_csv('alternative_fuels_data.csv', index=False)


    print('Data successfully saved to alternative_fuels_data.csv')
else:
    print(f'Error: {response.status_code}')

