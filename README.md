# Sales Prediction - Rossmann
## Predicting sales to next six weeks

[](https://www.cxtoday.com/wp-content/uploads/2021/06/Sales-Forecasting-1280x720.jpg)

Source: [CX Today](https://www.cxtoday.com/contact-centre/what-is-sales-forecasting/)


## 1. Business Problem

Rossmann operates over 3,000 drug stores in 7 European countries. Store sales are influenced by many factors, including promotions, competition, school and state holidays, seasonality, and locality.
Rossmann's CFO requested a daily sales prediction for each store for the next six weeks in advance in order to elaborate a budget plan for the stores' infraestructure renovation. Our goal is to create a machine learning model capable to deliver accurate sales forecast as well as able to be easily access by the CFO through a Telegram bot.

To accessa the dataset, click [here](https://www.kaggle.com/c/rossmann-store-sales).   

## 2. Business Assumptions

* Only consider open store days
* Days without sales were not included
* For stores that did not have the competition distance information available, it was adopted the longest distance registered in the dataset. 

## 3. Solution Strategy
The solution was based upon the following strategy:

1. **Step 1 - Data Description**: use descriptive statistics to identify important or ususual behaviours in the data.
2. **Step 2 - Feature Engeering**: create or derive new variables to help better understand the phenomenon or to improve model performance.
3. **Step 3 - Feature Filtering**: filter the unnecessary variables and row in terms of information gain of that are outside the business' scope.
4. **Step 4 - Exploratory Data Analysis**: explore the data to find insights, to comprehend the variables' behaviour and their consequent impact on the model's learning. 
5. **Step 5 - Data Preparation**: use techniques to better prepare the data to the machine learning model. 
6. **Step 6 - Feature Selection**: select the features that contain the main information and attributes requeried from the model to learn the the phenomenon's behaviour. 
7. **Step 7 - Machine Learning Modelling**: machine learning model training and performance comparasion. 
8. **Step 8 - Churn Analysis**: analyse the churn probability of TopBank's customers
9. **Step 9 - Bussiness Report and Financial Impact**: find out what is the financial impact if the model is implemented to avoid customer churn.
10. **Step 10 - Deploy**: deploy the model in production. 

## 4. Top 3 Data Insights

**Hypothesis 1**: Stores with the closer competitors should sell less.

R: False, because stores with the closer competitors sell more.

**Hypothesis 2**: Stores should sell more throughout the years.

R: False, because stores should sell less throughout the years.

**Hypothesis 3**: Stores should sell more in the second semester of the year.

R: False, because they actually sell less in the second semester of the year.

## 5. Machine Learning Modelling Application



## 6. Machine Learning Performance
## 7. Business Results
## 8. Conclusions
## 9. Lessons Learned
## 10. To Improve