# This python script imports quarter-hourly powergen data for Germany for a set date from https://transparency.entsoe.eu  

import requests
from bs4 import BeautifulSoup
import pandas as pd  # to be able to store data in pandas DataFrame and export to CSV file
import datetime # to create current year variable bcoz it's missing from date value on website. Also, to create today's date for timestamp of updates
import os # to check if csv file already exists before exporting the data into csv. Also to delete CSV file 
import numpy as np # used to replace 'n/e' values in 'output' column of DataFrame with blanks (or NaN)
import sys # used to do QC check and exit code unless all data lists have the same number of items in them

URL = 'https://transparency.entsoe.eu/generation/r2/actualGenerationPerProductionType/show?name=&defaultValue=false&viewType=TABLE&areaType=BZN&atch=false&datepicker-day-offset-select-dv-date-from_input=D&dateTime.dateTime=27.12.2021+00:00|CET|DAYTIMERANGE&dateTime.endDateTime=27.12.2021+00:00|CET|DAYTIMERANGE&area.values=CTY|10Y1001A1001A83F!BZN|10Y1001A1001A82H&productionType.values=B01&productionType.values=B02&productionType.values=B03&productionType.values=B04&productionType.values=B05&productionType.values=B06&productionType.values=B07&productionType.values=B08&productionType.values=B09&productionType.values=B10&productionType.values=B11&productionType.values=B12&productionType.values=B13&productionType.values=B14&productionType.values=B20&productionType.values=B15&productionType.values=B16&productionType.values=B17&productionType.values=B18&productionType.values=B19&dateTime.timezone=CET_CEST&dateTime.timezone_input=CET+(UTC+1)+/+CEST+(UTC+2)'
r = requests.get(URL) # pulls content of the website

soup = BeautifulSoup(r.content, 'html5lib') # parses and stores website contents in 'soup' object

date = [] # will store date values
quarterhour_list = [] # will store 15-minute values to be later stored in 'quarterhour' list
quarterhour = [] # will store 15-minute values
date_quarterhour = [] # will store date and quarterhour of power generation output values
fuel_list = [] # will store fuel type values to be later stored in 'fuel' list
fuel = [] # will store fuel type values to be later stored in DataFrame
bidding_zone = [] # will store bidding zone values
timestamp = [] # will store timestamp with time and date of data update
output = [] # will store power generation output values
dupe_check = [] # will store strings which will be used to remove duplicates

d8_only = soup.find_all('input', attrs={'id':'dv-date-to'})[0]['value'] #finds date and stores it in d8_only object
date_only = d8_only[0:10] # convert 'd8_only' object into string
#print(date_only) # print the date and save it in date_only variable

soup_cut = soup.table # reduces contents of soup object to first 'table' class, which contains all the data that I need

fuels = soup_cut.find_all('span', attrs={'class':'bold'}) # extracts fuels from website by finding all 'th' tag names with attribute 'colspan' set to '1' and storing dates in 'fuel' list
for fuel_type in fuels:
    fuel_list.append(str(fuel_type.text).strip('\n            ').rstrip('\n            ')) # remove '\n' and spaces before and after each entry
bid_zone = fuel_list[1] # assigns second element in 'fuel_list' list (i.e. 'BZN|DE-LU') to 'bidding_zone' variable
fuel_list = fuel_list[2:] # removes first two elements in 'fuel_list' list (i.e. removes 'MTU' and 'BZN|DE-LU')
H2O_index = fuel_list.index('Hydro Pumped Storage') # finds location of 'Hydro Pumped Storage' entry in the list
fuel_list.insert(H2O_index + 1, 'Hydro Pumped Storage Consumption') # inserts 'Hydro Pumped Storage Consumption' entry right after 'Hydro Pumped Storage' entry in the list as there're two columns under 'Hydro Pumped Storage' column in the table
#print(fuel_list)
#print(bid_zone)

# section below loops through second 'table' tag -> 'tr' tag -> 'td' tags to capture values for quarterhour slot, fuel type and output for each cell in the table and store them in 'quarterhour', 'fuel', 'output' lists in order to export to DataFrames later on  
rows_tr = soup_cut.find_all('tr') # loop statement... for each 'tr' tag in soup_cut
for row_tr in rows_tr:
    rows_td_qhr = row_tr.find_all('td', attrs={'class':'first'}) # capture row headings (i.e. quarterhours) from website within 'tr' tag -> 'td class = "first"' and store them in 'quarterhour_list' list                                                                 
    for row_td_qhr in rows_td_qhr:
        quarterhour_list.append(row_td_qhr.text) 
        for fuel_val in range(0,len(fuel_list)): # copies each fuel mix element from column headings to 'fuel' list. The number of elements in 'fuel' list should equal the number of elements in 'quarterhour' and output' lists below. 
            fuel.append(fuel_list[fuel_val])
            quarterhour.append(row_td_qhr.text) # copies each quarterhour from row headings to 'quarterhour' list. The number of elements in 'quarterhour' list should equal the number of elements in 'fuel' list above and output' list below.
            bidding_zone.append(bid_zone)
            date.append(date_only)
    rows_td_out = row_tr.find_all('td', attrs={'class':'dv-value-cell'}) # capture power output values from website within 'tr' tag -> 'td class = "dv-value-cell"' -> 'span' tag and store them in 'output' list
    for row_td_out in rows_td_out:
        rows_span = row_td_out.find_all('span')
        #print(rows_span)
        for row_val in rows_span:
            output.append(row_val.text)

for d8 in range(0, len(date)):
    timestamp.append(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) # creates timestamp of time and date of the data update
    date_quarterhour.append(str(date[d8]) + " " + str(quarterhour[d8])) # combines values for from 'date' and 'quarterhour' lists into a new 'date_quarterhour' list
    dupe_check.append(str(bidding_zone[d8]) + " " + str(date_quarterhour[d8]) + " " + str(fuel[d8])) # combines values for from 'date_quarterhour', '' and '' lists into a new 'dupe_check' list

# QC check to exit code unless all data lists have the same number of items in them
qc_check = len(bidding_zone) == len(date) == len(quarterhour) == len(date_quarterhour) == len(fuel) == len(output) == len(timestamp)
if qc_check:
    print('Data QC check is ok')
else:
    sys.exit("Data QC check failed as lists have varying number of items stored in them")

# copy values from lists to pandas DataFrame 
df = pd.DataFrame({'bidding_zone': bidding_zone, 'date': date, 'quarterhour': quarterhour, 'date_quarterhour': date_quarterhour, 'fuel': fuel, 'output': output, 'dupe_check': dupe_check, 'timestamp': timestamp}) # save data as DataFrame
df['date'] = pd.to_datetime(df['date'], format='%d.%m.%Y') # convert date from string to datetime64 format (i.e DD.MM-YYYY)
df['output'] = df['output'].replace('n/e', np.NaN) # replace 'n/e' values in 'output' column of DataFrame with blanks (or NaN) 

# Export DataFrame to CSV file and remove duplicate entries
csv_file_path = '/Users/elchi/Dropbox/Coding/Entso-E_powergen_DE_bs4.csv'
file_exists = os.path.exists(csv_file_path) # to check if csv file already exists before exporting the data into csv
# print(file_exists) # returns True if the file exists, False if the file doesn't exist
if file_exists: # if CSV file already exists, adds content of that CSV file to existing 'df' pandas DataFrame, then deletes CSV file, drops duplicate entries in 'df' DataFrame
    temp_df = pd.read_csv(csv_file_path) # copies content of CSV file into 'temp_df' pandas DataFrame
    os.remove(csv_file_path) # deletes CSV file
    df = pd.concat([df, temp_df]) # adds data from 'temp_df' pandas DataFrames to 'df' DataFrame 
    df = df.drop_duplicates(subset='dupe_check') # deletes duplicate entries in 'long_date' column of 'df' DataFrame 
df.to_csv(csv_file_path, index=False) # creates CSV file and paste all data from DataFrame