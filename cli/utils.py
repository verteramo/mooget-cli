import json
import sys
import typer
import yaml
from pathlib import Path

from moodle import AttemptPage
from moodle.questions.question_type import QuestionType

from .options import (
    OutputFileOption,
    IndentOption,
)


def dump(data: dict, output: OutputFileOption, indent: IndentOption) -> None:
    match Path(output.name).suffix:
        case ".yml" | ".yaml":
            yaml.dump(data, output, indent=indent)
        case ".json" | _:
            json.dump(data, output, indent=indent)


def scrap(attempt_page: AttemptPage) -> dict[str, list]:

    questions = []
    attempt_name = attempt_page.name
    attempt_questions = list(attempt_page.questions)

    with typer.progressbar(attempt_questions, label=attempt_name) as progress:
        for question in progress:
            questions.append((question.text, list(question.answer)))

    return {attempt_name: questions}


def get_question_type(answers: list) -> str:
    if len(answers) == 1:
        if type(answers[0]) == str:
            return "text"

    else:
        true_answers = 0
        for _, value in answers:
            if value == True:
                true_answers += 1

        if true_answers == 1:
            return "singlechoice"
        elif true_answers > 1:
            return "multichoice"
