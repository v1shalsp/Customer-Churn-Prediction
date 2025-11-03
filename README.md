# 📉 Customer Churn Prediction
### *Predicting customer attrition using data-driven machine learning models*

---

## 🧠 Overview

The **Customer Churn Prediction** project aims to identify customers who are most likely to stop using a company’s service (churn) based on behavioral and demographic data.  
By analyzing customer usage patterns and historical churn behavior, this system enables companies to **take proactive retention actions** such as discounts, loyalty offers, or personalized outreach.

This is a **supervised classification problem**, solved using advanced **machine learning models** and evaluated using multiple performance metrics.

---

## 🎯 Objectives
- Identify key factors influencing customer churn.  
- Build and compare machine learning models for churn prediction.  
- Provide actionable business insights for retention strategies.  
- Visualize churn distribution and model interpretability.  

---

## ⚙️ Tech Stack

| Category | Tools / Libraries |
|-----------|------------------|
| **Language** | Python |
| **Data Handling** | Pandas, NumPy |
| **Visualization** | Matplotlib, Seaborn, Plotly |
| **Machine Learning** | Scikit-learn, XGBoost, Random Forest |
| **Evaluation** | ROC-AUC, F1-Score, Confusion Matrix, SHAP |
| **Environment** | Jupyter Notebook |

---

## 📊 Dataset

- Source: Simulated telecom dataset with 7,043 customers.  
- Target variable: `Churn` (1 → churned, 0 → retained)  
- Key features:
  - `gender`, `tenure`, `Contract`, `PaymentMethod`
  - `MonthlyCharges`, `TotalCharges`
  - `InternetService`, `TechSupport`, `StreamingTV`, etc.

---

## 🧩 Project Workflow

### 1️⃣ Data Preprocessing
- Handled missing values and outliers.  
- Encoded categorical variables (One-Hot / Label Encoding).  
- Scaled numerical features using `StandardScaler`.  
- Balanced classes using **SMOTE** to handle imbalance.

### 2️⃣ Exploratory Data Analysis (EDA)
- Examined churn distribution and feature correlations.  
- Identified patterns such as:
  - Customers with **month-to-month contracts** churn more frequently.  
  - **Senior citizens** and **low tenure users** are at higher risk.  
  - **Automatic payment methods** and **fiber internet** usage impact churn.  

### 3️⃣ Feature Engineering
- Derived new features:
  - `AverageMonthlySpend = TotalCharges / Tenure`
  - `EngagementScore = OnlineSecurity + TechSupport + StreamingTV`
- Removed multicollinear features using VIF & correlation matrix.

### 4️⃣ Model Training
Trained and fine-tuned several classification models:
- Logistic Regression  
- Decision Tree  
- Random Forest  
- XGBoost  

### 5️⃣ Model Evaluation
Compared models based on Accuracy, F1-Score, and ROC-AUC.

---

## 📈 Results

| Model | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
|--------|-----------|------------|----------|-----------|----------|
| Logistic Regression | 0.81 | 0.79 | 0.77 | 0.78 | 0.85 |
| Decision Tree | 0.83 | 0.82 | 0.80 | 0.81 | 0.88 |
| **Random Forest** | **0.86** | **0.84** | **0.83** | **0.83** | **0.91** |
| XGBoost | 0.85 | 0.83 | 0.82 | 0.82 | 0.90 |

✅ **Random Forest** emerged as the best performer with an **ROC-AUC of 0.91** and balanced precision-recall scores.

---

### 🧠 Feature Importance (Top Predictors)
- `ContractType` – Long-term contracts reduce churn probability.  
- `MonthlyCharges` – Higher monthly charges increase churn likelihood.  
- `Tenure` – Longer tenure customers are more loyal.  
- `TechSupport` – Access to support lowers churn risk.  

---

### 📉 Confusion Matrix (Random Forest)
| | Predicted: No | Predicted: Yes |
|--|---------------|----------------|
| **Actual: No** | 946 | 74 |
| **Actual: Yes** | 114 | 231 |

- Precision: **84%**  
- Recall: **83%**  
- F1-Score: **83%**

---

### 📊 ROC Curve
The ROC-AUC score of **0.91** indicates excellent model discrimination between churners and non-churners.

---

## 💡 Business Insights

- Customers with **month-to-month contracts** and **high monthly charges** are most likely to churn.  
- Offering **discounted long-term contracts** or **bundled services** can improve retention.  
- **Automatic payment options** correlate with customer loyalty.  
- Customers without **tech support** or **online security** show higher churn probability.

