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
print(richlazypercent)'''

for country in df['native-country']:
    print(country)