import streamlit as st

st.set_page_config(
  page_title="Kuliah Praktisi 23.05",
  page_icon="🧊",
  initial_sidebar_state="expanded",
  layout="centered"
)

st.title("📊 Dashboard")
st.header("Laporan Bulanan")
st.subheader("📈 Monthly Expenses")
st.caption("Made with ❤️ using Streamlit")
st.write("Hello, *World!* 😃")

st.button("Reset", type="primary")
if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")

title = st.text_input("Movie title", "Life of Brian")
st.write("The current movie title is", title)
