import streamlit as st
from pages import Home, Menu, Mood_Tracker, Loyalty

st.set_page_config(page_title="Dopamine Coffee ☕", layout="wide")

def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "Menu", "Mood Tracker", "Loyalty"])
    
    if page == "Home":
        Home.show()
    elif page == "Menu":
        Menu.show()
    elif page == "Mood Tracker":
        Mood_Tracker.show()
    elif page == "Loyalty":
        Loyalty.show()

if __name__ == '__main__':
    main()

