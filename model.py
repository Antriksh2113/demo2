import streamlit as st
import pandas as pd
st.title('Medical Diagnostic Web Application')
import pickle

# Step 1. Load the pickle model
model = open('rfc.pickle','rb')
rfc = pickle.load(model)
model.close()

# Step 2. Create a UI for the front and user
pregs = st.sidebar.number_input('Pregnancies',0,20,step = 1)
Glucose = st.sidebar.slider('Glucose',40,200,40)
BP = st.sidebar.slider('BloodPressure',20,160,20)
skin = st.sidebar.slider('SkinThickness',5,100,5)
Insulin = st.sidebar.slider('Insulin',10,900,10)
BMI = st.sidebar.slider('BMI',15,70,15)
DPF = st.sidebar.slider('DiabetesPedigreeFunction',0.5,3.0,0.5)
age = st.sidebar.slider('Age',21,90,21)

# Step 3. Change user input as models input data
data = {'Pregnancies':pregs,
        'Glucose':Glucose,
        'BloodPressure':BP,
        'SkinThickness':skin,
        'Insulin':Insulin,
       'BMI':BMI,
        'DiabetesPedigreeFunction':DPF,
        'Age':age}
input_data = pd.DataFrame([data])
# Step 4. Get the predictions
predictions = rfc.predict(input_data)[0]
st.write(predictions)
if st.sidebar.button('Predict'):
    if predictions == 0:
        st.success('Diabeties Free')
    if predictions==1:
        st.error('Having Diabeties')
