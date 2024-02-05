####################################################################################################
# GENERAL ##########################################################################################
####################################################################################################

# General values
NEW_LINE = "\n"
EMPTY_STRING = ""
TRUE = "true"
RADIO = "radio"
CORRECT = "correct"
INCORRECT = "incorrect"

# HTML elements attributes
ATTR_DATA_CONTENT = "data-content"

# Login form default values
LOGIN_DEFAULT_USERNAME_ID = "username"
LOGIN_DEFAULT_PASSWORD_ID = "password"
LOGIN_DEFAULT_BUTTON_ID = "loginbtn"
LOGIN_DEFAULT_ERROR_ID = "loginerrormessage"

# Format strings
FORMAT_ERROR = "[bold red]Error:[/bold red] [red]{0}[/red]"
FORMAT_INSTRUCTIONS = "[bold blue]Instructions[/bold blue]\n[grey]{0}[/grey]"

####################################################################################################
# XPATH ############################################################################################
####################################################################################################

XPATH_GRADE_ITEMS = ".//a[starts-with(@class, 'gradeitemheader')]"
XPATH_ROW_LINKS = ".//tbody/tr/td/a"
# Multichoice questions constants
XPATH_TEXT = ".//div[@class='qtext']"
XPATH_IMAGES = ".//div[@class='qtext']//img"
XPATH_TEXT_SPANS = ".//div[@class='qtext']/span"
XPATH_NUMBER = ".//*[@class='qno']"
XPATH_GRADE = ".//*[@class='grade']"
XPATH_GENERALFEEDBACK = ".//*[@class='generalfeedback']"
XPATH_SPECIFICFEEDBACK = ".//*[@class='specificfeedback']"
XPATH_NUMPARTSCORRECT = ".//*[@class='numpartscorrect']"
XPATH_RIGHTANSWER = ".//div[@class='rightanswer']"
XPATH_BADGE = ".//div[contains(@class, 'badge')]"
XPATH_GRADINGDETAILS = ".//div[@class='gradingdetails']"
XPATH_CHOICES = ".//*[@class='answer']/div"
XPATH_CHOICE = ".//label[contains(@for, 'answer') or contains(@for, 'choice')]|.//div[contains(@id, 'answer') or contains(@id, 'choice')]"


# Multianswer questions constants
XPATH_FORMULATION_PARAGRAPHS = ".//*[contains(@class, 'formulation')]/p"
XPATH_MULTIANSWER_OPTIONS = ".//option[position()>1]"
XPATH_FEEBACKTRIGGER = ".//*[contains(@class, 'feedbacktrigger')]"

# Overview
XPATH_OVERVIEW_ITEMS = ".//tr[descendant::a]"

# Attempt
XPATH_ATTEMPT_NAME = "//li[@class='breadcrumb-item'][last()]"
XPATH_ATTEMPT_QUESTIONS = "//*[starts-with(@id, 'question')]"

XPATH_QUESTION_MATCHES = ".//table[@class='answer']/tbody/tr"
XPATH_QUESTION_MATCH_TEXT = ".//td[@class='text']"
XPATH_MATCH_OPTIONS = ".//tr[1]//option[position()>1]"
XPATH_QUESTION_MATCH_SELECTED = (
    ".//td[starts-with(@class, 'control')]//option[@selected]"
)

XPATH_INSTRUCTIONS = ".//div[contains(@class, 'instructions')]"

####################################################################################################
# REGEX ############################################################################################
####################################################################################################

REGEX_NUMERIC = r"\d+"
REGEX_GRADE = r"\d+[\.\,]?\d*"
REGEX_CHOICE = r"^(?:[a-z]\.\s)?([\S\s]+)$"
REGEX_QUESTION_TEXT = r"^([\S\s]+?)\:?$"
REGEX_RIGHTANSWER = r"(?:^.+\:\s)?(.+)"
REGEX_MATCH_RIGHTANSWER = r"(?:^.+\:\s)?(.+?)\s\→\s(.+?)(?:\,\s|$)"
REGEX_QUESTION_RIGHTANSWER_GAPSELECT = (
    r"(.+)\n\w+\s(\d)\s\w+\s(\d)\n\s([\S\s]+?)(?=.+\n\w+\s\d\s\w+\s\d\n\s|\n\.|\.$|$)"
)
REGEX_QUESTION_RIGHTANSWER_GAPSELECT_SUBSTITUTION = r"\1 {{\3\:\2}} "
