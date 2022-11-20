# This python script imports hourly weather data for St Albans from www.weather.com  
# this version runs slower than Beautiful-Soup-based file called 'webscraper - hourly weather - bs4.py'

from selenium import webdriver  # to be able to go to website and copy the data
from selenium.webdriver.common.by import By  # to be able to use By.XPATH and By.TAG_NAME with find_element()
import pandas as pd  # to be able to store data in pandas DataFrame and export to CSV file
import time  # to wait for certain number of seconds for webpage to load

path = '/Users/elchi/Dropbox/Coding/Webscrapers/chromedriver'  # location of chromedriver file
driver = webdriver.Chrome(path)  # creates new webdriver
website = 'https://weather.com/en-GB/weather/hourbyhour/l/St+Albans+England?canonicalCityId=969c164e50d945e77fcde5fe5e319b3650224764d4e98036ddac1b702738f186'
driver.get(website)  # opens the website in Chrome browser window

time.sleep(15)  # waits for 15 secs for the webpage content to load. Otherwise, the code will return errors when capturing temperature data.

matches = driver.find_elements(By.CLASS_NAME, 'HourlyForecast--DisclosureList--3CdxR')  # finds table element by class name and stores results as a list

# creates empty lists to store table values
dates = [] # will store unique dates, which are about 2-3 per web page
date = [] # will store non-unique date values, which will be matched to individual hourly values in 'hour' list
hour = [] # will store hour values
temp = [] # will store temperature values

hours = driver.find_elements(By.XPATH, ".//h2[@data-testid='daypartName']")  # extracts hours from website by finding all 'h2' tag names with attribute 'data-testid' set to 'daypartName' and storing dates in 'hour' list
for hr in hours:
    hour.append(hr.text)
#print(hour)

temps = driver.find_elements(By.XPATH, ".//span[@data-testid='TemperatureValue']")  # extracts temperature from website by finding all 'span' tag names with attribute 'data-testid' set to 'TemperatureValues' and storing dates in 'temp' list  
for t in temps:
    temp.append(t.text)
#print(temp)

# removes 'Feels like' entries from 'temp' list. These are even entries in 'temp' list.
del temp[1::2]
#print(temp)

all_dates = driver.find_elements(By.TAG_NAME, 'h3')  # extracts dates from website by finding all 'h3' tag names and storing dates in 'dates' list
for day in all_dates:
   dates.append(day.text)
dates.pop(0) # remove the first blank entry from the 'date' list
#print(dates)

# matches dates from 'dates' list with hours in 'hour' list so that the dates roll after 23:00 of each day. Saves the matched dates into 'date' list
datecount = 0
for hrz in range(0,len(hour)):
    date.append(dates[datecount])
    if hour[hrz] == '23:00':
        datecount = datecount + 1
    #print(hour[hrz], date[hrz])

df = pd.DataFrame({'date': date, 'hour': hour, 'temp': temp}) # save date, hour & temp data as DataFrame
df.to_csv('st_albans_hourly_weather_selenium.csv', index=False) # create CSV file and paste all data from DataFrame

driver.quit()  # closes Chrome browser window