import streamlit as st
from pages import home, menu, mood_tracker, loyalty

st.set_page_config(page_title="Dopamine Coffee ☕", layout="wide")

def main():
    st.sidebar.title("☕ Dopamine Coffee")
    page = st.sidebar.radio("Navigate", ["Home", "Menu", "Mood Tracker", "Loyalty Program"])

    if page == "Home":
        home.show()
    elif page == "Menu":
        menu.show()
    elif page == "Mood Tracker":
        mood_tracker.show()
    elif page == "Loyalty Program":
        loyalty.show()

if __name__ == '__main__':
    main()
