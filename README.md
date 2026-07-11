# 🌊 Flood Risk Prediction System

## 📌 Overview

The Flood Risk Prediction System is a Machine Learning-based web application that predicts the probability of flooding using environmental and infrastructure-related parameters.

The system uses a **Linear Regression** model trained on a dataset containing over **1.1 million records** and **20 environmental features**. Users can interactively enter environmental conditions through a Streamlit dashboard to estimate flood probability and receive risk-level recommendations.

This project demonstrates the complete Machine Learning workflow, including data preprocessing, model training, evaluation, and deployment.

---

## 🎯 Objectives

- Predict flood probability using Machine Learning.
- Provide an interactive dashboard for users.
- Classify flood risk into Low, Moderate, and High categories.
- Demonstrate practical application of regression algorithms.

---
## Dataset

The dataset used for this project is too large to be stored in this GitHub repository.

You can download it from:

**Kaggle:** https://www.kaggle.com/ (Add the exact dataset link here.)

After downloading, place `train.csv` and `test.csv` in the project directory before running the notebook.
---
## 🚀 Features

- Interactive Streamlit dashboard
- Flood probability prediction
- Risk classification
- Recommendation system
- Model performance metrics
- Dataset information
- User-friendly interface

---

## 📂 Dataset

The dataset contains:

- **Total Records:** 1,117,957
- **Features:** 20
- **Target Variable:** FloodProbability

### Input Features

- Monsoon Intensity
- Topography Drainage
- River Management
- Deforestation
- Urbanization
- Climate Change
- Dams Quality
- Siltation
- Agricultural Practices
- Encroachments
- Ineffective Disaster Preparedness
- Drainage Systems
- Coastal Vulnerability
- Landslides
- Watersheds
- Deteriorating Infrastructure
- Population Score
- Wetland Loss
- Inadequate Planning
- Political Factors

Target:

- Flood Probability

---

## 🧠 Machine Learning Workflow

1. Data Collection
2. Data Preprocessing
3. Feature Selection
4. Train-Test Split
5. Model Training
6. Model Evaluation
7. Model Deployment using Streamlit

---

## 🤖 Machine Learning Model

The project uses:

- Linear Regression

Models compared:

- Linear Regression
- Ridge Regression
- Lasso Regression

After evaluation, **Linear Regression** was selected as the final model.

---

## 📊 Model Performance

| Metric | Value |
|---------|-------|
| R² Score | 0.8449 |
| MAE | 0.0158 |
| RMSE | 0.0201 |

---

## 🖥️ Technologies Used

- Python
- Streamlit
- Scikit-learn
- Pandas
- NumPy
- Joblib

---

## 📁 Project Structure

```
Flood-Risk-Prediction-System/
│
├── app.py
├── best_flood_model.pkl
├── train.csv
├── requirements.txt
├── README.md
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/flood-risk-prediction.git
```

Go to the project directory

```bash
cd flood-risk-prediction
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## 📷 Application

The dashboard allows users to:

- Enter environmental parameters
- Predict flood probability
- View flood risk level
- Receive recommendations
- View model performance

---

## 📌 Future Improvements

- Integration with live weather APIs
- Satellite image analysis
- GIS-based visualization
- Interactive flood maps
- Real-time flood alerts
- Advanced Machine Learning models (Random Forest, XGBoost)

---

## ⚠️ Disclaimer

This project is developed for educational and research purposes.

The predictions are generated using a Machine Learning model trained on historical environmental and infrastructure-related data. It is intended as a decision-support tool and should not be considered an official flood warning system.

---

## 👩‍💻 Author

**Gahana Khandelwal**

B.Tech Computer Science and Engineering

Machine Learning Project

---

## ⭐ If you found this project useful, consider giving it a star on GitHub!
