"""
CSE 163 Final Project
Question 3
This file filters the main dataset for relevant information to calculate
relevant statisitcs to answer the third question of our analysis. This file
creates functions that will produce a visualization and run tests for the code
contained in this file.
"""

# Imports
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()  
from dataset import final_df

# Filter dataset for relevant information
gender_df = final_df[['name', 'year', 'starring', 'gender']]
gender_df = gender_df.dropna()
test1_value = len(gender_df[gender_df['year'] == 1980])

# Find the number of stars for each Year
all_stars = gender_df.groupby('year', as_index=False)['starring'].count()
all_stars = all_stars.rename(columns={'starring': 'total'})

# Find the number of male and female stars for each year
gender_df = gender_df.groupby(['year', 'gender'],
                              as_index=False)['starring'].count()

# Combine dataframes
gender_df = gender_df.merge(all_stars, left_on='year',
                            right_on='year', how='left')

# Find the percentage of each gender in a starring role for each year
gender_df['prc'] = gender_df['starring'] / gender_df['total']

# Separate by gender
males = gender_df[gender_df['gender'] == 'male']
females = gender_df[gender_df['gender'] == 'female']
unknowns = gender_df[gender_df['gender'] == 'unknown']


# Create lineplot
def gender_plot():
    fig, ax = plt.subplots(1)
    sns.histplot(gender_df, x='year', hue='gender',
                 weights='prc', bins=39, multiple='stack')

    plt.xticks(rotation=45)

    plt.title('Percentage of Male vs. Female Stars in Movies')
    plt.xlabel('Year')
    plt.ylabel('Percentage in a Starring Role')

    fig.savefig('gender_plot.png')


def q3_tests():
    # Test accuracy of all_stars dataframe
    assert all_stars.loc[0, 'total'] == test1_value
    # Test accuracy of gender percentages
    assert (gender_df.loc[0, 'starring'] /
            gender_df.loc[0, 'total']) == gender_df.loc[0, 'prc']
    assert (gender_df.loc[110, 'starring'] /
            gender_df.loc[110, 'total']) == gender_df.loc[110, 'prc']


def main():
    gender_plot()
    q3_tests()


if __name__ == '__main__':
    main()
