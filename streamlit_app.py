import streamlit as st
import pandas as pd
import requests
from st_aggrid import AgGrid

house = pd.read_csv('house_clean.csv')

def main ():
  st.header('This is Header')
  st.subheader('This is SubHeader')
  st.markdown('# Rendering Markdown ')
  st.write('Some Phytagorean Equation : ')
  st.latex('c^2 = a^2+b^2')

if __name__ == '__main__' :
  main()
