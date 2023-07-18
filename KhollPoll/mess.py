import streamlit as st
from PIL import Image
import pandas as pd
import plotly.express as px
import os
from streamlit_lottie import st_lottie
import requests

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    else:
        return r.json()




st.set_page_config(page_title="Mess Review", page_icon="🍞", layout="wide")
@st.cache(allow_output_mutation=True)
def get_data():
    return []
st.image("banner.png",width = 150)
st.write("")
st.write("")
user_id = st.text_input("Bennett NetID")
admins={"e22cseu1117":"Yash", "e22cseu1156":"Jatin", "e22cseu1116":"Mridul","e22cseu1154":"Yashswi", "e22cseu1149":"Adil","riti.kushwaha":"Riti Kushwaha", "sonal.kukreja":"Sonal Kukreja"}
if user_id.lower() in admins.keys():
    st.success(f"Welcome {admins[user_id.lower()]}, The Admin!!!")
else:
    st.write(user_id)


    
with st.container():
    col1, col2, col3= st.columns([2,1,1])
    with col1:
        st.subheader("*Hi User! Welcome to*")
        original_title= '<p style="font-family:ALGERIAN; color:Turquoise; font-size: 40px;">MESS REVIEW SYSTEM👋</p>'
        st.markdown(original_title, unsafe_allow_html=True)
        st.write("Don't forget to check the review!!!")
        st.write("")
    with col3:
        lottie_url1 = "https://assets10.lottiefiles.com/packages/lf20_TmewUx.json"
        lottie_json = load_lottieurl(lottie_url1)
        st_lottie(
                lottie_json,
                speed=1,
                loop=True,
                height=200,
                width=200,
                quality="medium")   
tab1, tab2, tab3 = st.tabs(["***Daily Menu***", "***Weekly Review***", "***Monthly Review***"])

with tab1:
    st.header("**Today's Menu** 🍽️")
    st.subheader("Breakfast 🥪")
    expander = st.expander("See Menu")
    expander.write("""
    Milk/Tea/Coffee\n
    Bread\n
    Jam\n
    Mix Fruit\n
    Dahi\n
    Parathe""")

    #taking review
    RevM = st.slider("Morning Review", 1, 5)
    
    
    
    st.subheader("Lunch 🍲")
    expander=st.expander("See Menu")
    expander.write("""
    Paneer\n
    Rice\n
    Chapati\n
    Burfi\n
    Salad\n
    Moong Dal\n
    Choley\n""")

    #taking review
    RevL = st.slider("Lunch Review", 1, 5)
    
    
    st.subheader("Snacks 🍟")
    expander=st.expander("See Menu")
    expander.write("""
    Tea/Coffee\n
    Bread Pakoda\n
    Dahi Bhalla\n""")

    #taking review
    RevS = st.slider("Snacks Review", 1, 5)
    


    st.subheader("Dinner 🥗")
    expander=st.expander("See Menu")
    expander.write("""
    Rice\n
    Chapati\n
    Kheer\n
    Salad\n
    Dal Makhani\n
    Custard\n
    Choley\n""")

    #taking review
    RevD = st.slider("Dinner Review", 1, 5)
    
    st.title("Overall Day Review")
    bar = st.slider("Overall Day Review", 1, 5)


    st.title("Stats 📈")
    st.write("Click On ***Add Row*** to reflect your Ratings!")
    if st.button("Add row"):
        if user_id.lower() in admins.keys():
            get_data().append({"Bennett NetID": user_id.lower(), "Name":admins[user_id.lower()], "User":"ADMIN", "Morning Review": RevM, "Lunch Review": RevL, "Snacks Review" : RevS, "Dinner Review": RevD, "Overall Day Review": bar, "Mean Review": int(((RevM+RevL+RevS+RevD)//4)+(bar//30))})
        else:
            get_data().append({"Bennett NetID": user_id.lower(), "Name":"USER" , "User":"Local User", "Morning Review": RevM, "Lunch Review": RevL, "Snacks Review" : RevS, "Dinner Review": RevD, "Overall Day Review": bar, "Mean Review": int(((RevM+RevL+RevS+RevD)//4)+(bar//30))})
    st.write(pd.DataFrame(get_data()))
    col1, col2, col3 = st.columns([1,3,1])
    with col2:
        lottie_url = "https://assets2.lottiefiles.com/packages/lf20_tll0j4bb.json"
        lottie_json = load_lottieurl(lottie_url)
        st_lottie(
            lottie_json,
            speed=1,
            loop=True,
            height=600,
            width=600,
            quality="medium")
with tab3:
    st.header("**Monthly Mess Review System🍱**")
    #ADDING LOTTIE ANIMATION
    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
             return None
        else:
            return r.json()

    lottie_url = "https://assets8.lottiefiles.com/packages/lf20_7aJ0JNKOVj.json"
    lottie_json = load_lottieurl(lottie_url)

    #loading database
    excel_file = "mess_monthly_review.xlsx"
    sheet_name = "month12"

    df = pd.read_excel(excel_file,
                        sheet_name=sheet_name,
                        usecols='A:C',
                        header = 0)

    df_participants=pd.read_excel(excel_file,sheet_name = sheet_name,usecols='G:h',header = 0)
    df_participants.dropna(inplace=True)

    # collection and selection
    food_item = df["FOOD_ITEM"].unique().tolist()

    date = df['DATE'].unique().tolist()

    date_selection = st.slider("Date:",
                    min_value=min(date),
                    max_value=max(date),
                    value = (min(date), max(date)))

    food_item_selection=st.multiselect('FOOD ITEM:',
                                    food_item,
                                    default=food_item)


    #FILTERING DATAFRAME BASED ON THE SELECTION
    mask=(df["DATE"].between(*date_selection)) & (df["FOOD_ITEM"].isin(food_item_selection))
    number_of_result = df[mask].shape[0]
    st.markdown(f"*Available Results: {number_of_result}*")

    df_grouped = df[mask].groupby(by = ["REVIEW"]).count()[["DATE"]]
    df_grouped = df_grouped.rename(columns={"DATE":"Date"})
    df_grouped = df_grouped.reset_index()


    #PLOTTING BAR_CHART
    bar_chart=px.bar(df_grouped,
                    x="REVIEW",
                    y="Date",
                    text="Date",
                    color_discrete_sequence=['#F63366']*len(df_grouped),
                    template='plotly_white')

    st.plotly_chart(bar_chart)


    #ADDING LOTTIE ANIMATION
    col1, col2= st.columns([5,6])
    with col1:
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.dataframe(df_participants)


    with col2:
        st_lottie(
                lottie_json,
                speed=1,
                loop=True,
                height=550,
                width=550,
                quality="medium")

    pie_chart = px.pie(df_participants,
                    title = "Monthly Review",
                    values = "Rev.",
                    names="Food")

    st.plotly_chart(pie_chart)

with tab2:
    st.header("**Weekly Mess Review System**🍱")
    #ADDING LOTTIE ANIMATION
    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
             return None
        else:
            return r.json()

    lottie_url = "https://assets3.lottiefiles.com/packages/lf20_nac8vvgu.json"
    lottie_json = load_lottieurl(lottie_url)

    #loading database
    excel_file = "mess_weekly_review.xlsx"
    sheet_name = "Week3"

    df = pd.read_excel(excel_file,
                        sheet_name=sheet_name,
                        usecols='A:C',
                        header = 0)



    df_participants=pd.read_excel(excel_file,sheet_name = sheet_name,usecols='G:h',header = 0)
    df_participants.dropna(inplace=True)

    # collection and selection
    food_item = df["FOOD_ITEM"].unique().tolist()

    date = df['DATE'].unique().tolist()

    date_selection = st.slider("Date:",
                    min_value=min(date),
                    max_value=max(date),
                    value = (min(date), max(date)))

    food_item_selection=st.multiselect('Food Item:',
                                    food_item,
                                    default=food_item)


    #FILTERING DATAFRAME BASED ON THE SELECTION
    mask=(df["DATE"].between(*date_selection)) & (df["FOOD_ITEM"].isin(food_item_selection))
    number_of_result = df[mask].shape[0]
    st.markdown(f"*Available Results: {number_of_result}*")

    df_grouped = df[mask].groupby(by = ["REVIEW"]).count()[["DATE"]]
    df_grouped = df_grouped.rename(columns={"DATE":"Date"})
    df_grouped = df_grouped.reset_index()


    #PLOTTING BAR_CHART
    bar_chart=px.bar(df_grouped,
                    x="REVIEW",
                    y="Date",
                    text="Date",
                    color_discrete_sequence=['#F63366']*len(df_grouped),
                    template='plotly_white')

    st.plotly_chart(bar_chart)


    #ADDING LOTTIE ANIMATION
    col1, col2= st.columns([5,6])
    with col1:
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.dataframe(df_participants)


    with col2:
        st_lottie(
                lottie_json,
                speed=1,
                loop=True,
                height=550,
                width=550,
                quality="medium")

    pie_chart = px.pie(df_participants,
                    title = "Weekly Review",
                    values = "Rev.",
                    names="Food")

    st.plotly_chart(pie_chart)




if st.button("**Logout**"):
    os.system('cmd/c "streamlit run Login.py"')