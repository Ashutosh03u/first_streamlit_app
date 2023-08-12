import streamlit

streamlit.title('Welcome to My First Apps')
streamlit.header('🥣 Breakfast Menu')
streamlit.text('🥗Omega 3 & Blueberry Oatmeal')
streamlit.text('🐔Kale, Spinach & Rocket Smoothie')
streamlit.text('🥑🍞Hard-Boiled Free-Range Egg')

import pandas 
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
Fruit_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Apple','Banana'])
Fruit_to_show = my_fruit_list.loc[Fruit_selected]

# Display the table on the page.
streamlit.dataframe(Fruit_to_show)

import requests
fruityvice_response = requests.get("https://www.fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)
