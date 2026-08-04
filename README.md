# advertising-sales-prediction
📈 Advertising Sales Prediction using Machine Learning
# 📈 Advertising Sales Prediction using Machine Learning

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas)
![NumPy](https://img.shields.io/badge/NumPy-013243?logo=numpy)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-F7931E?logo=scikitlearn)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-FF4B4B?logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📖 Project Overview

Advertising plays a significant role in driving product sales. Companies invest in multiple advertising channels such as **TV**, **Radio**, and **Newspaper** to reach potential customers. Predicting sales based on advertising budgets helps businesses optimize marketing strategies and improve return on investment (ROI).

This project applies Machine Learning regression techniques to predict product sales using advertising expenditure. It covers the complete machine learning workflow, including data preprocessing, exploratory data analysis (EDA), feature engineering, model training, model evaluation, performance comparison, and deployment using Streamlit.

---

## 🎯 Business Problem

Marketing teams often face questions such as:

- Which advertising channel contributes the most to sales?
- How much should be invested in advertising?
- What sales can be expected from a given marketing budget?
- How can advertising ROI be improved?

This project provides a data-driven solution to answer these business questions.

---

## 🚀 Project Objectives

- Perform comprehensive Exploratory Data Analysis (EDA)
- Understand relationships between advertising channels and sales
- Train and compare multiple regression models
- Evaluate model performance using standard metrics
- Select the best-performing model
- Deploy the model with an interactive Streamlit application

---

## 📊 Dataset Information

| Feature | Description |
|---------|-------------|
| TV | TV Advertising Budget |
| Radio | Radio Advertising Budget |
| Newspaper | Newspaper Advertising Budget |
| Sales | Product Sales (Target Variable) |

---

## 🔄 Project Workflow

```
Business Understanding
        │
        ▼
Data Collection
        │
        ▼
Data Cleaning
        │
        ▼
Exploratory Data Analysis
        │
        ▼
Feature Engineering
        │
        ▼
Train-Test Split
        │
        ▼
Model Training
        │
        ▼
Model Evaluation
        │
        ▼
Model Comparison
        │
        ▼
Best Model Selection
        │
        ▼
Streamlit Deployment
```

---

## 📈 Exploratory Data Analysis

The project includes:

- Dataset Overview
- Data Types
- Statistical Summary
- Missing Value Analysis
- Duplicate Value Check
- Correlation Heatmap
- Pair Plot
- Distribution Analysis
- Scatter Plots
- Box Plots
- Business Insights

---

## 💡 Key Business Insights

- TV advertising has the strongest positive impact on sales.
- Radio advertising also contributes significantly to product sales.
- Newspaper advertising has comparatively lower influence.
- Increasing investment in effective advertising channels improves expected sales.
- Data-driven marketing decisions help maximize advertising ROI.

---

## ⚙️ Feature Engineering

The dataset was prepared through the following steps:

- Data Cleaning
- Duplicate Removal
- Correlation Analysis
- Feature Selection
- Train-Test Split
- Data Scaling (where applicable)

---

## 🤖 Machine Learning Models

The following regression models were trained and evaluated:

- Linear Regression
- Ridge Regression
- Lasso Regression
- ElasticNet Regression
- Decision Tree Regressor
- Random Forest Regressor
- Extra Trees Regressor
- Gradient Boosting Regressor
- AdaBoost Regressor

---

## 📊 Model Evaluation

Models were evaluated using:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score
- Cross Validation

The best-performing model was selected based on predictive accuracy and generalization performance.

---

## 📱 Streamlit Application

The project includes a user-friendly Streamlit application that allows users to:

- Enter TV advertising budget
- Enter Radio advertising budget
- Enter Newspaper advertising budget
- Predict expected product sales instantly
- View results in an intuitive interface

---

## 🛠️ Technologies Used

| Category | Technologies |
|----------|--------------|
| Programming Language | Python |
| Data Analysis | Pandas, NumPy |
| Data Visualization | Matplotlib, Seaborn |
| Machine Learning | Scikit-learn |
| Model Serialization | Joblib |
| Web Application | Streamlit |
| Development Environment | Jupyter Notebook, VS Code |

---

## 📂 Project Structure

```
advertising-sales-prediction/
│
├── README.md
├── LICENSE
├── requirements.txt
├── app.py
│
├── data/
│   └── advertising.csv
│
├── notebook/
│   └── Advertising_Spend_Regression.ipynb
│
├── models/
│   └── advertising_sales_model.pkl
│
└── images/
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/rakeshdas-analyst/advertising-sales-prediction.git
```

### Navigate to the Project Directory

```bash
cd advertising-sales-prediction
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Streamlit Application

```bash
streamlit run app.py
```

---

## 📌 Future Improvements

- Hyperparameter Optimization
- Advanced Feature Engineering
- Model Monitoring
- REST API Integration
- Cloud Deployment
- Docker Support
- CI/CD Pipeline

---

## 👨‍💻 Author

**Rakesh Das**

**Data Analyst | Machine Learning Enthusiast**

### Connect with Me

- 💼 **LinkedIn:** https://linkedin.com/in/rakesh-das-analyst
- 💻 **GitHub:** https://github.com/rakeshdas-analyst

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome. Feel free to fork this repository and submit a pull request.

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub. It helps others discover the project and supports my work.

---

## 📜 License

This project is licensed under the MIT License.

---

**Transforming advertising data into actionable business insights through Machine Learning.**
