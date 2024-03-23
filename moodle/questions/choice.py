from nav.element import Element
from moodle.constants import (
    REGEX_CHOICE,
    TRUE,
    XPATH_CHOICE,
    XPATH_SPECIFICFEEDBACK,
)


class Choice:
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
