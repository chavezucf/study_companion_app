# utils/ui_helpers.py

import streamlit as st
from core.xp_system import LEVEL_THRESHOLDS

def hide_sidebar():
    print("Hiding sidebar")
    # st.markdown("""
    # <style>
    #     [data-testid="stSidebarNav"] { display: none; }
    #     [data-testid="stSidebar"] { display: none; }
    #     [data-testid="stSidebarCollapsedControl"] { display: none; }
    # </style>
    # """, unsafe_allow_html=True)

def back_to_main_menu():
    st.page_link("main.py", label="Back to Main Menu")

def render_page_header(title, profile_manager):
    st.title(title)
    st.write(f"Player: **{profile_manager.get_username()}** | Level: **{profile_manager.get_level()}** | XP: **{profile_manager.get_xp()}**")

def xp_progress_bar(st_module, profile_manager):
    current_xp = profile_manager.get_xp()
    current_level = profile_manager.get_level()
    next_level_threshold = LEVEL_THRESHOLDS[current_level - 1] if current_level - 1 < len(LEVEL_THRESHOLDS) else current_xp + 500

    xp_in_level = current_xp if current_level == 1 else current_xp - LEVEL_THRESHOLDS[current_level - 2] if current_level > 1 else 0
    xp_needed = next_level_threshold - (LEVEL_THRESHOLDS[current_level - 2] if current_level > 1 else 0)

    st_module.progress(min(xp_in_level / xp_needed, 1.0), text=f"Progress to next level: {xp_in_level}/{xp_needed} XP")

def render_footer(show_back_button=True):
    st.write("")
    st.write("---")
    col1, col2 = st.columns([1, 1])
    with col1:  
        if show_back_button:
            back_to_main_menu()
    with col2:
        st.caption("AZ-204 Study Companion v0.1 🚀 | Built by Miguel")
