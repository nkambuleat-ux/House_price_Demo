
import streamlit as st
import pickle #Helps load the pickle file created during model development
import numpy as np
#import os

st.title("House Price Prediction App")
st.header("Please fill in your details")

#Features used to train the model
#use number_input("Instruction", min, max, default value) for numerical values
#use selectbox for categorical values
MedInc=st.number_input("Median income in block group",0,10,5)
HouseAge=st.number_input("Enter house age",0,200)
AveRooms=st.number_input("Enter number of rooms",0,200)
AveBedrms=st.number_input("Enter number of bedrooms",0,200)
Population = st.number_input("Enter block group population",0,200)
AveOccup = st.number_input("Enter number of household members",0,200)
Latitude = st.slider('Select latitude:', 30, 50, 1)
Longitude = st.slider('Select longitude:', 100, 130, 1)
#all user inputs are stored in the respective variables(python variables)

#create a button to predict output
predict_clicked=st.button("Get the prediction")

if predict_clicked==True:
    model=pickle.load(open("Housing/model.pkl", 'rb'))

    #load the test data into numpy array
    data=[np.array(['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup', 'Latitude', 'Longitude'])]

    #call the model to predict the price
    result=model.predict(data)
    st.success('The predicted price is ${}'.format(result))
    #display the predicted price on the webpage
    




