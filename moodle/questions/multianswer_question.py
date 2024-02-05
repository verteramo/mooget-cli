import re
from typing import Iterable
from lxml import etree
from moodle.constants import (
    ATTR_DATA_CONTENT,
    EMPTY_STRING,
    NEW_LINE,
    REGEX_GRADE,
    TRUE,
    XPATH_FEEBACKTRIGGER,
    XPATH_MULTIANSWER_OPTIONS,
    XPATH_FORMULATION_PARAGRAPHS,
)
from .question import Question


class MultianswerQuestion(Question):

    @property
    def feedbacktrigger(self) -> str | None:
        return getattr(
            self.element.elem(value=XPATH_FEEBACKTRIGGER), ATTR_DATA_CONTENT, None
        )

    @property
    def text(self) -> str:
        return NEW_LINE.join(
            [
                element.text.replace(
                    EMPTY_STRING.join([child.text for child in element.childs]),
                    EMPTY_STRING,
                ).strip()
                for element in self.element.elems(value=XPATH_FORMULATION_PARAGRAPHS)
            ]
        ).strip()

    @property
    def rightanswer(self) -> str:
        return EMPTY_STRING.join(etree.fromstring(self.feedbacktrigger).itertext())

    @property
    def correct(self) -> bool:
        if super().correct:
            return True

        try:
            grade, max_grade = re.findall(
                REGEX_GRADE,
                self.feedbacktrigger,
            )
            if grade == max_grade:
                return True
        except:
            pass

        return None

    @property
    def answer(self) -> Iterable[tuple[str, bool | None]]:
        for text, selected in [
            (
                element.text,
                element.selected == TRUE,
            )
            for element in self.element.elems(value=XPATH_MULTIANSWER_OPTIONS)
        ]:
            if self.correct:
                yield text, selected
            elif self.rightanswer:
                yield text, self.in_rightanswer(text)
            else:
                yield text, None
