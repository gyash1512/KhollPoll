import streamlit as st
import os


def main():
    st.set_page_config(
    page_title="Kholl Poll",
    page_icon="logo.png",
    )
    
    l,mid,r= st.columns(3)
    with mid:
        st.image("banner.png", width=200)
    cred={"E22CSEU1156":"logmein","E22CSEU1154":"andmetoo","E22CSEU1116":"quackquack","E22CSEU1117":"iamserious","E22CSEU1149":"gigiantickid","RITI.KUSHWAHA":"bennett@btech", "SONAL.KUKREJA":"bennett@btech","VINOD.SHASTRI":"bennett@btech"}
    st.title("Login")
    username = st.text_input("Bennett ID")
    password = st.text_input("Password", type='password')
    
    if st.button("Submit"):
       for key in cred:
            if (username).upper()==key and password == cred[key]:
                st.success("Logged in successfully!!!")
                os.system('cmd /c "streamlit run app.py"')
            elif (username).upper()==key and password !=cred[key]:
                st.error("Incorrect username or password")
   


if __name__ == '__main__':
    main()