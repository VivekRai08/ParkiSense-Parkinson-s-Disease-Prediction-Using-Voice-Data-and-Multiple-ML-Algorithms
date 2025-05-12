# ParkiSense - Parkinson's Disease Prediction Using Voice Data and Multiple ML Algorithms  

## 📌 Overview  

This project explores Parkinson’s Disease detection using voice features and machine learning. It compares various algorithms, including:  

- **K-Nearest Neighbors (KNN)**  
- **Naïve Bayes (NB)**  
- **Logistic Regression (LR)**  
- **Random Forest (RF)**  
- **Support Vector Machine (SVM)**  
- **XGBoost**  
- **Neural Networks**  

Additionally, hybrid models (e.g., LR+NB, RF+LR) are tested to identify the most effective approach for early Parkinson’s Disease (PD) detection.  

---

## 🧠 Parkinson's Disease Detection App  

This project utilizes **Streamlit** and a machine learning model to detect Parkinson’s disease based on voice features.  

---

## 🚀 Running the Streamlit App  

Follow these steps to set up and run the Streamlit application using **VS Code Terminal**in a virtual environment.  

### 1. Create and Activate Virtual Environment  

```bash
python -m venv myenv
myenv\Scripts\activate
```

### 2. Verify Streamlit Installation
Check if Streamlit is installed correctly by running:
```bash
streamlit --version
```

### 3. Install Streamlit
If there is no Streamlit installed in your system

Install Streamlit using the following command
```bash
pip install streamlit
```

If you encounter any issues or wish to reinstall Streamlit, use:

```bash
pip install --force-reinstall streamlit
```

### 4. Run the Streamlit App
```bash 
myenv\Scripts\activate
```

You should have an "env" mark. 
This means your virtual environment is running

Then, run the application with the following command:
```bash 
streamlit run app.py
```

### 5.Fix Missing Packages (If Any)
If you encounter an error such as ModuleNotFoundError, make sure you install these packages inside the environment iand nstall the missing package using:

```bash
pip install package-name
```

Feel free to try out the project and hit me up if any issues occur :-)
