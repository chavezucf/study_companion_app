# /components/subject_selector.py

import streamlit as st

from core.subject_manager import SubjectManager
import streamlit as st

def render_subject_selector(subject_manager: SubjectManager, allow_override=False):
    """
    Renders subject/topic selectors using SubjectManager for persistence.
    Updates the user's profile with the selected subject/topic.
    """
    subjects = sorted(subject_manager.get_subjects())
    current_subject, current_topic = subject_manager.get_selection()
    selected_subject = st.selectbox(
        "Select Subject:",
        subjects,
        index=subjects.index(current_subject) if current_subject in subjects else 0
    )
    topics = subject_manager.get_topics(selected_subject)
    selected_topic = st.selectbox(
        "Select Topic:",
        topics,
        index=topics.index(current_topic) if current_topic in topics else 0
    )
    # Only update selection if not in override mode
    if not allow_override:
        subject_manager.set_selection(selected_subject, selected_topic)
    return selected_subject, selected_topic