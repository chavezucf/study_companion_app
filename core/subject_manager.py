# /core/subject_manager.py

import json
from collections import defaultdict
from utils.ui_helpers import render_footer
import streamlit as st
from components.subject_multi_selector import render_subject_multi_selector

class SubjectManager:
    def __init__(self, questions_file_path):
        self.questions_file_path = questions_file_path
        self.subjects_topics = self._extract_subjects_and_topics()

    def _extract_subjects_and_topics(self):
        with open(self.questions_file_path, "r") as f:
            questions = json.load(f)
        subjects_dict = defaultdict(set)
        for q in questions:
            subject = q.get("subject", "Unknown Subject")
            topic = q.get("topic", "Unknown Topic")
            subjects_dict[subject].add(topic)
        return {subject: sorted(topics) for subject, topics in subjects_dict.items()}

    def get_subjects(self):
        return list(self.subjects_topics.keys())

    def get_topics(self, subject):
        return self.subjects_topics.get(subject, [])

    @staticmethod
    def get_selected_subjects(questions, title="Select Subjects", key_prefix="subject"):
        subjects = sorted({q.get("subject", "Unknown Subject") for q in questions})
        if "selected_subjects" not in st.session_state:
            st.session_state.selected_subjects = set()
        if "subjects_confirmed" not in st.session_state:
            st.session_state.subjects_confirmed = False
        if not st.session_state["subjects_confirmed"]:
            st.title(title)
            selected_subjects = render_subject_multi_selector(subjects, key_prefix=key_prefix)
            if st.button("Continue", disabled=not selected_subjects, key=f"{key_prefix}_continue"):
                st.session_state.subjects_confirmed = True
                st.session_state.just_confirmed_subjects = True 
                st.session_state.selected_subjects = selected_subjects
                st.rerun()
            render_footer()
            st.stop()
        else:
            selected_subjects = st.session_state.selected_subjects
        return selected_subjects