# Credit Card Fraud Detection

A Machine Learning project that predicts whether a credit card transaction is fraudulent or normal.

## Project Overview

Credit card fraud detection is a binary classification problem where the goal is to identify whether a transaction is:

- 0 → Normal transaction
- 1 → Fraudulent transaction

This project uses Machine Learning to detect fraudulent transactions from transaction data.

## Dataset

The project uses the Credit Card Fraud Detection dataset.

The dataset contains transaction-related features and a target column called `Class`.

### Features

- `Time` → Time elapsed between transactions
- `V1` to `V28` → Anonymized transaction features
- `Amount` → Transaction amount
- `Class` → Target variable
  - `0` → Normal transaction
  - `1` → Fraudulent transaction

  ## Machine Learning Workflow

The project follows these steps:

1. Load the dataset
2. Explore and understand the data
3. Check missing values and class distribution
4. Split the data into training and testing sets
5. Handle class imbalance using SMOTE
6. Train Logistic Regression
7. Train Random Forest
8. Evaluate both models
9. Perform hyperparameter tuning
10. Analyze feature importance
11. Save the best trained model
12. Deploy the model using Flask

## Data Preprocessing

The following preprocessing steps were performed:

- Checked the dataset shape and data types
- Checked for missing values
- Checked the class distribution
- Separated features (`X`) and target (`y`)
- Split the dataset into training and testing sets
- Applied SMOTE to balance the training data

## Machine Learning Models

Two machine learning algorithms were trained and compared:

### 1. Logistic Regression

Logistic Regression was used as a baseline classification model.

Results:

- Precision: 13.41%
- Recall: 89.80%
- ROC-AUC: 97.65%

### 2. Random Forest

Random Forest was trained to improve the classification performance.

Results:

- Precision: 41.95%
- Recall: 87.76%
- ROC-AUC: 98.20%

Random Forest performed better overall than Logistic Regression based on the evaluation metrics.

## Hyperparameter Tuning

Hyperparameter tuning was performed on the Random Forest model by testing different combinations of:

- `n_estimators`
- `max_depth`

The tested configurations were:

| Configuration | ROC-AUC |
|---|---:|
| 10 trees, depth 10 | 0.98198 |
| 20 trees, depth 10 | 0.98283 |
| 10 trees, depth 15 | 0.96913 |

The best tested configuration was:

- `n_estimators = 20`
- `max_depth = 10`
- ROC-AUC = 0.98283

## Feature Importance

Random Forest feature importance was used to identify the features that contributed most to the model's predictions.

The top important features were:

| Feature | Importance |
|---|---:|
| V14 | 0.34399 |
| V17 | 0.15888 |
| V10 | 0.10610 |
| V12 | 0.09065 |
| V3 | 0.06835 |

V14 was the most important feature according to the trained Random Forest model.

Since V1 to V28 are anonymized features, feature importance indicates predictive contribution and does not imply that a feature is a direct cause of fraud.

## Model Deployment

The trained Random Forest model was saved using Joblib and deployed using Flask.

The Flask application:

1. Loads the saved Random Forest model.
2. Accepts transaction features from the web form.
3. Sends the input data to the trained model.
4. Predicts whether the transaction is normal or fraudulent.
5. Displays the fraud probability to the user.

### Prediction Output

- `0` → Normal Transaction
- `1` → Fraudulent Transaction

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Imbalanced-learn
- Matplotlib
- Joblib
- Flask
- HTML
- CSS

## Installation

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
cd Fraud_Detection

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

python app.py

http://127.0.0.1:5000

## Results

The models were evaluated using Precision, Recall and ROC-AUC.

| Model | Precision | Recall | ROC-AUC |
|---|---:|---:|---:|
| Logistic Regression | 13.41% | 89.80% | 97.65% |
| Random Forest | 41.95% | 87.76% | 98.20% |

Random Forest achieved better overall performance, especially in terms of Precision and ROC-AUC.

The best tested Random Forest configuration was:

- `n_estimators = 20`
- `max_depth = 10`
- ROC-AUC = 0.98283

## Conclusion

This project demonstrates how Machine Learning can be used to detect fraudulent credit card transactions.

The dataset was highly imbalanced, so SMOTE was applied to the training data. Logistic Regression was used as a baseline model and Random Forest was used as a stronger ensemble model.

After evaluation and hyperparameter tuning, Random Forest was selected as the final model. The trained model was saved using Joblib and deployed using Flask to provide a web-based fraud prediction system.

The final application can classify a transaction as either Normal or Fraud and also provides the estimated fraud probability.

## Project Structure

```text
Fraud_Detection/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   └── creditcard.csv
│
├── models/
│   └── fraud_detection_model.pkl
│
├── notebook/
│   └── fraud_detection.ipynb
│
├── src/
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css