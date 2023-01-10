import streamlit

streamlit.title('My Mom\'s New Healthy Diner')
streamlit.header('Breakfast Favorites')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard- Boiled Free-Range Egg')
streamlit.text('🥑🍞Avicado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
#Pandas
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#List to pick the fruit
streamlist.multiselect("Pick some fruits:", list(my_fruit_list.index))
#Display the table on the page
streamlit.dataframe(my_fruit_list)
