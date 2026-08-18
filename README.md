# 💳 Credit Card Fraud Detection

A Machine Learning project for detecting fraudulent credit card transactions using **Random Forest** and a **Flask web application**.

## 📌 Project Overview

Credit card fraud is a major problem in financial transactions. The goal of this project is to build a machine learning model that can classify a transaction as:

- **0 → Normal Transaction**
- **1 → Fraudulent Transaction**

The trained model is integrated with a Flask web application where users can enter transaction features and receive a fraud prediction along with the fraud probability.

## 🎯 Objectives

- Analyze credit card transaction data
- Perform data preprocessing
- Handle class imbalance
- Train a Random Forest classifier
- Evaluate the model using ROC-AUC
- Analyze feature importance
- Save the trained model using Joblib
- Deploy the model through a Flask application

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Flask
- Jupyter Notebook
- Git & GitHub

## 🤖 Machine Learning Model

The main model used in this project is:

**Random Forest Classifier**

Different Random Forest configurations were evaluated using ROC-AUC.

### Model Results

| Model | ROC-AUC |
|---|---:|
| Random Forest (10, 10) | 0.98198 |
| Random Forest (20, 10) | **0.98283** |
| Random Forest (10, 15) | 0.96913 |

The best result was achieved by **Random Forest (20, 10)** with a ROC-AUC of approximately **0.983**.

## 🔍 Feature Importance

The most important features identified by the Random Forest model were:

| Feature | Importance |
|---|---:|
| V14 | 0.343992 |
| V17 | 0.158876 |
| V10 | 0.106096 |
| V12 | 0.090651 |
| V3 | 0.068347 |
| V4 | 0.062689 |
| V16 | 0.032864 |
| V2 | 0.030075 |
| V9 | 0.025051 |
| V18 | 0.008015 |

**V14** was the most influential feature in the trained model.

## 🌐 Flask Web Application

The trained machine learning model is integrated with a Flask web application.

The application:

1. Accepts transaction feature values
2. Sends the input to the trained model
3. Predicts whether the transaction is fraudulent
4. Displays the fraud probability

### Example Prediction

```text
Prediction: 0
Fraud Probability: 0.01846