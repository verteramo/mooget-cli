from enum import StrEnum
from selenium import webdriver
from selenium.webdriver.common.options import ArgOptions
from selenium.webdriver.remote.webdriver import WebDriver


class Browser(StrEnum):
    Chrome = "Chrome"
    Edge = "Edge"
    Firefox = "Firefox"

    def create_options(self) -> ArgOptions:
        """
        Create the options for the browser.
        """
        match self:
            case self.Chrome:
                return webdriver.ChromeOptions()
            case self.Edge:
                return webdriver.EdgeOptions()
            case self.Firefox:
                return webdriver.FirefoxOptions()

    def create_driver(self, options: ArgOptions) -> WebDriver:
        """
        Create the driver for the browser.
        """
        match self:
            case self.Chrome:
                return webdriver.Chrome(options=options)
            case self.Edge:
                return webdriver.Edge(options=options)
            case self.Firefox:
                return webdriver.Firefox(options=options)
