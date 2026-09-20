from enum import Enum
class DocFormat(Enum):
    PDF = 1
    TXT = 2
    MD = 3
    HTML = 4

def convert_format(content: str, from_format: DocFormat, to_format: DocFormat | None) -> str:
    match (from_format, to_format):
        case (DocFormat.MD, DocFormat.HTML):
            return content.replace("# ", "<h1>") + "</h1>"
        case (DocFormat.TXT, DocFormat.PDF):
            return f"[PDF] {content} [PDF]"
        case (DocFormat.HTML, DocFormat.MD):
            return content.replace("<h1>", "# ").replace("</h1>", "")
        case _:
            raise Exception("invalid type")