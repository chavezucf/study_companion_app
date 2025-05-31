# AZ-204 Study Companion App

**Purpose:**  
A personal app to help study for the **AZ-204: Developing Solutions for Microsoft Azure** exam.

This is not meant to be a public tool — it’s designed for my personal use, to help me study interactively, reinforce key concepts, and gamify my preparation.

---

## ✨ Features

- **Main Menu:** Launch individual modules from a GUI.
- **User Profile:** XP and level progression, saved across sessions.
- **Study Adventure:** Freeform XP tracker — earn XP for any activity.
- **Scenario Generator:** Practice solving architecture and service selection scenarios.
- **CLI Trainer:** Practice Azure CLI and Bicep commands (multiple formats).
- **True/False Rapid Fire:** Answer rapid true/false questions with explanations.
- **Code Snippet Organizer:** Browse, review, and tag useful code snippets.

---

## 🏗️ Design Principles

- **Single app with modular architecture** — each module is a separate component.
- **GUI-first** — interactive and visual from the start (using PySimpleGUI or Streamlit).
- **Abstracted data layers** — data source (files or API) can easily be swapped in the future.
- **Profile abstraction** — for now, a single `profile.json`; later can be multi-user.
- **AI-ready** — data will be generated or imported from AI and structured in JSON or SQLite.

---

## 🚀 Planned Tech Stack

- **Language:** Python 3.x
- **GUI:** PySimpleGUI or Streamlit (easy cross-platform, rapid development)
- **Persistence:** JSON and/or SQLite
- **Third-party libraries:**  
    - `PySimpleGUI` or `Streamlit` (GUI)  
    - `Rich` (optional, for CLI formatting if needed)  
    - `tinydb` or `sqlite3` (persistence layer, if used)  
    - `pydantic` (optional, data validation for future extensibility)

---

## 📁 Project Structure

```plaintext
/
├── README.md
├── main.py                # Entry point - Main menu GUI
├── requirements.txt       # Required Python packages
├── data/
│   ├── profile.json       # User profile (XP, level, progress)
│   ├── questions.json     # True/False questions
│   ├── scenarios.json     # Scenario templates and data
│   ├── snippets.json      # Code snippets (CLI, C#, Python, Bicep)
├── modules/               # Each module = 1 file/class
│   ├── study_adventure.py
│   ├── scenario_generator.py
│   ├── cli_trainer.py
│   ├── true_false.py
│   ├── snippet_organizer.py
├── core/                  # Shared logic
│   ├── profile_manager.py # Abstract profile layer
│   ├── data_manager.py    # Abstract data layer for reading/writing questions/snippets/scenarios
│   ├── xp_system.py       # XP and level logic
├── utils/                 # Optional: helpers
│   ├── logger.py
│   ├── ui_helpers.py
└── tests/                 # Future test scripts
    ├── test_profile.py
    ├── test_data_manager.py
