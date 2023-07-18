from PIL import Image
import streamlit as st
import plotly.express as px0
import pandas as pd 
import os
from streamlit_lottie import st_lottie
import requests

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    else:
        return r.json()


st.set_page_config(page_title="Events", page_icon="📅",layout="wide")
col1, col2, col3 = st.columns([6,6,1])

with col1:
    st.image("banner.png",width = 150)
    st.write("")
    st.write("")
with st.container():
    col1, col2, col3= st.columns([2,1,1])
    with col1:
        st.subheader("*Hi User! Welcome to*")
        original_title= "<p style='font-family:ALGERIAN; color:aqua; font-size: 80px;'>EVENTS</p>"
        st.markdown(original_title, unsafe_allow_html=True)
        st.write("""
        Access Every Information Regarding Any Event\n
        **Stay Updated!!!**
    """)
    with col3:
        lottie_url1 = "https://assets3.lottiefiles.com/packages/lf20_uMjybUoeGN.json"
        lottie_json = load_lottieurl(lottie_url1)
        st_lottie(
                lottie_json,
                speed=1,
                loop=True,
                height=300,
                width=250,
                quality="medium")
    
    #st.markdown("# EVENT ❄")
    search=st.text_input("Search ")
    data=pd.read_csv("user1.csv")
    name=data["Name"]
    date=data["Date"]
    desc=data["Description"]

    for i in range(len(name)):
        if search == name[i]:
            st.write(name[i]+" \n "+date[i]+" \n "+desc[i])



tab1, tab2, tab3 = st.tabs(["***Daily Updates***", "***Clubs & Chapters***", "***Review For EVENTS***"])

with tab1:
    st.header("WIE PRESENTS")
    image_column, text_column, text1_column = st.columns((2,3,1))
    with image_column:
            st.image("ss.png",width=370)
            

    with text_column:
            st.subheader("FILS")
            st.write("""
            WIE Is coming with FILS for freelancing, internship, linkedin and startup \n
            Get to Known about the important topics.       
            """)
            st.markdown("[SITE LINK...](https://sites.google.com/d/1q7JYm--x3cUfGqZ_ZiaKuNJEBL0Jr117/p/1vpb9wyDlOQnXqZpa88dWMv1TiGHsBUNj/edit)")

    with  text1_column:
        st.write("""
        Date & Venue \n
        ON 11 - 12 - 2022  
        AT NLH-103
        """)
    st.header("GFG PRESENTS")
    image_column, text_column, text1_column = st.columns((2,3,1))
    with image_column:
            st.image("s1.png",width=370)
            

    with text_column:
            st.subheader("SPIN THE CODE")
            st.write("""
            GFG presents SPIN the Code,a team-based contest where team management and speed will shine and be tested\n
            Expierence the industrial simulation with the joyfulness of live audience of your hostel\n
            "Programming is fun because when in doubt,just spin it out".
             """)
            st.markdown("[SITE LINK...](https://sites.google.com/d/1q7JYm--x3cUfGqZ_ZiaKuNJEBL0Jr117/p/1vpb9wyDlOQnXqZpa88dWMv1TiGHsBUNj/edit)")

    with  text1_column:
        st.write("""
        Date & Venue \n
        ON 01 - 12 - 2022  
        AT ALH-002
        """)

    st.header("ATC PRESENTS")
    image_column, text_column, text1_column = st.columns((2,3,1))
    with image_column:
            st.image("s5.png",width=370)
            

    with text_column:
            st.subheader("BULLETPROOF")
            st.write("""
             Alan Turing Club get rid of all your fears and insecurities and inspired to work on yourself & make you"BULLETPROOF"\n
            Get ready to know more!.
           """)
            st.markdown("[SITE LINK...](https://sites.google.com/d/1q7JYm--x3cUfGqZ_ZiaKuNJEBL0Jr117/p/1vpb9wyDlOQnXqZpa88dWMv1TiGHsBUNj/edit)")

    with  text1_column:
        st.write("""
        Date & Venue \n
        ON 28 - 11 - 2022  
        AT ALH-002
        """)


    st.header("CODE_CHEF PRESENTS")
    image_column, text_column, text1_column = st.columns((2,3,1))
    with image_column:
            st.image("s2.png",width=370)
            

    with text_column:
            st.subheader("SYMPOSIUM")
            st.write("""
              Introducing by Codechef to help you make it big in the world of algorithms,programming and coding contests\n
            " Take a step ahead in coding ".
          """)
            st.markdown("[SITE LINK...](https://sites.google.com/d/1q7JYm--x3cUfGqZ_ZiaKuNJEBL0Jr117/p/1vpb9wyDlOQnXqZpa88dWMv1TiGHsBUNj/edit)")

    with  text1_column:
        st.write("""
        Date & Venue \n
        ON 13 - 12 - 2022  
        AT NLH-102
        """)
    

    st.header("GDSC AND FULL STACK PRESENT")
    image_column, text_column, text1_column = st.columns((2,3,1))
    with image_column:
            st.image("s3.png",width=370)
            

    with text_column:
            st.subheader("ANDROID CAMPUS FEST")
            st.write("""
             GDSC in collaboration with FullStack Club is organizing Android Campus Fest to share Modern Android Development(MAD)knowledge\n
            Let's Grab Some Knowledge.
            """)
            st.markdown("[SITE LINK...](https://sites.google.com/d/1q7JYm--x3cUfGqZ_ZiaKuNJEBL0Jr117/p/1vpb9wyDlOQnXqZpa88dWMv1TiGHsBUNj/edit)")

    with  text1_column:
        st.write("""
        Date & Venue \n
        ON 25 - 11 - 2022  
        AT NLH-101
        """)

    st.header("ANSH PRESENTS")
    image_column, text_column, text1_column = st.columns((2,3,1))
    with image_column:
            st.image("s6.png",width=370)
            

    with text_column:
            st.subheader("NUKKAD NATAK")
            st.write("""
            Ansh Present a Nukkad NatAK in support of a cause that is important all of us \n
            " DESTIGMATIZING PERIODS ".
            """)
            st.markdown("[SITE LINK...](https://sites.google.com/d/1q7JYm--x3cUfGqZ_ZiaKuNJEBL0Jr117/p/1vpb9wyDlOQnXqZpa88dWMv1TiGHsBUNj/edit)")

    with  text1_column:
        st.write("""
        Date & Venue \n
        ON 12 - 11 - 2022  
        IN FRONT OF C3
        """)
    
    st.header("CREBRUM PRESENTS")
    image_column, text_column, text1_column = st.columns((2,3,1))
    with image_column:
            st.image("s4.png",width=370)
            

    with text_column:
            st.subheader("THE BOOS & HOOS")
            st.write("""
            Cerebrum presents to you "THE BOOS AND HOOS",an open mic scary storytelling competition\n
             Get ready to participate and shine.
            """)
            st.markdown("[SITE LINK...](https://sites.google.com/d/1q7JYm--x3cUfGqZ_ZiaKuNJEBL0Jr117/p/1vpb9wyDlOQnXqZpa88dWMv1TiGHsBUNj/edit)")

    with  text1_column:
        st.write("""
        Date & Venue \n
        ON 31 - 10 - 2022  
        ON OPEN GROUND
        """)
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    Zol1, zol2, zol3=st.columns([2,5,1])
    with zol2:
        lottie_url1 = "https://assets6.lottiefiles.com/packages/lf20_2Ths6akDLy.json"
        lottie_json = load_lottieurl(lottie_url1)
        st_lottie(
                lottie_json,
                speed=1,
                loop=True,
                height=500,
                width=500,
                quality="medium")


with tab2:
   st.header("BENNETT UNIVERSITY")

   expander = st.expander("Clubs & Chapters")
   expander.write("""
    Ansh\n
    Yoga Club\n
    Silhouette\n
    Astronomy Club\n
    Anime Club\n
    Pulse\n
    Cerebrum Club\n
    Comedy\n
    Art of Living\n
    Sunset Movie\n
    Nomads\n
    Rivaaz\n
    ISAC\n
    Castify\n
    Food & Cuisine\n
    Advaita\n
    SPARK\n
    VERVE\n
""")

   st.header("School of ENGINERRING")

   expander = st.expander("Clubs & Chapters")
   expander.write("""\n
    Alan Turing Club(ATC)\n
    CodeChef(CC)\n
    Geeks for Geeks(GfG)\n
    Google Developer Student Club(GDSC)\n
    (IEEE)\n
    Women In Engineering(IEE-WIE)\n
    Computer Society of India(CSI)\n
    A Community of Tech Enthusiasts(ACM)\n
    FULL STACK\n
    BU Gamers\n
    Silhouette\n
    BlockChain\n
""")

   st.header("School of LAW")

   expander = st.expander("Clubs & Chapters")
   expander.write("""Moot COURT""") 
   st.write("")
   st.write("")
   st.write("")
   st.write("")
   st.write("")
   Zol1, zol2, zol3=st.columns([2,5,1])
   with zol2:
       lottie_url1 = "https://assets9.lottiefiles.com/packages/lf20_ilp95ggh.json"
       lottie_json = load_lottieurl(lottie_url1)
       st_lottie(
               lottie_json,
               speed=1,
               loop=True,
               height=500,
               width=500,
               quality="medium")
    
   

with tab3:
        image_column, text_column, text1_column = st.columns((2,3,1))
        with image_column:
            st.image("l2.png",width=350)
            

        with text_column:
            st.subheader("IEEE WIE")
            expander = st.expander("Clubs & Chapters")
            expander.markdown("""Alan Turing Club(ATC)\n
    CodeChef(CC)\n
    Geeks for Geeks(GfG)\n
    Google Developer Student Club(GDSC)\n
    (IEEE)\n
    Women In Engineering(IEE-WIE)\n
    Computer Society of India(CSI)\n
    A Community of Tech Enthusiasts(ACM)\n
    FULL STACK\n
    BU Gamers\n
    Silhouette\n
""")    

        image_column, text_column, text1_column = st.columns((2,3,1))
        with image_column:
            st.image("l6.png",width=350)
            

        with text_column:
            st.subheader("ATC")
            expander = st.expander("Clubs & Chapters")
            expander.markdown("""Alan Turing Club(ATC)\n
    CodeChef(CC)\n
    Geeks for Geeks(GfG)\n
    Google Developer Student Club(GDSC)\n
    (IEEE)\n
    Women In Engineering(IEE-WIE)\n
    Computer Society of India(CSI)\n
    A Community of Tech Enthusiasts(ACM)\n
    FULL STACK\n
    BU Gamers\n
    Silhouette\n
""")


        image_column, text_column, text1_column = st.columns((2,3,1))
        with image_column:
            st.image("l5.png",width=350)
            

        with text_column:
            st.subheader("ANSH")
            expander = st.expander("Clubs & Chapters")
            expander.markdown("""Alan Turing Club(ATC)\n
    CodeChef(CC)\n
    Geeks for Geeks(GfG)\n
    Google Developer Student Club(GDSC)\n
    (IEEE)\n
    Women In Engineering(IEE-WIE)\n
    Computer Society of India(CSI)\n
    A Community of Tech Enthusiasts(ACM)\n
    FULL STACK\n
    BU Gamers\n
    Silhouette\n
""")


        image_column, text_column, text1_column = st.columns((2,3,1))
        with image_column:
            st.image("l1.png",width=350)
            

        with text_column:
            st.subheader("IEEE")
            expander = st.expander("Clubs & Chapters")
            expander.markdown("""Alan Turing Club(ATC)\n
    CodeChef(CC)\n
    Geeks for Geeks(GfG)\n
    Google Developer Student Club(GDSC)\n
    (IEEE)\n
    Women In Engineering(IEE-WIE)\n
    Computer Society of India(CSI)\n
    A Community of Tech Enthusiasts(ACM)\n
    FULL STACK\n
    BU Gamers\n
    Silhouette\n
""")


        image_column, text_column, text1_column = st.columns((2,3,1))
        with image_column:
            st.image("l3.png",width=350)
            

        with text_column:
            st.subheader("CODE CHEF")
            expander = st.expander("Clubs & Chapters")
            expander.markdown("""Alan Turing Club(ATC)\n
    CodeChef(CC)\n
    Geeks for Geeks(GfG)\n
    Google Developer Student Club(GDSC)\n
    (IEEE)\n
    Women In Engineering(IEE-WIE)\n
    Computer Society of India(CSI)\n
    A Community of Tech Enthusiasts(ACM)\n
    FULL STACK\n
    BU Gamers\n
    Silhouette\n
""")


        image_column, text_column, text1_column = st.columns((2,3,1))
        with image_column:
            st.image("l4.png",width=350)
            

        with text_column:
            st.subheader("Google Developer Student Club(GDSC)")
            expander = st.expander("Clubs & Chapters")
            expander.markdown("""Alan Turing Club(ATC)\n
        CodeChef(CC)\n
        Geeks for Geeks(GfG)\n
        Google Developer Student Club(GDSC)\n
        (IEEE)\n
        Women In Engineering(IEE-WIE)\n
        Computer Society of India(CSI)\n
        A Community of Tech Enthusiasts(ACM)\n
        FULL STACK\n
        BU Gamers\n
        Silhouette
    """)
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        Zol1, zol2, zol3=st.columns([2,5,1])
        with zol2:
            lottie_url1 = "https://assets7.lottiefiles.com/packages/lf20_98vgucqb.json"
            lottie_json = load_lottieurl(lottie_url1)
            st_lottie(
                lottie_json,
                speed=1,
                loop=True,
                height=450,
                width=500,
                quality="medium")



    

if st.button("**Logout**"):
    os.system('cmd/c "streamlit run Login.py"')