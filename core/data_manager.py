# Abstract data layer for reading/writing questions, snippets, and scenarios

import os
import json
import streamlit as st

class DataManager:
    """
    Abstracts data loading for different types and sources.
    Consumers use high-level methods and do not care about backend details.
    """
    @staticmethod
    def load_questions():
        return DataManager._load_json("data/questions.json")

    @staticmethod
    def load_scenarios():
        return DataManager._load_json("data/scenarios.json")

    @staticmethod
    def load_snippets():
        return DataManager._load_json("data/snippets.json")

    @staticmethod
    def load_profile():
        return DataManager._load_json("data/profile.json")

    @staticmethod
    def _load_json(file_path):
        if not os.path.exists(file_path):
            st.error(f"No {os.path.basename(file_path)} found! Please add data.")
            st.stop()
        with open(file_path, "r") as f:
            data = json.load(f)
        return data

    # Future: add _load_from_db, _load_from_api, etc.
