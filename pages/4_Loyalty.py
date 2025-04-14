import streamlit as st

def show():
    st.title("Loyalty Program 🎉")
    st.markdown("Earn rewards and dopamine points for every cup!")

    st.write("You currently have:")
    st.metric("☕ Cups Collected", 7)
    st.progress(7 / 10)

    if st.button("Redeem Free Drink"):
        if 7 >= 10:
            st.success("You’ve redeemed a free drink!")
        else:
            st.warning("Not enough cups collected yet. Keep sipping!")
