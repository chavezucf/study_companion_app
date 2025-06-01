# /components/tf_question_block.py

import streamlit as st
from utils.logger import log_event

def render_current_question(profile_manager):
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
            if st.button("True", key="tf_answer_true"):
                process_answer(True, current_question, profile_manager)
        with col2:
            if st.button("False", key="tf_answer_false"):
                process_answer(False, current_question, profile_manager)
    else:
        # Show Next Question button
        if st.button("Next Question", key="tf_next_question"):
            st.session_state.tf_question_index += 1
            st.session_state.tf_last_answer_submitted = False
            st.rerun()

# === PROCESS ANSWER ===

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
    st.session_state.tf_last_answer_submitted = True