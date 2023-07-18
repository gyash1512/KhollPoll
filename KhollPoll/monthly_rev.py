import streamlit as st
import plotly.express as px
from PIL import Image
import pandas as pd

st.set_page_config(page_title="Mess Review", page_icon="🍞", layout="wide")
st.header("Welcome To ***Mess Review System*** 🍱")

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



st.dataframe(df_participants)

pie_chart = px.pie(df_participants,
                   title = "Weekly Review",
                   values = "Rev.",
                   names="Food")

st.plotly_chart(pie_chart)