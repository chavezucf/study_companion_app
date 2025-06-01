# /components/subject_selector_runner.py

import streamlit as st
from core.subject_manager import SubjectManager
from components.subject_multi_selector import render_subject_multi_selector

def get_selected_subjects(questions_file_path: str, key_prefix: str = "subject") -> list[str]:
    """
    Handles full subject selection flow.
    Returns the list of selected subjects.
    """
    # Initialize SubjectManager
    subject_manager = SubjectManager(questions_file_path)
    subjects = sorted(subject_manager.get_subjects())

    # If no subjects confirmed yet  show selector
    if "subjects_confirmed" not in st.session_state or not st.session_state["subjects_confirmed"]:
        selected_subjects = render_subject_multi_selector(subjects, key_prefix=key_prefix)
        
        if st.button("Continue", disabled=not selected_subjects):
            st.session_state.subjects_confirmed = True
            st.session_state.selected_subjects = selected_subjects
            st.rerun()
        
        st.stop()  # Prevent rest of page from running until confirmed

    else:
        selected_subjects = st.session_state.selected_subjects

    return selected_subjects
