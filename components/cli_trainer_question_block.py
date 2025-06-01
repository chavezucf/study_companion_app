# components/cli_trainer_question_block.py

import streamlit as st
from utils.logger import log_event

def render_cli_trainer_question(profile_manager):
    current_index = st.session_state.cli_trainer_question_index
    questions = st.session_state.cli_trainer_questions_shuffled

    if current_index >= len(questions):
        st.success("You've answered all available questions! Ending session.")
        st.session_state.cli_trainer_session_active = False
        log_event("CLI Trainer auto-ended after last question.")
        return

    current_question = questions[current_index]

    st.subheader(f"Question {current_index + 1}")
    st.markdown(f"**{current_question['question']}**")
    st.markdown(f"*Subject:* {current_question['subject']}")

    st.write("")

    if not st.session_state.cli_trainer_last_answer_submitted:
        # Detect question type
        q_type = current_question["question_type"]

        if q_type == "full_command":
            user_input = st.text_area("Enter full command:", height=120)
            if st.button("Next Question"):
                check_full_command(user_input, current_question, profile_manager)

        elif q_type == "fill_blank":
            st.code(current_question["command_template"], language="bash")
            blanks = current_question["blanks"]
            user_answers = {}
            for blank in blanks:
                user_answers[blank] = st.text_input(f"{blank}")
            if st.button("Next Question"):
                check_fill_blank(user_answers, current_question, profile_manager)

        elif q_type == "mcq":
            choice = st.radio("Choose the correct command:", current_question["choices"])
            if st.button("Next Question"):
                check_mcq(choice, current_question, profile_manager)

    else:
        # Next Question button
        if st.button("Go To Next Question"):
            st.session_state.cli_trainer_question_index += 1
            st.session_state.cli_trainer_last_answer_submitted = False
            st.rerun()

# === CHECK FUNCTIONS ===

def check_full_command(user_input, question, profile_manager):
    correct_answer = question["answer"]

    if user_input.strip() == correct_answer.strip():
        st.success("Correct!")
        st.code(correct_answer, language="bash")
        st.session_state.cli_trainer_correct_count += 1
        log_event(f"Correct full_command answer.")
        profile_manager.update_topic_performance(question["subject"], correct=True)
    else:
        st.error("Incorrect.")
        st.code(correct_answer, language="bash")
        st.info(f"Explanation: {question['explanation']}")
        st.session_state.cli_trainer_incorrect_count += 1
        log_event(f"Incorrect full_command answer.")
        profile_manager.update_topic_performance(question["subject"], correct=False)

    st.session_state.cli_trainer_last_answer_submitted = True

def check_fill_blank(user_answers, question, profile_manager):
    correct = True
    for key, correct_value in question["answer"].items():
        if user_answers[key].strip() != correct_value.strip():
            correct = False

    if correct:
        st.success("Correct!")
        st.code(question["command_template"].format(**question["answer"]), language="bash")
        st.session_state.cli_trainer_correct_count += 1
        log_event(f"Correct fill_blank answer.")
        profile_manager.update_topic_performance(question["subject"], correct=True)
    else:
        st.error("Incorrect.")
        st.code(question["command_template"].format(**question["answer"]), language="bash")
        st.info(f"Explanation: {question['explanation']}")
        st.session_state.cli_trainer_incorrect_count += 1
        log_event(f"Incorrect fill_blank answer.")
        profile_manager.update_topic_performance(question["subject"], correct=False)

    st.session_state.cli_trainer_last_answer_submitted = True

def check_mcq(choice, question, profile_manager):
    correct_answer = question["answer"]

    if choice == correct_answer:
        st.success("Correct!")
        st.code(correct_answer, language="bash")
        st.session_state.cli_trainer_correct_count += 1
        log_event(f"Correct mcq answer.")
        profile_manager.update_topic_performance(question["subject"], correct=True)
    else:
        st.error("Incorrect.")
        st.code(correct_answer, language="bash")
        st.info(f"Explanation: {question['explanation']}")
        st.session_state.cli_trainer_incorrect_count += 1
        log_event(f"Incorrect mcq answer.")
        profile_manager.update_topic_performance(question["subject"], correct=False)

    st.session_state.cli_trainer_last_answer_submitted = True
