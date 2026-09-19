from enum import Enum


class DocFormat(Enum):
    PDF = 1
    TXT = 2
    MD = 3
    HTML = 4


# Don't touch above this line


def convert_format(
    content: str, from_format: DocFormat, to_format: DocFormat | None
) -> str:
    pass
