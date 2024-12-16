import csv
import matplotlib.pyplot as plt
import math

deaths_compiled = {}
max_deaths = 0
max_deaths_date = ""

country_deaths = {}
max_country_deaths = 0 
min_country_deaths = 100000000
max_country_deaths_name = ""
min_country_deaths_name = ""

daily_deaths_max = 0 
daily_deaths_max_country = ""
daily_deaths_max_date = ""

dates = []
deaths_list = []

def date_get(date): 
    date_parts = date.split('/')
    
    month = date_parts[0]
    day = date_parts[1]
    year = date_parts[2]
    
    full_year = '20' + year
    year_month = full_year + "-" + month
    
    return year_month
    

with open('Users/eesha/data_global_data.csv', 'r') as fHandle:     
    csv_reader = csv.reader(fHandle)
    first_row = True
    
    for line in csv_reader: 

        if first_row: 
            first_row = False
            continue 
    
        country = line[0]     
        date = line[1]
        deaths = line[2]
        daily_deaths = line[3]

        deaths = int(deaths)
        daily_deaths = float(daily_deaths)

        year_month = date_get(date)

        if year_month not in deaths_compiled: 
            deaths_compiled[year_month] = 0 
        deaths_compiled[year_month] = deaths_compiled[year_month] + daily_deaths
            
        if country not in country_deaths: 
            country_deaths[country] = 0
        else: 
            country_deaths[country] = country_deaths[country] + daily_deaths
            
        if daily_deaths > daily_deaths_max: 
           daily_deaths_max = daily_deaths
           daily_deaths_max_country = country
           daily_deaths_max_date = date

for year_month in deaths_compiled: 
    total_deaths = deaths_compiled[year_month]
    if total_deaths > max_deaths: 
        max_deaths = total_deaths
        max_deaths_date = year_month
print(f'The maximum amount of deaths in a month occured on {max_deaths_date} with {max_deaths} deaths happening in that month.')

for country in country_deaths: 
    if country_deaths[country] > max_country_deaths: 
        max_country_deaths = country_deaths[country]
        max_country_deaths_name = country
    if country_deaths[country] < min_country_deaths and country_deaths[country] >= 10: 
        min_country_deaths = country_deaths[country]
        min_country_deaths_name = country
print(f'The maximum amount of deaths occured in {max_country_deaths_name} with {max_country_deaths} deaths occuring in that country.')
print(f'The minimum amount of deaths occured in {min_country_deaths_name} with {min_country_deaths} deaths occuring in that country. (Excluding countries where less than 10 deaths occured.)')

print(f'The maximum amount of daily deaths occured on {daily_deaths_max_date} in {daily_deaths_max_country} with {daily_deaths_max} deaths.')

with open('data_global_data.csv', 'r') as fHandle:
    csv_reader = csv.reader(fHandle)

    first_row = True
    
    for line in csv_reader:
        if first_row: 
            first_row = False
            continue 
        
        if line[0] == max_country_deaths_name:
            dates.append(line[1])
            deaths_list.append(float(line[3]))
            
len_dates = len(dates)
len_dates_split = math.ceil(len(dates)/11)

plt.figure(figsize=(12, 6))
plt.plot(dates, deaths_list, 'g-.')
plt.title(f"Daily Deaths in {max_country_deaths_name} Over Time")
plt.xlabel("Date")
plt.ylabel("Daily Deaths")
plt.xticks(ticks = range(0, len_dates, len_dates_split),rotation=0)
plt.show()