import streamlit as st
import pandas as pd

st.title("hell0")
name = st.text_input("enter your name")
age = st.slider("select your age",0,100,23)
st.write(f"hi {name}, you are {age} years old") #this will display text
if name:
    st.write(f"hi {name},you are {age} years old after eneter") #after clicking enter

options = ['py','java','c++','C']
choice = st.selectbox("select your language",options)
if(choice):
    st.write(f"you like {choice} lang")

data = pd.DataFrame({
    'id':[1,2,3,4],
    'name': ['a','b','c','d'],
    'age':[23,34,232,434]
})
st.write(data)

get_data = st.file_uploader("upload a csv file",type=['csv'])
if get_data is not None:
    df = pd.read_csv(get_data)
    st.write(df)
    
 