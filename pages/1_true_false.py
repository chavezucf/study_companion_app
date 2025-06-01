# pages/1_true_false.py

import streamlit as st
import random
from utils.logger import log_event
from core.data_manager import DataManager
from core.profile_manager import ProfileManager
from core.subject_manager import SubjectManager
from components.tf_question_block import render_current_question
from components.session_summary import render_session_summary
from utils.ui_helpers import (
    set_page_config,
    render_page_header,
    render_footer
)

# --- PAGE CONFIG ---
set_page_config(page_title="True/False Rapid Fire", page_icon="✅")   

# Initialize profile
profile_manager = ProfileManager()
questions = DataManager.load_questions()

# --- SUBJECT SELECTION FLOW ---
subject_manager = SubjectManager("data/questions.json")

selected_subjects = subject_manager.get_selected_subjects(
    title="Select subjects for True/False",
    key_prefix="tf_subject",
    questions=questions
)

# Filter questions
questions = [q for q in questions if q.get("subject") in selected_subjects] if selected_subjects else questions

# --- SESSION INIT ---
if "tf_questions_shuffled" not in st.session_state:
    random.shuffle(questions)
    st.session_state.tf_questions_shuffled = questions
    st.session_state.tf_question_index = 0
    st.session_state.tf_correct_count = 0
    st.session_state.tf_incorrect_count = 0
    st.session_state.tf_session_active = True
    st.session_state.tf_last_answer_submitted = False
    log_event("True/False session started")

# --- MAIN PAGE FLOW ---

render_page_header("True/False Rapid Fire", profile_manager)

# Action buttons
col1, col2 = st.columns([8, 2])
with col1:
    st.caption("Answer the following True/False questions to reinforce your knowledge.")
with col2:
    if st.button("End Session", key="tf_end_session"):
        st.session_state.tf_session_active = False
        log_event("True/False session ended")

st.write("")

# Content
if not st.session_state.tf_session_active:
    render_session_summary(
        module_name="true_false",
        profile_manager=profile_manager,
        correct_count=st.session_state.tf_correct_count,
        incorrect_count=st.session_state.tf_incorrect_count,
        xp_per_correct=5
    )
else:
    render_current_question(profile_manager)

# Footer
render_footer()