from typing import Iterable
from moodle.constants import XPATH_TEXT
from .question import Question

XPATH_DDWTOS_WORDS = ".//div[starts-with(@class, 'answercontainer')]//span"


class DragAndDropWordToStringQuestion(Question):
    @property
    def choices(self) -> list[str]:
        yield from [
            element.innerHTML
            for element in self.element.elems(value=XPATH_DDWTOS_WORDS)
        ]

    @property
    def text(self) -> str:
        text = self.element.elem(value=XPATH_TEXT).text
        for index, word in enumerate(self.choices):
            text = text.replace(word, f"{{{index}}}")
        
        return text

    @property
    def answer(self) -> Iterable:
        print(self.text.format(*self.choices))

        return []
