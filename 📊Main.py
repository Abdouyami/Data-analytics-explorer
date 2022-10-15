import streamlit as st
from streamlit_lottie import st_lottie
import requests

st.set_page_config(page_title="Data Science Projects", page_icon="📉", layout="wide")


def load_animation(url):
    r = requests.get(url)
    if r.status_code != 200:
        return none;
    else:
        return r.json()

animation = load_animation("https://assets7.lottiefiles.com/packages/lf20_nc0px8fd.json")
think = load_animation("https://assets7.lottiefiles.com/packages/lf20_yfsmbm0r.json")


left, right = st.columns((1,2))
with left:
    st_lottie(think, height=300, key="think")
with right:
    st.title("Welcome to Analytics Data 👋")

    st.markdown("""This Website will help You to explore some data<br>
             As you see in sidebar, we have :
           <ol>
             <li> NBA PLayer Stats Explorer
             <li> Molecular Solubility Prediction
             <li> Penguin Prediction (predict peguin species)
             <li> NFL Football Stats (Rashing) Explorer
             <li> SP500
         </ol> """, unsafe_allow_html=True)

st.write("---")
st_lottie(animation, height=500,  key="Analytics")
