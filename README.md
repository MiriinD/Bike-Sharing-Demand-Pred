# Project: Bike Sharing Demand Prediction

## Overview:
This project aims to develop a time series forecasting model for predicting bike rental demand for a bike-sharing company. The goal is to leverage SARIMA (Seasonal AutoRegressive Integrated Moving Average) modeling to capture and forecast the temporal patterns in bike rental instances. The analysis will utilize bike rental data, corresponding hourly weather information, and potentially available Twitter data, to build an accurate predictive model for future demand. Furthermore, data analysis will be conducted to explore customer segments, and business trends, and analyze instances where rentals were never returned.<br>
<br>
Initial project pitch: https://www.canva.com/design/DAF9-DTMKvE/NcH5Xf8OVZC1G2t7HWnMpA/edit?utm_content=DA[…]m_campaign=designshare&utm_medium=link2&utm_source=sharebutton<br>

## Dataset Description:
1. <b>Bike Rental Dataset from Ecobici in Mexico City:</b> Contains detailed records of bike rental instances, including user demographics, bike identification, stations for departure and arrival, timestamps for rental and return, and associated variables.
2. <b>Hourly Weather Dataset:</b> Provides hourly weather information corresponding to the bike rental period, such as temperature, humidity, precipitation, and wind conditions.


## Objective:
The primary objective of this project is to develop an accurate SARIMA model to forecast bicycle rental demand based on historical bike usage patterns, weather conditions, and potentially supplemented with Twitter data. The project encompasses the following key components:
- <b>Exploratory Data Analysis (EDA)</b> to understand the characteristics of the bike rental and weather datasets.
- <b>Data Preprocessing and Feature Engineering</b> by integrating and aligning the bike rental and weather data for modeling purposes.
- <b>SARIMA Modeling</b> to capture and forecast the temporal patterns in bike rental demand, accounting for seasonal variations and external factors.
- <b>Model Evaluation</b> to assess the accuracy and reliability of the forecasting model using appropriate metrics and visualization techniques.

## Deliverables:
1. <b>SARIMA Forecasting Model:</b> A trained SARIMA model that can predict hourly bike rental demand based on historical usage patterns and related factors.
2. <b>Visualization and Insights:</b> Visual representations and insights about the temporal dynamics and seasonal patterns in bike rental demand, as well as customer segments and business trends.
3. <b>Comprehensive Data Analysis:</b> Insights derived from analyzing customer segments, business trends.
4. <b>Project Presentation:</b> A presentation outlining the methodology & findings, demonstrating the predictions, and providing recommendations arising from the modeling and analysis.

## Technologies and Tools:
- <b>Python:</b> Primary programming language for data analysis, modeling, and visualization.
- <b>Pandas, NumPy, Matplotlib, Seaborn:</b> Libraries for data manipulation, numerical computing, and data visualization.
- <b>statsmodels:</b> Library for performing SARIMAX modeling and time series analysis.
- <b>Jupyter Notebooks:</b> Integrated development environment for exploratory data analysis and model building.

## Outcome and Impact:
The successful development of an accurate SARIMAX forecasting model will provide the bike-sharing company with actionable insights for optimizing bike deployment, resource allocation, and service efficiency. Additionally, the project aims to facilitate better operational and strategic decision-making through a deeper understanding of the temporal dynamics in bike rental demand.

### Contributors:
 - Miriam Godinez
 - Flora Kwong

### Acknowledgements:
Data sourced from open data from [Mexico City's EcoBici program](https://www.kaggle.com/datasets/fernandonuez/ecobici-ciudad-de-mexico-julio-2019-a-junio-2021?resource=download)
Weather data obtained from [Open Meteo](https://open-meteo.com/)

