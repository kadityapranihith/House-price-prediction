# 🏠 House Price Prediction - End-to-End ML Project

This project aims to predict house prices in Bengaluru using a machine learning model. The complete pipeline includes data preprocessing, model training, and deployment using a FastAPI backend.

## 📊 Dataset

The dataset used is from Kaggle:  
👉 [Bengaluru House Price Data](https://www.kaggle.com/datasets/amitabhajoy/bengaluru-house-price-data)

## 🔧 Project Workflow

1. **Data Cleaning**  
   - Handling null values  
   - Standardizing formats  

2. **Feature Engineering**  
   - Extracting BHK and square footage  
   - Converting categorical features  

3. **Outlier Removal**  
   - Price per square foot filtering  
   - Removing inconsistent BHK entries  

4. **Model Training & Evaluation**  
   - Linear Regression  
   - Cross-validation and performance metrics  

5. **Backend Deployment with FastAPI**  
   - Model served via REST API  
   - Built using FastAPI and Uvicorn  

## 🚀 Tech Stack

- Python  
- Pandas, NumPy, Scikit-learn  
- FastAPI  
- Uvicorn  
- Jupyter Notebook  



