from __future__ import annotations
from .element import Element
from typing import Iterable
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from .browser import Browser


class Driver:
    def __init__(self, browser: Browser, headless: bool = False) -> None:
        options = browser.create_options()

        if headless:
            options.add_argument("--headless")

        if browser == Browser.Chrome:
            options.set_capability("browserVersion", "117")

        if browser == Browser.Chrome or browser == Browser.Edge:
            options.add_experimental_option("excludeSwitches", ["enable-logging"])

        self.driver = browser.create_driver(options)

    def __enter__(self) -> Driver:
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        self.driver.quit()

    def elem(self, by: By = By.XPATH, value: str | None = None) -> Element | None:
        try:
            return Element(self.driver.find_element(by, value))
        except NoSuchElementException:
            return None

    def elems(self, by: By = By.XPATH, value: str | None = None) -> Iterable[Element]:
        try:
            yield from [
                Element(element) for element in self.driver.find_elements(by, value)
            ]
        except NoSuchElementException:
            yield from []

    def get(self, url: str) -> None:
        self.driver.get(url)

    def send(self, element_id: str, value: str) -> None:
        self.driver.find_element(value=element_id).send_keys(value)

    def click(self, element_id: str) -> None:
        self.driver.find_element(value=element_id).click()

    @property
    def current_url(self) -> str:
        return self.driver.current_url
