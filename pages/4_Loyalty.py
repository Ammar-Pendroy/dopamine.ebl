import streamlit as st
from utils.firebase_utils import get_loyalty_points, increment_loyalty_points, reset_loyalty_points

st.title("Loyalty Program 🎉")
st.markdown("Track your caffeine-powered progress and earn rewards!")

# User identifier (hardcoded for now)
user_id = "guest"

# Fetch points
points = get_loyalty_points(user_id)
st.metric("☕ Cups Collected", points)
st.progress(min(points, 10) / 10)

if points >= 10:
    if st.button("🎁 Redeem Reward"):
        st.success("You've redeemed a free drink! Your counter has been reset.")
        reset_loyalty_points(user_id)
else:
    st.info("Collect 10 cups to unlock a free drink!")
