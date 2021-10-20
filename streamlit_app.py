from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

st.line_chart(df)