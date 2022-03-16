"""
CSE 163 Final Project
Question 2
This file processes the all_movies dataset to train a DecisionTreeClassifier
model in order to answer the second question of our analysis. The program
will print out the accuracy score of the model and save a visualization of
the model's tree.
"""

from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.model_selection import train_test_split
from IPython.display import Image, display
import graphviz
import pandas as pd
from dataset import all_movies


def movie_classifier(data_set, max_depth):
    """
    Function takes in the all_movies dataframe and proccesses it for
    the sklearn tree classifier. The function then classifies each film
    in dataset as either are Succes or Failure based on whether the profit
    was greater than 0. The function splits data set randomly and trains
    a DecisionTreeClassifier model with max_depth(int). It then prints the
    accuracy score. The function then converts the model into dot data and
    plots it using graphviz ans saves the image as movie_tree.gv.png in the
    results folder.
    """

    # Data set is one_hot encoded
    proc_data = data_set.drop(columns=["name"])
    proc_data = proc_data.dropna()
    proc_data = pd.get_dummies(proc_data)

    # Profitabilty is determined whether the film's budget is greater than
    # or lesser than the budget
    proc_data["profitibility"] = proc_data["gross"] > proc_data["budget"]
    proc_data = proc_data.drop(columns=["gross"])
    proc_data["profitibility"] = \
        proc_data["profitibility"].replace(True, "Success")
    proc_data["profitibility"] = \
        proc_data["profitibility"].replace(False, "Failure")

    # Dataset is split into testing and training features and lables
    # and model is trained
    labels = proc_data["profitibility"]
    features = proc_data.loc[:, proc_data.columns != "profitibility"]
    features_train, features_test, labels_train, labels_test = \
        train_test_split(features, labels, test_size=0.2)
    movie_class = DecisionTreeClassifier(max_depth=max_depth)
    movie_class.fit(features_train, labels_train)

    # Testing dataset is compared to respective predictions and
    # accuracy score is printed
    predictions = movie_class.predict(features_test)
    print("Accuracy Score: " +
          str(accuracy_score(labels_test, predictions) * 100) + "%")

    # decision tree converted to dot_data and plotted using IPython.display
    dot_data = export_graphviz(
                movie_class, out_file=None,
                feature_names=features_train.columns,
                class_names=labels_train.unique(),
                impurity=False,
                filled=True, rounded=True, proportion=True,
                special_characters=True
                )
    graphviz.Source(dot_data) \
        .render("/home/results/movie_tree.gv", format="png")
    display(Image(filename="/home/results/movie_tree.gv.png"))


def main():
    max_depth = 4
    print("Max Depth for Classifier:", max_depth)
    movie_classifier(all_movies, max_depth=max_depth)


if __name__ == '__main__':
    main()
