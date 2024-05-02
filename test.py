import streamlit as st
import langchain_helper

st.title("Restaurant Name Generator")

cuisine = st.sidebar.selectbox("Pick a Cuisine", ("Indian", "Japanese", "Italian", "Mexican", "Arabic", "Spanish"))

if cuisine:
    response = langchain_helper.test(cuisine)
    st.header(response['restaurant_name'].strip())
    menu_items = response['menu_items'].strip().split(",")
    st.write("**Menu Items**")
    for idx, item in enumerate(menu_items, start=1):
        st.write(f"{idx}. {item.strip()}")

