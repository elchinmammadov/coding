# This python script imports hourly weather data for St Albans from www.weather.com  
# this version runs faster than selenium-based file called 'webscraper - hourly weather - selenium.py'

import requests
from bs4 import BeautifulSoup
import pandas as pd  # to be able to store data in pandas DataFrame and export to CSV file
import datetime # to create current year variable bcoz it's missing from date value on website. Also, to create today's date for timestamp of updates
import os # to check if csv file already exists before exporting the data into csv. Also to delete CSV file 

URL = 'https://weather.com/en-GB/weather/hourbyhour/l/St+Albans+England?canonicalCityId=969c164e50d945e77fcde5fe5e319b3650224764d4e98036ddac1b702738f186'
r = requests.get(URL) # pulls content of the website

soup = BeautifulSoup(r.content, 'html5lib') # parses and stores website contents in 'soup' object

# creates empty lists to store table values
dates = [] # will store unique dates, which are about 2-3 per web page
date = [] # will store non-unique date values, which will be matched to individual hourly values in 'hour' list
hour = [] # will store hour values
temp = [] # will store temperature values
timestamp = [] # will store timestamp with time and date of data update

hours = soup.find_all('h2', attrs={'data-testid':'daypartName'}) # extracts hours from website by finding all 'h2' tag names with attribute 'data-testid' set to 'daypartName' and storing dates in 'hour' list
for hr in hours:
    hour.append(hr.text)
#print(hour)

temps = soup.find_all('span', attrs={'data-testid':'TemperatureValue'})  # extracts temperature from website by finding all 'span' tag names with attribute 'data-testid' set to 'TemperatureValues' and storing dates in 'temp' list  
for t in temps:
    temp.append(t.text[:-1])
#print(temp)

# removes 'Feels like' entries from 'temp' list. These are even entries in 'temp' list.
del temp[1::2]
#print(temp)

day_parent = soup.find('main', attrs={'id':'MainContent'}) # finds parent tag that contains all date tags
all_dates = day_parent.find_all(['h3']) # finds all 'h3' tags within the parent tag that contains all date tags  
for day in all_dates: # extracts dates from website by finding all 'h3' tag names and storing dates in 'dates' list 
    dates.append(day.text)
#print(dates)

# matches dates from 'dates' list with hours in 'hour' list so that the dates roll after 23:00 of each day. Saves the matched dates into 'date' list
datecount = 0
for hrz in range(0,len(hour)):
    date.append(dates[datecount])
    if hour[hrz] == '23:00':
        datecount = datecount + 1
    #print(hour[hrz], date[hrz])

curr_year = datetime.datetime.now().year #create current year variable to be used later to create full date

#add year to the end of date in the 'date' list
for d8 in range(0, len(date)):
    date[d8] = date[d8] + " " + str(curr_year)
    timestamp.append(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) # creates timestamp of time and date of the data update
#print(date)
#print(timestamp)

df = pd.DataFrame({'date': date, 'hour': hour, 'temp': temp, 'timestamp': timestamp}) # save date, hour & temp data as DataFrame
df['date'] = pd.to_datetime(df['date'], format='%A, %d %B %Y') # convert date from string to datetime64 format (i.e DD-MM-YYYY)
df['long_date'] = df['date'].astype(str) + " " + df['hour'] # combine entries from 'date' and 'hour' lists to store date + time as string in DD-MM-YYYY HH:MM format in new long_date column
df = df[['long_date','date','hour', 'temp', 'timestamp']] # re-order columns in 'df' pandas DataFrame

csv_file_path = '/Users/elchi/Dropbox/Coding/st_albans_hourly_weather_bs4.csv'

file_exists = os.path.exists(csv_file_path) # to check if csv file already exists before exporting the data into csv
# print(file_exists) # returns True if the file exists, False if the file doesn't exist
if file_exists: # if CSV file already exists, adds content of that CSV file to existing 'df' pandas DataFrame, then deletes CSV file, drops duplicate entries in 'df' DataFrame
    temp_df = pd.read_csv(csv_file_path) # copies content of CSV file into 'temp_df' pandas DataFrame
    os.remove(csv_file_path) # deletes CSV file
    df = pd.concat([df, temp_df]) # adds data from 'temp_df' pandas DataFrames to 'df' DataFrame 
    df = df.drop_duplicates(subset='long_date') # deletes duplicate entries in 'long_date' column of 'df' DataFrame 
df.to_csv(csv_file_path, index=False) # creates CSV file and paste all data from DataFrame


