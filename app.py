import pandas as pd
import pickle
import streamlit as st
from sklearn.neighbors import KNeighborsClassifier

# Load the model
parkinsons_disease = pickle.load(open("parkinsons_model.sav", "rb"))

# Sidebar for navigation
selected = st.sidebar.selectbox(
    "Disease Prediction System using Machine L"
    "...earning",
    ["Parkinsons Disease Prediction"],
    index=0
)

# Parkinsons Disease Prediction Page
if selected == "Parkinsons Disease Prediction":
    st.title("Parkinsons Disease Prediction using Machine Learning")

    # Getting the input data from the user
    st.write("Enter the following details for prediction:")
    fo = st.text_input("MDVP:Fo(Hz)")
    fhi = st.text_input("MDVP:Fhi(Hz)")
    flo = st.text_input("MDVP:Flo(Hz)")
    Jitter_percent = st.text_input("MDVP:Jitter(%)")
    Jitter_Abs = st.text_input("MDVP:Jitter(Abs)")
    RAP = st.text_input("MDVP:RAP")
    PPQ = st.text_input("MDVP:PPQ")
    DDP = st.text_input("Jitter:DDP")
    Shimmer = st.text_input("MDVP:Shimmer")
    Shimmer_dB = st.text_input("MDVP:Shimmer(dB)")
    APQ3 = st.text_input("Shimmer:APQ3")
    APQ5 = st.text_input("Shimmer:APQ5")
    APQ = st.text_input("MDVP:APQ")
    DDA = st.text_input("Shimmer:DDA")
    NHR = st.text_input("NHR")
    HNR = st.text_input("HNR")
    RPDE = st.text_input("RPDE")
    DFA = st.text_input("DFA")
    spread1 = st.text_input("spread1")
    spread2 = st.text_input("spread2")
    D2 = st.text_input("D2")
    PPE = st.text_input("PPE")

    # Code for prediction
    parkinsons_diagnosis = ""

    # Creating a button for prediction
    if st.button("Parkinson's Test Result"):
        # Convert input values to float
        fo = float(fo)
        fhi = float(fhi)
        flo = float(flo)
        Jitter_percent = float(Jitter_percent)
        Jitter_Abs = float(Jitter_Abs)
        RAP = float(RAP)
        PPQ = float(PPQ)
        DDP = float(DDP)
        Shimmer = float(Shimmer)
        Shimmer_dB = float(Shimmer_dB)
        APQ3 = float(APQ3)
        APQ5 = float(APQ5)
        APQ = float(APQ)
        DDA = float(DDA)
        NHR = float(NHR)
        HNR = float(HNR)
        RPDE = float(RPDE)
        DFA = float(DFA)
        spread1 = float(spread1)
        spread2 = float(spread2)
        D2 = float(D2)
        PPE = float(PPE)

        # Make prediction
        parkinsons_prediction = parkinsons_disease.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]])

        if parkinsons_prediction[0] == 0:
            parkinsons_diagnosis = "Hurrah! You don't have Parkinson's Disease."
        else:
            parkinsons_diagnosis = "Sorry! You have Parkinson's Disease."

    st.success(parkinsons_diagnosis)
