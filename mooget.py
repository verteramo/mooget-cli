import sys
import typer
from navigation import Driver
from moodle import (
    AttemptPage,
    Authentication,
    OverviewPage,
    QuizPage,
    ReportPage,
    ReportType,
)
from cli.options import *
from cli.utils import *

cli = typer.Typer(add_completion=False)


@cli.command()
def attempt(
    uri: UriArgument,
    output: OutputFileOption = sys.stdout,
    indent: IndentOption = 2,
    browser: BrowserOption = "Chrome",
    headless: HeadlessOption = False,
    auth_fields: AuthFieldsOption = False,
    auth_credentials: AuthCredentialsOption = False,
):
    authentication = Authentication(auth_fields, auth_credentials)

    with Driver(browser, headless) as driver:
        if auth_credentials:
            authentication.authenticate(driver, uri)
        else:
            authentication.navigate(driver, uri)

        dump_output(scrap(AttemptPage(driver)), output, indent)


@cli.command()
def quiz(
    uri: UriArgument,
    output: OutputFileOption = sys.stdout,
    indent: IndentOption = 2,
    browser: BrowserOption = "Chrome",
    headless: HeadlessOption = False,
    auth_fields: AuthFieldsOption = False,
    auth_credentials: AuthCredentialsOption = False,
):
    """
    Downloads Moodle's quiz questions.
    """
    authentication = Authentication(auth_fields, auth_credentials)

    with Driver(browser, headless) as driver:
        if auth_credentials:
            authentication.authenticate(driver, uri)
        else:
            authentication.navigate(driver, uri)

        data = {}

        for attempt_link in list(QuizPage(driver)):
            if attempt_link:
                driver.get(attempt_link)
                data.update(scrap(AttemptPage(driver)))

        dump_output(data, output, indent)

        for name, questions in data.items():
            print(f"{name} ({len(questions)} questions)")


@cli.command()
def crawl(
    uri: UriArgument,
    output: OutputFileOption = sys.stdout,
    indent: IndentOption = 2,
    browser: BrowserOption = "Chrome",
    headless: HeadlessOption = False,
    auth_fields: AuthFieldsOption = False,
    auth_credentials: AuthCredentialsOption = False,
):
    """
    Crawls all quizzes from Moodle overview page.
    """
    authentication = Authentication(auth_fields, auth_credentials)

    with Driver(browser, headless) as driver:
        if auth_credentials:
            authentication.authenticate(driver, uri)
        else:
            authentication.navigate(driver, uri)

        data = {}

        for _, course_link in OverviewPage(driver):
            driver.get(course_link)

            for grade_type, grade_link in ReportPage(driver):
                if grade_type == ReportType.Quiz:
                    driver.get(grade_link)

                    for attempt_link in QuizPage(driver):
                        driver.get(attempt_link)
                        data.update(scrap(AttemptPage(driver)))

        print(json.dump(data, output, indent=indent))


if __name__ == "__main__":
    cli()
