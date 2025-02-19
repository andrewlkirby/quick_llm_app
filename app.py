import streamlit as st
from model import get_output

# Streamlit interface
st.title("C2 Proficiency Sentence Rewriter")

# Input box for user text
user_input = st.text_area(label = "Enter a sentence to be rewritten:",
                          height = 250
                          )

# When the user provides input, display the output
if user_input:
    with st.spinner("Generating rewrite..."):
        rewritten_sentence = get_output(user_input)
        st.success("Here's the rewrite:")
        st.write(rewritten_sentence)
