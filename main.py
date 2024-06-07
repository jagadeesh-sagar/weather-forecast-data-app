import streamlit as st
import plotly.express as px
from back_end import get_data

st.title("Weather forecast for the Next Days")
place=st.text_input("place:")
days=st.slider("Forecast Days",min_value=1,max_value=5,help="select the number of forecasted days")
option=st.selectbox("Select data to view",("Sky","Temperature"))
st.subheader(f"Temperature for the next {days} days in {place}")



if place:
    try:
        filter_data = get_data(place, days)
        if option == "Temperature":
            temperature = [dict["main"]["temp"]/10 for dict in filter_data]

            dates=[dict["dt_txt"] for dict in filter_data]
            figure=px.line(x=dates,y=temperature,labels={"x":"Date","y":"Temperaturec(c)"})
            st.plotly_chart(figure)
        if option == "Sky":
            images ={"Clear":"images (2)/Clear.png","Clouds":"images (2)/Clouds.png","Rain":"images (2)/rain.png","Snow":"images (2)/snow.png"}
            sky_conditions = [dict["weather"][0]["main"] for dict in filter_data]
            images_paths=[images[condition] for condition in sky_conditions]

            st.image(images_paths,width=115)

    except (KeyError):
        st.info("That place does not exit or not available")

