import streamlit as st
from core.profile_manager import ProfileManager
from utils.ui_helpers import (
    hide_sidebar,
    render_page_header,
    xp_progress_bar,
    render_footer,
)
from utils.logger import log_event

# Page config
st.set_page_config(page_title="AZ-204 Study Companion", page_icon="📚", layout="centered")

# Hide sidebar
hide_sidebar()

# Initialize profile
profile_manager = ProfileManager()

# Page header
render_page_header("AZ-204 Study Companion", profile_manager)

# XP Progress
xp_progress_bar(st, profile_manager)

# Module Links
st.header("📚 Study Modules")

st.page_link("pages/1_true_false.py", label="✅ True/False Rapid Fire")
st.page_link("pages/2_cli_trainer.py", label="🖥️ CLI Trainer")
st.page_link("pages/3_scenario_generator.py", label="🧩 Scenario Generator")
st.page_link("pages/4_snippet_organizer.py", label="💻 Code Snippet Organizer")
st.page_link("pages/5_study_adventure.py", label="🎮 Study Adventure")

# XP Progress again (optional, refresh)
st.write("---")
st.write(f"**Updated Level:** {profile_manager.get_level()} | **XP:** {profile_manager.get_xp()}")
xp_progress_bar(st, profile_manager)

# Footer
render_footer(show_back_button=False)
