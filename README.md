# DSC180A-SDGE-Q1

All data used in this repository were downloaded from the web or extracted via API.

### Content Run Down
- AFDC_EDA.ipynb contains EDA on AFDC data.
- DMV_EDA.ipynb contains EDA on EV registrations.
- cenpy_EDA.ipynb contains EDA on census data.
- AFDC_API.py and DMV_API.py extract AFDC data and dmv data via API.
  

### Setting Up AFDC API Key and Extracting AFDC Data

1. Create a `.env` file in the root directory of the project with the following content:
    NREL_API_KEY=your_nrel_api_key_here

2. Run the AFDC_API.py file in the terminal to access the AFDC CSV file via API 
```bash
    python3 AFDC_API.py
```

### Extracting DMV Data Via API

1. Run the DMV_API.py file in the terminal to access the DMV CSV file via API 
```bash
    python3 DMV_API.py
```

### To access the San Diego Shape File, visit the below website:
https://www2.census.gov/geo/tiger/TIGER2024/ZCTA520/

### All packages and dependencies to run the notebooks are found in "environment.yml".
