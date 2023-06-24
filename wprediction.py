# -*- coding: utf-8 -*-
"""
Created on Sun May 28 22:59:40 2023

@author: Seelam Murali
"""

import numpy as np
# pickle is used for loading
import pickle
# streamlit is used for deployment
import streamlit as st


loaded_model = open("classifier.sav","rb")

# creating fucntion
def water_prediciton(input_data):
    classifier=pickle.load(loaded_model)
    prediction=classifier.predict([input_data])
    if (prediction[0]==0):
        return "Water is safe for consumption"
    else:
        return "Water is not safe for consumption"

def main():
    st.title("Water potability WEB APP")
    
    #PH = 0.0
    #Hardness, Solids, Chloramines, Sulfate, Conductivity,Organic_carbon, Trihalomethanes, Turbidity=0.0
    # Getting input from users
    
    PH = st.number_input("PH : ")
    Hardness = st.number_input("hardness : ")
    Solids = st.number_input("Solids :")
    Chloramines = st.number_input("Chloramines :")
    Sulfate = st.number_input("Sulphate :")
    Conductivity = st.number_input("Conductivity  :")
    Organic_carbon = st.number_input(" Organic carbon :")
    Trihalomethanes = st.number_input(" Trihalomethanes :")
    Turbidity = st.number_input("Turbidity :")
    
    
    
    # Code for Predictions
    Prediction = ""
    # creating a button for Predictions
    if st.button("Prediction RESULT"):
        Prediction = water_prediciton([PH, Hardness, Solids, Chloramines, Sulfate, Conductivity,Organic_carbon, Trihalomethanes, Turbidity])
    
        st.success(Prediction)



if __name__ == "__main__":
    main()
