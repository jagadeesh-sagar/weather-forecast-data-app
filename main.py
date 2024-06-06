import streamlit as st
import plotly.express as px
from back_end import get_data

st.title("Weather forecast for the Next Days")
place=st.text_input("place:","Delhi")
days=st.slider("Forecast Days",min_value=1,max_value=5,help="select the number of forecasted days")
option=st.selectbox("Select data to view",("Temperature","Sky"))
st.subheader(f"Temperature for the next {days} days in {place}")


data=get_data(place,days,option)
figure=px.line(x=d,y=data,labels={"x":"Date","y":"Temperaturec(c)"})
st.plotly_chart(figure)