import typer
from typing import Annotated
from navigation import Browser

################################################################################
### Arguments ##################################################################
################################################################################

UriArgument = Annotated[str, typer.Argument(help="URI")]

################################################################################
### Options ####################################################################
################################################################################

BrowserOption = Annotated[
    Browser,
    typer.Option("-b", "--browser", help="Browser to use"),
]

HeadlessOption = Annotated[
    bool,
    typer.Option("-h", "--headless", help="Run browser in headless mode"),
]

AuthFileOption = Annotated[
    typer.FileText,
    typer.Option("--auth-file", help="File with authentication fields and credentials"),
]

AuthFieldsOption = Annotated[
    bool,
    typer.Option("--auth-fields", help="Change authentication default fields"),
]

AuthCredentialsOption = Annotated[
    bool,
    typer.Option("-a", "--auth-credentials", help="Provide authentication credentials"),
]

OutputFileOption = Annotated[
    typer.FileTextWrite,
    typer.Option("-o", "--output-file", help="Output file", show_default=False),
]

IndentOption = Annotated[
    int,
    typer.Option("-i", "--indent", help="Indentation level"),
]
