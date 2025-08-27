import streamlit as st
import pandas as pd
import numpy as np

st.title("Hello this is a streamlit app")
st.write("this is some ransdom text")

data = pd.DataFrame({
    'first col':[1,2,3,4],
    'second col':[10,20,30,30]
})
st.write(data)

chart_data = pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','d']
)
st.line_chart(chart_data)