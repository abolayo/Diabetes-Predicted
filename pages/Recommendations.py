import streamlit as st
def fancy_header(text, font_size=47):
    res = f'<span style="color:#3030FF; font-size: {font_size}px;"><b>{text}</b></span>'
    st.markdown(res, unsafe_allow_html=True )
    


bookings = ['www.iCliniq.com', 'www.sesamecare.com', 'www.secondopinions.com']
for i in bookings:
    st.write(i)
    
fancy_header('Under Construction!...🚧')