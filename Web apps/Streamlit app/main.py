import streamlit as st
import pandas as pd

header = st.container() # containers are like sections of rows rather than columns
dataset = st.container()
features = st.container()
model_training = st.container()

with header:
    st.title('Welcome to my awesome data science project') # adds title to the 'header' container on the HTML page
    st.text('In this project I look into transactions of taxis in NYC') # adds text to the 'header' container on the HTML page


with dataset:
    st.header('NYC taxi dataset') # adds header to the 'dataset' container on the HTML page
    st.text('found this dataset on blablabla.com')
    taxi_data = pd.read_csv('data/taxi_data.csv') # creates 'taxi_data' Pandas DataFrame using data from 'taxi_data.csv' file
    st.write(taxi_data.head()) # shows 'taxi_data' data on HTML page

    # creates a bar chart of location distibution for first 50 entries in 'taxi_data' DataFrame
    st.subheader('Pick-up location ID distribution on the NYC dataset') # adds sub-header 
    pulocation_dist = pd.DataFrame(taxi_data['PULocationID'].value_counts()).head(50) # creates 'pulocation_dist' DataFrame using 'PULocationID' and first 50 rows of 'taxi_data' DataFrame
    st.bar_chart(pulocation_dist)

with features:
    st.header('The features that I created')

    st.markdown('* **first feature:** I created this feature because of this... I calculated it using this logic...')
    st.markdown('* **second feature:** I created this feature because of this... I calculated it using this logic...')

with model_training:
    st.header('Time to train the model')
    st.text('Here you get to choose the hyperparameters of the model and see how the performance changes')

    sel_column, disp_column = st.columns(2) # creates two columns

    max_depth = sel_column.slider('What should be the max_depth of the model?', min_value=10, max_value=100, value=20, step=10) # creates a slider
    n_estimators = sel_column.selectbox('How many trees should there be?', options=[100, 200, 300, 'No limit'], index=0) # creates select box
    input_feature = sel_column.text_input('Which feature should be used as the input feature?', 'PULocationID') # creates text box for users to input values
    
