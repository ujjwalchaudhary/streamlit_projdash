import streamlit as st
import pandas as pd

st.set_page_config(page_title="Project Command Center", layout="wide")

st.title("🧭 Project Command Center – Phase 1")

# ---------------- DATA ----------------
data = {
    "Project": [
        "CRM Automation",
        "Excel Insight Engine",
        "Autonmous Agent",
        "RAG Pipeline",
        "Complaint Dashboard",
        "IoT Health Monitor",
        "Email Automation",
        "Snmp And Python Router TroubleShooting",
        "Excel to Outlook By Python",
        "Space Data Analysis",
        "Laptop Replacement App",
        "Reddit Streamlit Dasboard"
    ],
    "Progress": [60, 80, 20, 40, 70, 30, 70, 45, 25, 15,70,75]
}

df = pd.DataFrame(data)

# ---------------- KPI SECTION ----------------
total_projects = len(df)
avg_progress = round(df["Progress"].mean(), 1)
near_finish = (df["Progress"] >= 70).sum()
at_risk = (df["Progress"] < 40).sum()

col1, col2, col3, col4 = st.columns(4)
col1.metric("📦 Total Projects", total_projects)
col2.metric("📊 Avg Completion", f"{avg_progress}%")
col3.metric("🟢 Near Finish", near_finish)
col4.metric("🔴 At Risk", at_risk)

st.markdown("---")

# ---------------- PROGRESS BARS ----------------
st.subheader("📈 Project Progress")

for _, row in df.iterrows():
    progress = row["Progress"]

    if progress >= 70:
        status = "🟢"
    elif progress >= 40:
        status = "🟡"
    else:
        status = "🔴"

    st.markdown(f"**{row['Project']}** {status}")

    st.progress(progress / 100)

