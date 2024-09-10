import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df["race"].value_counts()

    # What is the average age of men?
    average_age_men = df.loc[df["sex"] == "Male", "age"].mean().round(1)

    # What is the percentage of people who have a Bachelor's degree?
    bachelors_filter = df.loc[df["education"] == "Bachelors"]
    total_bachelors = bachelors_filter.shape[0] #=5355

    total_people = df.shape[0] #=32561

    percentage_bachelors = ((total_bachelors / total_people) * 100)
    percentage_bachelors = round(percentage_bachelors, 1)
    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    advanced_education = ["Bachelors", "Masters", "Doctorate"]

    higher_education = df[df["education"].isin(advanced_education)].shape[0]
    lower_education = df[~df["education"].isin(advanced_education)].shape[0]

    # percentage with salary >50K
    df["salary"] = df["salary"].str.strip().str.lower()

    advanced_education_filter = df[df["education"].isin(advanced_education)]
    advanced_high_salary = advanced_education_filter[advanced_education_filter["salary"] == ">50k"]

    higher_education_rich = (advanced_high_salary.shape[0] / advanced_education_filter.shape[0]) * 100
    higher_education_rich = round(higher_education_rich, 1)  

    lower_education_filter = df[~df["education"].isin(advanced_education)]
    lower_education_high_salary = lower_education_filter[lower_education_filter["salary"] == ">50k"]

    lower_education_rich = (lower_education_high_salary.shape[0] / lower_education_filter.shape[0]) * 100
    lower_education_rich = round(lower_education_rich, 1) 

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df["hours-per-week"].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_hours_week = df["hours-per-week"].min()
    num_min_workers = df[df["hours-per-week"] == min_hours_week]
    min_salary = num_min_workers[num_min_workers["salary"] == ">50k"]
    rich_percentage = ((min_salary.shape[0] / num_min_workers.shape[0]) * 100) #10%
    
    # What country has the highest percentage of people that earn >50K?
    highest_salary = df[df["salary"] == ">50k"]
    highest_earning_country_counts = highest_salary["native-country"].value_counts()

    total_country_counts = df["native-country"].value_counts()

    percentage_high_earners = ((highest_earning_country_counts / total_country_counts) * 100)

    highest_earning_country =  percentage_high_earners.idxmax() 
    highest_earning_country_percentage = percentage_high_earners.max()
    highest_earning_country_percentage = round(highest_earning_country_percentage, 1)

    # Identify the most popular occupation for those who earn >50K in India.
    filter = df[(df["salary"] > "50k") & (df["native-country"] == "India")]
    ocupation = filter["occupation"].value_counts()

    most_popular_count = ocupation.max()

    top_IN_occupation =  ocupation.idxmax()

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
