# pages/2_cli_trainer.py

import streamlit as st
import json
import random
import os
from utils.logger import log_event
from core.profile_manager import ProfileManager
from utils.ui_helpers import (
    xp_progress_bar,
    render_page_header,
    render_footer,
    hide_sidebar,
)

from components.cli_question_block import render_cli_question
from components.cli_session_summary import render_cli_session_summary

QUESTIONS_PATH = "data/cli_questions.json"

# Page config
st.set_page_config(page_title="AZ-204 CLI Trainer", page_icon="💻", layout="centered")
hide_sidebar()

# Initialize profile
profile_manager = ProfileManager()

# Load questions
if not os.path.exists(QUESTIONS_PATH):
    st.error("No cli_questions.json found! Please add questions.")
    st.stop()

with open(QUESTIONS_PATH, "r") as f:
    questions = json.load(f)

# Initialize session state
if "cli_questions_shuffled" not in st.session_state:
    random.shuffle(questions)
    st.session_state.cli_questions_shuffled = questions
    st.session_state.cli_question_index = 0
    st.session_state.cli_correct_count = 0
    st.session_state.cli_incorrect_count = 0
    st.session_state.cli_session_active = True
    st.session_state.cli_last_answer_submitted_label = False
    st.session_state.cli_last_answer_submitted = False
    log_event("CLI Trainer session started")

# --- MAIN PAGE FLOW ---

render_page_header("CLI Trainer", profile_manager)

# Action buttons
col1, col2 = st.columns([8, 2])
with col1:
    st.caption("Practice Azure CLI and Bicep CLI commands.")
with col2:
    if st.button("End Session"):
        st.session_state.cli_session_active = False
        log_event("CLI Trainer session ended")

st.write("")

# Content
if not st.session_state.cli_session_active:
    render_cli_session_summary(profile_manager)
else:
    render_cli_question(profile_manager)

# Footer
render_footer()
