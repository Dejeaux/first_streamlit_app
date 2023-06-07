import streamlit 
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

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
#streamlit.dataframe(fruits_to_show)
#new header for api response
streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?')
streamlit.write('The user entered',fruit_choice)

#import requests

#take json and normalize it

#output to screen
streamlit.dataframe(fruityvice_normalized)   
# new header for api response
streamlit.header( "Fruityvice Fruit Advice!" )
try :
    fruit_choice = streamlit.text_input( 'What fruit would you like information about?' )
    if not fruit_choice:
        streamlit.error( "Please select a fruit to get information" )
    else :
        fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
        fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
        streamlit.dataframe(fruityvoice_normalized)

except URLerror as e:
    streamlit.error()
streamlit.stop()      



#create fruityvice function
def get_fruity_vice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized  

#add a button to load list
if streamlit.button('Get Fruit Load List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_fruit_load_list()
    streamlit.dataframe(my_data_rows)

except URLError as e:
  streamlit.error
#add a stop here

    

#try:
  
#  if not fruit_choice:
    streamlit.error("Please select a fruit to get information")
#  else:  
#    back_from_function = get_fruity_vice_data(fruit_choice)
#    streamlit.dataframe(back_from_function)  
    

#add another header for adding fruit
#def insert_row_snowflake(new_fruit):
#    with my_cnx.cursor() as my_cur:
#        my_cur.execute("insert into fruit_load_list values ('from streamlit')");
#        return "Thanks for adding " + new_fruit
   
#add_my_fruit = streamlit.text_input('What fruit would you like to add?')
#if streamlit.button('Add a Fruit to the List'):
#    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#    back_from_function = insert_row_snowflake(add_my_fruit)
#    streamlit.text(back_from_button)

# moved this area up so it would run. List is now inside a button
streamlit.header( "The Fruit Load List Contains:" )
#moved this area up so it would run. List is now inside a button
#streamlit.header("The Fruit Load List Contains:")
#streamlit add
#def get_fruit_load_list():
#    with my_cnx.cursor() as my_cur: 
#         my_cur.execute("select * from fruit_load_list") 
#         return my_cur.fetchall()

# streamlit add
def get_fruit_load_list ( ) :
    with my_cnx.cursor ( ) as my_cur :
        my_cur.execute ( "select * from fruit_load_list" )
        return my_cur.fetchall ( )


# add a button to load list
if streamlit.button ( 'Get Fruit Load List' ) :
    my_cnx = snowflake.connector.connect ( **streamlit.secrets [ "snowflake" ] )
    my_data_rows = get_fruit_load_list ( )
    streamlit.dataframe ( my_data_rows )

# new header for api response
streamlit.header( "Fruityvice Fruit Advice!" )
try :
    fruit_choice = streamlit.text_input( 'What fruit would you like information about?' )
    if not fruit_choice :
        streamlit.error( "Please select a fruit to get information" )
    else :
        back_from_function = get_fruity_vice_data( fruit_choice )
        streamlit.dataframe( back_from_function )



def insert_row_snowflake(new_fruit):
    with my_cnx.cursor() as my_cur:
        my_cur.execute("insert into fruit_load_list values ('from streamlit')");
        assert isinstance( new_fruit)
        return "Thanks for adding " + new_fruit


add_my_fruit = streamlit.text_input('What fruit would you like to add?')
if streamlit.button('Add a Fruit to the List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    back_from_function = insert_row_snowflake(add_my_fruit)
    streamlit.text(back_from_button)



    
    

    

    












