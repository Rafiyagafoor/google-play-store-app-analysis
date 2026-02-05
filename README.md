# Google Play Store App Analysis (EDA, Machine Learning, Tableau)

## Overview

This project analyzes the Google Play Store applications dataset using Exploratory Data Analysis, Machine Learning, and Tableau visualization.
The objective is to understand factors affecting app popularity, analyze category trends, and predict the number of installs.

## Tools and Technologies


+ Python
+ Pandas
+ NumPy
+ Matplotlib
+ Seaborn
+ scikit-learn
+ Tableau
+ Jupyter Notebook / VS Code


## Exploratory Data Analysis


The exploratory data analysis phase focused on understanding the structure and patterns in the dataset.
Key steps included dataset cleaning, handling missing values, analyzing the distribution of ratings and installs, and studying relationships between installs, reviews, rating, and price.
A comparison between free and paid applications was also performed to understand monetization trends.
## Machine Learning Implementation


Objective
The goal of the machine learning model was to predict the number of installs for a Google Play Store application.
Features Used
Rating
Reviews
Price
Models Applied
Multiple Linear Regression was used as the baseline model.
Random Forest Regressor was used as a comparison model.
Evaluation Metrics
Mean Absolute Error
R squared score
The Random Forest Regressor achieved better performance compared to Multiple Linear Regression.
## Tableau Dashboard


An interactive Tableau dashboard was created to visualize key insights from the dataset.
Insights Covered
Top app categories by count
Free vs paid apps by category
User engagement using reviews and ratings
Content rating versus reviews
Files Included
google_playstore_dashboard.png contains the dashboard preview image.
google_playstore_dashboard.twbx contains the packaged Tableau workbook.
## Conclusion


This project demonstrates an end to end data analytics workflow using exploratory data analysis, machine learning, and data visualization.
Ratings, reviews, and price were identified as important factors affecting app installs.
The integration of Tableau enhances insight communication and supports data driven decision making.
