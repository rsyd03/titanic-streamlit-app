import streamlit as st
import pickle
import numpy as np

with open('model.sav', 'rb') as file:
    model = pickle.load(file)

st.image('titanic_banner.webp', use_column_width=True)
st.title('Titanic Survival Prediction')

title_mapping = {
    "Mr.": 0, "Miss.": 1, "Mrs.": 2,
    "Master.": 3, "Dr.": 3, "Rev.": 3, "Col.": 3, "Major.": 3, "Mlle.": 3, "Countess.": 3,
    "Ms.": 3, "Lady.": 3, "Jonkheer.": 3, "Don.": 3, "Dona.": 3, "Mme.": 3, "Capt.": 3, "Sir.": 3
}
Title = st.selectbox('Title', options=list(title_mapping.keys()))
Title = title_mapping[Title]
Pclass = st.radio('Pclass "passenger Class"', [1, 2, 3])
Sex = st.radio('Sex', ['Male', 'Female'])
Sex = 0 if Sex == 'male' else 1
Age = st.slider('Age', min_value=0, max_value=100, value=25)
SibSp = st.number_input('SibSp "number of siblings / spouses aboard"', min_value=0, max_value=10, value=0)
Parch = st.number_input('Parch "number of parents / children aboard"', min_value=0, max_value=10, value=0)
Fare = st.slider('Fare "passenger fare"', min_value=0.0, max_value=512.3292, value=7.25)
Embarked = st.radio('Embarked "port of embarkation"', ['Cherbourg', 'Queenstown', 'Southampton'])
Embarked_C = 1 if Embarked == 'C' else 0
Embarked_Q = 1 if Embarked == 'Q' else 0
Embarked_S = 1 if Embarked == 'S' else 0

input_data = np.array([Pclass, Sex, Age, SibSp, Parch, Fare, Embarked_C, Embarked_Q, Embarked_S, Title]).reshape(1, -1)

if st.button('Predict'):
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.success('Survived like Rose DeWitt Bukater')
        st.image('MIBU1.webp', width=150)
    else:
        st.error('Did not survive like Jack Dawson')
        st.image('Phase_2.22.webp', width=150)