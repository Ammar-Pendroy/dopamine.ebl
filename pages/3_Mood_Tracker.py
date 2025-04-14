import streamlit as st
import datetime
import plotly.express as px
import pandas as pd

def show():
    st.title("Mood Tracker 📈")
    st.markdown("Track how your coffee affects your mood over time.")

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

        # Convert to DataFrame
        df = pd.DataFrame(st.session_state.mood_log)
        df['timestamp'] = pd.to_datetime(df['timestamp'])

        # Assign mood scores
        mood_score_map = {
            "😴 Sleepy": 1,
            "🙂 Okay": 2,
            "😁 Great": 3,
            "🚀 Hyper-Productive": 4
        }
        df["score"] = df["mood"].map(mood_score_map)

        # Line chart
        fig = px.line(df, x="timestamp", y="score", markers=True,
                      title="Mood Trend Over Time",
                      labels={"timestamp": "Time", "score": "Mood Score"})

        fig.update_layout(yaxis=dict(
            tickmode='array',
            tickvals=[1, 2, 3, 4],
            ticktext=["😴 Sleepy", "🙂 Okay", "😁 Great", "🚀 Hyper"]
        ))

        st.plotly_chart(fig, use_container_width=True)

        # Optional: Show raw log
        with st.expander("View Raw Mood Log"):
            st.dataframe(df[["timestamp", "mood"]])
