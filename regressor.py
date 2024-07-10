import numpy as np
import pickle
import streamlit as st
import pandas as pd

loaded_model  = pickle.load(open('/Users/josh2369/Downloads/trained_regressor.sav', 'rb'))

st.title('Communities and Crime Prediction App')

st.write('Enter the following information:')
pctWInvInc= st.slider('Percentage of people with a second income coming from investment or rent', min_value=0, max_value=100, value=100)
pctWPubAsst = st.slider('Percentage of people who receive public assistance', min_value=0, max_value=100, value=100)
PctPopUnderPov = st.slider('Percentage of people under poverty', min_value=0, max_value=100, value=0)
PctUnemployed= st.slider('Percentage of people who are unemployed', min_value=0, max_value=100, value=100)
PctTeen2Par = st.slider('Percentage of teens with 2 parents', min_value=0, max_value=100, value=100)
TotalPctDiv = st.slider('Percentage of people who are divorced', min_value=0, max_value=100, value=100)
PctFam2Par= st.slider('Percentage of families with 2 parents', min_value=0, max_value=100, value=100)
PctKids2Par = st.slider('Percentage of kids with 2 parents', min_value=0, max_value=100, value=100)
PctYoungKids2Par = st.slider('Percentage of young kids with 2 parents', min_value=0, max_value=100, value=100)
PctPersOwnOccup= st.slider('Percentage of people with their own house', min_value=0, max_value=100, value=100)

user_input=[[pctWInvInc,pctWPubAsst,PctUnemployed,PctPopUnderPov,PctTeen2Par,TotalPctDiv,PctFam2Par,PctKids2Par,PctYoungKids2Par,PctPersOwnOccup]]
prediction=loaded_model.predict(user_input)[0]

st.write(f'Predicted Output:{prediction}')