from typing import Iterable
from moodle.constants import (
    TRUE,
    RADIO,
    REGEX_CHOICE,
    XPATH_CHOICE,
    XPATH_CHOICES,
    XPATH_SPECIFICFEEDBACK,
)
from .question import Question
from navigation.element import Element


class Choice:
    def __init__(self, text: str, checked: bool | None):
        self.text = text
        self.checked = checked

    def __bool__(self) -> bool:
        return bool(self.checked)


class ChoiceElement:
    def __init__(self, element: Element):
        self.element = element

    @property
    def checked(self) -> bool:
        return self.element.tag("input").checked == TRUE

    @property
    def text(self) -> str:
        return self.element.elem(value=XPATH_CHOICE).first(REGEX_CHOICE)

    @property
    def feedback(self) -> str | None:
        try:
            return self.element.elem(value=XPATH_SPECIFICFEEDBACK).innerHTML
        except AttributeError:
            return None


class MultichoiceQuestion(Question):
    @property
    def choices(self) -> Iterable[Choice]:
        for choice in [
            ChoiceElement(element)
            for element in self.element.elems(value=XPATH_CHOICES)
        ]:
            if self.correct:
                yield Choice(choice.text, choice.checked)  # , choice.feedback
            elif self.rightanswer:
                yield Choice(
                    choice.text, self.text_in_rightanswer(choice.text)
                )  # , choice.feedback
            else:
                yield Choice(choice.text, None)  # , choice.feedback

    @property
    def answer(self) -> Iterable[Choice]:
        # Infer single choice correctnes
        if self.element.tag("input").type == RADIO and any(
            filter(lambda choice: choice, self.choices)
        ):
            # Set the rest as incorrect
            yield from [
                Choice(text, False if value is None else value)  # , feedback)
                for text, value in self.choices
            ]
        else:
            yield from self.choices