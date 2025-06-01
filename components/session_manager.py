# /components/session_manager.py

import streamlit as st

# Central known keys per module
MODULE_SESSION_KEYS = {
    "cli_trainer": {
        "keys": [
            "cli_questions_shuffled",
            "cli_question_index",
            "cli_correct_count",
            "cli_incorrect_count",
            "cli_session_active",
            "cli_last_answer_submitted_label",
            "cli_last_answer_submitted",
            "subjects_confirmed",
            "selected_subjects",
        ],
        "xp_per_correct": 10
    },
    "true_false": {
        "keys": [
            "tf_questions_shuffled",
            "tf_question_index",
            "tf_correct_count",
            "tf_incorrect_count",
            "tf_session_active",
            "tf_last_answer_submitted",
            "tf_xp_added",
            "subjects_confirmed",
            "selected_subjects",
        ],
        "xp_per_correct": 5
    }
}

def reset_session(keys: list[str]):
    """
    Resets the given list of keys in st.session_state and triggers rerun.
    """
    for key in keys:
        st.session_state.pop(key, None)
    st.rerun()