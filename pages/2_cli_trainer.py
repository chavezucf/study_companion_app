# pages/2_cli_trainer.py

from components.module_runner import run_module_with_subject_selector
from components.cli_trainer_question_block import render_cli_trainer_question

run_module_with_subject_selector(
    module_name="cli_trainer",
    questions_path="data/cli_questions.json",
    render_question_func=render_cli_trainer_question,
    page_icon="💻",
    page_title="AZ-204 CLI Trainer"
)