import streamlit as st

def show():
    st.title("Our Menu ☕")
    st.markdown("Browse our handcrafted beverages and bites.")

    menu_items = [
        {"name": "Espresso", "type": "Hot", "caffeine": "High"},
        {"name": "Iced Americano", "type": "Cold", "caffeine": "Medium"},
        {"name": "Cold Brew", "type": "Cold", "caffeine": "High"},
        {"name": "Vanilla Latte", "type": "Hot", "caffeine": "Medium"},
        {"name": "Affogato", "type": "Dessert", "caffeine": "Low"},
    ]

    for item in menu_items:
        st.subheader(item["name"])
        st.write(f"Type: {item['type']}")
        st.write(f"Caffeine Level: {item['caffeine']}")
        st.markdown("---")

