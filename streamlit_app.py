from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

x = st.slider('x')

df = pd.DataFrame({
  'first column': [1, 2, x, 4],
  'second column': [10, 20, 30, 40]
})

st.line_chart(df)