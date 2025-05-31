# components/cli_session_summary.py

import streamlit as st
from utils.logger import log_event
from utils.ui_helpers import xp_progress_bar

def render_cli_session_summary(profile_manager):
    xp_progress_bar(st, profile_manager)
    st.header("Session Summary")

    st.write(f"Correct: {st.session_state.cli_correct_count}")
    st.write(f"Incorrect: {st.session_state.cli_incorrect_count}")
    total_questions = st.session_state.cli_correct_count + st.session_state.cli_incorrect_count
    st.write(f"Total Answered: {total_questions}")

    xp_earned = st.session_state.cli_correct_count * 10
    st.write(f"XP Earned: {xp_earned}")

    if "cli_xp_added" not in st.session_state:
        profile_manager.add_xp(xp_earned)
        st.session_state.cli_xp_added = True
        log_event(f"CLI Trainer XP added: {xp_earned}")

    st.write("")

    if st.button("Start New Session"):
        for key in [
            "cli_questions_shuffled",
            "cli_question_index",
            "cli_correct_count",
            "cli_incorrect_count",
            "cli_session_active",
            "cli_last_answer_submitted",
            "cli_xp_added",
        ]:
            st.session_state.pop(key, None)

        st.rerun()
