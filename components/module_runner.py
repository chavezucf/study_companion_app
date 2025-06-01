# /components/module_runner.py

import streamlit as st
import random
from components.session_manager import reset_session, MODULE_SESSION_KEYS
from components.session_summary import render_session_summary
from core.subject_manager import SubjectManager
from utils.logger import log_event
from utils.ui_helpers import render_page_header, render_footer
from utils.ui_helpers import set_page_config
from core.profile_manager import ProfileManager
import json, os

def run_module_with_subject_selector(
    module_name: str,
    questions_path: str,
    render_question_func,
    page_icon: str = "🎓",
    page_title: str = None
):
    def initialize_session_state(prefix, shuffle_key, questions):
        """Initialize or reset all relevant session state keys."""
        st.session_state[shuffle_key] = questions
        st.session_state[f"{prefix}_question_index"] = 0
        st.session_state[f"{prefix}_correct_count"] = 0
        st.session_state[f"{prefix}_incorrect_count"] = 0
        st.session_state[f"{prefix}_session_active"] = True
        st.session_state[f"{prefix}_last_answer_submitted"] = False

    log_event(f"Running {module_name} module with subject selector")
    set_page_config(page_title=page_title or module_name, page_icon=page_icon)
    profile_manager = ProfileManager()

    # --- LOAD QUESTIONS ---
    if not os.path.exists(questions_path):
        st.error(f"No questions file found at {questions_path}!")
        st.stop()
    with open(questions_path, "r") as f:
        questions = json.load(f)

    # --- SUBJECT SELECTION ---
    subject_manager = SubjectManager(questions_path)
    selected_subjects = subject_manager.get_selected_subjects(
        title=f"Select subjects for {page_title}",
        key_prefix=f"{module_name}_subject",
        questions=questions
    )
    questions = [q for q in questions if q.get("subject") in selected_subjects] if selected_subjects else questions

    # --- SESSION INIT & SHUFFLE ---
    session_prefix = module_name
    shuffle_key = f"{session_prefix}_questions_shuffled"
    reinit_needed = (
        "subjects_confirmed" in st.session_state and
        st.session_state.get("just_confirmed_subjects")
    )
    if reinit_needed:
        st.session_state.pop("just_confirmed_subjects", None)
        log_event("Reinitializing session after new subject selection...")
        st.session_state.pop(shuffle_key, None)
        initialize_session_state(session_prefix, shuffle_key, questions)
    elif shuffle_key not in st.session_state:
        log_event("Shuffling questions...")
        random.shuffle(questions)
        initialize_session_state(session_prefix, shuffle_key, questions)

    # --- MAIN PAGE FLOW ---
    render_page_header(page_title, profile_manager)
    col1, col2 = st.columns([8, 2])
    with col1:
        st.caption(f"Practice your {page_title} skills.")
    with col2:
        if st.button("End Session", key=f"{module_name}_end_session"):
            st.session_state[f"{session_prefix}_session_active"] = False
            log_event(f"{module_name} session ended")
    st.write("")

    # --- MAIN CONTENT ---
    if not st.session_state[f"{session_prefix}_session_active"]:
        render_session_summary(
            module_name=module_name,
            page_title=page_title,
            profile_manager=profile_manager,
            correct_count=st.session_state[f"{session_prefix}_correct_count"],
            incorrect_count=st.session_state[f"{session_prefix}_incorrect_count"],
            xp_per_correct=MODULE_SESSION_KEYS[module_name]["xp_per_correct"]
        )
    else:
        st.session_state.current_questions = st.session_state[shuffle_key]
        render_question_func(profile_manager)

    render_footer()