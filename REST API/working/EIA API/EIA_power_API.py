# Daily net generation by balancing authority and energy source. Source: Form EIA-930 Product: Hourly Electric Grid Monitor. Data link: https://api.eia.gov/v2/electricity/rto/daily-fuel-type-data/data/?frequency=daily&data[0]=value&facets[respondent][]=US48&facets[timezone][]=Eastern&sort[0][column]=period&sort[0][direction]=desc&offset=0&length=5000
# Daily demand and net generation by balancing authority. Source: Form EIA-930 Product: Hourly Electric Grid Monitor. Data link: https://api.eia.gov/v2/electricity/rto/daily-region-data/data/?frequency=daily&data[0]=value&facets[respondent][]=US48&facets[timezone][]=Eastern&facets[type][]=D&facets[type][]=NG&sort[0][column]=period&sort[0][direction]=desc&offset=0&length=5000

# TODO: hide API key

import pandas as pd
import requests # to request/download data via API
from datetime import datetime, timedelta # to break up start & end dates into smaller monthly intervals
from dateutil import rrule # to break up start & end dates into smaller monthly intervals
from dateutil.relativedelta import relativedelta # to break up start & end dates into smaller monthly intervals

# declare variables
start_date = datetime(2019, 11, 1) # start date for downloading data
end_date = datetime(2022, 1, 1) # end date for downloading data
startDates = [] # list to store start dates
endDates = [] # list to store end dates
list_data = [] # list to store data downloaded via API in json format
api_key = 'q6uV6bK4CBECvdpqyeQ6CvldEcQazws5pSJqaw6D'

def API_function(start_date, end_date, list_data):
    # Download raw data using API
    URL = 'https://api.eia.gov/v2/electricity/rto/daily-fuel-type-data/data/?api_key=' + api_key + '&frequency=daily&data[0]=value&facets[respondent][]=US48&facets[timezone][]=Eastern&start=' + start_date.strftime('%Y-%m-%d') + '&end=' + end_date.strftime('%Y-%m-%d') + '&sort[0][column]=period&sort[0][direction]=desc&offset=0&out=json' # convert datetime format (e.g. '2019, 1, 1') to string format (e.g. '2019-01-01') for start and end dates so that these can be understood by this API request
    #URL = 'https://api.eia.gov/v2/electricity/rto/daily-region-data/data/?api_key=' + api_key + '&frequency=daily&data[0]=value&facets[respondent][]=US48&facets[timezone][]=Eastern&facets[type][]=D&facets[type][]=NG&sort[0][column]=period&start=' + start_date.strftime('%Y-%m-%d') + '&end=' + end_date.strftime('%Y-%m-%d') + '&sort[0][direction]=desc&offset=0&out=json' # convert datetime format (e.g. '2019, 1, 1') to string format (e.g. '2019-01-01') for start and end dates so that these can be understood by this API request
    #URL = 'https://api.eia.gov/series/?series_id=PET.MCRRIP12.M&api_key=q6uV6bK4CBECvdpqyeQ6CvldEcQazws5pSJqaw6D&out=json'
    #URL = 'http://api.eia.gov/category/?api_key=q6uV6bK4CBECvdpqyeQ6CvldEcQazws5pSJqaw6D&category_id=3&out=json'
    #URL = 'https://api.eia.gov/v2/electricity/retail-sales&api_key=q6uV6bK4CBECvdpqyeQ6CvldEcQazws5pSJqaw6D&out=json'
    headers = {'Accept-Encoding': 'identity'}
    r = requests.get(URL, headers=headers)
    json_data = r.json()

    # convert json data format to pandas DataFrame, then extract data as 'temp_list_data' list of dictionaries, then append to 'list_data' list of dictionaries and return it
    df_json = pd.DataFrame(json_data)
    temp_list_data = df_json.at['data', 'response']
    list_data.append(temp_list_data) 
    return list_data

# because each API request is limited to 5000 rows, I need to split the API request into several smaller chunks by creating a code to loop through start & end dates in 1-month increments.
for dt in rrule.rrule(rrule.MONTHLY, dtstart=start_date, until=end_date): # create 'startDates' list and 'endDates' list by looping through start & end dates in monthly increments
    startDates.append(dt) # add start-of-month date to 'startDates' list
    dt = dt + relativedelta(months=+1, days=-1) # calculate end of month date
    endDates.append(dt) # add end-of-month date to 'endDates' list
for start, end in zip(startDates, endDates): # runs 'API_function' function request for each pair of start and end dates stored in 'startDates' and 'endDates' lists and saves the result of each request it to 'list_data' list
    list_data = API_function(start, end, list_data)

# convert data from list of dictionaries format to pandas DataFrame format
col_names = list_data[0][0].keys() # create list of column names as 'col_names' dictionary
col_names = list(col_names) # convert 'col_names' dictionary to list
list_data = [item for sublist in list_data for item in sublist] # flatten 'list_data' list of lists of dictionaries into 'list_date' list of dictionaries in order to be able to parse it in creating a 'df' DataFrame below
df = pd.DataFrame(list_data, columns=col_names) # convert 'list_data' list of dictionaries to 'df' pandas DataFrame
df