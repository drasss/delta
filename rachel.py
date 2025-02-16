import streamlit as st
import time
import datetime
from datetime import date
dt=st.date_input("date",value=date.fromisoformat('2019-02-16'))

click=st.button("Calculate")
if click:
      d=(date.today()-dt).days
      
      e=st.expander("Click to discover the result")
      e.text("c'était il y a "+str(d)+" jours")
      e.text("c'était il y a "+str(int(d//30.19))+" mois")
      e.text("c'était il y a "+str(int(d//364.2425))+" an")
