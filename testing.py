import pandas as pd

df = pd.read_csv('adult.data.csv')
'''degrees = ['Bachelors','Masters','Doctorate']
higher = df[df['education'].isin(degrees)]
lower = df[~df['education'].isin(degrees)]
richhigher = higher[higher['salary'] == '>50K']
richlower = lower[lower['salary'] == '>50K']

min_work_hours = df['hours-per-week'].min()
lazys = df[df['hours-per-week'] == min_work_hours]
#print(lazys)
richlazys = (lazys[lazys['salary'] == '>50K']).shape[0]
richlazypercent = round((richlazys/lazys.shape[0])*100, 1)
print(richlazypercent)
origins = df['native-country'].value_counts()
countries = df['native-country'].unique()
highest_earning_country = ''
highest_earning_country_percentage = 0
for land in countries:
    temp = df[df['native-country'] == land]
    rich = temp[temp['salary'] == '>50K'].shape[0]
    if (round((rich/origins[land])*100, 1)) > highest_earning_country_percentage:
        highest_earning_country_percentage = round((rich/origins[land])*100, 1)
        highest_earning_country = land 
print(highest_earning_country)
print(highest_earning_country_percentage) '''
india = df[df['native-country'] == 'India']
richIndia = india[india['salary'] == '>50K']
bestIndiajob = (richIndia['occupation'].value_counts()).index[0]
print(bestIndiajob)
