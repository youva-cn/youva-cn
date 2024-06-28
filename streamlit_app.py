import streamlit as st
import pandas as pd
# import requests
from st_aggrid import AgGrid

house = pd.read_csv('house_clean.csv')

def main ():
  st.header('This is Header')
  st.subheader('This is SubHeader')
  st.markdown('# Rendering Markdown ')
  st.write('Some Pythagorean Equation : ')
  st.latex('c^2 = a^2+b^2')

  st.dataframe(house)

  # Untuk menulis metric
  st.write('Metrics')
  st.metric(label="Temperature", value="70 °F", delta="-1.2 °F")
  # Menampilkan AgGrid
  st.write('Menampilkan Dataframe dengan St AgGrid')
  AgGrid(house)
  
  st.table([x for x in range(1,5)])
  
  click_me_btn = st.button('Click Me')
  st.write(click_me_btn) #Return True kalo di Click 
  check_btn = st.checkbox('Klik Jika Setuju')
  if check_btn :
      st.write('Anda Setuju')
  
  radio_button= st.radio('Choose below',[x for x in range(1,3)])
  st.write('Anda Memilih',radio_button)

  #slider
  age_slider = st.slider('Berapa Usia Anda',0,100)
  st.write('Usia Anda',age_slider)

  #Input (Typing)
  num_input = st.number_input('Input Berapapun')
  st.write('Kuadrat dari {} adalah {}'.format(num_input,num_input**2))

if __name__ == '__main__' :
  main()
