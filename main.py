import PySimpleGUI as sg
from core.profile_manager import ProfileManager

# Initialize profile
profile_manager = ProfileManager()

# Layout for main menu
layout = [
    [sg.Text(f"Welcome, {profile_manager.get_username()}!", font=("Helvetica", 16))],
    [sg.Text(f"Level: {profile_manager.get_level()}    XP: {profile_manager.get_xp()}")],
    [sg.Button("1️⃣  Study Adventure")],
    [sg.Button("2️⃣  Scenario Generator")],
    [sg.Button("3️⃣  CLI Trainer")],
    [sg.Button("4️⃣  True/False Rapid Fire")],
    [sg.Button("5️⃣  Code Snippet Organizer")],
    [sg.Button("Exit")]
]

# Create window
window = sg.Window("AZ-204 Study Companion", layout)

# Main event loop
while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == "Exit":
        break
    elif event == "1️⃣  Study Adventure":
        sg.popup("Study Adventure - coming soon!")
        profile_manager.add_xp(10)  # Example: +10 XP for opening
    elif event == "2️⃣  Scenario Generator":
        sg.popup("Scenario Generator - coming soon!")
        profile_manager.add_xp(10)
    elif event == "3️⃣  CLI Trainer":
        sg.popup("CLI Trainer - coming soon!")
        profile_manager.add_xp(10)
    elif event == "4️⃣  True/False Rapid Fire":
        sg.popup("True/False - coming soon!")
        profile_manager.add_xp(10)
    elif event == "5️⃣  Code Snippet Organizer":
        sg.popup("Code Snippet Organizer - coming soon!")
        profile_manager.add_xp(10)

    # Update displayed XP/Level
    window["Level: " + str(profile_manager.get_level()) + "    XP: " + str(profile_manager.get_xp())].update(
        f"Level: {profile_manager.get_level()}    XP: {profile_manager.get_xp()}"
    )

# Close window
window.close()
