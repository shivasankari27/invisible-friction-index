import streamlit as st
import pandas as pd
import numpy as np

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Invisible Friction Index",
    layout="wide"
)

st.title("Invisible Friction Index")
st.caption("System-level academic design friction — not student weakness")

uploaded = st.file_uploader("Upload student-mat.csv", type="csv")

if uploaded:
    # --------------------------------------------------
    # LOAD DATA
    # --------------------------------------------------
    df = pd.read_csv(uploaded, sep=",")

    # --------------------------------------------------
    # FRICTION FEATURE ENGINEERING
    # --------------------------------------------------
    df["schedule_density"] = df["studytime"] * 2 + df["absences"] * 0.1
    df["back_to_back_score"] = (df["studytime"] >= 3).astype(int)
    df["deadline_density"] = df["failures"] + (df["studytime"] > 2).astype(int)
    df["temporal_rigidity"] = df["studytime"] + (df["absences"] > 5).astype(int)

    friction_features = [
        "schedule_density",
        "back_to_back_score",
        "deadline_density",
        "temporal_rigidity",
    ]

    df["friction_index"] = df[friction_features].mean(axis=1)
    df["friction_index"] = df["friction_index"] / df["friction_index"].max()

    # --------------------------------------------------
    # RISK BANDS
    # --------------------------------------------------
    def risk_band(x):
        if x < 0.33:
            return "🟢 Survivable"
        elif x < 0.66:
            return "🟡 Warning"
        else:
            return "🔴 Unsafe"

    df["risk_band"] = df["friction_index"].apply(risk_band)

    # --------------------------------------------------
    # SYSTEM-LEVEL DASHBOARD
    # --------------------------------------------------
    st.subheader("System-Level Friction Summary")

    avg_friction = round(df["friction_index"].mean(), 3)
    band_pct = df["risk_band"].value_counts(normalize=True) * 100

    c1, c2, c3 = st.columns(3)
    c1.metric("Average Friction Index", avg_friction)
    c2.metric("Unsafe (%)", f"{round(band_pct.get('🔴 Unsafe', 0), 1)}%")
    c3.metric("Warning (%)", f"{round(band_pct.get('🟡 Warning', 0), 1)}%")

    st.divider()

    # --------------------------------------------------
    # RISK DISTRIBUTION CHART
    # --------------------------------------------------
    st.subheader("Friction Risk Distribution")

    chart_df = (
        df["risk_band"]
        .value_counts()
        .reindex(["🟢 Survivable", "🟡 Warning", "🔴 Unsafe"])
        .fillna(0)
    )

    st.bar_chart(chart_df)

    st.divider()

    # --------------------------------------------------
    # DESIGN FIX SUGGESTIONS
    # --------------------------------------------------
    st.subheader("Design-Level Fix Suggestions")

    mean_components = df[friction_features].mean()
    top_issue = mean_components.idxmax()

    if top_issue == "back_to_back_score":
        st.warning(
            "High back-to-back intensity detected. "
            "Insert 15–30 minute buffer gaps between sessions."
        )
    elif top_issue == "deadline_density":
        st.warning(
            "Deadline clustering detected. "
            "Spread assessments across weeks instead of stacking them."
        )
    elif top_issue == "temporal_rigidity":
        st.warning(
            "Early + late scheduling detected. "
            "Introduce flexible start times or protected recovery windows."
        )
    else:
        st.warning(
            "High daily compression detected. "
            "Reduce schedule density to preserve cognitive energy."
        )

    st.divider()

    # --------------------------------------------------
    # DATA PREVIEW
    # --------------------------------------------------
    st.subheader("Sample Friction Analysis")

    st.dataframe(
        df[
            [
                "studytime",
                "absences",
                "friction_index",
                "risk_band",
            ]
        ].head(10),
        use_container_width=True,
    )

    st.divider()

    # --------------------------------------------------
    # MODEL CARD
    # --------------------------------------------------
    with st.expander("📄 Model Card & Scope"):
        st.markdown(
            """
            **What this model measures**
            - Academic design friction derived from schedule and workload proxies.
            - System-imposed stress, not student behavior.

            **What this model does NOT do**
            - No mental health diagnosis.
            - No behavioral surveillance.
            - No student labeling or grading decisions.

            **Intended users**
            - Timetable designers
            - Academic planners
            - Institutional policy teams

            **Purpose**
            - Detect unsafe academic design patterns **before** burnout and failure occur.
            """
        )
