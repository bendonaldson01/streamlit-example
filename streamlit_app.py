from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

st.table("Here's our first attempt at using data to create a table:")
st.table(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))