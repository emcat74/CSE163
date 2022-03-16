"""
CSE 163 Final Project
Question 1
This file filters the main dataset for relevant information to calculate
relevant statisitcs to answer the first question of our analysis. This file
creates functions that will produce 3 visualization and run t-tests to spot
any trends within certain movie characteristics over the years.
"""

# Imports
from dataset import final_df
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
sns.set()


# Create lineplot to see the trends of runtime over the years
def runtime_plot():
    print(final_df['runtime'].mean())
    fig, ax = plt.subplots(1)
    sns.lineplot(ax=ax, x='year', y='runtime', data=final_df,
                 color='blue', label='runtime')
    plt.title('Runtime changes over the years')
    plt.xlabel('Year')
    plt.ylabel('Average Runtime of the movies')
    plt.legend()

    fig.savefig('runtime_plot.png')


# Create lineplot to see the trend of budget over the years
def budget_plot():
    fig, ax = plt.subplots(1)
    sns.lineplot(ax=ax, x='year', y='budget', data=final_df,
                 color='blue', label='budget')
    plt.title('Budget changes over the years')
    plt.xlabel('Year')
    plt.ylabel('Average budget of the movies (in 10 millions)')
    plt.legend()

    fig.savefig('budget_plot.png')


# Create lineplot to see the trends of gross rate over the years
def gross_plot():
    fig, ax = plt.subplots(1)
    sns.lineplot(ax=ax, x='year', y='gross', data=final_df,
                 color='blue', label='gross')
    plt.title('Gross rating changes over the years')
    plt.xlabel('Year')
    plt.ylabel('Average gross rating of the movies')
    plt.legend()

    fig.savefig('gross_plot.png')


# Filter dataset for relevant information
df_2018 = final_df[final_df["year"] == 2018]
df_1980 = final_df[final_df["year"] == 1980]
df_2018 = df_2018.dropna(subset=['budget', 'gross'])
df_1980 = df_1980.dropna(subset=['budget', 'gross'])


# Runs t-tests to test statistical significance of runtime, gross and budget
def tests():
    test1 = stats.ttest_ind(df_2018['runtime'],
                            df_1980['runtime'], equal_var=False)
    print("Runtime t-test")
    print(test1)
    test2 = stats.ttest_ind(df_2018['budget'],
                            df_1980['budget'], equal_var=False)
    print("Budget t-test")
    print(test2)
    test3 = stats.ttest_ind(df_2018['gross'],
                            df_1980['gross'], equal_var=False)
    print("Gross t-test")
    print(test3)


# main method to call other functions
def main():
    runtime_plot()
    budget_plot()
    gross_plot()
    tests()


if __name__ == '__main__':
    main()
