from typing import Iterable
from selenium.webdriver.common.by import By
from navigation.driver import Driver
from navigation.element import Element


class Page:
    def __init__(self, driver: Driver) -> None:
        self.driver = driver

    def elem(self, by: By = By.XPATH, value: str | None = None) -> Element | None:
        return self.driver.elem(by, value)

    def elems(self, by: By = By.XPATH, value: str | None = None) -> Iterable[Element]:
        yield from self.driver.elems(by, value)
