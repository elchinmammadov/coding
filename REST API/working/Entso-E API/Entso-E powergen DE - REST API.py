# This python script imports quarter-hourly powergen data for Germany from https://transparency.entsoe.eu using RESTful API
# more detailed instructions on how to use API are on https://github.com/EnergieID/entsoe-py
# mappings of all available parameters are in 'Appendix A' on https://transparency.entsoe.eu/content/static_content/Static%20content/web%20api/Guide.html#_generation_domain AND also on https://github.com/EnergieID/entsoe-py
# Maximum of 400 requests per user per minute. Reaching of 400 query/minute limit will result in a temporary ban of 10 minutes.

from entsoe import EntsoePandasClient # to pull Entso-E data thru API
import pandas as pd
import os # to check if csv file already exists before exporting the data into csv. Also to delete CSV file 
from dotenv import load_dotenv # I need this to hide API key
import os # I need this to hide API key

# I need this to hide API key
load_dotenv()
client = EntsoePandasClient(api_key=os.getenv('api_key')) # enters my API token

start = pd.Timestamp('20211227', tz='Europe/Brussels') # start date
end = pd.Timestamp('20211228', tz='Europe/Brussels') # end date

country_codes = ['AT', 'BE', 'CZ', 'DE', 'DE_LU', 'ES', 'FR', 'HR', 'HU', 'IE', 'IT', 'LT', 'ME', 'MK', 'NL', 'PT', 'SE', 'SK', 'UA']
# BUG!!!!
# find out why the following country codes aren't working: 'AL', 'BA', 'BG', 'BY', 'CH', 'DK', 'EE', 'FI', 'GB', 'GB'_NIR', 'GR', 'LU', 'LV', 'MD', 'MT', 'NO', 'PL', 'RO', 'RS', 'RU', 'RU_KGD', 'SI', 'TR', 'DE_AT_LU'
# ...however, these countries are working every other time. It works when you run it once, the next time you get 'Reindexing only valid with uniquely valued Index objects' error. The next time it works again, etc...
# ...similarly, these countries are working if 'country_codes = ['GR']' has one country but not if it has 'country_codes = ['FI', 'GR']'

data_types = ['powergen', 'consumption'] # create list for data types in Entso-E's database (i.e. power generation, power consumption, power capacity). If you add new data type here, make sure you add it to 'if data_type...' statement below
# BUG!!!!
# unable to add 'capacity' to 'data_types = ['powergen', 'consumption']' because it triggers an error if 'Entso-E_capacity_per_country_API.csv' file already exists because of the  bug in 'df3 = pd.concat([df3, temp_df3])' line below
for data_type in data_types: # loops through types of data in Entso-E's database (i.e. power generation, power consumption, power capacity) to determine which type of API query and CSV file name to use 
    for country_code in country_codes: # loops through countries in 'country_codes' list

        # get data from API for each data type in 'data_types' list above
        if data_type == "powergen":
            df1 = client.query_generation(country_code, start=start,end=end) # get data for power generation and store in 'df1' DataFrame
            csv_file_path = '/Users/elchi/Dropbox/Coding/Entso-E_powergen_per_country_API.csv' # create file path to store data for power generation
        elif data_type == "capacity":
            df1 = client.query_installed_generation_capacity(country_code, start=start,end=end) # get data for power capacity and store in 'df1' DataFrame
            csv_file_path = '/Users/elchi/Dropbox/Coding/Entso-E_capacity_per_country_API.csv' # create file path to store data for power capacity
        elif data_type == ('consumption'):
            df1 = client.query_load(country_code, start=start,end=end) # get data for power consumption and store in 'df1' DataFrame
            csv_file_path = '/Users/elchi/Dropbox/Coding/Entso-E_consumption_per_country_API.csv' # create file path to store data for power consumption
        else:
            print('not recognised')

        df1.reset_index(inplace=True) # remove time & date stored as index value (i.e. row header) by resetting index values and storing time and date under new 'Time and Date' column
        df1 = df1.rename(columns={'index': 'Time and Date'})

        # Within multi-level columns in 'df1' DataFrame, search for lower columns (i.e. columns in second row) titled "Actual Consumption", then for the upper column (i.e. columns in first row) copy the name of the column to the left of it and add 'Consumption' to the end of that column title. Then, delete all lower columns (i.e. second-row column).
        col_list = [] # creates empty list to store column values
        for col_num in range(0, len(df1.columns)): # loops through columns in 'df1' DataFrame
            if df1.columns[col_num][1] == "Actual Consumption": # finds lower columns who's name equal 'Actual Consumption'
                col_list.append(df1.columns[col_num-1][0] + " Consumption") # adds name of upper column to the left of the matching column (i.e. the one that says 'Actual Consumption') and suffix 'Consumption' to 'col_list'
            else:
                col_list.append(df1.columns[col_num][0]) # adds name of column to 'col_list'
        df1.columns = col_list # renames columns in 'df1' DataFrame using names set in 'col_list' and deletes lower collumns (i.e. columns in second row)

        # Create 'df2' DataFrame and populate it with single 'Country' column and set row values to country code used in 'country_code' variable 
        country_val = [] # will store values which will be used to add country code to df2 DataFrame 
        dupe_check = [] # will store strings which will be used to remove duplicates

        for cntry in range(0, len(df1.index)): # populates 'df2' DataFrame with country code under 'Country' column and adds 'dupe_check' column which will be later used to remove duplicate entries when exporting data to Excel
            country_val.append(country_code)
            dupe_check.append(str(df1.iloc[cntry][0]) + " " + str(country_code)) # combines values for from 'date_quarterhour', '' and '' lists into a new 'dupe_check' list
        df2 = pd.DataFrame({'dupe_check':dupe_check, 'Country':country_val})

        # merge 'df1' and 'df2' into a single 'df3' DataFrame
        df3 = df2.join(df1, how='left')
        df3 # display DataFrame

        # BUG!!!!
        # below code doesn't keep non-duplicate rows. For example, if you remove countries from 'country_codes' list above and then run this code, the csv file will not have those removed countries in the list. It's to do with error called 'Reindexing only valid with uniquely valued Index objects' error.'
        # Export DataFrame to CSV file and remove duplicate entries
        file_exists = os.path.exists(csv_file_path) # to check if csv file already exists before exporting the data into csv. Returns True if the file exists, False if the file doesn't exist.
        if file_exists: # if CSV file already exists, adds content of that CSV file to existing 'df3' pandas DataFrame, then deletes CSV file, drops duplicate entries in 'df3' DataFrame
            temp_df3 = pd.read_csv(csv_file_path) # copies content of CSV file into 'temp_df3' pandas DataFrame
            os.remove(csv_file_path) # deletes CSV file
            df3 = pd.concat([df3, temp_df3]) # adds data from 'temp_df3' pandas DataFrames to 'df3' DataFrame 
            df3 = df3.drop_duplicates(subset='dupe_check') # deletes duplicate entries in 'long_date' column of 'df3' DataFrame 
        df3.to_csv(csv_file_path, index=False) # creates CSV file and paste all data from DataFrame
                
# # get data for "A72 - Reservoir filling information"

# CREATE NEW DATAFRAMES AND CSV FILES WITH DATA AGGREGATED TO MONTHLY & YEARLY VALUES