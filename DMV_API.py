import requests
import pandas as pd

# Base API endpoint
base_url = "https://data.ca.gov/api/3/action/datastore_search"

# Resource IDs for each year's dataset
resource_ids = [
    "d304108a-06c1-462f-a144-981dd0109900",  # Year 1
    "4254a06d-9937-4083-9441-65597dd267e8",  # Year 2
    "888bbb6c-09b4-469c-82e6-1b2a47439736",  # Year 3
    "1856386b-a196-4e7c-be81-44174e29ad50",  # Year 4
    "9aa5b4c5-252c-4d68-b1be-ffe19a2f1d26",  # Year 5
    "d599c3d3-87af-4e8c-8694-9c01f49e3d93"   # Year 6
]

def fetch_data(resource_id, limit=5000):
    records = []
    offset = 0
    while True:
        # Make a GET request to the CKAN API
        params = {
            "resource_id": resource_id,
            "limit": limit,
            "offset": offset
        }
        response = requests.get(base_url, params=params)
        response_data = response.json()
        
        # Check for success
        if response_data["success"]:
            new_records = response_data["result"]["records"]
            records.extend(new_records)
            
            # Break the loop if no more records
            if len(new_records) < limit:
                break
            offset += limit
        else:
            raise Exception("Failed to fetch data for resource_id:", resource_id)
    return records

all_data = []

for resource_id in resource_ids:
    print(f"Fetching data for resource_id: {resource_id}")
    data = fetch_data(resource_id)
    
    # Convert to DataFrame for column standardization
    df = pd.DataFrame(data)
    
    # Standardize column names to ensure consistency
    if "ZIP Code" in df.columns:
        df.rename(columns={"ZIP Code": "Zip Code"}, inplace=True)
    elif "Zip_Code" in df.columns:
        df.rename(columns={"Zip_Code": "Zip Code"}, inplace=True)
    
    # Append standardized data back as records
    all_data.extend(df.to_dict("records"))

# Convert the combined data into a DataFrame
df = pd.DataFrame(all_data)

# Display the first few rows to confirm
print(df.head())

# Save to CSV
df.to_csv("vehicle_fuel_type.csv", index=False)

# Start analysis
print(df.info())
