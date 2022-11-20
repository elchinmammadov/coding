#BEAUTIFUL SOUP

import requests # import 'requests' library which is used to send HTTP requests using Python. It'll be used in conjunction with Beautiful Soup.
from bs4 import BeautifulSoup #imports Beautiful Soup. Use it if you don't need to click on parts of website to load data that you wanna webscrape
r = requests.get('https://weather.com/en-GB/weather/hourbyhour/l/St+Albans+England?canonicalCityId=969c164e50d945e77fcde5fe5e319b3650224764d4e98036ddac1b702738f186')
soup = BeautifulSoup(r.content, 'html5lib') # converts HTML website into Unicode then parses the whole document
print(soup.prettify()) # prints nested data structure of the parsed website
print(soup.contents[1].name) # prints second tag in parsed website
print(soup.title) # prints first 'title' tag
print(soup.h3) # prints first 'h3' tag
print(soup.div['id']) # prints first 'div' tag with 'id' attribute
print(soup.find('h2', attrs={'data-testid':'daypartName'})) # prints first 'h2' tag with 'data-testid' attribute set to 'daypartName'
print(soup.find_all('h2', attrs={'data-testid':'daypartName'})) # prints all 'h2' tags with 'data-testid' attribute set to 'daypartName'
#find_next_sibling
#find_next_siblings
#find_previous_sibling
#find_previous_siblings
#find_next
#find_previous
#find_all_next
#find_all_previous
#previous_element
#content
#contents
#children
#descendants
#parent
#parents
#next_sibling
#next_siblings
#previous_sibling
#previous_siblings
#previous_element
#next_element


#SELENIUM
# from selenium import webdriver  # to be able to go to website and copy the data
# from selenium.webdriver.common.by import By  # to be able to use By.XPATH and By.TAG_NAME with find_element()
# import pandas as pd  # to be able to store data in pandas DataFrame and export to CSV file
# import time  # to wait for certain number of seconds for webpage to load

# path = '/Users/elchi/Documents/Coding/Webscrapers/chromedriver'  # location of chromedriver file
# driver = webdriver.Chrome(path)  # creates new webdriver
# website = 'https://weather.com/en-GB/weather/hourbyhour/l/St+Albans+England?canonicalCityId=969c164e50d945e77fcde5fe5e319b3650224764d4e98036ddac1b702738f186'
# driver.get(website)  # opens the website in Chrome browser window

# time.sleep(15)  # waits for 15 secs for the webpage content to load. Otherwise, the code will return errors when capturing temperature data.

# matches = driver.find_elements(By.CLASS_NAME, 'HourlyForecast--DisclosureList--3CdxR') # finds table element by class name and stores results as a list
# all_dates = driver.find_elements(By.TAG_NAME, 'h3')  # extracts dates from website by finding all 'h3' tag names and storing dates in 'dates' list
# hours = driver.find_elements(By.XPATH, ".//h2[@data-testid='daypartName']")  # extracts hours from website by finding all 'h2' tag names with attribute 'data-testid' set to 'daypartName' and storing dates in 'hour' list

# driver.quit()  # closes Chrome browser window