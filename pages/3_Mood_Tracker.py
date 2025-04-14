import streamlit as st
import plotly.express as px
import pandas as pd
from utils.firebase_utils import log_mood_entry, get_mood_logs, increment_loyalty_points

st.title("Mood Tracker 📈")
st.markdown("Track how your coffee affects your mood over time.")

mood = st.radio("How do you feel right now?", ["😴 Sleepy", "🙂 Okay", "😁 Great", "🚀 Hyper-Productive"])

if st.button("Log Mood"):
    log_mood_entry(mood)
    increment_loyalty_points("guest")  # hardcoded for now, will be dynamic after login
    st.success("Mood saved and cup collected!")

mood_logs = get_mood_logs()

if mood_logs:
    df = pd.DataFrame(mood_logs)
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    mood_score_map = {
        "😴 Sleepy": 1,
        "🙂 Okay": 2,
        "😁 Great": 3,
        "🚀 Hyper-Productive": 4
    }
    df["score"] = df["mood"].map(mood_score_map)

    fig = px.line(df, x="timestamp", y="score", markers=True,
                  title="Mood Trend Over Time",
                  labels={"timestamp": "Time", "score": "Mood Score"})

    fig.update_layout(yaxis=dict(
        tickmode='array',
        tickvals=[1, 2, 3, 4],
        ticktext=["😴 Sleepy", "🙂 Okay", "😁 Great", "🚀 Hyper"]
    ))

    st.plotly_chart(fig, use_container_width=True)

    with st.expander("📄 View Mood Log Table"):
        st.dataframe(df[["timestamp", "mood"]])

    # CSV Export button
    csv = df[["timestamp", "mood"]].to_csv(index=False).encode("utf-8")
    st.download_button(
        label="📥 Download Mood Log as CSV",
        data=csv,
        file_name="mood_log.csv",
        mime="text/csv"
    )
else:
    st.info("No mood logs yet. Start by logging one above!")
