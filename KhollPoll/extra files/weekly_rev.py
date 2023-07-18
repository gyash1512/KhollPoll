import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image
from streamlit_lottie import st_lottie
import requests

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    else:
        return r.json()

lottie_url = "https://assets8.lottiefiles.com/packages/lf20_7aJ0JNKOVj.json"
lottie_json = load_lottieurl(lottie_url)

st.set_page_config(page_title="Mess Review", page_icon="🍞", layout="wide")
st.header("Welcome To ***Mess Review System*** 🍱")

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