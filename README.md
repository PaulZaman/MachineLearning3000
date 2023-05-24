# Machine Learning to explain the price of electricity

## Authors

👨‍💻 Paul Zamanian
👨‍💻 Matthieu Vichet
👨‍💻 Benjamin Rossignol

## Summary

This project aims to explain the price of electricity in France and Germany and predict its future prices. We will analyze various factors that influence electricity prices and develop machine learning models to understand and predict these prices accurately.

## Table of Contents

1. Introduction
2. Data Description
3. Data Preparation
   - Removing Empty Cells
   - Categories
   - Normalizing the Data
   - Removing Outliers
   - Correlation
   - Feature Selection
   - Target Variable Analysis
   - Testing and Training Data
4. Data Modelling and Evaluation
   - Creating the Models
   - Training the Models
   - Making Predictions
   - Evaluating the Models
   - Hyperparameter Tuning
   - Feature Importance
5. Conclusion

## Introduction

📅 As of 2023, the price of electricity has been steadily rising for the past 10 years. This increase has posed a significant challenge for the population in France. Understanding the factors driving these price fluctuations is crucial for finding effective solutions. In this project, we aim to explain the price of electricity in France and Germany while also predicting its future prices. By addressing questions such as the main factors influencing electricity prices and forecasting future prices, we hope to provide valuable insights into this complex subject.

## Data Description

📊 The project utilizes three datasets:

1. Data_X: This dataset contains daily prices of various commodities in France and Germany over approximately 1,000 days. It includes 35 columns, covering aspects such as energy consumption, energy exchange between countries, energy production by source, weather data, and prices of gas, coal, and carbon.

2. Data_Y: This dataset represents the electricity price data corresponding to the IDs in Data_X. We will train our model on Data_X and predict electricity prices using Data_Y.

3. DataNew_X: This dataset is similar to Data_X but contains data for different days. It serves as the testing data for our prediction.
