# Sales Prediction - Rossmann
## Predicting sales to next six weeks

![](https://www.cxtoday.com/wp-content/uploads/2021/06/Sales-Forecasting-1280x720.jpg)

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

**Step 1 - Data Description**: use descriptive statistics to identify important or ususual behaviours in the data.
**Step 2 - Feature Engeering**: create or derive new variables to help better understand the phenomenon or to improve model performance.
**Step 3 - Feature Filtering**: filter the unnecessary variables and row in terms of information gain of that are outside the business' scope.
**Step 4 - Exploratory Data Analysis**: explore the data to find insights, to comprehend the variables' behaviour and their consequent impact on the model's learning. 
**Step 5 - Data Preparation**: use techniques to better prepare the data to the machine learning model. 
**Step 6 - Feature Selection**: select the features that contain the main information and attributes requeried from the model to learn the the phenomenon's behaviour. 
**Step 7 - Machine Learning Modelling**: machine learning model training and performance comparasion. 
**Step 8 - Churn Analysis**: analyse the churn probability of TopBank's customers
**Step 9 - Bussiness Report and Financial Impact**: find out what is the financial impact if the model is implemented to avoid customer churn.
**Step 10 - Deploy**: deploy the model in production. 

## 4. Top 3 Data Insights

**Hypothesis 1**: Stores with the closer competitors should sell less.

R: False, because stores with the closer competitors sell more.

**Hypothesis 2**: Stores should sell more throughout the years.

R: False, because stores should sell less throughout the years.

**Hypothesis 3**: Stores should sell more in the second semester of the year.

R: False, because they actually sell less in the second semester of the year.

## 5. Machine Learning Modelling 

The following classification algorithms were tested:

- Average Model
- Linear Regression
- Linear Regression - Lasso
- XGBoost Regressor

MAE, MAPE and RMSE were chosen as performance evalution metrics. The Random Forest Regressor was tested and had the best result between all the algorithms. However, this algorithm tends to require a large amount of memory space on the server in deployment, which might create a expressive cost to the company.

|     Model Name     |       MAE        |       MAPE         |     RMSE     |   
|--------------------|------------------|--------------------|--------------|
|    Average Model   |    1354.800353   |      0.455051      |  1835.135542 | 
|--------------------|------------------|--------------------|--------------|
|  Linear Regression |    1867.616829   |      0.292633      |  2672.508806 | 
|--------------------|------------------|--------------------|--------------|
|       Lasso        |    1892.200337   |       0.289065     |  2745.442033 |  
|--------------------|------------------|--------------------|--------------|
|  XGBoost Regressor |    6684.076383   |      0.949586      | 7331.191587  | 
|--------------------|------------------|--------------------|--------------|
|  Random  Forest    |    679.614332    |      0.100005      | 1014.247337  | 
|--------------------|------------------|--------------------|--------------|


## 6. Machine Learning Performance

The XGBoost Regressor was the chosen model because, after the hyperparameter fine-tunning, it presented a very satisfying result, close to the Random Forest Regressor's one, but with less memory space requeritment. 


|    Chosen Model    |       MAE        |       MAPE         |     RMSE     | 
|--------------------|------------------|--------------------|--------------|
|  XGBoost Regressor |    763.114913    |       0.1146       | 1095.543457  | 
|--------------------|------------------|--------------------|--------------|

## 7. Business Results
In the table below, it shows our XGBoost Regressor model's total performance in financial terms, after forecasting six weeks of sales.

|      Prediction     |    Best Scenario    |    Worst Scenario    |
|---------------------|---------------------|----------------------|
|   $286,046,123.11   |   $286,900,060.10   |   $285,192,186.12    |
 

## 8. Conclusions
## 9. Lessons Learned
## 10. To Improve