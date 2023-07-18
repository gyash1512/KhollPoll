import streamlit as st
from PIL import Image
import os
from streamlit_lottie import st_lottie
import requests
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    else:
        return r.json()


#setting page configuration
st.set_page_config(page_title="Kholl Poll", page_icon="logo.png", layout="wide")


#column wize adding image
col1, col2, col3 = st.columns([6,6,1])

with col1:
    st.image("banner.png",width = 150)
    st.write("")
    st.write("")
with st.container():
    col1, col2, col3 = st.columns([2.8,0.5,1])
    with col1:
        st.subheader("*Hi User! Welcome to*")
        original_title= '<p style="font-family:ALGERIAN; color:Turquoise; font-size: 80px;">Khollपोल</p>'
        st.markdown(original_title, unsafe_allow_html=True)
        st.write("The place where you are having connection and interaction with your Organisation:office:.")
        st.markdown("[Learn More ->](https://www.canva.com/design/DAFUuLA-kEE/sIVtZWZwSSPJe0fs-WklSw/edit?utm_content=DAFUuLA-kEE&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)")

    
    
    with col3:
        lottie_url = "https://assets10.lottiefiles.com/packages/lf20_calza6zj.json"
        lottie_json = load_lottieurl(lottie_url)
        st_lottie(
                lottie_json,
                speed=1,
                loop=True,
                height=230,
                width=230,
                quality="medium")


st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")


#COLUMN WISE ADDING ANIMATIONS
Sol1, Sol2, Sol3 = st.columns([2,1.9,1.2])
with Sol1:
    lottie_url1 = "https://assets9.lottiefiles.com/private_files/lf30_6yjihjym.json"
    lottie_json1 = load_lottieurl(lottie_url1)
    st_lottie(
                lottie_json1,
                speed=1,
                loop=True,
                height=250,
                width=250,
                quality="medium")


with Sol2:
    lottie_url2 = "https://assets2.lottiefiles.com/packages/lf20_uqlolnxx.json"
    lottie_json2 = load_lottieurl(lottie_url2)
    st_lottie(
                lottie_json2,
                speed=1,
                loop=True,
                height=250,
                width=250,
                quality="medium")


with Sol3:
    lottie_url3 = "https://assets10.lottiefiles.com/packages/lf20_aqbbxmsx.json"
    lottie_json3 = load_lottieurl(lottie_url3)
    st_lottie(
                lottie_json3,
                speed=1,
                loop=True,
                height=250,
                width=250,
                quality="medium")


#column wize adding buttons

col1, col2, col3 = st.columns([3.5,3,1])

with col1:

    if st.button('***Messy*** OR ***Sassy***'):
        st.success("Redirecting To Mess Review System!")
        os.system('cmd /c "streamlit run mess.py"')
with col2:
    
    if st.button('Events'):
        st.success("Redirecting To Events Management!")
        os.system('cmd /c "streamlit run Test.py"')
with col3:
    
    if st.button('News'):
        st.error("""System Under Maintainance !!!""")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
original_title= '<p style="font-family:ALGERIAN; color:AQUA; font-size: 50px;">OUR WORDS</p>'
st.markdown(original_title, unsafe_allow_html=True)
st.markdown(""""Kholl Poll" is basically a medium for student to review Mess food, get scoop on events, daily briefings of current events.\n
The idea behind this project is to resolve some of the major problems which almost every one of us faced but till now the problem persisted.\n
We have worked hard to make Kholl Poll look simple and user-friendly, thereby facilitating smooth n sleek user-experience.\nThis is just the starting, there are a lot of\n 
problems in our university which students face but no one tries to fix them but we will as we are going official in a few months with more features and a proper smooth experience!""")
Zol1, zol3=st.columns([1,1])
with zol3:
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    lottie_url1 = "https://assets10.lottiefiles.com/packages/lf20_o6spyjnc.json"
    lottie_json1 = load_lottieurl(lottie_url1)
    st_lottie(
        lottie_json1,
        speed=1,
        loop=True,
        height=600,
        width=600,
        quality="medium") 
with Zol1:
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.header("Contact Us")
    original_title= '<p style="font-family:ALDHABI; color:AQUA; font-size: 17px;">YASH GUPTA</p>'
    st.markdown(original_title, unsafe_allow_html=True)
    st.markdown("[Linkedin ->](https://www.linkedin.com/in/yash-gupta-57907b257/)")

    original_title= '<p style="font-family:ALDHABI; color:AQUA; font-size: 17px;">JATIN YADAV</p>'
    st.markdown(original_title, unsafe_allow_html=True)
    st.markdown("[Linkedin ->](https://www.linkedin.com/in/jatin-yadav-455373259/)")

    original_title= '<p style="font-family:ALDHABI; color:AQUA; font-size: 17px;">ADIL KHAN</p>'
    st.markdown(original_title, unsafe_allow_html=True)
    st.markdown("[Linkedin ->](https://www.linkedin.com/in/adil-khan-0595b8231/)")

    original_title= '<p style="font-family:ALDHABI; color:AQUA; font-size: 17px;">MRIDUL MADHAV JINDAL</p>'
    st.markdown(original_title, unsafe_allow_html=True)
    st.markdown("[Linkedin ->](https://www.linkedin.com/in/mridul-jindal-91bb49253/)")

    original_title= '<p style="font-family:ALDHABI; color:AQUA; font-size: 17px;">YASHSWI SHUKLA</p>'
    st.markdown(original_title, unsafe_allow_html=True)
    st.markdown("[Linkedin ->](https://www.linkedin.com/in/yashswi-shukla-8384ba252/)")


if st.button("**Logout**"):
    os.system('cmd/c "streamlit run Login.py"')