# /components/subject_multi_selector.py

import streamlit as st
from typing import List

def render_subject_multi_selector(subjects: List[str], key_prefix: str = "subject") -> List[str]:
    """
    Card-style multi-select for subjects using st.toggle (stateful).
    Returns the list of selected subjects.
    """
    if "selected_subjects" not in st.session_state:
        st.session_state.selected_subjects = set()

    # --- TOGGLE ALL ---
    toggle_all = st.toggle(
        "Select All",
        key=f"{key_prefix}_toggle_all",
        value=len(st.session_state.selected_subjects) == len(subjects)
    )

    if toggle_all:
        st.session_state.selected_subjects = set(subjects)
    else:
        st.session_state.selected_subjects = set()

    # --- Subject Toggles ---
    cols = st.columns(3)

    for i, subject in enumerate(subjects):
        col = cols[i % 3]

        with col:
            toggle_value = st.toggle(
                subject,
                key=f"{key_prefix}_{i}_{subject}_toggle",
                value=subject in st.session_state.selected_subjects
            )

            if toggle_value:
                st.session_state.selected_subjects.add(subject)
            else:
                st.session_state.selected_subjects.discard(subject)

    return list(st.session_state.selected_subjects)