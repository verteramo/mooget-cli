import re
import base64
from typing import Iterable, Iterator
from urllib.request import urlopen

from navigation.element import Element
from .question_type import QuestionType
from moodle.constants import (
    CORRECT,
    INCORRECT,
    XPATH_BADGE,
    XPATH_GRADINGDETAILS,
    XPATH_IMAGES,
    XPATH_TEXT,
    XPATH_NUMBER,
    XPATH_GRADE,
    XPATH_GENERALFEEDBACK,
    XPATH_SPECIFICFEEDBACK,
    XPATH_NUMPARTSCORRECT,
    XPATH_RIGHTANSWER,
    REGEX_NUMERIC,
    REGEX_QUESTION_TEXT,
    REGEX_GRADE,
)


class Question:
    def __init__(self, element: Element):
        self.element = element

    @property
    def type(self) -> QuestionType | None:
        for type in QuestionType:
            if type.value in self.element.classes:
                return type

    @property
    def number(self) -> int:
        return int(self.element.elem(value=XPATH_NUMBER).first(REGEX_NUMERIC))

    @property
    def text(self) -> str:
        return self.element.elem(value=XPATH_TEXT).first(REGEX_QUESTION_TEXT).strip()

    @property
    def generalfeedback(self) -> str | None:
        return self.element.etext(value=XPATH_GENERALFEEDBACK)

    @property
    def specificfeedback(self) -> str | None:
        return self.element.etext(value=XPATH_SPECIFICFEEDBACK)

    @property
    def numpartscorrect(self) -> int | None:
        try:
            return int(
                self.element.elem(value=XPATH_NUMPARTSCORRECT).first(REGEX_NUMERIC)
            )
        except AttributeError:
            return None

    @property
    def rightanswer(self) -> str:
        return self.element.etext(value=XPATH_RIGHTANSWER)

    @property
    def images(self) -> Iterable[str]:
        for src in [image.src for image in self.element.elems(value=XPATH_IMAGES)]:
            if src:
                if src.startswith("data:image"):
                    yield src
                else:
                    yield base64.b64encode(urlopen(src).read()).decode()

    @property
    def correct(self) -> bool | None:
        if CORRECT in self.element.classes:
            return True

        if INCORRECT in self.element.classes:
            return False

        badge = self.element.elem(value=XPATH_BADGE)
        if badge:
            if CORRECT in badge.classes:
                return True

            if INCORRECT in badge.classes:
                return False

        try:
            grade, max_grade = self.element.elem(
                value=XPATH_GRADE,
            ).all(REGEX_GRADE)
            if grade == max_grade:
                return True
        except:
            pass

        try:
            grade, max_grade = self.element.elem(
                value=XPATH_GRADINGDETAILS,
            ).all(REGEX_GRADE)
            if grade == max_grade:
                return True
        except:
            pass

        return None

    def in_rightanswer(self, text: str) -> bool:
        return bool(re.search(rf"\b{text}[\,\b]?", self.rightanswer))

    @property
    def answer(self) -> Iterator:
        pass
