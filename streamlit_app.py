from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import numpy as np

left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button(chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])
st.line_chart(chart_data))
# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
st.write(f"You are in {chosen} house!") 
