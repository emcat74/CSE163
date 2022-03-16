"""
CSE 163 Final Project
This file merges together the datasets used for our analysis.
"""
import pandas as pd

# Filter gender dataset for appropiate columns
gender = pd.read_csv("/home/data/gender.csv")
gender = gender[["name", "starring", "gender"]]

all_movies = pd.read_csv("/home/data/movies.csv")
all_movies = all_movies[["name", "rating", "genre", "year", "score",
                         "budget", "gross", "runtime"]]
all_movies = all_movies[all_movies["year"] <= 2018]

final_df = all_movies.merge(gender, left_on="name",
                            right_on="name", how="left")
