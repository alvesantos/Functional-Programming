from enum import Enum
class DocFormat(Enum):
    PDF = 1
    TXT = 2
    MD = 3
    HTML = 4

def convert_format(content: str, from_format: DocFormat, to_format: DocFormat | None) -> str:
    if from_format == DocFormat.MD and to_format == DocFormat.HTML:
        return "MD para HTML"

    elif from_format == DocFormat.TXT and to_format == DocFormat.PDF:
        return "TXT para PDF"

    elif from_format == DocFormat.HTML and to_format == DocFormat.MD:
        return "HTML para MD"
    else:
        raise Exception("invalid type")

