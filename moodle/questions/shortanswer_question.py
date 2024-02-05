from typing import Iterable
from .question import Question

Shortanswer = str


class ShortanswerQuestion(Question):
    @property
    def answer(self) -> Iterable[Shortanswer]:
        if self.rightanswer:
            yield self.rightanswer
        elif self.correct is True:
            yield self.element.tag("input").value
