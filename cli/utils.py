import typer
import yaml
import jsonpickle
from pathlib import Path

from moodle import AttemptPage

from .options import (
    OutputFileOption,
    IndentOption,
)


def dump_output(data: dict, output: OutputFileOption, indent: IndentOption) -> None:
    match Path(output.name).suffix:
        case ".yml" | ".yaml":
            yaml.dump(data, output, indent=indent)
        case ".json" | _:
            print(jsonpickle.encode(data, indent=indent, unpicklable=False), file=output)


def scrap(attempt_page: AttemptPage) -> dict[str, list]:
    questions = []
    attempt_questions = list(attempt_page.questions)
    with typer.progressbar(
        attempt_questions,
        label=f"Scraping {len(attempt_questions)} questions from '{attempt_page.name}'",
    ) as progress:
        for question in progress:
            questions.append(
                {
                    "type": question.type,
                    "text": question.text,
                    "images": list(question.images),
                    "answer": list(question.answer),
                }
            )

    return {attempt_page.name: questions}
