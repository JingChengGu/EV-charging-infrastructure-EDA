from dotenv import load_dotenv
import os
import requests
import pandas as pd

# Load environment variables from .env
load_dotenv()

# Get the API key from the environment
api_key = os.getenv('NREL_API_KEY')
if not api_key:
    raise ValueError("API key is missing. Set the NREL_API_KEY environment variable in the .env file.")

# Define the API endpoint
url = f'https://developer.nrel.gov/api/alt-fuel-stations/v1.json?&api_key={api_key}'

# Make the GET request to the API
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    fuel_stations = data['fuel_stations']
    df = pd.json_normalize(fuel_stations)
    df.to_csv('datasets/alternative_fuels_data.csv', index=False)
    print('Data successfully saved to alternative_fuels_data.csv')
else:
    print(f'Error: {response.status_code}')
