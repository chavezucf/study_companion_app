import streamlit as st
from core.profile_manager import ProfileManager
from utils.ui_helpers import render_page_header, back_to_main_menu, xp_progress_bar
from utils.logger import log_event

# Initialize profile
profile_manager = ProfileManager()

# Page header
render_page_header("🧩 Scenario Generator", profile_manager)

# TODO: Implement CLI Trainer logic here!
st.info("Scenario Generator - Module coming soon! 🚧")

# Example XP reward for visiting
profile_manager.add_xp(5)
log_event("Scenario Generator opened - +5 XP")

# XP Progress
xp_progress_bar(st, profile_manager)

# Back to main menu
back_to_main_menu()
