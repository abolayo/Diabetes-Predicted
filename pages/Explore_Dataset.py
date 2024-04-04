import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('diabetes.csv')

def heading(text, font_size):
    res = f'<span style="color:#FFFFFF; font-size: {font_size}px;"><b>{text}</b></span>'
    st.markdown(res, unsafe_allow_html=True)
    
    
def head(text):
    res = f'<span style="color:#3030FF; font-size: 25px;"><b>{text}</b></span>'
    st.markdown(res, unsafe_allow_html=True)
     
def dataset_highlights():
    highlights = ['* The average BMI of the patients is 32 which is above the healthy weight range 18-25',
                  '* The maximum and minimum age among the patients are 81 and 21 respectively with the mean age at 33',
                  '* The average(120) glucose level of the patients falls within the healthy range (70 - 140)',
                  '* 75% of the patients have their glucose level at the max healthy range which implies most of the patients are more likely to be diagnosed with diabetes']
    for i in highlights:
        st.markdown(i)

heading('EXPLORE DATASET', 40)
    

head('OVERVIEW')
st.write()

st.table(df.head(5))    

if st.button('Show Highlights'):
    dataset_highlights()


types = {'Categorical':['Outcome'], 
         'Numerical':['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness',  'BMI', 'DiabetesPedigreeFunction', 'Age']}


head('ANALYSIS')

type_of_analysis = st.radio('What type of analysis', ['Numerical','Categorical'])

column = st.selectbox('Select a column',types [type_of_analysis])


if type_of_analysis == 'Numerical':
    st.write(df[column].describe()) 
    fig =  plt.figure(figsize=(8, 4))
    sns.boxplot(data= df, x='Outcome', y=df[column]) #type of plot
    plt.title('AVERAGE {} BY OUTCOME'.format(column).upper(), color='red') #title of the plot
    st.pyplot(fig) #display plot on streamlit
    

if type_of_analysis == "Categorical":
    dist = pd.DataFrame(df[column].value_counts())
    st.bar_chart(dist)
    
    
#highlights for each column
def Age():
    highlights = ['* Majority of the patients falls between the ages of 20 and 40',
                  '* Patients between the ages of 30 and 45 are more likely to be diagnosed with diabetes']
    for i in highlights:
        st.markdown(i)

def BMI():
    st.markdown('* The BMI of positively diagnosed patients are quite higher than the negatively diagnosed')
    
def SkinThickness():
    st.markdown('* The SkinThickness of the patients has almost no effect on the outcome')
    
def DiabetesPedigreeFunction():
    st.markdown('* Diabetes Pedigree Function represents the likelihood that a person will develop diabetes based on their family history of the disease. A value of this function is between 0-2.5 ')

def Glucose():
    st.markdown('* Patients with glucode level more than 125 are more likely to be diagnosed with diabetes')
    
def Pregnancies():
    st.markdown('* Postively diagnosed patients(females) seem to have had more pregnancies on an average than the others     ')

def BloodPressure():
    highlights = ['* The average pressure of both positively and negatively diagnosed patients are almost the same',
                '* Hence blood pressure has little or no effect on the outcome of the diagnosis']
    for i in highlights:
        st.markdown(i)
        
def Outcome():
    st.markdown('* The dataset contains 268 +ly diagnosed patients and 500 -ly diagnosed patients')
        
f_name = column
function = globals()[f_name]
function()