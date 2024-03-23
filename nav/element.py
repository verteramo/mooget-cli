from __future__ import annotations
import re
from typing import Iterable
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException

ATTR_CLASS = "class"
XPATH_CHILDS = "./*"


class Element:
    def __init__(self, element: WebElement) -> None:
        self.element = element

    def __getattr__(self, name: str) -> str | None:
        return self.element.get_attribute(name)

    @property
    def text(self) -> str:
        return self.element.text

    @property
    def classes(self) -> list[str]:
        return self.element.get_attribute(ATTR_CLASS).split()

    @property
    def childs(self) -> Iterable[Element]:
        yield from self.elems(value=XPATH_CHILDS)

    def elem(self, by: By = By.XPATH, value: str | None = None) -> Element | None:
        try:
            return Element(self.element.find_element(by, value))
        except NoSuchElementException:
            return None

    def elems(self, by: By = By.XPATH, value: str | None = None) -> Iterable[Element]:
        try:
            yield from [
                Element(element) for element in self.element.find_elements(by, value)
            ]
        except NoSuchElementException:
            yield from []

    def tag(self, name: str) -> Element:
        return self.elem(By.TAG_NAME, name)

    def tags(self, name: str) -> Iterable[Element]:
        yield from self.elems(By.TAG_NAME, name)

    def all(self, regex: str) -> list[str]:
        return re.findall(regex, self.element.text)

    def first(self, regex: str) -> str | None:
        try:
            return self.all(regex).pop()
        except IndexError:
            return None

    def etext(self, by: By = By.XPATH, value: str | None = None, default: str | None = None) -> str | None:
        try:
            return self.elem(by, value).text
        except AttributeError:
            return default
