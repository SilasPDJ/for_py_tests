import streamlit as st

# Create a sample list of tuples
data = [('A', 10), ('B', 20), ('C', 30), ('D', 40)]

# Reverse the order of the tuples
data = data[::-1]

# Create a horizontal bar chart
st.bar_chart(data, height=200, width=400)
