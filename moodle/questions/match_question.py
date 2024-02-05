import re
from typing import Iterable
from moodle.constants import REGEX_MATCH_RIGHTANSWER
from .question import Question


class MatchQuestion(Question):
    @property
    def rightanswer(self) -> Iterable[tuple[str, str]]:
        yield from re.findall(REGEX_MATCH_RIGHTANSWER, super().rightanswer)

    @property
    def answer(self) -> Iterable[tuple[str, str, bool | None]]:
        if self.rightanswer:
            for text, answer in self.rightanswer:
                yield text, answer, True
