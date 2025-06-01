# Bugs & Improvements

---

## 🚩 Bugs

---

### 1️⃣ Double-click required to advance questions  
**Behavior:**  
- In True/False, after answering a question, "Next Question" sometimes requires two clicks.  
**Hypothesis:**  
- Possible Streamlit rerun / state timing issue.  
**Plan:**  
- Revisit at **end of v1.2**. Track root cause.

---

### 2️⃣ XP Progress Bar does not refresh immediately on new session  
**Behavior:**  
- XP bar sometimes appears stale after "Start New Session". XP itself is updated correctly.  
**Hypothesis:**  
- Rerun flow — possible state timing vs XP calculation.  
**Plan:**  
- Investigate in v1.2 polish phase.

---

## 🚀 Global Improvements

---

### ✅ Add `ModuleRunner`  
**Purpose:**  
- Standardize module page flow  
- DRY out subject selection + session init + rendering  
**Plan:**  
- Component `/components/module_runner.py`

---

### ✅ Add `xp_per_correct` to `MODULE_SESSION_KEYS`  
**Purpose:**  
- DRY out XP calculation in session summary

---

### ✅ Implement Profile Loader  
**Purpose:**  
- Support multi-user  
- Prompt for username → auto-load or create profile file  
**Behavior:**  
- Until logout, user profile is active  
- Profile files → `profile_{username}.json`

---

### ✅ Remove Top Nav  
**Goal:**  
- Fully clean Streamlit page — no extra nav or deploy button

---

### ✅ Add `logout` flow  
**Behavior:**  
- Clears st.session_state[“current_user”]  
- Returns to "Login" screen

---

## 🚀 Module Improvements

---

### True/False

✅ Move to **ModuleRunner**  
✅ Refactor to match CLI Trainer  
✅ Use shared `render_session_summary()`  
✅ Keep separate `tf_question_block.py`

---

### CLI Trainer

✅ Already following target pattern  
✅ Migrate to **ModuleRunner**  
✅ Use shared `render_session_summary()`  
✅ Keep separate `cli_question_block.py`

---

### Scenario Generator (v1.3)

✅ Build from start using **ModuleRunner**  
✅ Decide if it uses subject selection or not (likely yes)  
✅ Add `scenario_question_block.py`

---

### Snippet Organizer (v1.3)

✅ Build from start using **ModuleRunner**  
✅ May or may not use subject selection  
✅ If no subject selection → ModuleRunner should handle optional subject selection

---

### Study Adventure (v1.3+)

✅ Build from start using **ModuleRunner**  
✅ Will likely require separate adventure_question_block.py

---

## 🚀 Future Ideas

---

- Add "Practice Mode" vs "Test Mode" toggle  
- Use `streamlit-code-editor` for CLI Trainer Full Command  
- Add **Dashboard Page** showing XP progress, module stats  
- Add **Leaderboard** (even if local only)  
- Add ability to "favorite" questions for later review  
- Add "Daily Practice" reminders / streaks  
- UX polish: Icons in subject cards  
- Support per-module settings in profile  

---

# ✅ v1.2 Release Checklist

✅ CLI Trainer using ModuleRunner  
✅ True/False using ModuleRunner  
✅ Profile Loader working  
✅ Bugs confirmed and tracked  
✅ Top Nav removed  
✅ XP per correct in session keys  
✅ Final structure DRY and consistent  
✅ Bugs & Improvements up to date  
✅ Ready for tag: **v1.2**

---

# END