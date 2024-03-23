import logging
import sys
import typer
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from nav.driver import Driver
from moodle.constants import (
    FORMAT_ERROR,
    LOGIN_DEFAULT_USERNAME_ID,
    LOGIN_DEFAULT_PASSWORD_ID,
    LOGIN_DEFAULT_BUTTON_ID,
    LOGIN_DEFAULT_ERROR_ID,
)


class Authentication:
    def __init__(self, auth_fields: bool, auth_credentials: bool):
        [self.username_id, self.password_id, self.button_id, self.error_id] = (
            [
                typer.prompt("Username input ID", default=LOGIN_DEFAULT_USERNAME_ID),
                typer.prompt("Password input ID", default=LOGIN_DEFAULT_PASSWORD_ID),
                typer.prompt("Login button ID", default=LOGIN_DEFAULT_BUTTON_ID),
                typer.prompt("Error anchor ID", default=LOGIN_DEFAULT_ERROR_ID),
            ]
            if auth_fields
            else [
                LOGIN_DEFAULT_USERNAME_ID,
                LOGIN_DEFAULT_PASSWORD_ID,
                LOGIN_DEFAULT_BUTTON_ID,
                LOGIN_DEFAULT_ERROR_ID,
            ]
        )

        [self.username, self.password] = (
            [
                typer.prompt("Username"),
                typer.prompt("Password", hide_input=True, confirmation_prompt=True),
            ]
            if auth_credentials
            else [None, None]
        )

    def authenticate(self, driver: Driver, uri: str):
        driver.get(uri)
        try:
            driver.send(self.username_id, self.username)
            driver.send(self.password_id, self.password)
            driver.click(self.button_id)

            error = driver.elem(By.ID, self.error_id)

            if error:
                print(FORMAT_ERROR.format(error.text))
                sys.exit(1)
        except NoSuchElementException:
            logging.info("No authentication required.")

    def navigate(self, driver: Driver, uri: str):
        driver.get(uri)

        error = driver.elem(By.ID, self.error_id)
        if error:
            print(FORMAT_ERROR.format(error.text))
            sys.exit(1)
