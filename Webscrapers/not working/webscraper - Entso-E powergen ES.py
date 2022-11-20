# instructions from https://www.geeksforgeeks.org/implementing-web-scraping-python-beautiful-soup/

#Python program to scrape website
#and save quotes from website
import requests
from bs4 import BeautifulSoup
import csv

URL = "https://transparency.entsoe.eu/generation/r2/actualGenerationPerProductionType/show?name=&defaultValue=false&viewType=TABLE&areaType=BZN&atch=false&datepicker-day-offset-select-dv-date-from_input=D&dateTime.dateTime=28.11.2021+00:00|CET|DAYTIMERANGE&dateTime.endDateTime=28.11.2021+00:00|CET|DAYTIMERANGE&area.values=CTY|10YES-REE------0!BZN|10YES-REE------0&productionType.values=B01&productionType.values=B02&productionType.values=B03&productionType.values=B04&productionType.values=B05&productionType.values=B06&productionType.values=B07&productionType.values=B08&productionType.values=B09&productionType.values=B10&productionType.values=B11&productionType.values=B12&productionType.values=B13&productionType.values=B14&productionType.values=B20&productionType.values=B15&productionType.values=B16&productionType.values=B17&productionType.values=B18&productionType.values=B19&dateTime.timezone=CET_CEST&dateTime.timezone_input=CET+(UTC+1)+/+CEST+(UTC+2)"

r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')

quotes=[] # creates a list to store quotes

table1 = soup.find('div', attrs = {'id':'dv-data-table'}) # finds first 'div' tag where id = 'dv-data-table'

table2 = table1.find_all('span', 'bold') # finds all children 'span' tags (within 'div' tag where id = 'dv-data-table') where 'class' = 'bold'

colheads = [] # creates list to store names of column headers of the data table
for x in range(2, len(table2)):
	colheads.append(table2[x].get_text(strip=True)) # gets column headers of the data table. Ignores the first two entries of 'span' tags where 'class' = 'bold' and displays the rest of content of those tags as text
print(colheads) # shows stored column headers of the data table


table3 = table1.find_all('td', 'dv-value-cell') # finds all children 'td' tags (within 'div' tag where id = 'dv-data-table') where 'class' = 'dv-value-cell'
print(table3)

rowvalues = []
for y in table3:
	rowvalue = {} # create empty dictionary to store values
	rowvalue ['ACTUAL_OUTPUT'] = y.span['class'] # CAN'T figure out how to pull in numeric value for power OUTPUT
	### !!! CONTINUE CODING HERE....
	rowvalues.append(rowvalue) # gets row headers of the data table. Ignores the first two entries of 'td' tags where 'class' = 'first' and displays the rest of content of those tags as text
print(rowvalues) # shows stored row headers of the data table




table4 = table1.find_all('td', 'first') # finds all children 'td' tags (within 'div' tag where id = 'dv-data-table') where 'class' = 'first'

rowheads = [] # creates list to store names of row headers of the data table
for z in table4:
	rowheads.append(z.get_text(strip=True)) # gets row headers of the data table. Ignores the first two entries of 'td' tags where 'class' = 'first' and displays the rest of content of those tags as text
print(rowheads) # shows stored row headers of the data table