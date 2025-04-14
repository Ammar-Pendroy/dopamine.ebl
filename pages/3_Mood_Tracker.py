import streamlit as st
import datetime

def show():
    st.title("Mood Tracker 📈")
    st.markdown("Track how your coffee affects your mood.")

    mood = st.radio("How do you feel right now?", ["😴 Sleepy", "🙂 Okay", "😁 Great", "🚀 Hyper-Productive"])

    if "mood_log" not in st.session_state:
        st.session_state.mood_log = []

    if st.button("Log Mood"):
        st.session_state.mood_log.append({
            "mood": mood,
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        })
        st.success("Mood logged!")

    if st.session_state.mood_log:
        st.markdown("### Your Mood History:")
        for entry in reversed(st.session_state.mood_log):
            st.write(f"{entry['timestamp']} — {entry['mood']}")
