import streamlit as st
import pandas as pd
import info

st.header("What sport are you!!⚡🏃")
st.write(info.firstline)


##NEW
types= ("Competitive", "Team player", "Independent")
select= st.selectbox(
    "1.What kind of player are you?👻 ",
    types
)
st.image(info.competitive, width= 300)
st.write("---")

##NEW              
time= st.number_input("2.How many hours a day do you exercise?🧘‍", min_value=0, max_value=24)
st.image(info.exercise, width=300)
st.write("---")

##NEW
height = st.slider("3.How tall are you (ft)⛹?", 4.0, 7.0)
st.image(info.height, width= 300)
st.write("---")

env = st.radio(
"4.What environment do you enjoy being in?⛅",
["Sunny Outdoors", "Indoors everytime", "Breezy Outdoors", "Rainy Settings"]
)
st.image(info.sunny, width= 300)
st.write("---")
ans= ("I like to use a racket to direct the ball", "I just like to use my body in sports", "I prefer using other equipment")
selected_type= st.selectbox(
    "5. What type of movement do you like in sports (if any)🤺?",
    ans
)
st.image(info.racket, width= 300)
st.write("---")

def get_result(select, time, height, env, ans):
    if select=="Competitive" or env=="Indoors everytime":
        return "🏸 Badminton"
    elif select=="Team player" or ans=="I just like to use my body in sports":
        return "🏐 Volleyball"
    elif select=="Independent" or height>5.0:
        return "🏊 Swimming"
    elif time>2 or height>5.5:
        return "🏀 Basketball"
    else:
        return "🎾 Tennis"
        
if st.button("Show My Sport Personality!"):
         result= get_result(select, time, height, env, ans)
         st.subheader(f"You're {result}!")

####


