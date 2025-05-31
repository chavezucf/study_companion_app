import streamlit as st
import random
from utils.logger import log_event
from core.data_manager import DataManager
from core.profile_manager import ProfileManager
from utils.ui_helpers import (
    xp_progress_bar,
    render_page_header,
    render_footer,
    hide_sidebar,
)

# Page config
st.set_page_config(page_title="AZ-204 Study Companion", page_icon="📚", layout="centered")
hide_sidebar()

# Initialize profile
profile_manager = ProfileManager()
questions = DataManager.load_questions()

# Initialize session state
if "tf_questions_shuffled" not in st.session_state:
    random.shuffle(questions)
    st.session_state.tf_questions_shuffled = questions
    st.session_state.tf_question_index = 0
    st.session_state.tf_correct_count = 0
    st.session_state.tf_incorrect_count = 0
    st.session_state.tf_session_active = True
    st.session_state.tf_last_answer_submitted = False
    log_event("True/False session started")

# Define process_answer
def process_answer(user_answer, question, profile_manager):
    log_event(f"User Answer: {user_answer}")
    correct_answer = question["answer"]
    topic = question["topic"]

    if user_answer == correct_answer:
        st.success("Correct!")
        st.info(f"Explanation: {question['explanation']}")
        st.session_state.tf_correct_count += 1
        log_event(f"Correct answer for topic '{topic}'")
        profile_manager.update_topic_performance(topic, correct=True)
    else:
        st.error("Incorrect.")
        st.info(f"Explanation: {question['explanation']}")
        st.session_state.tf_incorrect_count += 1
        log_event(f"Incorrect answer for topic '{topic}'")
        profile_manager.update_topic_performance(topic, correct=False)

    # Mark that answer was submitted → need to show Next button
    log_event("Answer submitted")
    log_event(f"State before: {st.session_state.tf_last_answer_submitted}")
    st.session_state.tf_last_answer_submitted = True
    log_event(f"State after: {st.session_state.tf_last_answer_submitted}")

# COMPONENT: End session summary
def render_session_summary():
    xp_progress_bar(st, profile_manager)
    st.header("Session Summary")
    st.write(f"Correct: {st.session_state.tf_correct_count}")
    st.write(f"Incorrect: {st.session_state.tf_incorrect_count}")
    total_questions = st.session_state.tf_correct_count + st.session_state.tf_incorrect_count
    st.write(f"Total Answered: {total_questions}")
    xp_earned = st.session_state.tf_correct_count * 5
    st.write(f"XP Earned: {xp_earned}")

    if "tf_xp_added" not in st.session_state:
        profile_manager.add_xp(xp_earned)
        st.session_state.tf_xp_added = True
        log_event(f"True/False XP added: {xp_earned}")

    st.write("")

    if st.button("Start New Session"):
        for key in [
            "tf_questions_shuffled",
            "tf_question_index",
            "tf_correct_count",
            "tf_incorrect_count",
            "tf_session_active",
            "tf_xp_added",
            "tf_last_answer_submitted",
        ]:
            st.session_state.pop(key, None)

        st.rerun()

# COMPONENT: Question block
def render_current_question():
    current_index = st.session_state.tf_question_index
    questions = st.session_state.tf_questions_shuffled

    if current_index >= len(questions):
        st.success("You've answered all available questions! Ending session.")
        st.session_state.tf_session_active = False
        log_event("True/False session auto-ended after last question.")
        return

    current_question = questions[current_index]

    st.subheader(f"Question {current_index + 1}")
    st.markdown(f"**{current_question['question']}**")
    st.markdown(f"*Subject:* {current_question['subject']}  \n*Topic:* {current_question['topic']}")

    st.write("")

    if not st.session_state.tf_last_answer_submitted:
        # Show True/False buttons
        col1, col2 = st.columns(2)
        with col1:
            if st.button("True"):
                process_answer(True, current_question, profile_manager)
        with col2:
            if st.button("False"):
                process_answer(False, current_question, profile_manager)
    else:
        # Show Next Question button
        if st.button("Next Question"):
            st.session_state.tf_question_index += 1
            st.session_state.tf_last_answer_submitted = False
            st.rerun()

# --- MAIN PAGE FLOW ---

render_page_header("True/False Rapid Fire", profile_manager)

# Action buttons
col1, col2 = st.columns([8, 2])
with col1:
    st.caption("Answer the following True/False questions to reinforce your knowledge.")
with col2:
    if st.button("End Session"):
        st.session_state.tf_session_active = False
        log_event("True/False session ended")

st.write("")

# Content
if not st.session_state.tf_session_active:
    render_session_summary()
else:
    render_current_question()

# Footer
render_footer()
