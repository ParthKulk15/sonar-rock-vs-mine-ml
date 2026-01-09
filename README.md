# sonar-rock-vs-mine-ml
End-to-end ML project using Logistic Regression and Streamlit

# Sonar Rock vs Mine Prediction 

## Overview
This is an end-to-end machine learning project that classifies sonar signals as **Rock** or **Naval Mine** using supervised learning techniques.

## Dataset
- 208 samples
- 60 numeric sonar signal features
- Binary classification: Rock vs Mine

## Approach
- Data preprocessing and feature scaling
- Logistic Regression with GridSearchCV
- Model comparison with SVM and KNN
- Feature importance analysis
- Deployment using Streamlit

## Model Performance
Logistic Regression : 
  accuracy : 80%
  recall : 81%
SVM : 
  accuracy : 83%
  recall : 77%
KNN : 
  accuracy : 83%
  recall : 82%

## Feature Importance
Logistic Regression coefficients were analyzed to identify the most influential sonar features contributing to mine detection.

## Web Application
An interactive Streamlit app allows users to input sonar signal values and receive predictions along with confidence scores.

## Tech Stack
- Python
- NumPy, Pandas
- Scikit-learn
- Matplotlib
- Streamlit

## App Link : # Sonar Rock vs Mine Prediction 🚢⚠️

## Overview
This is an end-to-end machine learning project that classifies sonar signals as **Rock** or **Naval Mine** using supervised learning techniques.

## Dataset
- 208 samples
- 60 numeric sonar signal features
- Binary classification: Rock vs Mine

## Approach
- Data preprocessing and feature scaling
- Logistic Regression with GridSearchCV
- Model comparison with SVM and KNN
- Feature importance analysis
- Deployment using Streamlit

## Model Performance
Logistic Regression : 
  accuracy : 80% 
  recall : 81% 
SVM : 
  accuracy : 83% 
  recall : 77%
KNN : 
  accuracy : 83%
  recall : 82%

## Feature Importance
Logistic Regression coefficients were analyzed to identify the most influential sonar features contributing to mine detection.

## Web Application
An interactive Streamlit app allows users to input sonar signal values and receive predictions along with confidence scores.

## Tech Stack
- Python
- NumPy, Pandas
- Scikit-learn
- Matplotlib
- Streamlit

## App Link : https://sonar-rock-vs-mine-ml.streamlit.app/

## Feature Selection Experiment
To improve interpretability and reduce dimensionality, a reduced model was trained using only the top 10 most important features identified via Logistic Regression coefficients.  
While accuracy decreased from 80% to 71%, recall for mine detection remained relatively high at 77%, indicating that a small subset of sonar features captures most of the predictive signal.


