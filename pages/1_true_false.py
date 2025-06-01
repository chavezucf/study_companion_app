from components.module_runner import run_module_with_subject_selector
from components.true_false_question_block import render_true_false_question

run_module_with_subject_selector(
    module_name="true_false",
    questions_path="data/questions.json",
    render_question_func=render_true_false_question,
    page_icon="✅",
    page_title="True/False Rapid Fire"
)