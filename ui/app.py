import streamlit as st
st.title("Agentic Code Reviewer (dev)")
st.write("UI placeholder. Upload a file or paste GitHub repo URL to analyze.")
uploaded = st.file_uploader("Upload Python file", type=["py"])
if uploaded:
    content = uploaded.read().decode("utf-8")
    st.code(content, language="python")
    st.info("Analysis will appear here (coming soon).")
