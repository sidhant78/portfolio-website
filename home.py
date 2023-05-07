import streamlit as st
import pandas
st.set_page_config(layout="wide")
col1,col2 = st.columns(2)
with col1:
    st.image("images/photo.png")
with col2:
    st.title("Sidhant Sarangi")
    content = """Hey! Sidhant here,i started my journey with python a few years ago, now i cant keep my hands off
    my python programs,Python was my introduction to the coding world and i am grateful for such a great introduction.
    I had a lot of fun and learned a lot while creating fun and interactive apps simultaneously and raising the bar
    higher in terms of functionality and features.It is a very simple yet very powerful language.I am a Btech student
    at NIT Rourkela, and aspire to become a great data analyst,Here are some of my projects i hope you like them.
    """
    st.info(content)
st.write("Below are some of the apps i have designed,Feel free to contact me")
col3,empty_space, col4 = st.columns([1.5,0.5,1.5])
df = pandas.read_csv("excel.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.info(row["description"])
        st.image("images/"+row["image"])
        st.write(f"[Source Code]({row['url']})")
with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.info(row['description'])
        st.image("images/"+row["image"])
        st.write(f"[Source Code]({row['url']})")

