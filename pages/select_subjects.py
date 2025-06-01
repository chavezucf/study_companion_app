import streamlit as st
from core.subject_manager import SubjectManager
from components.subject_multi_selector import render_subject_multi_selector

st.set_page_config(page_title="Select Subjects", page_icon="🗂️", layout="centered")

QUESTIONS_PATH = "data/questions.json"
subject_manager = SubjectManager(QUESTIONS_PATH)
subjects = sorted(subject_manager.get_subjects())

st.title("Choose Subjects to Study")
st.write("Pick one or more subjects to focus your study session.")

# Render selector
selected_subjects = render_subject_multi_selector(subjects)

# Confirm selection
if st.button("Continue", disabled=not selected_subjects):
    st.session_state.subjects_confirmed = True
    st.success(f"Selected: {', '.join(selected_subjects)}. Ready to start!")

# Show selected subjects
if selected_subjects:
    st.info(f"Selected subjects: {', '.join(selected_subjects)}")