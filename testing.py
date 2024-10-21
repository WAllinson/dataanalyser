import pandas as pd

df = pd.read_csv('adult.data.csv')
men = df[df['sex'] == 'Male']
print(round(men['age'].mean(), 1))