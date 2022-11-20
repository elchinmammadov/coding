import pandas as pd
from matplotlib import pyplot as plt # to use with 'plot' function
import seaborn as sns # to create Seaborn chart

df = pd.read_csv('/Users/elchi/Dropbox/Coding/st_albans_hourly_weather_bs4.csv') # create 'df' DataFrame using data in CSV file
df = df.drop(['timestamp', 'date', 'hour'], axis=1) # remove unnecessary columns from 'df' DataFrame
print(df.head())

# Plotting first 40 rows from df DataFrame using Seaborn
sns.set()
sns.barplot(
    x='long_date', 
    y='temp', 
    color='salmon', 
    data=df[0:40]
)
# Again, Matplotlib style formatting commands are used
# to customise the output details.
plt.xticks(rotation=60)
plt.xlabel("Date & time")
plt.ylabel("Degrees Celsius °C")
plt.title("Temperature in St Albans")
plt.gca().yaxis.grid(linestyle=':')



