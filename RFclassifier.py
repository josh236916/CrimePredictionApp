import numpy as np
import pickle
import streamlit as st
import pandas as pd

with open('/Users/josh2369/Downloads/model2.pkl','rb') as model_file,open('/Users/josh2369/Downloads/label_encoder.pkl','rb') as encoder_file:
    model=pickle.load(model_file)
    label_encoder=pickle.load(encoder_file)




# Load the trained model and other necessary components

# Streamlit app title
st.title('Communities and Crime Prediction App')

# User input widgets
st.write('Enter the following information:')
state=st.selectbox('State',label_encoder.classes_)
pctWInvInc= st.slider('Percentage of people with a second income coming from investment or rent', min_value=0, max_value=90, value=100)
pctWPubAsst = st.slider('Percentage of people who receive public assistance', min_value=0, max_value=100, value=100)
PctPopUnderPov = st.slider('Percentage of people under poverty', min_value=0, max_value=100, value=100)
PctUnemployed= st.slider('Percentage of people who are unemployed', min_value=0, max_value=100, value=100)
PctTeen2Par = st.slider('Percentage of teens with 2 parents', min_value=0, max_value=100, value=100)
TotalPctDiv = st.slider('Percentage of people who are divorced', min_value=0, max_value=100, value=100)
PctFam2Par= st.slider('Percentage of families with 2 parents', min_value=0, max_value=100, value=100)
PctKids2Par = st.slider('Percentage of kids with 2 parents', min_value=0, max_value=100, value=100)
PctYoungKids2Par = st.slider('Percentage of young kids with 2 parents', min_value=0, max_value=100, value=100)
PctPersOwnOccup= st.slider('Percentage of people with their own house', min_value=0, max_value=100, value=100)

# Prepare user input for prediction

encoded_state= label_encoder.transform([state])[0]

user_input = pd.DataFrame({
     'State':[encoded_state],
     'Population Density':[pctWInvInc],
     'Median Income':[pctWPubAsst],
     'Percentage Under 18':[PctPopUnderPov],
     'test1':[PctUnemployed],
     'test2':[PctTeen2Par],
     'test3':[TotalPctDiv],
     'test4':[PctFam2Par],
     'test5':[PctKids2Par],
     'test6':[PctYoungKids2Par],
     'test7':[PctPersOwnOccup]})

# Make predictions
prediction = model.predict(user_input)
prediction_mapping = {'low': 'Low Crime Rate', 'moderate': 'Moderate Crime Rate', 'high': 'High Crime Rate'}
prediction_result = prediction_mapping[prediction[0]]

# Display prediction
st.subheader('Prediction:')
st.write(f'The predicted crime rate for the given input is: {prediction_result}')
 