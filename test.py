import streamlit as st
import langchain_helper

st.title("Restaurant Name Generator")

cuisine = st.sidebar.selectbox("Pick a Cuisine", ("Indian", "Bengali", "Mexican", "Arabic", "American"))

if cuisine:
    response = langchain_helper.generate_restaurant_name_and_items(cuisine)
    st.header(response['restaurant_name'].strip())

    # Display menu items with proper formatting
    menu_items = response['menu_items'].strip().split(",")
    st.write("**Menu Items**")
     if "(" in item:
            # Display only the dish name and description (remove additional items)
            dish_name, dish_description = item.split("(", 1)
            st.write(f"{dish_name.strip()} ({dish_description.strip()}")
        else:
            st.write(item)
