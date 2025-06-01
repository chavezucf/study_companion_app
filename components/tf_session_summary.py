from components.session_summary import render_session_summary

if not st.session_state.tf_session_active:
    render_session_summary(
        module_name="true_false",
        profile_manager=profile_manager,
        correct_count=st.session_state.tf_correct_count,
        incorrect_count=st.session_state.tf_incorrect_count,
        xp_per_correct=5
    )