import streamlit as st
st.title("Weather forecast for the Next Days")
place=st.text_input("place:")
days=st.slider("Forecast Days",min_value=1,max_value=5,help="select the number of forecasted days")
option=st.selectbox("Select data to view",("Temperature","Sky"))
st.subheader(f"Temperature for the next {days} days in {place}")