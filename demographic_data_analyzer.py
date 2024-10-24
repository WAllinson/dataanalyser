import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    men = df[df['sex'] == 'Male']
    average_age_men = round(men['age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    edu = df['education'].value_counts()
    percentage_bachelors = round((edu['Bachelors']/edu.sum())*100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    degrees = ['Bachelors','Masters','Doctorate']
    higher = df[df['education'].isin(degrees)]
    lower = df[~df['education'].isin(degrees)]
    higher_education = round((higher.shape[0]/df.shape[0])*100, 1)
    lower_education = round((lower.shape[0]/df.shape[0])*100, 1)

    # percentage with salary >50K
    richhigher = higher[higher['salary'] == '>50K']
    richlower = lower[lower['salary'] == '>50K']
    higher_education_rich = round((richhigher.shape[0]/higher.shape[0])*100, 1)
    lower_education_rich = round((richlower.shape[0]/lower.shape[0])*100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df['hours-per-week'] == min_work_hours].shape[0]
    lazys = df[df['hours-per-week'] == min_work_hours]
    richlazys = (lazys[lazys['salary'] == '>50K']).shape[0]
    rich_percentage = round((richlazys/lazys.shape[0])*100, 1)

    # What country has the highest percentage of people that earn >50K?
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

    # Identify the most popular occupation for those who earn >50K in India.
    india = df[df['native-country'] == 'India']
    richIndia = india[india['salary'] == '>50K']
    top_IN_occupation = (richIndia['occupation'].value_counts()).index[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
