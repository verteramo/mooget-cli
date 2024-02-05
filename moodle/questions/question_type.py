from enum import StrEnum


class QuestionType(StrEnum):
    """Question type"""

    Description = "description"

    # Multiple choice
    TrueFalse = "truefalse"
    Multichoice = "multichoice"
    CalculatedMulti = "calculatedmulti"
    Multianswer = "multianswer"

    # Textbox
    Shortanswer = "shortanswer"
    Numerical = "numerical"
    Calculated = "calculated"
    CalculatedSimple = "calculatedsimple"

    # Matching
    # TODO
    Match = "match"
    RandomShortanswerMatch = "randomsamatch"

    # Early questions
    # TODO
    GapSelect = "gapselect"
    DragAndDropMarker = "ddmarker"
    DragAndDropImageOrText = "ddimageortext"
    DragAndDropWordToString = "ddwtos"

    # Text (manual feedback)
    # TODO
    Essay = "essay"
