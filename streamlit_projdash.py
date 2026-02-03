import streamlit as st
import pandas as pd
import plotly.express as px

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


st.subheader("🏆 Project Progress – Ranked View")

# Sort projects by progress
df_sorted = df.sort_values(by="Progress", ascending=True)

# Color logic
def status_color(p):
    if p >= 70:
        return "🟢 Near Completion"
    elif p >= 40:
        return "🟡 In Progress"
    else:
        return "🔴 At Risk"

df_sorted["Status"] = df_sorted["Progress"].apply(status_color)

fig = px.bar(
    df_sorted,
    x="Progress",
    y="Project",
    orientation="h",
    color="Status",
    text="Progress",
    color_discrete_map={
        "🟢 Near Completion": "green",
        "🟡 In Progress": "orange",
        "🔴 At Risk": "red"
    },
    title="Project Completion Leaderboard"
)

fig.update_layout(
    xaxis_title="Completion (%)",
    yaxis_title="",
    showlegend=True,
    height=500
)

fig.update_traces(texttemplate="%{text}%", textposition="outside")

st.plotly_chart(fig, use_container_width=True) 


