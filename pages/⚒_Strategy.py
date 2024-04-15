import streamlit as st
from runLLM import get_strategy, write_strategy


st.title('quantLLM: An automated crypto strategy generator.')
st.markdown("## How does it work?")

st.markdown("""**A backtester has been implemented with the Python backtrader. Then, an OpenAI assistant has been given access to backtester documentation to implement
any sort of indicators. It also been given a strict template to follow, in order to its code being interpretable by the backtester. It also provides a range of params to optimise.**""")

with open("./assistant_files/GeneratedStrategy.txt", "r") as f:
    comment = f.read()

with open("./assistant_files/GeneratedStrategy.py", "r") as f:
    code = f.read()


prompt = st.text_input('Please describe your strategy here. If you have no idea, you can ask for an orginal one.')
if st.button('Get a new strategy'):
    comment, code = get_strategy(prompt)
    write_strategy(code, comment)

st.markdown("## Current strategy:")
st.markdown(comment)
st.code(code)
