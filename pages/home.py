import streamlit as st


def fancy_header(text, font_size=47):
    res = f'<span style="color:#3030FF; font-size: {font_size}px;"><b>{text}</b></span>'
    st.markdown(res, unsafe_allow_html=True )
    
def body(text, font_size=23):
    res = f'<span style="color:#FFFFFF; font-size: {font_size}px;">{text}</span>'
    st.markdown(res, unsafe_allow_html=True )
    
def disclaim(text, font_size=35):
    res = f'<span style="color:#FF0000; font-size: {font_size}px;"><b>{text}</b></span>'
    st.markdown(res, unsafe_allow_html=True )
    
def body1(text, font_size=20):
    res = f'<span style="color:#FFFFFF; font-size: {font_size}px;"><b>{text}</b></span>'
    st.markdown(res, unsafe_allow_html=True )

def image():   
    st.markdown("""
        <style type="text/css">
        div[data-testid="stHorizontalBlock"] {
            border:10px;
            padding:30px;
            border-radius: 10px;
            background:#FFFFFF;
        }
        </style>
    """, unsafe_allow_html=True)
#st.image(image('solution1.jpg'))

fancy_header('WELCOME TO OUR DIABETES PREDICTION APP!')

body('Our app is designed to help you understand your risk of developing diabetes based on a few simple inputs. Diabetes is a chronic condition that affects millions of people worldwide, and it is characterized by high levels of sugar (glucose) in the blood. This can lead to a range of health problems, including heart disease, nerve damage, and kidney damage.')


body1('\n Our app uses advanced algorithms to analyze your <b>personal</b> information and provide you with an estimated risk of developing diabetes. To get started, simply input your Glucose level , BloodPressure, SkinThickness,  BMI, DiabetesPedigreeFunction, Age. Based on this information, our app will provide you with an estimate of your risk for developing diabetes, as well as suggestions for lifestyle changes and other steps you can take to reduce your risk.')



disclaim('\n DISCLAIMER!')
body('It is important to note that our app is not a substitute for professional medical advice. If you have concerns about your risk for diabetes or any other health condition, please consult with your healthcare provider. With our Diabetes Prediction App, you can take control of your health and make informed decisions to protect your well-being.')


st.image('solution1.jpg')
st.markdown("[![Foo](63-630946_why-do-we-come-to-work-office-girl.png)](https://thehealthcareinsights.com/can-diabetes-be-cured-permanently-in-the-future/)")
st.markdown("[![Foo](http://www.google.com.au/images/nav_logo7.png)](http://google.com.au/)") 