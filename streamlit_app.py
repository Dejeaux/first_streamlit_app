import streamlit 
import pandas
import requests

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')


# Display the table on the page.

streamlit.title('My parents new healthy diner')

streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & blueberry oatmeal')
streamlit.text(' 🥗 Kale, Spinach & Rocket smoothie')
streamlit.text(' 🐔 Hard-boiled free-range egg')
streamlit.text('🥑🍞 Avacodo Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

#streamlit.dataframe(my_fruit_list)

#new header for api response
streamlit.header("Fruityvice Fruit Advice!")

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")
#streamlit.text(fruityvice_response.json())

# standardize output
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output normalize data
streamlit.dataframe(fruityvice_normalized)


