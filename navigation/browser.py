from enum import StrEnum
from selenium import webdriver
from selenium.webdriver.common.options import ArgOptions
from selenium.webdriver.remote.webdriver import WebDriver


class Browser(StrEnum):
    Chrome = "Chrome"
    Edge = "Edge"
    Firefox = "Firefox"

    def get_options(self) -> ArgOptions:
        match self:
            case self.Chrome:
                return webdriver.ChromeOptions()
            case self.Edge:
                return webdriver.EdgeOptions()
            case self.Firefox:
                return webdriver.FirefoxOptions()

    def get_driver(self, options: ArgOptions) -> WebDriver:
        match self:
            case self.Chrome:
                return webdriver.Chrome(options=options)
            case self.Edge:
                return webdriver.Edge(options=options)
            case self.Firefox:
                return webdriver.Firefox(options=options)
