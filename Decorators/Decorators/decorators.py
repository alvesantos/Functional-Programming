from collections.abc import Callable

def markdown_to_text_decorator(func: Callable[..., str]) -> Callable[..., str]:
    def wrapper(*args: str, **kwargs: str) -> str:
        pass

    return wrapper


def convert_md_to_txt(doc: str) -> str:
    lines = doc.split("\n")
    for i in range(len(lines)):
        line = lines[i]
        lines[i] = line.lstrip("# ")
    return "\n".join(lines)
