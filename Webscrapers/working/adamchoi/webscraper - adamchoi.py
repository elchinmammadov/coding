# instructions from https://www.youtube.com/watch?v=UOsRrxMKJYk&t=8s

from selenium import webdriver  # to be able to go to website and copy the data
from selenium.webdriver.common.by import By  # to be able to use By.XPATH and By.TAG_NAME with find_element()
from selenium.webdriver.support.ui import Select  # to be able to select country from dropdown
import pandas as pd  # to be able to store data in pandas DataFrame and export to CSV file
import time  # to wait for certain number of seconds for webpage to load

path = '/Users/elchi/Dropbox/Coding/Webscrapers/chromedriver'  # location of chromedriver file
driver = webdriver.Chrome(path)  # creates new webdriver
website = 'https://www.adamchoi.co.uk/overs/detailed'
driver.get(website)  # opens the website in Chrome browser window

all_matches_button = driver.find_element(By.XPATH, '//label[@analytics-event="All matches"]')
all_matches_button.click()  # clicks on 'All matches' button on the website


dropdown = Select(driver.find_element(By.ID, 'country'))
dropdown.select_by_visible_text('Spain')  # goes to 'Select Country' dropdown and clicks on Spain 

time.sleep(5)  # waits for 5 secs for the webpage content to load after selecting country from dropdown. Otherwise, the code will capture blank data

matches = driver.find_elements(By.TAG_NAME, 'tr')  # finds table element by tag name and stores results as a list

# creates empty lists to store table values
date = []
home_team = []
score = []
away_team = []

for match in matches:
	#print(match.text)
	date.append(match.find_element(By.XPATH, './td[1]').text)  # stores values from column 1 in 'date' list
	home_team.append(match.find_element(By.XPATH, './td[2]').text)  # stores values from column 1 in 'home_team' list
	score.append(match.find_element(By.XPATH, './td[3]').text)  # stores values from column 1 in 'score' list
	away_team.append(match.find_element(By.XPATH, './td[4]').text)  # stores values from column 1 in 'away_team' list

df = pd.DataFrame({'date': date, 'home_team': home_team, 'score': score, 'away_team': away_team})
df.to_csv('football_scores.csv', index=False)

driver.quit()  # closes Chrome browser window 