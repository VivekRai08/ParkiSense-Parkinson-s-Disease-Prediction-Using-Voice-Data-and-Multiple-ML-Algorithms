# ParkiSense-Parkinson's Disease Prediction Using Voice Data and Multiple ML Algorithms
This project explores Parkinson’s Disease detection using voice features and machine learning. It compares algorithms like KNN, Naïve Bayes, Logistic Regression, Random Forest, SVM, XGBoost, and Neural Networks, alongside hybrid models (e.g., LR+NB, RF+LR), to identify the most effective approach for early PD detection.

# 🧠 Parkinson's Disease Detection App

This project uses Streamlit and a machine learning model to detect Parkinson's disease based on voice features.

## 🚀 Running the Streamlit App

Follow these steps to set up and run the Streamlit application in a virtual environment.
Use Terminal in the VS code
---

### ✅ 1. Create and Activate Virtual Environment

  python -m venv myenv
  myenv\Scripts\activate

2. Activate the Virtual Environment
   myenv\Scripts\activate
You should see (myenv) appear in your terminal prompt.

3.Install Required Package (Streamlit)
  pip install streamlit
If there are any issues or you want to reinstall Streamlit:
  pip install --force-reinstall streamlit

4.Verify Streamlit Installation
  streamlit --version

5.Run the Streamlit App
Make sure the environment is active:
  myenv\Scripts\activate

Then run the app using:
  streamlit run app.py

6.Fix Missing Packages (If Any)
If you get an error like ModuleNotFoundError, install the missing package using:
pip install package-name
