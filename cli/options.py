import sys
import typer
from typing import Annotated
from navigation import Browser

################################################################################
### Arguments ##################################################################
################################################################################

UriArgument = Annotated[str, typer.Argument(help="URI")]


InputFileArgument = Annotated[
    typer.FileText,
    typer.Argument(help="Input file", show_default=False),
]

################################################################################
### Options ####################################################################
################################################################################

BrowserOption = Annotated[
    Browser,
    typer.Option("-b", "--browser", help="Browser"),
]

HeadlessOption = Annotated[
    bool,
    typer.Option("-h", "--headless", help="Headless mode"),
]

AuthFieldsOption = Annotated[
    bool,
    typer.Option("--auth-fields", help="Modify authentication fields"),
]

AuthCredentialsOption = Annotated[
    bool,
    typer.Option("-a", "--auth-credentials", help="Use credentials to authenticate"),
]

OutputFileOption = Annotated[
    typer.FileTextWrite,
    typer.Option("-o", "--output-file", help="Output file", show_default=False),
]

IndentOption = Annotated[
    int, typer.Option("-t", "--indent", help="Indentation level", min=0)
]
