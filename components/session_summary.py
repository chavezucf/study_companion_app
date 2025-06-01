# /components/session_summary.py

import streamlit as st
from components.session_manager import reset_session, MODULE_SESSION_KEYS
from utils.ui_helpers import xp_progress_bar
from utils.logger import log_event

def render_session_summary(module_name: str, profile_manager, correct_count: int, incorrect_count: int, xp_per_correct: int):
    """
    Shared session summary component.
    """
    xp_progress_bar(st, profile_manager)
    st.header("Session Summary")

    st.write(f"Correct: {correct_count}")
    st.write(f"Incorrect: {incorrect_count}")
    total_questions = correct_count + incorrect_count
    st.write(f"Total Answered: {total_questions}")

    xp_earned = correct_count * xp_per_correct
    st.write(f"XP Earned: {xp_earned}")

    xp_flag_key = f"{module_name}_xp_added"
    if xp_flag_key not in st.session_state:
        profile_manager.add_xp(xp_earned)
        st.session_state[xp_flag_key] = True
        log_event(f"{module_name} XP added: {xp_earned}")

    st.write("")

    if st.button("Start New Session", key=f"{module_name}_start_new_session"):
        reset_session(MODULE_SESSION_KEYS[module_name])