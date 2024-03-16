import sys
import typer
from moodle.pages import OverviewPage, QuizPage, ReportPage, ReportType
from navigation import Driver
from moodle import (
    AttemptPage,
    Authentication,
)
from cli.options import *
from cli.utils import *

cli = typer.Typer(add_completion=False, help="Download Moodle's quizzes.")


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
    """
    Downloads a single quiz attempt.
    """
    authentication = Authentication(auth_fields, auth_credentials)

    with Driver(browser, headless) as driver:
        if auth_credentials:
            authentication.authenticate(driver, uri)
        else:
            authentication.navigate(driver, uri)

        dump(scrap(AttemptPage(driver)), output, indent)


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
    Downloads all quizzes.
    """
    authentication = Authentication(auth_fields, auth_credentials)

    with Driver(browser, headless) as driver:
        if auth_credentials:
            authentication.authenticate(driver, uri)

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

        dump(data, output, indent=indent)


@cli.command()
def convert(
    input: InputFileArgument = sys.stdin,
    output: OutputFileOption = sys.stdout,
    indent: IndentOption = 2,
):
    """
    Converts a legacy JSON file to new format.
    """
    data = json.load(input)

    new_data = []
    for quiz_name, quiz_questions in data.items():
        new_questions = []
        for question_text, question_answers in quiz_questions:
            new_questions.append(
                {
                    "type": get_question_type(question_answers),
                    "text": question_text,
                    "answers": question_answers,
                }
            )

        new_data.append(
            {
                "name": quiz_name,
                "questions": new_questions,
            }
        )

    dump(new_data, output, indent=indent)


if __name__ == "__main__":
    cli()


# @cli.command()
# def quiz(
#     uri: UriArgument,
#     output: OutputFileOption = sys.stdout,
#     indent: IndentOption = 2,
#     browser: BrowserOption = "Chrome",
#     headless: HeadlessOption = False,
#     auth_fields: AuthFieldsOption = False,
#     auth_credentials: AuthCredentialsOption = False,
# ):
#     """
#     Downloads Moodle's quiz questions.
#     """
#     authentication = Authentication(auth_fields, auth_credentials)

#     with Driver(browser, headless) as driver:
#         if auth_credentials:
#             authentication.authenticate(driver, uri)
#         else:
#             authentication.navigate(driver, uri)

#         data = {}

#         for attempt_link in list(QuizPage(driver)):
#             if attempt_link:
#                 driver.get(attempt_link)
#                 data.update(scrap(AttemptPage(driver)))

#         dump_output(data, output, indent)

#         for name, questions in data.items():
#             print(f"{name} ({len(questions)} questions)")
