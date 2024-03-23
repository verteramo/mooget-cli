from enum import StrEnum
import json
from typing import Iterable

import jsonpickle
from moodle.questions.multichoice_question import MultichoiceQuestion

from nav.page import Page
from moodle.constants import (
    XPATH_ATTEMPT_NAME,
    XPATH_ATTEMPT_QUESTIONS,
    XPATH_GRADE_ITEMS,
    XPATH_ROW_LINKS,
)
from .questions.question import Question, QuestionType
from .questions.multianswer_question import MultianswerQuestion
from .questions.shortanswer_question import ShortanswerQuestion
from .questions.match_question import MatchQuestion


class ReportType(StrEnum):
    Assignment = "assign"
    Database = "data"
    Forum = "forum"
    Glossary = "glossary"
    H5PActivity = "h5pactivity"
    Lesson = "lesson"
    Quiz = "quiz"
    ScormPackage = "scorm"
    Workshop = "workshop"


class OverviewPage(Page):
    def __iter__(self) -> Iterable[tuple[str, str]]:
        yield from [
            (element.text, element.href)
            for element in self.elems(value=XPATH_ROW_LINKS)
        ]


class ReportPage(Page):
    def __iter__(self) -> Iterable[tuple[str, ReportType]]:
        yield from [
            (
                [type for type in ReportType if type.value in element.href].pop(),
                element.href,
            )
            for element in self.elems(value=XPATH_GRADE_ITEMS)
        ]


class QuizPage(Page):
    def __iter__(self) -> Iterable[str]:
        yield from [element.href for element in self.elems(value=XPATH_ROW_LINKS)]


class AttemptPage(Page):
    @property
    def name(self) -> str:
        return self.elem(value=XPATH_ATTEMPT_NAME).text

    @property
    def questions(self) -> Iterable[Question]:
        for element in self.elems(value=XPATH_ATTEMPT_QUESTIONS):
            match [
                type for type in QuestionType if type.value in element.classes
            ].pop():
                case (
                    QuestionType.TrueFalse
                    | QuestionType.Multichoice
                    | QuestionType.CalculatedMulti
                ):
                    yield MultichoiceQuestion(element)
                case QuestionType.Multianswer:
                    yield MultianswerQuestion(element)
                case (
                    QuestionType.Shortanswer
                    | QuestionType.Numerical
                    | QuestionType.Calculated
                    | QuestionType.CalculatedSimple
                ):
                    yield ShortanswerQuestion(element)
                case QuestionType.Match | QuestionType.RandomShortanswerMatch:
                    yield MatchQuestion(element)
                # case QuestionType.DragAndDropWordToString:
                #     yield DragAndDropWordToStringQuestion(element)
