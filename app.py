import streamlit as st
import json
import os
import plotly.express as px
from core.orchestrator import Orchestrator

st.set_page_config(page_title="AI Code Reviewer", page_icon="🤖", layout="wide")

st.title("🤖 AI Code Reviewer")
st.write("Upload your code file and get an automated analysis and refactor suggestions.")

uploaded_file = st.file_uploader("Upload a Python file", type=["py"])

if uploaded_file:
    os.makedirs("temp", exist_ok=True)
    file_path = os.path.join("temp", uploaded_file.name)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.info("🔍 Running AI Code Review...")
    orchestrator = Orchestrator(file_path)
    report_path = orchestrator.run()

    st.success("✅ Code review completed successfully!")

    # Find latest report
    if os.path.exists(report_path):
        try:
            with open(report_path, "r", encoding="utf-8") as f:
                report = json.load(f)

            st.subheader("📊 Final Review Summary")
            st.json(report)

            # Display Original and Refactored Code Side-by-Side
            refactored_file = report.get("refactor_suggestions", "")

            if os.path.exists(refactored_file):
                st.subheader("🧾 Original vs Refactored Code")

                col1, col2 = st.columns(2)
                with col1:
                    st.markdown("### 🧱 Original Code")
                    with open(file_path, "r", encoding="utf-8") as f:
                        original_code = f.read()
                    st.code(original_code, language="python")

                with col2:
                    st.markdown("### 🧠 Refactored Code")
                    with open(refactored_file, "r", encoding="utf-8") as f:
                        refactored_code = f.read()
                    st.code(refactored_code, language="python")

            else:
                st.warning("⚠️ Refactored file not found.")

        except json.JSONDecodeError:
            st.error("⚠️ Report file could not be read properly. Please re-upload your file and try again.")
    else:
        st.warning("⚠️ No report generated yet.")
